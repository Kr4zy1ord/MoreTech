from flask import Blueprint, jsonify

audit_blueprint = Blueprint('audit', __name__)

# Example in-memory audit log
AUDIT_LOG = []

@audit_blueprint.route('/logs', methods=['GET'])
def get_logs():
    return jsonify({'logs': AUDIT_LOG}), 200

def log_action(action):
    AUDIT_LOG.append(action)
