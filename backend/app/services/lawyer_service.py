from app.models.lawyer import Lawyer
from app.utils.logger import get_logger

logger = get_logger(__name__)

class LawyerService:
    def search(self, specialization: str = None):
        query = Lawyer.query
        if specialization:
            query = query.filter(Lawyer.specialization.ilike(f'%{specialization}%'))
        return query.all()
    
    def get_by_id(self, lawyer_id: int):
        return Lawyer.query.get(lawyer_id)
