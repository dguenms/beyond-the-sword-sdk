## Sid Meier's Civilization 4
## Copyright Firaxis Games 2005
import CvMainInterface
import CvTechChooser
import CvForeignAdvisor
import CvExoticForeignAdvisor
import CvReligionScreen
import CvCorporationScreen
import CvCivicsScreen
import CvVictoryScreen
import CvEspionageAdvisor

import CvOptionsScreen
import CvReplayScreen
import CvHallOfFameScreen
import CvDanQuayle
import CvUnVictoryScreen

import CvDawnOfMan
import CvTechSplashScreen
import CvTopCivs
import CvInfoScreen

import CvIntroMovieScreen
import CvVictoryMovieScreen
import CvWonderMovieScreen
import CvEraMovieScreen
import CvSpaceShipScreen

# BUG - Sevopedia - start
import SevoScreenEnums
# BUG - Sevopedia - end

import CvWorldBuilderScreen
import CvWorldBuilderDiplomacyScreen

import CvDebugTools
import CvDebugInfoScreen
#import CvDiplomacy

import CvUtil
import CvEventInterface
import CvPopupInterface
import CvScreenUtilsInterface
import ScreenInput as PyScreenInput
from CvScreenEnums import *
from CvPythonExtensions import *

# BUG - Options - end
import BugCore
AdvisorOpt = BugCore.game.Advisors
CustDomAdvOpt = BugCore.game.CustDomAdv
TechWindowOpt = BugCore.game.TechWindow
# BUG - Options - end

g_bIsScreenActive = -1

def toggleSetNoScreens():
	global g_bIsScreenActive
	print "SCREEN OFF"
	g_bIsScreenActive = -1

def toggleSetScreenOn(argsList):
	global g_bIsScreenActive
	print "%s SCREEN TURNED ON" %(argsList[0],)
	g_bIsScreenActive = argsList[0]

#diplomacyScreen = CvDiplomacy.CvDiplomacy()
	
mainInterface = CvMainInterface.CvMainInterface()
def showMainInterface():
	mainInterface.interfaceScreen()

def reinitMainInterface():
	mainInterface.initState()

def numPlotListButtons():
	return mainInterface.numPlotListButtons()

techChooser = CvTechChooser.CvTechChooser()
def showTechChooser():
	if (-1 != CyGame().getActivePlayer()):
		techChooser.interfaceScreen()

hallOfFameScreen = CvHallOfFameScreen.CvHallOfFameScreen(HALL_OF_FAME)
def showHallOfFame(argsList):
	hallOfFameScreen.interfaceScreen(argsList[0])

civicScreen = CvCivicsScreen.CvCivicsScreen()
def showCivicsScreen():
	if (-1 != CyGame().getActivePlayer()):
		civicScreen.interfaceScreen()

religionScreen = CvReligionScreen.CvReligionScreen()
def showReligionScreen():
	if (-1 != CyGame().getActivePlayer()):
		religionScreen.interfaceScreen()

corporationScreen = CvCorporationScreen.CvCorporationScreen()
def showCorporationScreen():
	if (-1 != CyGame().getActivePlayer()):
		corporationScreen.interfaceScreen()

optionsScreen = CvOptionsScreen.CvOptionsScreen()
def showOptionsScreen():
	optionsScreen.interfaceScreen()

#foreignAdvisor = CvForeignAdvisor.CvForeignAdvisor()
foreignAdvisor = CvExoticForeignAdvisor.CvExoticForeignAdvisor()
def showForeignAdvisorScreen(argsList):
	if (-1 != CyGame().getActivePlayer()):
		foreignAdvisor.interfaceScreen(argsList[0])

# BUG - Finance Advisor - start
financeAdvisor = None
def createFinanceAdvisor():
	"""Creates the correct Finance Advisor based on an option."""
	global financeAdvisor
	if financeAdvisor is None:
		if (AdvisorOpt.isBugFinanceAdvisor()):
			import BugFinanceAdvisor
			financeAdvisor = BugFinanceAdvisor.BugFinanceAdvisor()
		else:
			import CvFinanceAdvisor
			financeAdvisor = CvFinanceAdvisor.CvFinanceAdvisor()
		HandleInputMap[FINANCE_ADVISOR] = financeAdvisor
# BUG - Finance Advisor - end
			
def showFinanceAdvisor():
	if (-1 != CyGame().getActivePlayer()):
		financeAdvisor.interfaceScreen()

# BUG - CustDomAdv - start
domesticAdvisor = None
def createDomesticAdvisor():
	"""Creates the correct Domestic Advisor based on an option."""
	global domesticAdvisor
	if domesticAdvisor is None:
		if (CustDomAdvOpt.isEnabled()):
			import CvCustomizableDomesticAdvisor
			domesticAdvisor = CvCustomizableDomesticAdvisor.CvCustomizableDomesticAdvisor()
		else:
			import CvDomesticAdvisor
			domesticAdvisor = CvDomesticAdvisor.CvDomesticAdvisor()
		HandleInputMap[DOMESTIC_ADVISOR] = domesticAdvisor
# BUG - CustDomAdv - end

def showDomesticAdvisor(argsList):
	if (-1 != CyGame().getActivePlayer()):
		domesticAdvisor.interfaceScreen()

# BUG - Military Advisor - start
militaryAdvisor = None
def createMilitaryAdvisor():
	"""Creates the correct Military Advisor based on an option."""
	global militaryAdvisor
	if militaryAdvisor is None:
		if (AdvisorOpt.isBUG_MA()):
			import CvBUGMilitaryAdvisor
			militaryAdvisor = CvBUGMilitaryAdvisor.CvMilitaryAdvisor(MILITARY_ADVISOR)
		else:
			import CvMilitaryAdvisor
			militaryAdvisor = CvMilitaryAdvisor.CvMilitaryAdvisor(MILITARY_ADVISOR)
		HandleInputMap[MILITARY_ADVISOR] = militaryAdvisor

def showMilitaryAdvisor():
	if (-1 != CyGame().getActivePlayer()):
		if (AdvisorOpt.isBUG_MA()):
			# TODO: move to CvBUGMilitaryAdvisor.interfaceScreen()
			militaryAdvisor.IconGridActive = False
		militaryAdvisor.interfaceScreen()
