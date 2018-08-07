import os #python modules
import cfg, p #adi modules

def zips(page):
	os.system("cls")
	zipsList = os.listdir(cfg.zipsDir)
	
	pageLength = int(cfg.pageLen)
	min = 0 + pageLength*page
	max = pageLength - 1 + pageLength*page
	maxPage = len(zipsList) // pageLength
	
	print("\n\t    Asset Zips Detected")
	print("\t    Page " + str(page+1) + " of " + str(maxPage+1))
	display(zipsList, min, max, 0, True)
	page = pageMenu(page, maxPage)
	
	if page == "back":
		return
	else:
		zips(page)
		
def imported(page):
	os.system("cls")
	importedList = p.gAssets()
	
	pageLength = int(cfg.pageLen)
	min = 0 + pageLength*page
	max = pageLength - 1 + pageLength*page
	maxPage = len(importedList) // pageLength
	
	print("\n\t    Assets Imported")
	print("\t    Page " + str(page+1) + " of " + str(maxPage+1))
	display(importedList, min, max, 0, True)
	page = pageMenu(page, maxPage)
	
	if page == "back":
		return
	else:
		imported(page)
		
def installed(page):
	os.system("cls")
	installedList = p.gInstalled()
	
	pageLength = int(cfg.pageLen)
	min = 0 + pageLength*page
	max = pageLength - 1 + pageLength*page
	maxPage = len(installedList) // pageLength
	
	print("\n\t    Assets Installed")
	print("\t    Page " + str(page+1) + " of " + str(maxPage+1))
	display(installedList, min, max, 0, True)
	page = pageMenu(page, maxPage)
	
	if page == "back":
		return
	else:
		installed(page)
		
def display(list, min, max, trim=0, number=True): #display a list with pages
	print()
	i = min
	for file in list:
		index = i+1
		if i > max or index > len(list):
			break
		filename = list[i]
		print("\t    ", end="")
		if number == True:
			print(format(index, "2") + ". ", end=" ")
		if trim == 0:
			print(filename)
		else:
			print(filename[:trim])
		i += 1
		
def pageMenu(page, maxPage):
	print()
	if page > 0:
		print("\t    z. Previous Page")
	if page != maxPage:
		print("\t    x. Next Page")
	print("\n\t    b. Back")
	choice = input("	  >>")
	
	if choice.lower() == "z" and page > 0:
		page -= 1
		if page < 0:
			page = 0
			print("\t Already on First Page")
			input("		")
		return page
		
	elif choice.lower() == "x" and page != maxPage:
		page += 1
		if page > maxPage:
			page = maxPage
			print("\tAlready on Last Page")
			input("\t")
		return page
	
	elif choice.lower() == "b":
		page = "back"
		return page
	elif choice.lower() == "c":
		pass
	elif choice.lower() == "i":
		pass
	else:
		print("\t   Please Choose a valid option")
		input("\t   ")
		return page