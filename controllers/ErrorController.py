from flask import Blueprint, render_template

error_controller = Blueprint('error_controller', __name__)

@error_controller.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

@error_controller.app_errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html'), 500