# BUG - Military Advisor - end

espionageAdvisor = CvEspionageAdvisor.CvEspionageAdvisor()
def showEspionageAdvisor():
	if (-1 != CyGame().getActivePlayer()):
		espionageAdvisor.interfaceScreen()

dawnOfMan = CvDawnOfMan.CvDawnOfMan(DAWN_OF_MAN)
def showDawnOfMan(argsList):
	dawnOfMan.interfaceScreen()

introMovie = CvIntroMovieScreen.CvIntroMovieScreen()
def showIntroMovie(argsList):
	introMovie.interfaceScreen()
	
victoryMovie = CvVictoryMovieScreen.CvVictoryMovieScreen()
def showVictoryMovie(argsList):
	victoryMovie.interfaceScreen(argsList[0])
	
wonderMovie = CvWonderMovieScreen.CvWonderMovieScreen()
def showWonderMovie(argsList):
	wonderMovie.interfaceScreen(argsList[0], argsList[1], argsList[2])

eraMovie = CvEraMovieScreen.CvEraMovieScreen()
def showEraMovie(argsList):
	eraMovie.interfaceScreen(argsList[0])
	
spaceShip = CvSpaceShipScreen.CvSpaceShipScreen()
def showSpaceShip(argsList):
	if (-1 != CyGame().getActivePlayer()):
		spaceShip.interfaceScreen(argsList[0])
	
replayScreen = CvReplayScreen.CvReplayScreen(REPLAY_SCREEN)
def showReplay(argsList):
	if argsList[0] > -1:
		CyGame().saveReplay(argsList[0])
	replayScreen.showScreen(argsList[4])

danQuayleScreen = CvDanQuayle.CvDanQuayle()
def showDanQuayleScreen(argsList):
	danQuayleScreen.interfaceScreen()

unVictoryScreen = CvUnVictoryScreen.CvUnVictoryScreen()
def showUnVictoryScreen(argsList):
	unVictoryScreen.interfaceScreen()

topCivs = CvTopCivs.CvTopCivs()
def showTopCivs():
	topCivs.showScreen()

infoScreen = CvInfoScreen.CvInfoScreen(INFO_SCREEN)
def showInfoScreen(argsList):
	if (-1 != CyGame().getActivePlayer()):
		iTabID = argsList[0]
		iEndGame = argsList[1]
		infoScreen.showScreen(-1, iTabID, iEndGame)

debugInfoScreen = CvDebugInfoScreen.CvDebugInfoScreen()
def showDebugInfoScreen():
	debugInfoScreen.interfaceScreen()

# BUG - Tech Splash Screen - start
techSplashScreen = None
def createTechSplash():
	"""Creates the correct Tech Splash Screen based on an option."""
	global techSplashScreen
	if techSplashScreen is None:
		if (TechWindowOpt.isDetailedView()):
			import TechWindow
			techSplashScreen = TechWindow.CvTechSplashScreen(TECH_SPLASH)
		elif (TechWindowOpt.isWideView()):
			import TechWindowWide
			techSplashScreen = TechWindowWide.CvTechSplashScreen(TECH_SPLASH)
		else:
			import CvTechSplashScreen
			techSplashScreen = CvTechSplashScreen.CvTechSplashScreen(TECH_SPLASH)
	HandleInputMap[TECH_SPLASH] = techSplashScreen

def deleteTechSplash(option=None, value=None):
	global techSplashScreen
	techSplashScreen = None
	if TECH_SPLASH in HandleInputMap:
		del HandleInputMap[TECH_SPLASH]

def showTechSplash(argsList):
	if techSplashScreen is None:
		createTechSplash()
	techSplashScreen.interfaceScreen(argsList[0])
# BUG - Tech Splash Screen - end

victoryScreen = CvVictoryScreen.CvVictoryScreen(VICTORY_SCREEN)
def showVictoryScreen():
	if (-1 != CyGame().getActivePlayer()):
		victoryScreen.interfaceScreen()

# BUG - Sevopedia - start

