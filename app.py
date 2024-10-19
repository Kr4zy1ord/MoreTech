from flask import Flask
from app.auth.auth import auth_blueprint
from app.secrets.secrets import secrets_blueprint
from app.audit.audit import audit_blueprint

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(secrets_blueprint, url_prefix='/secrets')
app.register_blueprint(audit_blueprint, url_prefix='/audit')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
