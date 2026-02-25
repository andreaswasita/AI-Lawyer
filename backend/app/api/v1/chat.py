from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from app.schemas.chat import ChatQuerySchema
from app.services.ai_service import AIService
from app.extensions import db
from app.models.chat_log import ChatLog

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/query', methods=['POST'])
@jwt_required()
def query():
    schema = ChatQuerySchema()
    try:
        data = schema.load(request.get_json() or {})
    except ValidationError as e:
        return jsonify({'success': False, 'error': 'Validation error', 'message': str(e.messages), 'status_code': 400}), 400
    
    user_id = int(get_jwt_identity())
    ai_service = AIService()
    result = ai_service.query(data['query'], data.get('conversation_history', []))
    
    # Log to DB
    log = ChatLog(user_id=user_id, query=data['query'], response=result.get('response', ''))
    db.session.add(log)
    db.session.commit()
    
    return jsonify({'success': True, 'data': result})

@chat_bp.route('/history', methods=['GET'])
@jwt_required()
def history():
    user_id = int(get_jwt_identity())
    logs = ChatLog.query.filter_by(user_id=user_id).order_by(ChatLog.created_at.desc()).limit(50).all()
    return jsonify({'success': True, 'data': [log.to_dict() for log in logs]})
