import os.path
import glob

conffiles = glob.glob(os.path.join(
    os.path.dirname(__file__), 'settings.d', '*.py'))
conffiles.sort()
for f in conffiles:
    execfile(os.path.abspath(f))

try:
    execfile(os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'localsettings.py')))
except IOError:
    pass