pediaMainScreen = None
bUsingSevopedia = False
def createCivilopedia():
	"""Creates the correct Civilopedia based on an option."""
	global pediaMainScreen
	global bUsingSevopedia
	if pediaMainScreen is None:
		import SevoPediaUtil
		if (AdvisorOpt.Sevopedia()):
			import SevoPediaMain
			import SevoPediaHistory
			bUsingSevopedia = True
			pediaMainScreen = SevoPediaMain.SevoPediaMain()
		else:
			import CvPediaMain
			import CvPediaHistory
			bUsingSevopedia = False
			pediaMainScreen = CvPediaMain.CvPediaMain()
		HandleInputMap.update(
							{
								PEDIA_MAIN : pediaMainScreen,
								PEDIA_TECH : pediaMainScreen,
								PEDIA_UNIT : pediaMainScreen,
								PEDIA_BUILDING : pediaMainScreen,
								PEDIA_PROMOTION : pediaMainScreen,
								PEDIA_PROJECT : pediaMainScreen,
								PEDIA_UNIT_CHART : pediaMainScreen,
								PEDIA_BONUS : pediaMainScreen,
								PEDIA_IMPROVEMENT : pediaMainScreen,
								PEDIA_TERRAIN : pediaMainScreen,
								PEDIA_FEATURE : pediaMainScreen,
								PEDIA_CIVIC : pediaMainScreen,
								PEDIA_CIVILIZATION : pediaMainScreen,
								PEDIA_LEADER : pediaMainScreen,
								PEDIA_RELIGION : pediaMainScreen,
								PEDIA_CORPORATION : pediaMainScreen,
								PEDIA_HISTORY : pediaMainScreen,
								
								SevoScreenEnums.PEDIA_MAIN		: pediaMainScreen,
								SevoScreenEnums.PEDIA_TECHS		: pediaMainScreen,
								SevoScreenEnums.PEDIA_UNITS		: pediaMainScreen,
								SevoScreenEnums.PEDIA_UNIT_UPGRADES	: pediaMainScreen,
								SevoScreenEnums.PEDIA_UNIT_CATEGORIES	: pediaMainScreen,
								SevoScreenEnums.PEDIA_PROMOTIONS	: pediaMainScreen,
								SevoScreenEnums.PEDIA_PROMOTION_TREE	: pediaMainScreen,
								SevoScreenEnums.PEDIA_BUILDINGS		: pediaMainScreen,
								SevoScreenEnums.PEDIA_NATIONAL_WONDERS	: pediaMainScreen,
								SevoScreenEnums.PEDIA_GREAT_WONDERS	: pediaMainScreen,
								SevoScreenEnums.PEDIA_PROJECTS		: pediaMainScreen,
								SevoScreenEnums.PEDIA_SPECIALISTS	: pediaMainScreen,
								SevoScreenEnums.PEDIA_TERRAINS		: pediaMainScreen,
								SevoScreenEnums.PEDIA_FEATURES		: pediaMainScreen,
								SevoScreenEnums.PEDIA_BONUSES		: pediaMainScreen,
								SevoScreenEnums.PEDIA_IMPROVEMENTS	: pediaMainScreen,
								SevoScreenEnums.PEDIA_CIVS		: pediaMainScreen,
								SevoScreenEnums.PEDIA_LEADERS		: pediaMainScreen,
								SevoScreenEnums.PEDIA_TRAITS		: pediaMainScreen,
								SevoScreenEnums.PEDIA_CIVICS		: pediaMainScreen,
								SevoScreenEnums.PEDIA_RELIGIONS		: pediaMainScreen,
								SevoScreenEnums.PEDIA_CORPORATIONS	: pediaMainScreen,
								SevoScreenEnums.PEDIA_CONCEPTS		: pediaMainScreen,
								SevoScreenEnums.PEDIA_BTS_CONCEPTS	: pediaMainScreen,
								SevoScreenEnums.PEDIA_HINTS		: pediaMainScreen,
								SevoScreenEnums.PEDIA_SHORTCUTS		: pediaMainScreen,
							})
		global HandleNavigationMap
		HandleNavigationMap = {
							MAIN_INTERFACE : mainInterface,
							PEDIA_MAIN : pediaMainScreen,
							PEDIA_TECH : pediaMainScreen,
							PEDIA_UNIT : pediaMainScreen,
							PEDIA_BUILDING : pediaMainScreen,
							PEDIA_PROMOTION : pediaMainScreen,
							PEDIA_PROJECT : pediaMainScreen,
							PEDIA_UNIT_CHART : pediaMainScreen,
							PEDIA_BONUS : pediaMainScreen,
							PEDIA_IMPROVEMENT : pediaMainScreen,
							PEDIA_TERRAIN : pediaMainScreen,
							PEDIA_FEATURE : pediaMainScreen,
							PEDIA_CIVIC : pediaMainScreen,
							PEDIA_CIVILIZATION : pediaMainScreen,
							PEDIA_LEADER : pediaMainScreen,
							PEDIA_HISTORY : pediaMainScreen,
							PEDIA_RELIGION : pediaMainScreen,
							PEDIA_CORPORATION : pediaMainScreen,
							
							SevoScreenEnums.PEDIA_MAIN		: pediaMainScreen,
							SevoScreenEnums.PEDIA_TECHS		: pediaMainScreen,
							SevoScreenEnums.PEDIA_UNITS		: pediaMainScreen,
							SevoScreenEnums.PEDIA_UNIT_UPGRADES	: pediaMainScreen,
							SevoScreenEnums.PEDIA_UNIT_CATEGORIES	: pediaMainScreen,
							SevoScreenEnums.PEDIA_PROMOTIONS	: pediaMainScreen,
							SevoScreenEnums.PEDIA_PROMOTION_TREE	: pediaMainScreen,
							SevoScreenEnums.PEDIA_BUILDINGS		: pediaMainScreen,
							SevoScreenEnums.PEDIA_NATIONAL_WONDERS	: pediaMainScreen,
							SevoScreenEnums.PEDIA_GREAT_WONDERS	: pediaMainScreen,
							SevoScreenEnums.PEDIA_PROJECTS		: pediaMainScreen,
							SevoScreenEnums.PEDIA_SPECIALISTS	: pediaMainScreen,
							SevoScreenEnums.PEDIA_TERRAINS		: pediaMainScreen,
							SevoScreenEnums.PEDIA_FEATURES		: pediaMainScreen,
							SevoScreenEnums.PEDIA_BONUSES		: pediaMainScreen,
							SevoScreenEnums.PEDIA_IMPROVEMENTS	: pediaMainScreen,
							SevoScreenEnums.PEDIA_CIVS		 	: pediaMainScreen,
							SevoScreenEnums.PEDIA_LEADERS		: pediaMainScreen,
							SevoScreenEnums.PEDIA_TRAITS		: pediaMainScreen,
							SevoScreenEnums.PEDIA_CIVICS		: pediaMainScreen,
							SevoScreenEnums.PEDIA_RELIGIONS		: pediaMainScreen,
							SevoScreenEnums.PEDIA_CORPORATIONS	: pediaMainScreen,
							SevoScreenEnums.PEDIA_CONCEPTS		: pediaMainScreen,
							SevoScreenEnums.PEDIA_BTS_CONCEPTS	: pediaMainScreen,
							SevoScreenEnums.PEDIA_HINTS			: pediaMainScreen,
							SevoScreenEnums.PEDIA_SHORTCUTS		: pediaMainScreen,
						}

def linkToPedia(argsList):
	pediaMainScreen.link(argsList[0])

def pediaShow():
	createCivilopedia()
	return pediaMainScreen.pediaShow()

def pediaBack():
	return pediaMainScreen.back()

def pediaForward():
	return pediaMainScreen.forward()

def pediaMain(argsList):
	if (bUsingSevopedia):
		pediaMainScreen.pediaJump(SevoScreenEnums.PEDIA_MAIN, argsList[0], True, False)
	else:
		pediaMainScreen.pediaJump(PEDIA_MAIN, argsList[0], True)

def pediaJumpToTech(argsList):
	if (bUsingSevopedia):
		pediaMainScreen.pediaJump(SevoScreenEnums.PEDIA_TECHS, argsList[0], True, False)
	else:
		pediaMainScreen.pediaJump(PEDIA_TECH, argsList[0], True)

def pediaJumpToUnit(argsList):
	if (bUsingSevopedia):
		pediaMainScreen.pediaJump(SevoScreenEnums.PEDIA_UNITS, argsList[0], True, False)
	else:
		pediaMainScreen.pediaJump(PEDIA_UNIT, argsList[0], True)

