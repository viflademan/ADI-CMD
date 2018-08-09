import os, sys, zipfile, pickle, shutil, subprocess #python modules
import cfg, p, dsa #adi modules
from pathlib import Path

def makePs(show): #make reference files
	zips = p.gZips()
	assets = p.gAssets() #get list of imported assets
	if show == True:
		print("\n	Assets Imported")
	for file in zips:
		path = Path(cfg.zipsDir) / file
		try:
			zFile = zipfile.ZipFile(path)
		except:
			print("Cannot open asset zip file.")
			input("Check settings.cfg and relaunch ADI.")
			sys.exit()
		asset = list()
		
		assets.append(file[:-4]) #add to asset list without extension
		for name in zFile.namelist():
			if name[:8] == "Content/":
				asset.append(name[8:]) #strip Content/
			elif name[:11] == "My Library/":
				asset.append(name[11:]) #strip My Library/
			else:
				asset.append(name) #strip nothing
		
		if show == True:
			print("\t    " + file[:-4])
		del asset[0]
		
		p.sFile(asset, Path(cfg.txtsDir, file[:-4]))
		zFile.close()
	assets = list(set(assets)) #remove duplicates
	assets = sorted(assets, key=str.lower) #sort alphabetically
	p.sAssets(assets) #save list of imported assets
	
def install(): #install zips
	toInstall = p.gToInstall() #get list of assets to install
	installed = p.gInstalled() #get list of installed assets
	
	print() #skip a line
	for file in toInstall: #loop for every asset in toInstall
		print("\t   Installing " + str(file) + "...", end=' ', flush=True)
		path = cfg.zipsDir / str(file + ".zip") #make zip path
		zFile = zipfile.ZipFile(path) #open the asset's zip file
		zList = zFile.infolist() #list of files in zip file
		importList = [] #make an empty array 
		i = 0
		for member in zFile.namelist(): #for every file in zipfile
			if "Manifest" in member or "Supplement" in member: #skip manifest and supplement
				continue
				
			filename = os.path.basename(member)
			if zList[i].filename[:8] == "Content/": #chop off Content/ from zipfile location
				localDir = zList[i].filename[8:]
			elif zList[i].filename[:11] == "My Library/": #chop off My Library/ from zipfile location
				localDir = zList[i].filename[11:]
			else:
				localDir = zList[i].filename
			path = os.path.join(cfg.dazDir, localDir)
			i += 1
			if not filename:
				if not os.path.exists(path):
					os.makedirs(path)
				continue
	
			# copy file (taken from zipfile's extract)
			source = zFile.open(member)
			dest = os.path.join(cfg.dazDir, localDir)
			pathFolder = path.replace(filename, "")
			if not os.path.exists(pathFolder): #if folder does not exist
				os.makedirs(pathFolder) #create folder
			with zFile.open(member) as source, open(dest, 'wb') as out:
				shutil.copyfileobj(source, out)
			
			# add dsx metadata file to list of assets to be imported in daz
			if cfg.dsaImport and member.endswith('.dsx'):
				importList.append(filename)
					
		zFile.close() #close zip file
		dsa.writeImport(importList) #write import.dsa
		
		installed.append(file) #add asset to list of installed assets
		installed = list(set(installed)) #remove duplicate assets
		installed = sorted(installed, key=str.lower) #sort assets alphabetically
		print("Installed")

	p.sInstalled(installed) #update installed assets
	p.sToInstall(list()) #reset toInstall list
	
	if cfg.launch:
		print("\t   Launching Daz Studio")
		os.system('start import.dsa')
	input("	  ")
		
	return
	
def uninstall(): #uninstall zips
	installed = p.gInstalled() #get list of installed assets
	toUninstall = p.gToUninstall() #get list of assets to uninstall
	print()
	for file in toUninstall:
		print("\t   Uninstalling " + str(file) + "...", end=" ", flush=True)
		installed.remove(file)
		installed = list(set(installed))
		installed = sorted(installed, key=str.lower)
		
		with open(cfg.txtsDir / str(file + ".p"), 'rb') as f:
			currentAsset = pickle.load(f)
		for line in currentAsset:
			path = cfg.dazDir / line
			if "." in line:
				try:
					os.remove(path)
				except:
					if ".dsx" in line:
						pass
					else:
						print("\n\t   " + str(path) + " could not be deleted.")
		print("Uninstalled")

	remove_empty_dirs(cfg.dazDir)
	
	toUninstall = list()
	p.sInstalled(installed)
	p.sToUninstall(toUninstall)
	input("	  ")
	return
	
def remove_empty_dir(path):
	try:
		os.rmdir(path)
	except OSError:
		pass
		
def remove_empty_dirs(path):
	for root, dirnames, filenames in os.walk(path, topdown=False):
		for dirname in dirnames:
			remove_empty_dir(os.path.realpath(os.path.join(root, dirname)))