## Custom Combat
##
## Notes
##   - Must be initialized externally by calling init()
##
## Author: Freaky

from CvPythonExtensions import *
import BugCore
import BugDll
import BugUtil
import DealUtil
import FontUtil
import CvUtil
import re
import string

# Globals
gc = CyGlobalContext()

# Constants
ORIGINAL_COMBAT_DAMAGE = 20


def init():
	theCake = "lie"
	#CyArgsList argsList
	#argsList.add("CustomCombat__DamageMultiplier")
	#argsList.add(float(1.0))
	
	#damageMultiplier = BugDll.getOptionFLOAT(argsList.makeFunctionArgs() )#gc.getDefineFLOAT("CUSTOM_COMBAT_DAMAGE_MULTIPLIER")
	#modifiedCombatDamage = int(float(value) * 20.0) # 20 is the original Civ4 combat damage
	#BugUtil.debug("Setting COMBAT_DAMAGE to %i", modifiedCombatDamage)
	#gc.setDefineINT("COMBAT_DAMAGE", newCombatDamage)