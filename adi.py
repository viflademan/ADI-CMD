import sys, menu, manage, p, cfg #adi modules

p.makeDirs() #make directories on startup
manage.makePs(False) #make reference files

if len(sys.argv) == 1:
	menu.main() #go to main menu
elif sys.argv[1] == "-ia":
	zips = p.gZips()
	toInstall = p.gToInstall()
	for file in zips:
		toInstall.append(file[:-4])
	p.sToInstall(toInstall)
	manage.install()
else:
	print("Invalid arguments.")
	input("	  ")