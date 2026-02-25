from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.lawyer import Lawyer

lawyers_bp = Blueprint('lawyers', __name__)

@lawyers_bp.route('/', methods=['GET'])
@jwt_required()
def list_lawyers():
    lawyers = Lawyer.query.all()
    return jsonify({'success': True, 'data': [l.to_dict() for l in lawyers]})

@lawyers_bp.route('/<int:lawyer_id>', methods=['GET'])
@jwt_required()
def get_lawyer(lawyer_id):
    lawyer = Lawyer.query.get(lawyer_id)
    if not lawyer:
        return jsonify({'success': False, 'error': 'Not found', 'status_code': 404}), 404
    return jsonify({'success': True, 'data': lawyer.to_dict()})

@lawyers_bp.route('/search', methods=['GET'])
@jwt_required()
def search_lawyers():
    specialization = request.args.get('specialization', '')
    query = Lawyer.query
    if specialization:
        query = query.filter(Lawyer.specialization.ilike(f'%{specialization}%'))
    lawyers = query.all()
    return jsonify({'success': True, 'data': [l.to_dict() for l in lawyers]})
