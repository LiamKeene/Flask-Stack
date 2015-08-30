import os

from appname import create_app

# Defaults to development environment
env = os.environ.get('APPNAME_ENV', 'development')
app = create_app('appname.config.%sConfig' % env.capitalize(), env=env)

app.run(debug=True)