def pediaJumpToUnitChart(argsList):
	if (bUsingSevopedia):
		pediaMainScreen.pediaJump(SevoScreenEnums.PEDIA_UNIT_CATEGORIES, argsList[0], True, False)
	else:
		pediaMainScreen.pediaJump(PEDIA_UNIT_CHART, argsList[0], True)

def pediaJumpToPromotion(argsList):
	if (bUsingSevopedia):
		pediaMainScreen.pediaJump(SevoScreenEnums.PEDIA_PROMOTIONS, argsList[0], True, False)
	else:
		pediaMainScreen.pediaJump(PEDIA_PROMOTION, argsList[0], True)

def pediaJumpToBuilding(argsList):
	if (bUsingSevopedia):
		pediaMainScreen.pediaJump(SevoScreenEnums.PEDIA_BUILDINGS, argsList[0], True, False)
	else:
		pediaMainScreen.pediaJump(PEDIA_BUILDING, argsList[0], True)

def pediaJumpToProject(argsList):
	if (bUsingSevopedia):
		pediaMainScreen.pediaJump(SevoScreenEnums.PEDIA_PROJECTS, argsList[0], True, False)
	else:
		pediaMainScreen.pediaJump(PEDIA_PROJECT, argsList[0], True)

def pediaJumpToSpecialist(argsList):
	if (bUsingSevopedia):
		pediaMainScreen.pediaJump(SevoScreenEnums.PEDIA_SPECIALISTS, argsList[0], True, False)
	else:
		pediaMainScreen.pediaJump(PEDIA_SPECIALIST, argsList[0], True)

def pediaJumpToTerrain(argsList):
	if (bUsingSevopedia):
		pediaMainScreen.pediaJump(SevoScreenEnums.PEDIA_TERRAINS, argsList[0], True, False)
	else:
		pediaMainScreen.pediaJump(PEDIA_TERRAIN, argsList[0], True)

def pediaJumpToFeature(argsList):
	if (bUsingSevopedia):
		pediaMainScreen.pediaJump(SevoScreenEnums.PEDIA_FEATURES, argsList[0], True, False)
	else:
		pediaMainScreen.pediaJump(PEDIA_FEATURE, argsList[0], True)

def pediaJumpToBonus(argsList):
	if (bUsingSevopedia):
		pediaMainScreen.pediaJump(SevoScreenEnums.PEDIA_BONUSES, argsList[0], True, False)
	else:
		pediaMainScreen.pediaJump(PEDIA_BONUS, argsList[0], True)

def pediaJumpToImprovement(argsList):
	if (bUsingSevopedia):
		pediaMainScreen.pediaJump(SevoScreenEnums.PEDIA_IMPROVEMENTS, argsList[0], True, False)
	else:
		pediaMainScreen.pediaJump(PEDIA_IMPROVEMENT, argsList[0], True)

def pediaJumpToCiv(argsList):
	if (bUsingSevopedia):
		pediaMainScreen.pediaJump(SevoScreenEnums.PEDIA_CIVS, argsList[0], True, False)
	else:
		pediaMainScreen.pediaJump(PEDIA_CIVILIZATION, argsList[0], True)

def pediaJumpToLeader(argsList):
	if (bUsingSevopedia):
		pediaMainScreen.pediaJump(SevoScreenEnums.PEDIA_LEADERS, argsList[0], True, False)
	else:
		pediaMainScreen.pediaJump(PEDIA_LEADER, argsList[0], True)

def pediaJumpToCivic(argsList):
	if (bUsingSevopedia):
		pediaMainScreen.pediaJump(SevoScreenEnums.PEDIA_CIVICS, argsList[0], True, False)
	else:
		pediaMainScreen.pediaJump(PEDIA_CIVIC, argsList[0], True)

def pediaJumpToReligion(argsList):
	if (bUsingSevopedia):
		pediaMainScreen.pediaJump(SevoScreenEnums.PEDIA_RELIGIONS, argsList[0], True, False)
	else:
		pediaMainScreen.pediaJump(PEDIA_RELIGION, argsList[0], True)

def pediaJumpToCorporation(argsList):
	if (bUsingSevopedia):
		pediaMainScreen.pediaJump(SevoScreenEnums.PEDIA_CORPORATIONS, argsList[0], True, False)
	else:
		pediaMainScreen.pediaJump(PEDIA_CORPORATION, argsList[0], True)

def pediaShowHistorical(argsList):
	if (bUsingSevopedia):
		if (argsList[0] == CivilopediaPageTypes.CIVILOPEDIA_PAGE_CONCEPT_NEW):
			pediaMainScreen.pediaJump(SevoScreenEnums.PEDIA_BTS_CONCEPTS, argsList[1], True, False)
		else:
			pediaMainScreen.pediaJump(SevoScreenEnums.PEDIA_CONCEPTS, argsList[1], True, False)
	else:
		iEntryId = pediaMainScreen.pediaHistorical.getIdFromEntryInfo(argsList[0], argsList[1])
		pediaMainScreen.pediaJump(PEDIA_HISTORY, iEntryId, True)

# BUG - Sevopedia - end

#################################################
## Worldbuilder
#################################################
worldBuilderScreen = CvWorldBuilderScreen.CvWorldBuilderScreen()
def getWorldBuilderScreen():
	return worldBuilderScreen

def showWorldBuilderScreen():
	worldBuilderScreen.interfaceScreen()

def hideWorldBuilderScreen():
	worldBuilderScreen.killScreen()

def WorldBuilderToggleUnitEditCB():
	worldBuilderScreen.toggleUnitEditCB()

def WorldBuilderAllPlotsCB():
	CvEventInterface.beginEvent(CvUtil.EventWBAllPlotsPopup)

def WorldBuilderEraseCB():
	worldBuilderScreen.eraseCB()

def WorldBuilderLandmarkCB():
	worldBuilderScreen.landmarkModeCB()

def WorldBuilderExitCB():
	worldBuilderScreen.Exit()

def WorldBuilderToggleCityEditCB():
	worldBuilderScreen.toggleCityEditCB()

def WorldBuilderNormalPlayerTabModeCB():
	worldBuilderScreen.normalPlayerTabModeCB()

