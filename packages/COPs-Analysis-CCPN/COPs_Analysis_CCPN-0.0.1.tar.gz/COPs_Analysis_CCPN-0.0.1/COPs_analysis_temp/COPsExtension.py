"""

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

import typing
from ccpn.util.Logging import getLogger
import pandas as pd
from ccpn.core.NmrResidue import NmrResidue
from ccpn.core.lib.Notifiers import Notifier
from ccpn.AnalysisAssign.modules.backboneExtensions.BackboneAssignmentExtensionABC import BackboneAssignmentExtensionFrame
from ccpn.AnalysisAssign.modules.backboneExtensions.COPs_analysis.cops_analysis import cops_analyze
from ccpn.ui.gui.widgets.PulldownListsForObjects import SpectrumGroupPulldown, DataTablePulldown, PeakListPulldown
from ccpn.ui.gui.widgets.CompoundWidgets import CheckBoxCompoundWidget


_cwWidth = 200

class COPsExtensionFrame(BackboneAssignmentExtensionFrame):
    """
    COPs Extension for the Analysis Backbone Assignment
    """

    NAME = 'COPs Analysis'
    isGuiActive = True

    def __init__(self, guiModule, *args, **Framekwargs):
        BackboneAssignmentExtensionFrame.__init__(self, guiModule, **Framekwargs)

        self.guiModule.findAndDisplayMatches = self.findAndDisplayMatches
        self.ca = None

    def registerNotifiers(self):
        self._resChangedNotifier = Notifier(self.project,
                                            [Notifier.RENAME, Notifier.DELETE],
                                            'NmrResidue', self._change_Res)
        self._peakChangedNotifier = Notifier(self.project,
                                             [Notifier.CHANGE, Notifier.RENAME, Notifier.DELETE, Notifier.CREATE],
                                             'Peak', self._change_Peak)

    def initWidgets(self):

        row = 0
        self.SGWidget = SpectrumGroupPulldown(self, mainWindow=self.mainWindow, fixedWidths=(_cwWidth, _cwWidth), grid=(row,0))
        row += 1
        self.DTWidget = DataTablePulldown(self, mainWindow=self.mainWindow, fixedWidths=(_cwWidth,_cwWidth), grid=(row, 0))
        row += 1
        self.PLWidget = PeakListPulldown(self, mainWindow=self.mainWindow, fixedWidths=(_cwWidth, _cwWidth), grid=(row, 0))
        row += 1
        self.calculate_CB = CheckBoxCompoundWidget(self,
                                                 grid=(row, 0),
                                                 fixedWidths=(_cwWidth, _cwWidth),
                                                 orientation='left',
                                                 labelText='Calculate CB',
                                                 checked=False
                                                 )

    def findAndDisplayMatches(self, nmrResidue):
        """Find and displays the matches to nmrResidue"""

        assignMatrix = self.guiModule.getAssignedMatrix(nmrResidue)
        if self.isGuiActive:
            assignMatrix = self._getCopAssignedMatrix(nmrResidue, assignMatrix)

        ## Native behaviour
        self.guiModule._createMatchStrips(assignMatrix)

    def _initialize_analyzer(self):
        sg_pid, pl_pid = self.SGWidget.getText(), self.PLWidget.getText()
        sg = self.application.project.getByPid(sg_pid)
        pl = self.application.project.getByPid(pl_pid)
        try:
            self.ca = cops_analyze(self.application, sg, peak_list=pl)
        except:
            raise ValueError("Check set spectrum group and/or peak list!")


    def updateMatchesByLineshape(self, cops_analyzer: cops_analyze, this_Residue: NmrResidue,
                                 assignMatrix: typing.Dict[float, NmrResidue],
                                 df: pd.DataFrame) -> typing.Dict[float, NmrResidue]:

        # compresses the dataframe to contain slices for only residues found in AssignMatrix.
        res_pids = [i.pid for i in assignMatrix.values()]
        slices_list = df[df['residues'].isin(res_pids)]


        this_data = df[df['residues'] == this_Residue.pid]
        if len(this_data)>0:
            this_data = this_data.iloc[0]['1D_slice']
        else:
            getLogger().warning("No matches by Lineshape found. Returning native matches")
            return assignMatrix

        # compute correlation score and sets new element in DataFrame
        lineshape_correlations = cops_analyzer.find_best_correlation(this_data, slices_list)
        slices_list['correlation'] = lineshape_correlations

        # updates the keys of assignMatrix with new scores
        new_assignMatrix = {}
        for matchscore, nmrRes in assignMatrix.items():
            try:
                corr = float(max(slices_list['correlation'][slices_list['residues']==nmrRes.pid]))
            except:
                corr = 0

            # a better correlation value results in a smaller update score.
            update_score = 1.5-corr
            # The correlation values are steepened.
            new_assignMatrix[(1-10**(-10*matchscore))*update_score]=nmrRes
        return new_assignMatrix

    def _getCopAssignedMatrix(self, nmrResidue, assignMatrix, plot=True):
        """ Overriden _getAssignedMatrix method to allow the COP analysis."""
        sg_pid, dt_pid, pl_pid = self.SGWidget.getText(), self.DTWidget.getText(), self.PLWidget.getText()
        sg = self.application.project.getByPid(sg_pid)
        pl = self.application.project.getByPid(pl_pid)
        dt = self.application.project.getByPid(dt_pid)

        if dt is not None:
            data = dt.data
            if not self.ca:
                self.ca = cops_analyze(self.application, sg, data_table=data)

        else:
            if not self.ca:
                self.ca = cops_analyze(self.application, sg, data_table=None, peak_list=pl)
            data = self.ca.tb
        self.ca.set_CB(self.calculate_CB.isChecked())
        assignMatrix = self.updateMatchesByLineshape(self.ca, nmrResidue, assignMatrix, data)

        if plot: # TODO Plotting should be an option.
            fig = self.ca.plot_matches(nmrResidue, assignMatrix)
            fig.show()

        return assignMatrix

    def _change_Res(self, data):
        if not self.ca:
            self._initialize_analyzer()
        self.ca.updateNmrResidue(data['trigger'], data['object'], oldPid=data['oldPid'])

    def _change_Peak(self, data):
        if not self.ca:
            self._initialize_analyzer()
        self.ca.updatePeak(data['trigger'], data['object'])

    def close(self):
        """ de-register anything left or close table etc"""
        self._resChangedNotifier.unRegister()
        self._peakChangedNotifier.unRegister()

## Register the Extension in the BackboneAssignmentModule
from ccpn.AnalysisAssign.modules.BackboneAssignmentModule import BackboneAssignmentModule
BackboneAssignmentModule.registerExtension(BackboneAssignmentModule, COPsExtensionFrame)