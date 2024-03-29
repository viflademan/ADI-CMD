import os, sys #python modules
import cfg, manage, lst, p #adi modules

def main(): #main menu
	os.system('cls')
	print("\n\t Alternative Daz Importer")
	print("\n\t 1. List Menu")
	print("\t 2. Import Assets")
	print("\t 3. Install Assets")
	print("\t 4. Uninstall Assets")
	if cfg.debug:
		print("\t 5. Test Menu")
	print("\n\t a. About")
	print("\t q. Quit")
	choice = input("\n	>>  ")
	
	if choice == "1":
		listMenu()
		main()
	elif choice == "2":
		manage.makePs(True)
		input("")
		main()
	elif choice == "3":
		install()
		main()
	elif choice == "4":
		uninstall()
		main()
	elif choice == "5" and os.path.exists('debug.cfg'):
		print(cfg.zipsDir)
		input()
		main()
	elif choice.lower() == "a":
		about()
		main()
	elif choice.lower() == "q":
		os.system('cls')
		sys.exit()
	else:
		invalid()
		main()


def listMenu(): #list Menu
	os.system('cls')
	print("\n 	 List Menu")
	print("\n\t 1. Zips")
	print("\t 2. Imported")
	print("\t 3. Installed")
	print("\n	 b. Back")
	choice = input("\n	>>  ")
	
	if choice == "1":
		print("\n	Zips Detected")
		lst.zips(0)
		listMenu()
	elif choice == "2":
		print("\n	Imported Assets")
		lst.imported(0)
		listMenu()
	elif choice == "3":
		print("\n	Installed Assets")
		lst.installed(0)
		listMenu()
	elif choice.lower() == "b":
		main()
	else:
		invalid()
		listMenu()
		
def install(curPage=0):
	os.system('cls')
	zips = p.gZips()
	toInstall = p.gToInstall()
	pageLength = int(cfg.pageLen)
	min = 0 + pageLength*curPage
	max = pageLength - 1 + pageLength*curPage
	maxPage = len(zips) // pageLength
	print("\n	Assets Ready to be Installed")
	print("\t    Page " + str(curPage+1) + " of " + str(maxPage+1))
	lst.display(zips, min, max)
	i = 1
	choiceInt = -1
	print("\n\tAssets to be installed")
	
	for name in toInstall:
		i = 1
		for zip in zips:
			if zip[:-4] == name:
				break
			i += 1
		print("\t     " + str(i) + ". " + str(name))
	print("\n\ta. Mark All Assets")
	print("\tc. Clear List")
	print("\ti. Install Assets")
	#print("\ts. Search") #unfinished feature
	curPage, choice = page(curPage, maxPage)
	
	if choice.isdigit():
		choiceInt = int(choice)
	elif choice.lower() == "c":
		toInstall = list()
		p.sToInstall(toInstall)
		install(curPage)
	elif choice.lower() == "b":
		main()
	elif choice.lower() == "i":
		manage.install()
		install(curPage)
	#elif choice.lower() == "s":
	#	search(zips, "install")
	#	install(curPage)
	elif choice.lower() == "a":
		for file in zips:
			toInstall.append(file[:-4])
		p.sToInstall(toInstall)
		install(curPage)
	
	if choiceInt >= 1 and choiceInt <= len(zips):
		toInstall.append(zips[choiceInt-1][:-4])
		toInstall = set(toInstall)
		toInstall = list(toInstall)
		toInstall = sorted(toInstall, key=str.lower)
		
	p.sToInstall(toInstall)
	install(curPage)
	
