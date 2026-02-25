from app.utils.logger import get_logger

logger = get_logger(__name__)

class DocumentService:
    def generate(self, doc_type: str, title: str, template_data: dict) -> str:
        templates = {
            'contract': self._generate_contract,
            'letter': self._generate_letter,
            'agreement': self._generate_agreement,
        }
        generator = templates.get(doc_type, self._generate_generic)
        return generator(title, template_data)
    
    def _generate_contract(self, title, data):
        return f"CONTRACT: {title}\n\nThis contract is entered into between the parties as described herein.\n\n{str(data)}"
    
    def _generate_letter(self, title, data):
        return f"LETTER: {title}\n\nDear Sir/Madam,\n\n{str(data)}"
    
    def _generate_agreement(self, title, data):
        return f"AGREEMENT: {title}\n\nThis agreement is made between the following parties:\n\n{str(data)}"
    
    def _generate_generic(self, title, data):
        return f"DOCUMENT: {title}\n\n{str(data)}"
