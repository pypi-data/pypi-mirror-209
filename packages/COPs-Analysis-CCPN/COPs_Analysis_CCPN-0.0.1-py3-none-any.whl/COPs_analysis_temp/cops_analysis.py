"""
TODO Harrison: Add Documentation and update Credits
"""
#=========================================================================================
# Licence, Reference and Credits
#=========================================================================================
__copyright__ = "Copyright (C) CCPN project (https://www.ccpn.ac.uk) 2014 - 2022"
__credits__ = ("Ed Brooksbank, Joanna Fox, Victoria A Higman, Luca Mureddu, Eliza Płoskoń",
               "Timothy J Ragan, Brian O Smith, Gary S Thompson & Geerten W Vuister")
__licence__ = ("CCPN licence. See https://ccpn.ac.uk/software/licensing/")
__reference__ = ("Skinner, S.P., Fogh, R.H., Boucher, W., Ragan, T.J., Mureddu, L.G., & Vuister, G.W.",
                 "CcpNmr AnalysisAssign: a flexible platform for integrated NMR analysis",
                 "J.Biomol.Nmr (2016), 66, 111-124, http://doi.org/10.1007/s10858-016-0060-y")
#=========================================================================================
# Last code modification
#=========================================================================================
__modifiedBy__ = "$modifiedBy: Luca Mureddu $"
__dateModified__ = "$dateModified: 2022-06-29 11:57:45 +0100 (Wed, June 29, 2022) $"
__version__ = "$Revision: 3.1.0 $"
#=========================================================================================
# Created
#=========================================================================================
__author__ = "$Author: Harrison Wang $"
__date__ = "$Date: 2022-05-20 12:59:02 +0100 (Fri, May 20, 2022) $"
#=========================================================================================
# Start of code
#=========================================================================================

import matplotlib.pyplot as plt
import typing
import os
import numpy as np
import pandas as pd
import numpy.linalg
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit
from ccpn.core.NmrAtom import UnknownIsotopeCode
from ccpn.core.Peak import Peak
from ccpn.core.Spectrum import Spectrum
from ccpn.core.SpectrumGroup import SpectrumGroup
from ccpn.core.DataTable import DataTable
from ccpn.core.PeakList import PeakList
from ccpn.core.NmrResidue import NmrResidue



