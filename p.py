import os, sys, pickle #python modules
import cfg #adi modules

error = False

def gAssets():
	with open(cfg.txtsDir + "assets" + ".p", 'rb') as f:
		try:
			return pickle.load(f)
		except:
			print("Error getting list of imported assets.")
			input("Relaunch ADI.")
			sys.exit()
		
def sAssets(assets):
	with open(cfg.txtsDir + "assets" + ".p", 'wb') as f:
		try:
			pickle.dump(assets, f)
		except:
			print("Error saving asset file to pickle directory. Do you have permissions there?")
			input("Check settings.cfg and relaunch ADI.")
			sys.exit()
		
def gInstalled():
	with open(cfg.txtsDir + "installed" + ".p", 'rb') as f:
		try:
			return pickle.load(f)
		except:
			print("Error getting list of installed assets.")
			input("Relaunch ADI.")
			sys.exit()
		
def sInstalled(installed):
	with open(cfg.txtsDir + "installed" + ".p", 'wb') as f:
		try:
			pickle.dump(installed, f)
		except:
			print("Error saving installed assets file to pickle directory. Do you have permissions there?")
			input("Check settings.cfg and relaunch ADI.")
			sys.exit()
		
def gToInstall():
	with open(cfg.txtsDir + "toInstall" + ".p", 'rb') as f:
		try:
			return pickle.load(f)
		except:
			print("Error getting list of assets to install.")
			input("Relaunch ADI to recreate file.")
			sys.exit()
		
def sToInstall(toInstall):
	with open(cfg.txtsDir + "toInstall" + ".p", 'wb') as f:
		try:
			pickle.dump(toInstall, f)
		except:
			print("Error saving toInstall file to pickle directory. Do you have permissions there?")
			input("Check settings.cfg and relaunch ADI.")
			sys.exit()
		
def gToUninstall():
	with open(cfg.txtsDir + "toUninstall" + ".p", 'rb') as f:
		try:
			return pickle.load(f)
		except:
			print("Error getting list of assets to to uninstall.")
			input("Relaunch ADI to recreate file.")
			sys.exit()
		
def sToUninstall(toUninstall):
	with open(cfg.txtsDir + "toUninstall" + ".p", 'wb') as f:
		try:
			pickle.dump(toUninstall, f)
		except:
			print("Error saving toUninstall file to pickle directory. Do you have permissions there?")
			input("Check settings.cfg and relaunch ADI.")
			sys.exit()
		
def sFile(obj, loc):
	with open(loc + ".p", 'wb') as f:
			try:
				pickle.dump(obj, f)
			except:
				print("Error saving asset file to pickle directory. Do you have permissions there?")
				input("Check settings.cfg and relaunch ADI.")
				sys.exit()
				
def gZips():
	try:
		return os.listdir(cfg.zipsDir) #list of all zips in directory
	except:
		print("Error listing assets in zips directory.")
		input("Check settings.cfg and relaunch ADI.")
		sys.exit()
			
def makeDirs():
	error = False
	if not os.path.exists(cfg.zipsDir):
		try:
			os.makedirs(cfg.zipsDir)
		except:
			if cfg.zipsDir == "":
				input("Add your zips directory to settings.cfg and restart ADI.")
				sys.exit()
			print("Cannot create zips folder at " + cfg.zipsDir)
			error = True

	if not os.path.exists(cfg.txtsDir):
		try:
			os.makedirs(cfg.txtsDir)
		except:
			print("Cannot create pickle folder at " + cfg.txtsDir)
			error = True
		
	if not os.path.exists(cfg.dazDir):
		try:
			os.makedirs(cfg.dazDir)
		except:
			if cfg.dazDir == "":
				input("Add your Daz3D directory to settings.cfg and restart ADI.")
				sys.exit()
			else:
				print("Cannot create Daz3D content folder at " + cfg.dazDir)
				error = True
	
	if error:
		input("Check settings.cfg and relaunch ADI. Do you have permissions there?")
		sys.exit()
		
	if not os.path.exists(cfg.txtsDir + "assets" + ".p"): #create assets.p if it does not exist
		assetList = list()
		with open(cfg.txtsDir + "assets" + ".p", 'wb') as f:
			try:
				pickle.dump(assetList, f)
			except:
				print("Error saving assets file to pickle directory. Do you have permissions there?")
				input("Check settings.cfg and relaunch ADI.")
				sys.exit()
		
	toInstall = list()
	with open(cfg.txtsDir + "toInstall" + ".p", 'wb') as f: #overwite toInstall list with blank one
			try:
				pickle.dump(toInstall, f)
			except:
				print("Error saving toInstall file to pickle directory. Do you have permissions there?")
				input("Check settings.cfg and relaunch ADI.")
				sys.exit()

	if not os.path.exists(cfg.txtsDir + "installed.p"): #create installed.p if it does not exist
		installed = list()
		with open(cfg.txtsDir + "installed" + ".p", 'wb') as f: 
				try:
					pickle.dump(installed, f)
				except:
					print("Error saving installed assets file to pickle directory. Do you have permissions there?")
					input("Check settings.cfg and relaunch ADI.")
					sys.exit()
			
	toUninstall = list()
	with open(cfg.txtsDir + "toUninstall" + ".p", 'wb') as f: #overwite toUninstall list with blank one
			try:
				pickle.dump(toUninstall, f)
			except:
				print("Error saving toUninstall file to pickle directory. Do you have permissions there?")
				input("Check settings.cfg and relaunch ADI.")
				sys.exit()