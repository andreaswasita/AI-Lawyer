import os
from app.utils.logger import get_logger

logger = get_logger(__name__)

SYSTEM_PROMPT = (
    "You are an AI legal assistant specializing in Indonesian law. "
    "Provide accurate, helpful legal guidance while clarifying you are not "
    "a substitute for professional legal advice."
)

class AIService:
    def query(self, user_query: str, conversation_history: list = None) -> dict:
        api_key = os.environ.get('AZURE_OPENAI_API_KEY', '')
        endpoint = os.environ.get('AZURE_OPENAI_ENDPOINT', '')
        deployment = os.environ.get('AZURE_OPENAI_DEPLOYMENT_NAME', 'gpt-4o')
        api_version = os.environ.get('AZURE_OPENAI_API_VERSION', '2024-08-01-preview')
        
        if not api_key or not endpoint:
            logger.warning("Azure OpenAI not configured - using demo response")
            return {
                'response': 'Demo mode: AI service not configured. Please set AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT.',
                'confidence': 0.0,
                'disclaimer': 'This is not legal advice. Please consult a licensed lawyer.'
            }
        
        try:
            from openai import AzureOpenAI
            client = AzureOpenAI(
                api_key=api_key,
                api_version=api_version,
                azure_endpoint=endpoint
            )
            
            messages = [{'role': 'system', 'content': SYSTEM_PROMPT}]
            if conversation_history:
                messages.extend(conversation_history)
            messages.append({'role': 'user', 'content': user_query})
            
            response = client.chat.completions.create(
                model=deployment,
                messages=messages,
                max_tokens=1000,
                temperature=0.7
            )
            
            return {
                'response': response.choices[0].message.content,
                'confidence': 0.95,
                'disclaimer': 'This is AI-generated legal information, not legal advice. Consult a licensed Indonesian lawyer for specific legal advice.'
            }
        except Exception as e:
            logger.error(f"AI query error: {e}")
            return {
                'response': 'Sorry, I encountered an error processing your query.',
                'confidence': 0.0,
                'disclaimer': 'Service temporarily unavailable.'
            }
