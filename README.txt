Version 3.1 of Alternate Daz Importer by raldios

First time Setup
	Open settings.cfg and change the directories of your DAZ library and where your asset zips are stored. The path to your DAZ library is where it will dump the files directly. (data/, Runtime/, People/, etc) You can change your zips folder after importing them and installing them, but I don't recommend it.

Prepping Zips for ADI
	Zip files must be in the format of having a Content folder in the root of the zip (.dsx files will be removed automatically) or with the folders under Content at the root of the zip. I may add more functionality later to have it auto find files, but for now this is how each one must be.
	
Importing Assets into ADI
	The program will auto import all zips inside your zip folder on launch, but if you add more zips after the program is launched you will need to reimport your Assets with the menu option or restart ADI. When ADI imports zips it will make a corresponding .p file that archives where each file was located when extracted and other .p files to keep track of what is installed and imported. DO NOT delete these unless you realise what you are doing. You may lose the ability to uninstall assets installed into your library.
	
Installing and Uninstalling Assets
	Installation and Uninstallation is simple. Enter the appropriate menu, select the assets you would like to install or uninstall, and trigger the process with the appropiate option.
	
Bugs
	If you encounter any bugs, use debug.bat instead of ADI.exe to keep the error on screen. Please send me the error and the files associated with the error (.p files).