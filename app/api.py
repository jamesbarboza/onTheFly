import functools
import os
import shutil
from . import config
from . import messages

from flask import (
    Blueprint, jsonify, request
)

api = Blueprint('api', __name__, url_prefix='/')

@api.route('/')
def index():
    return 'OnTheFly API Version: %s' % config.version

@api.route('/project/create', methods=('GET', 'POST'))
def create_project():
    if not request.method == 'POST':
        return jsonify({'status': 400, 'result': messages.POST_REQUEST_REQUIRED}) 

    project_name = request.json.get('name')
    if not project_name or project_name == "":
        return jsonify({'status': 400, 'result': messages.PROJECT_NAME_NOT_PASSED_OR_EMPTY}) 

    # cd to project directory
    os.chdir(config.project_directory)
    
    # mkdir with project name
    os.mkdir(project_name)
    os.chdir(project_name)

    # create the django project

    return jsonify({'status': 200, 'result': messages.PROJECT_CREATED_SUCCESSFULLY}) 

@api.route('/project/delete', methods=('GET', 'POST'))
def delete_project():
    if not request.method == 'POST':
        return jsonify({'status': 400, 'result': messages.POST_REQUEST_REQUIRED}) 

    project_name = request.json.get('name')
    if not project_name or project_name == "":
        return jsonify({'status': 400, 'result': messages.PROJECT_NAME_NOT_PASSED_OR_EMPTY}) 

    project_path = os.path.join(config.project_directory, project_name)
    print("Deleting project %s" % project_path)

    shutil.rmtree(project_path)
    return jsonify({'status': 200, 'result': messages.PROJECT_DELETED_SUCCESSFULLY}) 
