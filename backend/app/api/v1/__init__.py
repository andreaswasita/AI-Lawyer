from flask import Blueprint

v1_bp = Blueprint('v1', __name__)

from app.api.v1.auth import auth_bp
from app.api.v1.chat import chat_bp
from app.api.v1.documents import documents_bp
from app.api.v1.lawyers import lawyers_bp
from app.api.v1.health import health_bp

v1_bp.register_blueprint(auth_bp, url_prefix='/auth')
v1_bp.register_blueprint(chat_bp, url_prefix='/chat')
v1_bp.register_blueprint(documents_bp, url_prefix='/documents')
v1_bp.register_blueprint(lawyers_bp, url_prefix='/lawyers')
v1_bp.register_blueprint(health_bp, url_prefix='/health')
