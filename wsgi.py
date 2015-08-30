import os
import sys

# Don't forget to set the name of the virtualenv here
activate_this = os.path.expanduser(
    '~/.pyenv/versions/{VIRTUAL_ENV}/bin/activate_this.py'.format(VIRTUAL_ENV='flask-stack')
)
execfile(activate_this, dict(__file__=activate_this))

from appname import app as application
