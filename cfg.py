import os, configparser

cfg = configparser.ConfigParser()
cfg.read('settings.cfg')
zipsDir = os.path.join(cfg.get('DIRS', 'zip'))
txtsDir = os.path.join(cfg.get('DIRS', 'pickle'))
dazDir = os.path.join(cfg.get('DIRS', 'daz'))
pageLen = cfg.get('OPTIONS', 'pageLen')

if cfg.get('OPTIONS', 'dsaImport') == "True":
	dsaImport = True
else:
	dsaImport = False
	
if cfg.get('OPTIONS', 'launch') == "True":
	launch = True
else:
	launch = False