def WorldBuilderNormalMapTabModeCB():
	worldBuilderScreen.normalMapTabModeCB()

def WorldBuilderRevealTabModeCB():
	worldBuilderScreen.revealTabModeCB()

def WorldBuilderDiplomacyModeCB():
	worldBuilderScreen.diplomacyModeCB()

def WorldBuilderRevealAllCB():
	worldBuilderScreen.revealAll(True)

def WorldBuilderUnRevealAllCB():
	worldBuilderScreen.revealAll(False)

def WorldBuilderHandleUnitCB( argsList ):
	worldBuilderScreen.handleUnitCB(argsList)

def WorldBuilderHandleTerrainCB( argsList ):
	worldBuilderScreen.handleTerrainCB(argsList)

def WorldBuilderHandleFeatureCB(argsList):
	worldBuilderScreen.handleFeatureCB(argsList)

def WorldBuilderHandleBonusCB( argsList ):
	worldBuilderScreen.handleBonusCB(argsList)

def WorldBuilderHandleImprovementCB(argsList):
	worldBuilderScreen.handleImprovementCB(argsList)

def WorldBuilderHandleTerritoryCB(argsList):
	worldBuilderScreen.handleTerritoryCB(argsList)

def WorldBuilderHandlePlotTypeCB( argsList ):
	worldBuilderScreen.handlePlotTypeCB(argsList)

def WorldBuilderHandleAllPlotsCB( argsList ):
	worldBuilderScreen.handleAllPlotsCB(argsList)

def WorldBuilderHandleUnitEditExperienceCB( argsList ):
	worldBuilderScreen.handleUnitEditExperienceCB(argsList)
	
def WorldBuilderHandleUnitEditLevelCB( argsList ):
	worldBuilderScreen.handleUnitEditLevelCB(argsList)
	
def WorldBuilderHandleUnitEditNameCB( argsList ):
	worldBuilderScreen.handleUnitEditNameCB(argsList)
	
def WorldBuilderHandleCityEditPopulationCB( argsList ):
	worldBuilderScreen.handleCityEditPopulationCB(argsList)

def WorldBuilderHandleCityEditCultureCB( argsList ):
	worldBuilderScreen.handleCityEditCultureCB(argsList)

def WorldBuilderHandleCityEditGoldCB( argsList ):
	worldBuilderScreen.handleCityEditGoldCB(argsList)

def WorldBuilderHandleCityEditAddScriptCB( argsList ):
	worldBuilderScreen.getCityScript()

def WorldBuilderHandleUnitEditAddScriptCB( argsList ):
	worldBuilderScreen.getUnitScript()

def WorldBuilderHandleCityEditNameCB( argsList ):
	worldBuilderScreen.handleCityEditNameCB(argsList)

def WorldBuilderHandleLandmarkTextCB( argsList ):
	worldBuilderScreen.handleLandmarkTextCB(argsList)

def WorldBuilderHandleUnitEditPullDownCB( argsList ):
	worldBuilderScreen.handleUnitEditPullDownCB(argsList)

def WorldBuilderHandleUnitAITypeEditPullDownCB( argsList ):
	worldBuilderScreen.handleUnitAITypeEditPullDownCB(argsList)

def WorldBuilderHandlePlayerEditPullDownCB( argsList ):
	worldBuilderScreen.handlePlayerEditPullDownCB(argsList)

def WorldBuilderHandlePlayerUnitPullDownCB( argsList ):
	worldBuilderScreen.handlePlayerUnitPullDownCB(argsList)

def WorldBuilderHandleSelectTeamPullDownCB( argsList ):
	worldBuilderScreen.handleSelectTeamPullDownCB(argsList)

def WorldBuilderHandlePromotionCB( argsList ):
	worldBuilderScreen.handlePromotionCB(argsList)

def WorldBuilderHandleBuildingCB( argsList ):
	worldBuilderScreen.handleBuildingCB(argsList)

def WorldBuilderHandleTechCB( argsList ):
	worldBuilderScreen.handleTechCB(argsList)

def WorldBuilderHandleRouteCB( argsList ):
	worldBuilderScreen.handleRouteCB(argsList)

def WorldBuilderHandleEditCityBuildingCB( argsList ):
	worldBuilderScreen.handleEditCityBuildingCB(argsList)

def WorldBuilderHandleBrushWidthCB( argsList ):
	worldBuilderScreen.handleBrushWidthCB(argsList)

def WorldBuilderHandleBrushHeightCB( argsList ):
	worldBuilderScreen.handleBrushHeightCB(argsList)

def WorldBuilderHandleLandmarkCB( argsList ):
	worldBuilderScreen.handleLandmarkCB(argsList)

def WorldBuilderHandleFlyoutMenuCB( argsList ):
	worldBuilderScreen.handleFlyoutMenuCB(argsList)

def WorldBuilderGetHighlightPlot(argsList):
	return worldBuilderScreen.getHighlightPlot(argsList)

def WorldBuilderOnAdvancedStartBrushSelected(argsList):
	iList,iIndex,iTab = argsList;
	print("WB Advanced Start brush selected, iList=%d, iIndex=%d, type=%d" %(iList,iIndex,iTab))	
	if (iTab == worldBuilderScreen.m_iASTechTabID):
		showTechChooser()
	elif (iTab == worldBuilderScreen.m_iASCityTabID and iList == worldBuilderScreen.m_iASAutomateListID):
		CyMessageControl().sendAdvancedStartAction(AdvancedStartActionTypes.ADVANCEDSTARTACTION_AUTOMATE, worldBuilderScreen.m_iCurrentPlayer, -1, -1, -1, true)
		
	if (worldBuilderScreen.setCurrentAdvancedStartIndex(iIndex)):
		if (worldBuilderScreen.setCurrentAdvancedStartList(iList)):
			return 1
	return 0

def WorldBuilderOnNormalPlayerBrushSelected(argsList):
	iList,iIndex,iTab = argsList;
	print("WB brush selected, iList=%d, iIndex=%d, type=%d" %(iList,iIndex,iTab))	
	if (worldBuilderScreen.setCurrentNormalPlayerIndex(iIndex)):
		return 1
	return 0

