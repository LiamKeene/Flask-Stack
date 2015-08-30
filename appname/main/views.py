from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

main_blueprint = Blueprint(
    'main', __name__,
    template_folder='templates'
)

@main_blueprint.route('/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)