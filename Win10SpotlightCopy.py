import os

def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

try:
	from PIL import Image #pip install pillow
except:
	print('Module not installed, run pip install pillow')
	input('Enter to exit')
	exit()
from os import listdir,environ, sep, makedirs
from os.path import isfile
from shutil import copy2

USERPROFILE = environ['USERPROFILE']

SPOTLIGHTDIR = fr'{USERPROFILE}\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
DESTDIR = get_download_path() + '\WinSpotlight'

flist = listdir(SPOTLIGHTDIR)
makedirs(DESTDIR, exist_ok = True)
for item in flist:
	im=Image.open(SPOTLIGHTDIR + '\\'+item)
	width, height = im.size

	if width == 1920 and height == 1080:
		if isfile(DESTDIR + '\\' + item + '.jpg'):
			print('Existing, skipping...')
		else:
			copy2(SPOTLIGHTDIR + '\\' + item, DESTDIR + '\\' + item + '.jpg')
			print('File copied')
#~ input() 
