from app.services.ai_service import AIService

class LegalChatbot:
    def __init__(self):
        self.ai_service = AIService()
    
    def respond(self, query: str, history: list = None) -> dict:
        return self.ai_service.query(query, history or [])
