import os, sys

# Use dev settings if not otherwise configured.
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
try:
    os.symlink('settings_main.py', THIS_DIR+'/settings.py')
except OSError:
    pass
print(THIS_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
os.environ.setdefault("SETTINGS_MODULE", "website.settings")
sys.path.append(THIS_DIR)

# This application object is used by the development server
# as well as any WSGI server configured to use this file.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
