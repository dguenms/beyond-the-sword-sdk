## CustomCombatOptionsTab
##
## Author: Freaky

import BugOptionsTab

class CustomCombatOptionsTab(BugOptionsTab.BugOptionsTab):
	"Custom Combat Options Screen Tab"
	
	def __init__(self, screen):
		BugOptionsTab.BugOptionsTab.__init__(self, "CustomCombat", "Custom Combat")

	def create(self, screen):
		tab = self.createTab(screen)
		panel = self.createMainPanel(screen)
		column = self.addOneColumnLayout(screen, panel)
	
		self.addCheckbox(screen, column, "CustomCombat__Enabled")

		columnL, columnR = self.addTwoColumnLayout(screen, column, "CustomCombat")
		self.addTextEdit(screen, columnL, columnR, "CustomCombat__MaxCombatRounds")