def WorldBuilderOnNormalMapBrushSelected(argsList):
	iList,iIndex,iTab = argsList;
	print("WB brush selected, iList=%d, iIndex=%d, type=%d" %(iList,iIndex,iTab))	
	if (worldBuilderScreen.setCurrentNormalMapIndex(iIndex)):
		if (worldBuilderScreen.setCurrentNormalMapList(iList)):
			return 1
	return 0

def WorldBuilderOnWBEditBrushSelected(argsList):
	iList,iIndex,iTab = argsList;
	if (worldBuilderScreen.setEditButtonClicked(iIndex)):
		return 1
	return 0

def WorldBuilderOnWBEditReligionSelected(argsList):
	iList,iIndex,iTab = argsList;
	if (worldBuilderScreen.setEditReligionSelected(iIndex)):
		return 1
	return 0

def WorldBuilderOnWBEditHolyCitySelected(argsList):
	iList,iIndex,iTab = argsList;
	if (worldBuilderScreen.setEditHolyCitySelected(iIndex)):
		return 1
	return 0

def WorldBuilderOnWBEditCorporationSelected(argsList):
	iList,iIndex,iTab = argsList;
	if (worldBuilderScreen.setEditCorporationSelected(iIndex)):
		return 1
	return 0

def WorldBuilderOnWBEditHeadquartersSelected(argsList):
	iList,iIndex,iTab = argsList;
	if (worldBuilderScreen.setEditHeadquartersSelected(iIndex)):
		return 1
	return 0

def WorldBuilderOnAllPlotsBrushSelected(argsList):
	if (worldBuilderScreen.handleAllPlotsCB(argsList)):
		return 1
	return 0

def WorldBuilderGetASUnitTabID():
	return worldBuilderScreen.getASUnitTabID()

def WorldBuilderGetASCityTabID():
	return worldBuilderScreen.getASCityTabID()

def WorldBuilderGetASCityListID():
	return worldBuilderScreen.getASCityListID()

def WorldBuilderGetASBuildingsListID():
	return worldBuilderScreen.getASBuildingsListID()

def WorldBuilderGetASAutomateListID():
	return worldBuilderScreen.getASAutomateListID()

def WorldBuilderGetASImprovementsTabID():
	return worldBuilderScreen.getASImprovementsTabID()

def WorldBuilderGetASRoutesListID():
	return worldBuilderScreen.getASRoutesListID()

def WorldBuilderGetASImprovementsListID():
	return worldBuilderScreen.getASImprovementsListID()

def WorldBuilderGetASVisibilityTabID():
	return worldBuilderScreen.getASVisibilityTabID()

def WorldBuilderGetASTechTabID():
	return worldBuilderScreen.getASTechTabID()

def WorldBuilderGetUnitTabID():
	return worldBuilderScreen.getUnitTabID()

def WorldBuilderGetBuildingTabID():
	return worldBuilderScreen.getBuildingTabID()

def WorldBuilderGetTechnologyTabID():
	return worldBuilderScreen.getTechnologyTabID()

def WorldBuilderGetImprovementTabID():
	return worldBuilderScreen.getImprovementTabID()

def WorldBuilderGetBonusTabID():
	return worldBuilderScreen.getBonusTabID()

def WorldBuilderGetImprovementListID():
	return worldBuilderScreen.getImprovementListID()

def WorldBuilderGetBonusListID():
	return worldBuilderScreen.getBonusListID()

def WorldBuilderGetTerrainTabID():
	return worldBuilderScreen.getTerrainTabID()

def WorldBuilderGetTerrainListID():
	return worldBuilderScreen.getTerrainListID()

def WorldBuilderGetFeatureListID():
	return worldBuilderScreen.getFeatureListID()

def WorldBuilderGetPlotTypeListID():
	return worldBuilderScreen.getPlotTypeListID()

def WorldBuilderGetRouteListID():
	return worldBuilderScreen.getRouteListID()

def WorldBuilderGetTerritoryTabID():
	return worldBuilderScreen.getTerritoryTabID()

def WorldBuilderGetTerritoryListID():
	return worldBuilderScreen.getTerritoryListID()

def WorldBuilderHasTech(argsList):
	iTech = argsList[0]
	return worldBuilderScreen.hasTech(iTech)

def WorldBuilderHasPromotion(argsList):
	iPromotion = argsList[0]
	return worldBuilderScreen.hasPromotion(iPromotion)

def WorldBuilderHasBuilding(argsList):
	iBuilding = argsList[0]
	return worldBuilderScreen.getNumBuilding(iBuilding)

def WorldBuilderHasReligion(argsList):
	iReligion = argsList[0]
	return worldBuilderScreen.hasReligion(iReligion)

def WorldBuilderHasHolyCity(argsList):
	iReligion = argsList[0]
	return worldBuilderScreen.hasHolyCity(iReligion)

def WorldBuilderHasCorporation(argsList):
	iCorporation = argsList[0]
	return worldBuilderScreen.hasCorporation(iCorporation)

def WorldBuilderHasHeadquarters(argsList):
	iCorporation = argsList[0]
	return worldBuilderScreen.hasHeadquarters(iCorporation)

def WorldBuilderHandleDiploPlayerDropdownCB( argsList ):
	worldBuilderScreen.handleDiploPlayerDropdownCB(argsList)
	
##### WORLDBUILDER DIPLOMACY SCREEN #####

worldBuilderDiplomacyScreen = CvWorldBuilderDiplomacyScreen.CvWorldBuilderDiplomacyScreen()
def showWorldBuilderDiplomacyScreen():
	worldBuilderDiplomacyScreen.interfaceScreen()

def hideWorldBuilderDiplomacyScreen():
	worldBuilderDiplomacyScreen.killScreen()

def handleWorldBuilderDiplomacyPlayerPullDownCB(argsList):
	worldBuilderDiplomacyScreen.handlePlayerPullDownCB(int(argsList[0]))

def handleWorldBuilderDiplomacyVassalPullDownCB(argsList):
	worldBuilderDiplomacyScreen.handleVassalPullDownCB(int(argsList[0]))

def handleWorldBuilderDiplomacyAtWarPullDownCB(argsList):
	worldBuilderDiplomacyScreen.handleAtWarPullDownCB(argsList)

def handleWorldBuilderDiplomacyAIWeightPullDownCB(argsList):
	worldBuilderDiplomacyScreen.handleAIWeightPullDownCB(argsList)

