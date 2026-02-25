from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from app.extensions import db
from app.models.document import Document
from app.schemas.document import DocumentSchema, DocumentGenerateSchema
from app.services.document_service import DocumentService

documents_bp = Blueprint('documents', __name__)

@documents_bp.route('/', methods=['GET'])
@jwt_required()
def list_documents():
    user_id = int(get_jwt_identity())
    docs = Document.query.filter_by(user_id=user_id).all()
    return jsonify({'success': True, 'data': [d.to_dict() for d in docs]})

@documents_bp.route('/generate', methods=['POST'])
@jwt_required()
def generate_document():
    schema = DocumentGenerateSchema()
    try:
        data = schema.load(request.get_json() or {})
    except ValidationError as e:
        return jsonify({'success': False, 'error': 'Validation error', 'message': str(e.messages), 'status_code': 400}), 400
    
    user_id = int(get_jwt_identity())
    service = DocumentService()
    content = service.generate(data['type'], data['title'], data.get('template_data', {}))
    
    doc = Document(user_id=user_id, type=data['type'], title=data['title'], content=content)
    db.session.add(doc)
    db.session.commit()
    
    return jsonify({'success': True, 'data': doc.to_dict()}), 201

@documents_bp.route('/<int:doc_id>', methods=['GET'])
@jwt_required()
def get_document(doc_id):
    user_id = int(get_jwt_identity())
    doc = Document.query.filter_by(id=doc_id, user_id=user_id).first()
    if not doc:
        return jsonify({'success': False, 'error': 'Not found', 'status_code': 404}), 404
    return jsonify({'success': True, 'data': doc.to_dict()})