def uninstall(curPage=0):
	os.system('cls')
	installed = p.gInstalled()
	toUninstall = p.gToUninstall()
	pageLength = int(cfg.pageLen)
	min = 0 + pageLength*curPage
	max = pageLength - 1 + pageLength*curPage
	maxPage = len(installed) // pageLength
	print("\n	Assets Installed")
	print("\t    Page " + str(curPage+1) + " of " + str(maxPage+1))
	lst.display(installed, min, max)
	choiceInt = -1
	print("\n\tAssets to be uninstalled")
	for name in toUninstall:
		i = 1
		for asset in installed:
			if asset == name:
				break
			i += 1
		print("\t     " + str(i) + ". " + str(name))
	print("\n\tu. Uninstall Assets")
	print("\tc. Clear List")
	curPage, choice = page(curPage, maxPage)
	
	if choice.isdigit():
		choiceInt = int(choice)
	elif choice.lower() == "c":
		toUninstall = list()
		p.sToUninstall(toUninstall)
		uninstall(curPage)
	elif choice.lower() == "b":
		main()
	elif choice.lower() == "u":
		manage.uninstall()
		uninstall(curPage)
	
	if choiceInt >= 1 and choiceInt <= len(installed):
		toUninstall.append(installed[choiceInt-1])
		toUninstall = set(toUninstall)
		toUninstall = list(toUninstall)
		toUninstall = sorted(toUninstall, key=str.lower)
	
	p.sToUninstall(toUninstall)
	uninstall(curPage)
	
def search(assets, dest):
	os.system('cls')
	results = list()
	term = input("\n	Search: ")
	for asset in assets:
		if term in asset:
			results.append(asset)
	searchResults(assets, results, dest)
	
def searchResults(assets, results, dest, curPage=0):
	os.system('cls')
	choiceInt = -1
	
	pageLength = int(cfg.pageLen)
	min = 0 + pageLength*curPage
	max = pageLength - 1 + pageLength*curPage
	maxPage = len(results) // pageLength
	
	print("\n\tResults")
	for name in results:
		i = 1
		for asset in assets:
			if asset == name:
				break
			i += 1
		print("\t     " + str(i) + ". " + str(name))
			
			
	if dest == "install":
		print("\n\tAssets to be installed")
		processList = p.gToInstall()
	else:
		print("\n\tAssets to be uninstalled")
		processList = p.gToUninstall()
	for name in processList:
		i = 1
		for asset in results:
			if asset[:-4] == name:
				break
			i += 1
		print("\t     " + str(i) + ". " + str(name))
	if dest == "install":
		print("\n\ti. Install Assets")
	else:
		print("\n\tu. Uninstall Assets")
	print("\tc. Clear List")
	curPage, choice = page(curPage, maxPage)
	
	if choice.isdigit():
		choiceInt = int(choice)
	elif choice.lower() == "c":
		processList = list()
		if dest == "install":
			p.sToInstall(processList)
		else:
			p.sToUninstall(processList)
		searchResults(assets, results, dest, curPage)
	elif choice.lower() == "b":
		if dest == "install":
			install()
		else:
			uninstall()
	elif choice.lower() == "u" and dest == "uninstall":
		manage.uninstall()
		uninstall()
	elif choice.lower() == "i" and dest == "install":
		manage.install()
		install()
	
	if choiceInt >= 1 and choiceInt <= len(results):
		if dest == "install":
			processList.append(results[choiceInt-1][:-4])
		else:
			processList.append(results[choiceInt-1])
		processList = set(processList)
		processList = list(processList)
		processList = sorted(processList, key=str.lower)
		
	if dest == "install":
		p.sToInstall(processList)
	else:
		p.sToUninstall(processList)

	searchResults(assets, results, dest, curPage)
	
def page(curPage, maxPage):
	print()
	if curPage > 0:
		print("\tz. Previous Page")
	if curPage != maxPage:
		print("\tx. Next Page")
	print("\n\tb. Back")
	choice = input("	  >>")
	
	if choice.lower() == "z" and curPage > 0:
		curPage -= 1
		if curPage < 0:
			curPage = 0
			print("\t Already on First Page")
			input("		")
		return curPage, choice
		
	elif choice.lower() == "x" and curPage != maxPage:
		curPage += 1
		if curPage > maxPage:
			curPage = maxPage
			print("\tAlready on Last Page")
			input("\t")
		return curPage, choice
	
	validChoices = ["b", "i", "u", "c", "a", "s", ]
	if choice.isdigit() or choice.lower() in validChoices:
		return curPage, choice
	else:
		invalid()
		return curPage, choice
		
def about():
	print("\n\t Alternative Daz Importer by indusfre")
	print("\n\t Version 1.2.0")
	input()
	
		
def invalid():
	print("\t    Please Choose a valid option")
	input("\t    ")