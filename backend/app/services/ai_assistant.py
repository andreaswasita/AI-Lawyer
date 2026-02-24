"""
AI Legal Assistant Service
Handles Azure OpenAI integration with RAG for Indonesian law
"""

from typing import Optional
from loguru import logger
from app.config import get_settings

settings = get_settings()


class AILegalAssistant:
    """
    Core AI service for the legal chatbot.
    Uses Azure OpenAI GPT-4o with RAG (Retrieval-Augmented Generation)
    against an Indonesian legal knowledge base.
    """

    def __init__(self):
        self._client = None
        self._embeddings = None
        self._vector_store = None

    async def initialize(self):
        """Initialize Azure OpenAI and Qdrant connections"""
        try:
            if settings.azure_openai_api_key:
                from openai import AsyncAzureOpenAI

                self._client = AsyncAzureOpenAI(
                    api_key=settings.azure_openai_api_key,
                    api_version=settings.azure_openai_api_version,
                    azure_endpoint=settings.azure_openai_endpoint,
                )
                logger.info("✅ Azure OpenAI client initialized")
            else:
                logger.warning("⚠️ Azure OpenAI API key not configured - using demo mode")

        except Exception as e:
            logger.error(f"❌ Failed to initialize AI client: {e}")

    async def chat(
        self,
        message: str,
        conversation_history: list[dict] = None,
        language: str = "id",
        system_prompt: str = None,
    ) -> dict:
        """
        Process a legal question using Azure OpenAI with RAG.
        
        Flow:
        1. Embed the user's question
        2. Search Qdrant for relevant Indonesian law passages
        3. Build context from retrieved passages
        4. Call GPT-4o with system prompt + context + conversation history + question
        5. Return structured response with sources
        """
        if not self._client:
            return self._demo_response(message, language)

        try:
            # Step 1: Retrieve relevant legal context (RAG)
            context = await self._retrieve_legal_context(message)

            # Step 2: Build messages
            messages = [
                {"role": "system", "content": system_prompt or self._get_system_prompt(language)},
            ]

            # Add context from RAG
            if context:
                messages.append({
                    "role": "system",
                    "content": f"Berikut adalah rujukan hukum yang relevan:\n\n{context}",
                })

            # Add conversation history
            if conversation_history:
                messages.extend(conversation_history[-10:])  # Keep last 10 messages

            # Add current question
            messages.append({"role": "user", "content": message})

            # Step 3: Call Azure OpenAI
            response = await self._client.chat.completions.create(
                model=settings.azure_openai_deployment,
                messages=messages,
                temperature=0.3,  # Low temperature for legal accuracy
                max_tokens=2000,
                top_p=0.9,
            )

            return {
                "content": response.choices[0].message.content,
                "usage": {
                    "prompt_tokens": response.usage.prompt_tokens,
                    "completion_tokens": response.usage.completion_tokens,
                },
            }

        except Exception as e:
            logger.error(f"❌ AI chat error: {e}")
            return self._demo_response(message, language)

    async def _retrieve_legal_context(self, query: str, top_k: int = 5) -> str:
        """
        Search the Indonesian legal knowledge base using vector similarity.
        Returns relevant passages from laws, regulations, and legal articles.
        """
        # TODO: Implement Qdrant vector search
        # 1. Embed the query using text-embedding-3-large
        # 2. Search Qdrant collection for nearest neighbors
        # 3. Return concatenated passages with source attribution
        
        return ""  # No context in demo mode

    async def generate_document(
        self,
        template_content: str,
        fields: dict,
        additional_context: str = "",
    ) -> str:
        """
        Use AI to enhance a document template with contextually appropriate language.
        """
        if not self._client:
            return template_content  # Return raw template in demo mode

        try:
            prompt = (
                "Kamu adalah ahli hukum Indonesia yang berpengalaman. "
                "Lengkapi template dokumen hukum berikut dengan bahasa hukum yang tepat "
                "dan sesuai dengan peraturan Indonesia yang berlaku.\n\n"
                f"Template:\n{template_content}\n\n"
                f"Data:\n{fields}\n\n"
                f"Konteks tambahan:\n{additional_context}\n\n"
                "Hasilkan dokumen lengkap dalam Bahasa Indonesia yang formal dan sesuai hukum."
            )

            response = await self._client.chat.completions.create(
                model=settings.azure_openai_deployment,
                messages=[
                    {"role": "system", "content": "Kamu adalah AI pembuat dokumen hukum Indonesia."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.2,
                max_tokens=4000,
            )

            return response.choices[0].message.content

        except Exception as e:
            logger.error(f"❌ Document generation error: {e}")
            return template_content

    def _get_system_prompt(self, language: str) -> str:
        """Get the appropriate system prompt based on language"""
        if language == "id":
            return (
                "Kamu adalah AI Lawyer (Hukum AI), asisten hukum AI untuk warga Indonesia.\n\n"
                "ATURAN:\n"
                "1. Berikan informasi hukum umum, BUKAN nasihat hukum spesifik\n"
                "2. Selalu rujuk undang-undang dan peraturan yang relevan\n"
                "3. Gunakan Bahasa Indonesia yang mudah dipahami\n"
                "4. Jika kasus kompleks, sarankan konsultasi dengan Advokat\n"
                "5. Selalu sertakan disclaimer\n"
                "6. Berikan langkah-langkah praktis\n"
            )
        return (
            "You are AI Lawyer (Hukum AI), an AI legal assistant for Indonesian citizens.\n\n"
            "RULES:\n"
            "1. Provide general legal information, NOT specific legal advice\n"
            "2. Always reference relevant Indonesian laws and regulations\n"
            "3. Use simple, easy-to-understand language\n"
            "4. If the case is complex, recommend consultation with an Advocate\n"
            "5. Always include a disclaimer\n"
            "6. Provide practical steps\n"
        )

    def _demo_response(self, message: str, language: str) -> dict:
        """Generate a demo response when AI is not configured"""
        if language == "id":
            content = (
                "🤖 *Mode Demo - Azure OpenAI belum dikonfigurasi*\n\n"
                f"Pertanyaan Anda: \"{message}\"\n\n"
                "Dalam mode produksi, AI Lawyer akan:\n"
                "1. Mencari undang-undang yang relevan di knowledge base\n"
                "2. Memberikan jawaban detail dalam Bahasa Indonesia\n"
                "3. Menyertakan rujukan pasal dan undang-undang\n"
                "4. Merekomendasikan template atau konsultasi Advokat\n\n"
                "⚠️ Ini adalah informasi umum, bukan nasihat hukum."
            )
        else:
            content = (
                "🤖 *Demo Mode - Azure OpenAI not configured*\n\n"
                f"Your question: \"{message}\"\n\n"
                "In production mode, AI Lawyer will:\n"
                "1. Search relevant laws in the knowledge base\n"
                "2. Provide detailed answers in your language\n"
                "3. Include law and article references\n"
                "4. Recommend templates or lawyer consultation\n\n"
                "⚠️ This is general information, not legal advice."
            )

        return {"content": content, "usage": {"prompt_tokens": 0, "completion_tokens": 0}}


# Singleton instance
ai_assistant = AILegalAssistant()
