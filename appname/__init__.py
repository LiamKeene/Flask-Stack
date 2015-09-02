from flask import Flask
from flask.ext.assets import Environment, Bundle

from webassets.filter import get_filter

from appname.main.views import main_blueprint

def create_app(object_name, env='prod'):

    app = Flask(__name__)

    app.config.from_object(object_name)
    app.config['ENV'] = env

    app.register_blueprint(main_blueprint)

    assets = Environment(app)
    css = Bundle('css/style.scss', filters='scss', output='css/style.css')
    assets.register('base_style', css)

    return app
