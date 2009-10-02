from distutils.core import setup
import py2exe

levelfiles = []
for i in range(1, 38):
	levelfiles.append('level{0}'.format(i))

setup(windows=['tudi.py'], data_files=['crap.png', 'victor-pixel.ttf', 'oalinst.exe', 'dead.ogg', 'collect.ogg'], options={"py2exe":{"includes": levelfiles}})