def handleWorldBuilderDiplomacyAIWeightResetAllCB(argsList):
	worldBuilderDiplomacyScreen.handleAIWeightResetAll()

def handleWorldBuilderDiplomacyExitCB(argsList):
	worldBuilderDiplomacyScreen.killScreen()

#################################################
## Utility Functions (can be overridden by CvScreenUtilsInterface
#################################################

def movieDone(argsList):
	# allows overides for mods
	if (CvScreenUtilsInterface.getScreenUtils().movieDone(argsList)):
		return
	
	if (argsList[0] == INTRO_MOVIE_SCREEN):
		introMovie.hideScreen()

	if (argsList[0] == VICTORY_MOVIE_SCREEN):
		victoryMovie.hideScreen()

def leftMouseDown (argsList):
	# allows overides for mods
	if (CvScreenUtilsInterface.getScreenUtils().leftMouseDown(argsList)):
		return
	
	if ( argsList[0] == WORLDBUILDER_SCREEN ):
		worldBuilderScreen.leftMouseDown(argsList[1:])
		return 1
	return 0
		
def rightMouseDown (argsList):
	# allows overides for mods
	if (CvScreenUtilsInterface.getScreenUtils().rightMouseDown(argsList)):
		return
	
	if ( argsList[0] == WORLDBUILDER_SCREEN ):
		worldBuilderScreen.rightMouseDown(argsList)
		return 1
	return 0

def mouseOverPlot (argsList):
	# allows overides for mods
	if (CvScreenUtilsInterface.getScreenUtils().mouseOverPlot(argsList)):
		return
	
	if (WORLDBUILDER_SCREEN == argsList[0]):
		worldBuilderScreen.mouseOverPlot(argsList)

def handleInput (argsList):
	' handle input is called when a screen is up '
	inputClass = PyScreenInput.ScreenInput(argsList)
	
	# allows overides for mods
	ret = CvScreenUtilsInterface.getScreenUtils().handleInput( (inputClass.getPythonFile(),inputClass) )

	# get the screen that is active from the HandleInputMap Dictionary
	screen = HandleInputMap.get( inputClass.getPythonFile() )
	
	# call handle input on that screen
	if ( screen and not ret):
		return screen.handleInput(inputClass)
	return 0

def update (argsList):
	# allows overides for mods
	if (CvScreenUtilsInterface.getScreenUtils().update(argsList)):
		return
	
	if (HandleInputMap.has_key(argsList[0])):
		screen = HandleInputMap.get(argsList[0])
		screen.update(argsList[1])

def onClose (argsList):
	# allows overides for mods
	if (CvScreenUtilsInterface.getScreenUtils().onClose(argsList)):
		return

	if (HandleCloseMap.has_key(argsList[0])):
		screen = HandleCloseMap.get(argsList[0])
		screen.onClose()
		
# Forced screen update
def forceScreenUpdate (argsList):
	# allows overides for mods
	if (CvScreenUtilsInterface.getScreenUtils().forceScreenUpdate(argsList)):
		return
		
	# Tech chooser update (forced from net message)
	if ( argsList[0] == TECH_CHOOSER ):
		techChooser.updateTechRecords(false)
	# Main interface Screen
	elif ( argsList[0] == MAIN_INTERFACE ):
		mainInterface.updateScreen()
	# world builder Screen
	elif ( argsList[0] == WORLDBUILDER_SCREEN ):
		worldBuilderScreen.updateScreen()
	# world builder diplomacy Screen
	elif ( argsList[0] == WORLDBUILDER_DIPLOMACY_SCREEN ):
		worldBuilderDiplomacyScreen.updateScreen()

# Forced redraw
def forceScreenRedraw (argsList):
	# allows overides for mods
	if (CvScreenUtilsInterface.getScreenUtils().forceScreenRedraw(argsList)):
		return
	
	# Main Interface Screen
	if ( argsList[0] == MAIN_INTERFACE ):
		mainInterface.redraw()
	elif ( argsList[0] == WORLDBUILDER_SCREEN ):
		worldBuilderScreen.redraw()
	elif ( argsList[0] == WORLDBUILDER_DIPLOMACY_SCREEN ):
		worldBuilderDiplomacyScreen.redraw()
	elif ( argsList[0] == TECH_CHOOSER ):
		techChooser.updateTechRecords(true)


def minimapClicked (argsList):
	# allows overides for mods
	if (CvScreenUtilsInterface.getScreenUtils().minimapClicked(argsList)):
		return
	
	if (MILITARY_ADVISOR == argsList[0]):
		militaryAdvisor.minimapClicked()
	return

############################################################################
## Misc Functions
############################################################################

def handleBack(screens):
	for iScreen in screens:
		if (HandleNavigationMap.has_key(iScreen)):
			screen = HandleNavigationMap.get( iScreen )
			screen.back()
	print "Mouse BACK"
	return 0

def handleForward(screens):
	for iScreen in screens:
		if (HandleNavigationMap.has_key(iScreen)):
			screen = HandleNavigationMap.get( iScreen )
			screen.forward()
	print "Mouse FWD"
	return 0

def refreshMilitaryAdvisor (argsList):
	if (1 == argsList[0]):
		militaryAdvisor.refreshSelectedGroup(argsList[1])
	elif (2 == argsList[0]):
		militaryAdvisor.refreshSelectedLeader(argsList[1])
	elif (3 == argsList[0]):
		militaryAdvisor.drawCombatExperience()
	elif (argsList[0] <= 0):
		militaryAdvisor.refreshSelectedUnit(-argsList[0], argsList[1])
	
def updateMusicPath (argsList):
    szPathName = argsList[0]
    optionsScreen.updateMusicPath(szPathName)

def refreshOptionsScreen():
	optionsScreen.refreshScreen()

def cityWarningOnClickedCallback(argsList):
	iButtonId = argsList[0]
	iData1 = argsList[1]
	iData2 = argsList[2]
	iData3 = argsList[3]
	iData4 = argsList[4]
	szText = argsList[5]
	bOption1 = argsList[6]
	bOption2 = argsList[7]
	city = CyGlobalContext().getPlayer(CyGlobalContext().getGame().getActivePlayer()).getCity(iData1)
	if (not city.isNone()):
		if (iButtonId == 0):
			if (city.isProductionProcess()):
				CyMessageControl().sendPushOrder(iData1, iData2, iData3, False, False, False)
			else:
				CyMessageControl().sendPushOrder(iData1, iData2, iData3, False, True, False)
		elif (iButtonId == 2):
			CyInterface().selectCity(city, False)