class cops_analyze():
    def __init__(self, application, HNCA_spectrum_group: SpectrumGroup, data_table: pd.DataFrame = None, peak_list: PeakList = None):
        """format of self.tb given by the extract_1D_to_table function"""
        self.application = application
        self.sg = HNCA_spectrum_group
        self.pl = peak_list
        self.tb = None
        self.cop_nums = []

        #two internal dictionaries keeping track of which peaks are CA peaks and which are CB peaks
        #self.peak_to_CAres = {}
        #self.peak_to_CBpeak = {}

        for i in self.sg.series:
            self.cop_nums.append(i - 1 if i > 2 else i)
        self.mat = np.loadtxt(os.path.dirname(__file__)+'/dec_profiles.csv')

        self.cops = self.mat[0].reshape(1, -1)
        self.cop_nums = [int(i) for i in self.cop_nums]
        self.cop_num = len(self.cop_nums)
        for i in self.cop_nums:
            self.cops = np.concatenate((self.cops, self.mat[i].reshape(1, -1)), axis=0)
        self.cops = self.cops[:, :171]

        # generates array of interpolation functions to determine value of decoupling for a particular Cb.
        self.dec_interpolation = [interp1d(self.cops[0], self.cops[i + 1], kind='cubic') for i in range(self.cop_num)]

        if data_table is not None:
            self.tb = data_table
        else:
            self.extract_1D_to_table(self.pl)

        self.CB_calc = None

    def _getCBPeak(self, peak):
        '''
        given an HNCA peak, point to its created HNCB peak.
        '''

        res = self._getCAResidue(peak)
        if not res:
            return None

        CA_res_atoms = self.application.project.getByPid(res).nmrAtoms
        for atom in CA_res_atoms:
            if atom.name == 'CB' and atom.chemicalShifts != ():
                self.peak_to_CBpeak[atom.chemicalShifts[0].assignedPeaks[0].pid] = peak.pid
                return peak.pid
        return self.peak_to_CBpeak.get(peak.pid, None)


    def set_CB(self, is_checked: bool):
        self.CB_calc = is_checked
        if is_checked:
            if self.pl is not None:
                for peak in self.pl.peaks:
                    if bool(self._peak_to_CB_peak(peak)):
                        continue
                    try:
                        self.create_CB_peak(peak)
                    except:
                        print("unconverged or inaccurate CB calculation for peak", peak.pid)
            elif self.tb is not None:
                print("if you want to recalculate CB, delete the DT and recalculate. Else, see source code")
                #below code can be uncommented, but it basically reruns unconverged runs.
                '''
                for peak_pid in self.tb['peaks']:
                    peak = self.application.project.getByPid(peak_pid)
                    if bool(self._getCBPeak(peak)):
                        continue
                    try:
                        self.create_CB_peak(peak)
                    except:
                        print("unconverged or inaccurate CB calculation for peak", peak_pid)
                '''

    ###############################################
    # SECTION 0. EXPERIMENTAL LINESHAPE EXTRACTION #
    ###############################################

    ## requires checks to robustness....
    def _extract1D(self, peak: Peak, spectrum: Spectrum, sw: float = 60,
                   normalize: bool =False, mode: str = "ppm"):
        """
        given: peak (Peak), spectrum (Spectrum),
            sw: float (Hz), default 60. half the width in each direction of the desired 1D slice
            normalize: bool, default False. normalize=True divides the 1D slice intensity by the RMS intensity.
            mode: str, default 'ppm', can set to 'Hz'. The units of the output centered_x_vals.
        returns:
            centered_x_vals: list[float], x values in ppm or Hz.
            trace: list[float], intensity of 1D trace.
            center: float, center value in ppm.

        """
        # pull out position in ppm of peak, along with spectral parameters.
        position = peak.position
        ax_codes = peak.axisCodes
        ppm_pts = spectrum.ppmPerPoints
        sw_hz = spectrum.spectralWidthsHz
        sw_ppm = spectrum.spectralWidths
        ppm_per_hz = np.divide(sw_ppm, sw_hz)
        limits_dict = {}
        N_H_index = []

        # enter limits of the spectral region extracted
        for ind, code in enumerate(ax_codes):
            if code == 'C':
                C_index = ind
                center = position[ind]
                limits_dict[code] = center + sw * ppm_per_hz[ind] * np.array([-1, 1])
            else:
                N_H_index.append(ind)
                limits_dict[code] = position[ind] + ppm_pts[ind] * np.array([-2, 2])

        # 1D slice through peak center, weight-added by tensor product to 1D 13C slices nearby (in the HN, N dimensions)
        # to return a final 1D slice
        weights = np.array([[0.6, 0.9, 1, 0.9, 0.6]])  # weights vector to compute weighted sum
        slices = spectrum.getRegion(**limits_dict)

        trace = np.tensordot(slices.T, weights.T @ weights, axes=(N_H_index, [0, 1]))
        trace = np.array(trace)

        normalizer = numpy.linalg.norm(trace) / sw

        if normalize:
            # normalize by peak volume
            trace = trace / normalizer
        if mode=="Hz":
            factor = 1/ppm_per_hz[C_index]
        else:
            factor = 1

        centered_x_vals = (np.linspace(limits_dict['C'][0], limits_dict['C'][1], len(trace)) - position[C_index])*factor

        return centered_x_vals, trace, center

    ##################################
    # SECTION 1. LINESHAPE SIMULATION #
    ##################################

    # ### should be vectorizable.
    def _lineshape(self, w, k_abs, fraction, c, j, lwid):
        """
        DEFINITION
        __________
        /given/ an input frequency axis w and peak profile parameters:
        /returns/ a simulated 13C peak profile.


        PARAMETERS
        __________

        w: list
        frequency axis of the 13C peak profile, in Hz, centered at 0.

        k_abs: float
        absolute height of fully-decoupled gaussian, in arbitrary and normalized units.

        fraction: float between 0 and 1
        Cb recoupling fraction.

        c: float
        offset from center c of the the 13C peak profile, in Hz.

        j: float
        J coupling between CA and CB, in Hz.

        lwid: float
        13C linewidth, in Hz.

        OUTPUT
        _______

        C_profile: list
        13C peak profile, in arbitrary intensity units. 1 intensity value per point on the frequency axis (w).

        """
        C_profile = k_abs / 2 * fraction * np.exp(-(w - c - j) ** 2 / (2 * lwid ** 2)) + \
                    k_abs * (1 - fraction) * np.exp(-(w - c) ** 2 / (2 * lwid ** 2)) + \
                    k_abs / 2 * fraction * np.exp(-(w - c + j) ** 2 / (2 * lwid ** 2))
        return C_profile

    def _lineshape_Cb(self, w, k_abs, pyr_fraction, Cb, c, j, lwid):
        """
        DEFINITION
        __________
        /given/ a value of CB chemical shift, pyruvate Cb labeling fraction, and a frequency axis w, along with peak profile parameters:
        /returns/ a self.cop_num*len(w) list containing predicted lineshapes for the no-cop spectrum (index 0 of the lineshapes variable
        pre-reshaping) and each GRADCOP (index 1-self.cop_num). This is used for fitting experimental lineshapes.

        PARAMETERS
        __________

        peak profile parameters (w, k_abs, c, j, lwid) defined as in the lineshape function.

        Cb: float
        CB chemical shift in ppm.

        pyr_fraction: float between 0 and 1
        CB labeling fraction for the given resonance.

        OUTPUT
        ______
        lineshapes: list
        a list of the predicted 13C peak profile for each GRADCOP spectrum, appended end-to-end.

        """

        # calculates the decoupling fraction for each GRADCOP given the Cb.
        decoupling_fractions = [(1 + self.dec_interpolation[i](Cb)) / 2 for i in range(self.cop_num)]
        # generates lineshape
        lineshapes = np.array(
            [self._lineshape(w, k_abs, pyr_fraction * decoupling_fractions[i], c, j, lwid) for i in range(self.cop_num)])
        # reshapes to provide a target list for fitting experimental lineshapes.
        lineshapes = lineshapes.reshape(-1)
        return lineshapes

        return None

    ###########################
    # SECTION 2. CB prediction
    ###########################

    # takes in data point coordinates in ppm, and outputs the triangulated Cb, directly optimized over lineshapes.
    def _CalcCB(self, peak: Peak, sw: float=60, simple_output: bool =True):
        """
        DEFINITION
        __________
        /given/ a single peak center in ppm:
        /returns/ the triangulated Cb value.

        PARAMETERS
        __________
        data_pt: list of length 3
        15N, 13C, 1H chemical shift of the peak center (ppm).

        fit_tol: float, default value 3
        tolerance in arbitrary units for fitting COPs spectral parameters given the nocop paramter fit.

        simple_output: boolean, default value True
        if True, outputs only CB value. if False, outputs entire fit parameters as well as a credence value.

        OUTPUT
        ______
        best_params: list
        fit parameters. See description of lineshape_Cb for variable definitions.
        index 0: best fit of the k_abs variable
        index 1: best fit of the pyr_fraction variable
        index 2: best fit of CB (ppm)
        index 3: best fit of the c variable
        index 4: best fit of the j variable
        index 5: best fit of the linewidth variable

        1/min_sq: float
        fit credence. a large value (>50) indicates the fit is very good. A small value (~5) indicates the fit is poor.

        """
        j_ab = 40  # Hz
        lwid = 10  # Hz

        # reshapes experimental lineshape
        hz = self._extract1D(peak, self.sg.spectra[0], sw=sw, normalize=True, mode="Hz")[0]
        cop_1Ds = np.array(
            [self._extract1D(peak, self.sg.spectra[i], sw=sw, normalize=True, mode="Hz")[1] for i in range(self.cop_num)])
        cop_1Ds = cop_1Ds.reshape(-1)

        """bounds: [k_abs, pyr_fraction, Cb, c, j, lwid]"""
        for i in range(7):

            # initializes CB to a ppm value between 10 and 46, inclusive.
            prior_cb = 16 + i * 5

            # initialize prior and bounds of fitting.
            p = [40, 1, prior_cb - 0.01, 0, j_ab, lwid]
            bounds = ([0, 0.999, prior_cb - 6, -30, j_ab - 40, lwid - 10], [150, 1, prior_cb, 30, j_ab + 40, lwid + 10])
            params = self._lineshape_Cb_fit(hz, cop_1Ds, prior=p, bounding=bounds)

            # measures the squared error between experimental and simulated peak profile
            sq_error = np.sum((self._lineshape_Cb(hz, *params) - cop_1Ds) ** 2) / len(hz) / params[0]

            # determines which of the initial CB values produces the smallest error.
            if i == 0:
                min_sq = sq_error
                best_params = params
            if sq_error < min_sq:
                best_params = params
                min_sq = sq_error

        #FOR TESTING
        """
        hz_long = np.array([hz + 200 * i for i in range(4)]).reshape(-1)
        plt.cla()
        plt.plot(hz_long, cop_1Ds, hz_long, self._lineshape_Cb(hz, *best_params))
        plt.show()"""

        if simple_output:
            return best_params[2], min_sq  # returns CB shift value in ppm
        else:
            return best_params, min_sq  # returns every fit parameter: CB shift (ppm), linewidth, J coupling; as well as 1/error of the CB estimate


    def create_CB_peak(self, peak: Peak):
        """
        given an HNCA Peak in the HNCA, predicts CB value and creates a HNCB Peak in the SpectrumGroup's first Spectrum.
        """
        if not self._getCAResidue(peak):
            return

        position = peak.position
        ax_codes = np.array(peak.axisCodes)
        try:
            new_CB, FOM = self._CalcCB(peak)
            assert(FOM < 1.2)
        except:
            raise ValueError("CB peak not created: Figure of Merit too low")
            return

        # convert FOM value to a number between 0 and 1, where 1 is best.
        FOM = np.exp(-FOM/2)

        # create a dictionary to assign the peak to the correct residues' atoms.
        if peak.assignments != ():
            for atom in peak.assignments[0]:
                if atom:
                    if atom.name == 'CA':
                        res_C = atom.nmrResidue
                    if atom.name == 'N':
                        res = atom.nmrResidue
        else:
            print("peak not assigned!")
            return

        try:
            assert(res)
            assert(res_C)
            atom_dic = {"C": res_C.fetchNmrAtom('CB'), "H": res.fetchNmrAtom('H'), "N":res.fetchNmrAtom('N')}
        except:
            return

        # create new Peak at the position specified by the new CB and the old H and N.
        new_position = list(position)
        for ind, code in enumerate(ax_codes):
            if code == 'C':
                new_position[ind]=new_CB
        new_peak = self.sg.spectra[0].peakLists[-1].newPeak(ppmPositions=new_position)

        for axisCode in new_peak.axisCodes:
            # assign
            new_peak.assignDimension(axisCode, atom_dic[axisCode])

            # set isotope code
            isotopeCode = peak.peakList.spectrum.getByAxisCodes('isotopeCodes', [axisCode], exactMatch=True)[-1]
            if atom_dic[axisCode].isotopeCode in [UnknownIsotopeCode, None]:
                atom_dic[axisCode]._setIsotopeCode(isotopeCode)

        # print(res_C.fetchNmrAtom('CB').chemicalShifts[0].value)
        # set figure of merit
        res_C.fetchNmrAtom('CB').chemicalShifts[0].figureOfMerit = FOM
        new_peak.figureOfMerit = FOM

        #set dictionary with residue pointing to peak
        self.tb['CB_peaks'].loc[self.tb['CA_peaks']==peak.pid] = new_peak.pid

    ###############################
    # SECTION 3. FITTING UTILITIES #
    ###############################

    """bounding: [k_abs, fraction, c, j, lwid]"""
    def _lineshape_fit(self, x, y, bounding=([0, 0, -10, 0, 0], [40, 1, 10, 40, 10])):
        """
        DEFINITION
        /given/ a list of frequency values and a list of experimental lineshape intensity values,
        /returns/ the lineshape function's parameters that produce the best fit.

        PARAMETERS
        __________
        x: list
        list of frequency values (Hz).

        y: list, size of x
        lineshape intensity values (arbitrary units).

        bounding: tuple of two lists of length 5, default: ([0,0,-2,0,0],[30,1,2,40,10])
        bounds for arguments of the lineshape function; see the lineshape definition.

        OUTPUT
        ______
        param_best: list
        fit parameters. See description of lineshape for variable definitions.
        index 0: best fit of the k_abs variable
        index 1: best fit of the fraction variable
        index 3: best fit of the c variable
        index 4: best fit of the j variable
        index 5: best fit of the linewidth variable

        """

        param_best, _ = curve_fit(self._lineshape, x, y, p0=np.add(bounding[0], bounding[1]) / 2, bounds=bounding)
        return param_best

    """bounding: [k_abs, pyr_fraction, Cb, c, j, lwid]"""
    def _lineshape_Cb_fit(self, x, y, prior=None, bounding=([0, 0, 9, -20, 0, 0], [10, 1, 46, 20, 70, 15])):
        """
        DEFINITION
        /given/ a list of frequency values and a list of experimental lineshape intensity values for the COPs,
        /returns/ the lineshape function's parameters that produce the best fit.

        PARAMETERS
        __________
        x: list
        list of frequency values (Hz).

        y: list, size of x
        lineshape intensity values of COPs spectra, appended end-to-end (arbitrary units).

        prior: list, default None
        fitting initial parameters for the lineshape_Cb function parameters.

        bounding: tuple of two lists of length 5, default: ([0,0,9,-5,0,0],[20,1,46,5,40,10])
        fitting bounds for the lineshape_Cb function parameters; see the lineshape_Cb definition.

        OUTPUT
        ______
        param_best: list
        fit parameters. See description of lineshape_Cb for variable definitions.
        index 0: best fit of the k_abs variable
        index 1: best fit of the pyr_fraction variable
        index 2: best fit of the Cb variable
        index 3: best fit of the c variable
        index 4: best fit of the j variable
        index 5: best fit of the linewidth variable

        """

        if prior == None:
            prior = np.add(bounding[0], bounding[1]) / 2
        param_best, _ = curve_fit(self._lineshape_Cb, x, y, p0=prior, bounds=bounding)
        return param_best

    ####
    # SECTION 4. LINESHAPE COMPARISON
    ####

    def _extract_1D_row(self, peak: Peak):
        ppm = []
        trace = []
        mask = []

        for i in range(self.cop_num):
            ppm_temp, trace_temp, position_temp = self._extract1D(peak, self.sg.spectra[i], sw=60, normalize=True)
            mask_temp = np.zeros(len(ppm_temp)) + i
            ppm.append(ppm_temp)
            trace.append(trace_temp)
            mask.append(mask_temp)

        res = self._getCAResidue(peak)

        ppm = np.array(ppm).reshape(-1)
        trace = np.array(trace).reshape(-1)
        mask = np.array(mask).reshape(-1)


        return res, position_temp, trace.tolist(), ppm.tolist(), mask.tolist()

    def _getCAResidue(self, peak: Peak) -> str:
        res = None

        #when getCAResidue is called for peak deletion
        if self.tb is not None:
            peak_row = self.tb['residues'].loc[self.tb['CA_peaks'] == peak.pid]
            if len(peak_row) > 0:
                res = peak_row.iloc[0]

        #overwrite CA when getCAResidue is called for peak creation
        if peak.assignments != ():
            for atom in peak.assignments[0]:
                if atom:
                    if atom.name == 'CA':
                        res = atom.nmrResidue.pid

        return res

    def extract_1D_to_table(self, peak_list: PeakList, out_name: str = "cops_ls") -> None:
        """
        given a peak list, generates a DataTable with the PID DT:<out_name>, containing the following columns.

        residues: NmrResidue pid
        CA center: float, CA chemical shift of the residue
        1D_slice: list, intensity values at each coordinate given by ppm_vals.
                    This will be used for lineshape matching.
        ppm_vals: list, x axis in the units of ppm
        COPS_mask: list, which cop_num the 1D_slice corresponds to
        """

        peaks = peak_list.peaks
        residues = []
        center = []
        matrix_1D = []
        matrix_ppm = []
        matrix_mask = []
        peaks_pid = []

        for peak in peaks:
            if not self._getCAResidue(peak):
                continue
            res, position, trace, ppm, mask = self._extract_1D_row(peak)

            residues.append(res)
            center.append(position)
            peaks_pid.append(peak.pid)

            matrix_ppm.append(ppm)
            matrix_1D.append(trace)
            matrix_mask.append(mask)

        self.tb = pd.DataFrame({"residues": residues, "CA_peaks": peaks_pid, "CA center": center,
                                "1D_slice": matrix_1D, "ppm_vals": matrix_ppm,
                                "COPS_mask": matrix_mask})
        self.tb['CB_peaks'] = None

        self._update_DT(self.tb, out_name=out_name)
        return None

    def _update_DT(self, tb, out_name: str = "cops_ls"):
        try:
            self.application.project.getByPid("DT:"+out_name).data = tb
        except:
            self.application.project.newDataTable(name=out_name, data=tb)


    def _set_1D_length(self, list_in, length) -> list:
        #sets a list's length by either truncating or zero filling.
        Os = np.zeros(length)
        m = min(len(list_in), length)
        Os[:m] = list_in[:m]
        return Os

    def _slice_table_to_array(self, match_data, slice_table) -> np.array:
        #sets a slice_table's '1D slice' column's lists to the length of the comparison data.
        datasize = len(match_data)
        stacked_array = np.vstack(slice_table['1D_slice'].apply(lambda x: self._set_1D_length(x, datasize)))
        return stacked_array

    def find_best_correlation(self, match_data: list, slice_table: pd.DataFrame) -> np.array:
        """
        given: 1D slice of match data and a DataFrame of 1D slices,
        determines: the correlation value between the match data and every 1D slice in the DataFrame
        """
        slices = self._slice_table_to_array(match_data, slice_table)
        for i in range(7):
            corr = [np.corrcoef(match_data, np.roll(slices, i - 3, axis=1))[1:, 0]]
            if i == 0:
                corrs = (corr)
            else:
                corrs = corrs + corr
        corrs = np.vstack(corrs)
        return np.max(corrs, axis=0)

    def plot_matches(self, this_residue: NmrResidue, assignMatrix: typing.Dict[float, NmrResidue]) -> plt.figure:
        """
        given: a ccpn NmrResidue and assignMatrix object from BackboneAssignmentModule,
        returns: a plot of the residue's best match 1D HNCA lineshapes across all COPs spectra.
        """
        plt.clf()
        cmap = ['b', 'r', 'm', 'y']
        fig = plt.figure(figsize=(13, 6))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        COP_SEP = 1.3
        ax.set_xticks(COP_SEP*np.arange(self.cop_num).astype(int))
        ax.set_xticklabels(self.sg.series)
        ax.set_xlabel("COP number")

        this_data = self.tb[self.tb['residues'] == this_residue.pid]

        if len(this_data)>0:
            this_residue_info = this_data.iloc[0]
        else:
            getLogger().warning("No matches by Lineshape found. No plot generated")

        this_data, this_center, this_ppm, this_mask = this_residue_info[['1D_slice', 'CA center', 'ppm_vals', 'COPS_mask']]

        for i in range(self.cop_num):
            this_mask = np.array(this_mask)
            this_ppm = np.array(this_ppm)
            this_data = np.array(this_data)

            indices = this_mask == i
            if i == 0:
                plt.plot(np.flip(this_ppm[indices]) + COP_SEP * i, np.flip(this_data[indices]), 'k', figure=fig,
                         label=this_residue.pid)
            else:
                plt.plot(np.flip(this_ppm[indices]) + COP_SEP * i, np.flip(this_data[indices]), 'k', figure=fig)

        #returns the best 5 match scores in AssignMatrix.
        assignMatrix_vals_sorted = np.flip(-np.sort(-np.fromiter(assignMatrix.keys(), dtype=float)))[:5]

        for ind, i in enumerate(assignMatrix_vals_sorted):
            residue = assignMatrix[i]
            try:
                data, cent, ppm, mask = self.tb[self.tb['residues'] == residue.pid].iloc[0][['1D_slice', 'CA center', 'ppm_vals', 'COPS_mask']]
            except:
                print(residue.pid+" CA peak missing!")
                continue

            mask = np.array(mask)
            data = np.array(data)
            ppm = np.array(ppm)
            relative_center = this_center - cent

            #does not plot residues with larger than 0.5 ppm offset from this residue's center.
            if np.abs(relative_center)>0.5:
                continue
            for k in range(self.cop_num):
                indices = mask == k
                if k == 0:
                    label_str = residue.pid
                    plt.plot(relative_center+np.flip(ppm[indices]) + COP_SEP * k,
                             np.flip(data[indices]) - 25 * (1 + ind),
                             cmap[ind % 4], label=label_str,
                             figure=fig)
                else:
                    plt.plot(relative_center+np.flip(ppm[indices]) + COP_SEP * k,
                             np.flip(data[indices]) - 25 * (1 + ind),
                             cmap[ind % 4], figure=fig)
        fig.legend()
        return fig


    #####
    #SECTION 5. LINESHAPE UPDATES
    #####
    def updateNmrResidue(self, trigger, residue: NmrResidue, oldPid: str=None):
        if trigger == 'delete':
            self.tb = self.tb.drop(self.tb.index[[self.tb['residues']==residue.pid]])
        elif trigger == 'rename' and oldPid is not None:
            self.tb.loc[self.tb['residues']==oldPid, 'residues']=residue.pid
        self._update_DT(self.tb)

    def _append_1D_row(self, peak):
        out = self._getCAResidue(peak)
        if not bool(out):
            return
        res, position, trace, ppm, mask = self._extract_1D_row(peak)
        new_row = {"residues": res, "CA_peaks": peak.pid, "CA center": position,
                   "1D_slice": [trace], "ppm_vals": [ppm],
                   "COPS_mask": [mask], "CB_peaks":None}
        self.tb = pd.concat([self.tb, pd.DataFrame(new_row)], ignore_index=True)

    def updatePeak(self, trigger: str, peak: Peak):
        peakname = peak.pid
        if trigger != 'delete':
            out = self._getCAResidue(peak)
            if not bool(out):
                return

        if trigger == 'delete' or trigger == 'change':
            if self.CB_calc:
                self.delete_CB_peak(peak)
            try:
                self.tb = self.tb.drop(self.tb.index[[self.tb['CA_peaks'] == peakname]])
            finally:
                pass

        if trigger == 'create' or trigger == 'change':
            self._append_1D_row(peak)
            if self.CB_calc:
                try:
                    self.create_CB_peak(peak)
                except:
                    print("unconverged or inaccurate CB calculation for peak", peak.pid)

        self._update_DT(self.tb)
        return

    def _peak_to_CB_peak(self, peak) -> str:
        CB_peak_pid = None
        peak_row = self.tb['CB_peaks'].loc[self.tb['CA_peaks']==peak.pid]
        if len(peak_row)>0:
            CB_peak_pid = peak_row.iloc[0]
        return CB_peak_pid

    def delete_CB_peak(self, peak):
        CB_peak = self.application.project.getByPid(self._peak_to_CB_peak(peak))
        if CB_peak:
            CB_peak.delete()
            print("deleting all created CB peaks associated with " + peak.pid)
        return