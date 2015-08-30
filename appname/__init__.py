from flask import Flask

from appname.main.views import main_blueprint

def create_app(object_name, env='prod'):
    
    app = Flask(__name__)

    app.config.from_object(object_name)
    app.config['ENV'] = env

    app.register_blueprint(main_blueprint)

    return app