def cityWarningOnFocusCallback(argsList):
	CyInterface().playGeneralSound("AS2D_ADVISOR_SUGGEST")
	CyInterface().lookAtCityOffset(argsList[0])
	return 0

def liberateOnClickedCallback(argsList):
	iButtonId = argsList[0]
	iData1 = argsList[1]
	iData2 = argsList[2]
	iData3 = argsList[3]
	iData4 = argsList[4]
	szText = argsList[5]
	bOption1 = argsList[6]
	bOption2 = argsList[7]
	city = CyGlobalContext().getPlayer(CyGlobalContext().getGame().getActivePlayer()).getCity(iData1)
	if (not city.isNone()):
		if (iButtonId == 0):
			CyMessageControl().sendDoTask(iData1, TaskTypes.TASK_LIBERATE, 0, -1, False, False, False, False)
		elif (iButtonId == 2):
			CyInterface().selectCity(city, False)

def colonyOnClickedCallback(argsList):
	iButtonId = argsList[0]
	iData1 = argsList[1]
	iData2 = argsList[2]
	iData3 = argsList[3]
	iData4 = argsList[4]
	szText = argsList[5]
	bOption1 = argsList[6]
	bOption2 = argsList[7]
	city = CyGlobalContext().getPlayer(CyGlobalContext().getGame().getActivePlayer()).getCity(iData1)
	if (not city.isNone()):
		if (iButtonId == 0):
			CyMessageControl().sendEmpireSplit(CyGlobalContext().getGame().getActivePlayer(), city.area().getID())
		elif (iButtonId == 2):
			CyInterface().selectCity(city, False)

def featAccomplishedOnClickedCallback(argsList):
	iButtonId = argsList[0]
	iData1 = argsList[1]
	iData2 = argsList[2]
	iData3 = argsList[3]
	iData4 = argsList[4]
	szText = argsList[5]
	bOption1 = argsList[6]
	bOption2 = argsList[7]
	
	if (iButtonId == 1):
		if (iData1 == FeatTypes.FEAT_TRADE_ROUTE):
			showDomesticAdvisor(())
		elif ((iData1 >= FeatTypes.FEAT_UNITCOMBAT_ARCHER) and (iData1 <= FeatTypes.FEAT_UNIT_SPY)):
			showMilitaryAdvisor()
		elif ((iData1 >= FeatTypes.FEAT_COPPER_CONNECTED) and (iData1 <= FeatTypes.FEAT_FOOD_CONNECTED)):
			showForeignAdvisorScreen([0])
		elif ((iData1 == FeatTypes.FEAT_NATIONAL_WONDER)):
			# 2 is for the wonder tab...
			showInfoScreen([2, 0])
		elif ((iData1 >= FeatTypes.FEAT_POPULATION_HALF_MILLION) and (iData1 <= FeatTypes.FEAT_POPULATION_2_BILLION)):
			# 1 is for the demographics tab...
			showInfoScreen([1, 0])
		elif iData1 == FeatTypes.FEAT_CORPORATION_ENABLED:
			showCorporationScreen()

def featAccomplishedOnFocusCallback(argsList):
	iData1 = argsList[0]
	iData2 = argsList[1]
	iData3 = argsList[2]
	iData4 = argsList[3]
	szText = argsList[4]
	bOption1 = argsList[5]
	bOption2 = argsList[6]
	
	CyInterface().playGeneralSound("AS2D_FEAT_ACCOMPLISHED")
	if ((iData1 >= FeatTypes.FEAT_UNITCOMBAT_ARCHER) and (iData1 <= FeatTypes.FEAT_FOOD_CONNECTED)):
		CyInterface().lookAtCityOffset(iData2)
		
	return 0


#######################################################################################
## Handle Close Map
#######################################################################################
HandleCloseMap = {  DAWN_OF_MAN : dawnOfMan,
					SPACE_SHIP_SCREEN : spaceShip,			
					TECH_CHOOSER : techChooser,			
				# add new screens here
				}

#######################################################################################
## Handle Input Map
#######################################################################################
HandleInputMap = {  MAIN_INTERFACE : mainInterface,
#					DOMESTIC_ADVISOR : domesticAdvisor,
					RELIGION_SCREEN : religionScreen,
					CORPORATION_SCREEN : corporationScreen,
					CIVICS_SCREEN : civicScreen,
					TECH_CHOOSER : techChooser,
					FOREIGN_ADVISOR : foreignAdvisor,
#					FINANCE_ADVISOR : financeAdvisor,
#					MILITARY_ADVISOR : militaryAdvisor,
					DAWN_OF_MAN : dawnOfMan,
					WONDER_MOVIE_SCREEN : wonderMovie,
					ERA_MOVIE_SCREEN : eraMovie,
					SPACE_SHIP_SCREEN : spaceShip,
					INTRO_MOVIE_SCREEN : introMovie,
					OPTIONS_SCREEN : optionsScreen,
					INFO_SCREEN : infoScreen,
					REPLAY_SCREEN : replayScreen,
					VICTORY_SCREEN : victoryScreen,
					TOP_CIVS : topCivs,
					HALL_OF_FAME : hallOfFameScreen,
					VICTORY_MOVIE_SCREEN : victoryMovie,
					ESPIONAGE_ADVISOR : espionageAdvisor,
					DAN_QUAYLE_SCREEN : danQuayleScreen,

					WORLDBUILDER_SCREEN : worldBuilderScreen,
					WORLDBUILDER_DIPLOMACY_SCREEN : worldBuilderDiplomacyScreen,
					
					DEBUG_INFO_SCREEN : debugInfoScreen,
				
				# add new screens here
				}

#######################################################################################
## Handle Navigation Map
#######################################################################################
HandleNavigationMap = {}


# BUG - Options - start
def init():
	createDomesticAdvisor()
	createFinanceAdvisor()
	createMilitaryAdvisor()
	createCivilopedia()
	createTechSplash()
# BUG - Options - end
