Version 1.1 of Alternative Daz Importer by indusfre

First time Setup
	Open settings.cfg and change the directories of your DAZ library and where your asset zips are stored. The path to your DAZ library is where it will dump the files directly. (data/, Runtime/, People/, etc) You can change your zips folder after importing them and installing them, but I don't recommend it.

Prepping Zips for ADI
	ADI has minor ability to adjust how asset zips are structured before install. Zips with a "Content" (Daz3D.com) or "My Library" directory will automatically be changed during extraction to remove those folders. Otherwise the content folders (data/, Runtime/, etc) will have to be in the root of the zip. If you accidently install an asset that was not properly structured, you can uninstall the asset with ADI and delete the corresponding .p file (<zip name>.p).
	
Importing Assets into ADI
	The program will auto import all zips inside your zip folder on launch, but if you add more zips after the program is launched you will need to reimport your Assets with the menu option or restart ADI. When ADI imports zips it will make a corresponding .p file that archives where each file is located when extracted and other .p files to keep track of what is installed and imported. DO NOT delete these unless you realise what you are doing. You may lose the ability to uninstall assets installed into your library.
	
Installing and Uninstalling Assets
	Installation and Uninstallation is simple. Enter the appropriate menu, select the assets you would like to install or uninstall, and trigger the process with the appropiate option.
	
Metadata
	ADI will create a Daz script (.dsa) automatically on installation of assets to your library (import.dsa). By default it will automatically run the script after installation, launching Daz3D to import metadata. Change these options in settings.cfg.
	
Bugs
	If you encounter any bugs, use debug.bat instead of ADI.exe to keep the error on screen. Please send indusfre the error as a private message on the discord in #bugs.
	
Discord Support Server
	https://discord.gg/7VThc5J 