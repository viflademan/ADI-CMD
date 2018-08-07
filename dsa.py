import os, cfg

def writeImport(list):
	importFile = open("import.dsa", 'w') #open file for writing
	importFile.write("var oAssetMgr = App.getAssetMgr();\n") #get asset manager
	for asset in list: #for loop of all assets to be processed
		path = os.path.join(cfg.dazDir, "Runtime/Support/", asset) #create full path to .dsx file
		importFile.write("oAssetMgr.processDBMetaFile( \"" + path + '\" );\n') #write process asset line
	importFile.close() #close file