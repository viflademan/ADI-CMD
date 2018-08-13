import os, configparser
from pathlib import Path

cfg = configparser.ConfigParser()
if os.path.exists('debug.cfg'):
	cfg.read('debug.cfg')
	debug = True
else:
	cfg.read('settings.cfg')
	debug = False
	
zipsDir = Path(cfg.get('DIRS', 'zip'))
arcDir = Path(cfg.get('DIRS', 'archive'))
txtsDir = Path(cfg.get('DIRS', 'pickle'))
dazDir = Path(cfg.get('DIRS', 'daz'))
pageLen = cfg.get('OPTIONS', 'pageLen')

if cfg.get('OPTIONS', 'dsaImport') == "True":
	dsaImport = True
else:
	dsaImport = False
	
if cfg.get('OPTIONS', 'launch') == "True":
	launch = True
else:
	launch = False
	
if cfg.get('OPTIONS', 'archive') == "True":
	archive = True
else:
	archive = False