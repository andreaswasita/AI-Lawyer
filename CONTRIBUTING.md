# Contributing to AI Lawyer

Thank you for your interest in contributing to AI Lawyer! We're building a platform to democratize legal services in Indonesia, and we need help from developers, lawyers, designers, and legal tech enthusiasts.

## 🌟 Ways to Contribute

### 1. Code Contributions
- **Frontend Development**: React/Next.js UI components
- **Backend Development**: API endpoints, database schemas
- **AI/ML**: LLM integration, RAG optimization, NER models
- **Mobile Development**: React Native iOS/Android app
- **DevOps**: Infrastructure, CI/CD, monitoring

### 2. Legal Expertise
- **Legal Templates**: Draft standard legal document templates
- **Legal Corpus**: Collect and curate Indonesian legal texts
- **Legal Review**: Validate AI-generated content accuracy
- **Practice Area Expertise**: Domain knowledge for specific legal areas

### 3. Design & UX
- **UI Design**: Create accessible, intuitive interfaces
- **User Research**: Interview users, conduct usability tests
- **Content Design**: Write clear, plain-language legal explanations
- **Localization**: Ensure Bahasa Indonesia translations are natural

### 4. Documentation
- **Technical Docs**: API docs, architecture guides
- **User Guides**: Help articles, tutorials, FAQs
- **Legal Guides**: Plain-language explanations of Indonesian law
- **Translation**: Translate docs to Bahasa Indonesia

### 5. Testing & QA
- **Bug Reports**: Identify and report issues
- **Testing**: Manual testing of new features
- **Accessibility Testing**: Ensure WCAG compliance
- **Security Testing**: Penetration testing, vulnerability reports

## 🚀 Getting Started

### Prerequisites
- Node.js 18+ or Python 3.10+
- Git
- PostgreSQL 14+
- Azure account (for cloud services)

### Setup Local Development Environment

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/AI-Lawyer.git
cd AI-Lawyer
```

2. **Install dependencies**

For frontend:
```bash
cd frontend
npm install
```

For backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Set up environment variables**

Create `.env.local` files in frontend and backend directories:

```env
# Backend .env
DATABASE_URL=postgresql://user:password@localhost:5432/ailawyer
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
REDIS_URL=redis://localhost:6379
SECRET_KEY=your_secret_key

# Frontend .env.local
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_MIDTRANS_CLIENT_KEY=your_midtrans_key
```

4. **Run database migrations**
```bash
cd backend
alembic upgrade head
```

5. **Start development servers**

Backend:
```bash
cd backend
uvicorn app.main:app --reload
```

Frontend:
```bash
cd frontend
npm run dev
```

6. **Access the application**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## 📝 Development Workflow

### 1. Pick an Issue
- Browse [open issues](https://github.com/yourusername/AI-Lawyer/issues)
- Look for issues tagged with `good first issue` or `help wanted`
- Comment on the issue to let others know you're working on it

### 2. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/bug-description
```

**Branch naming conventions**:
- `feature/` - New features
- `bugfix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Adding/updating tests

### 3. Make Your Changes
- Write clean, readable code
- Follow existing code style and conventions
- Add comments for complex logic
- Write unit tests for new features
- Update documentation if needed

### 4. Test Your Changes
```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test

# Linting
npm run lint
```

### 5. Commit Your Changes
Follow [Conventional Commits](https://www.conventionalcommits.org/):

```bash
git commit -m "feat: add document generation for rental agreements"
git commit -m "fix: resolve authentication bug in lawyer portal"
git commit -m "docs: update API documentation for chat endpoint"
```

**Commit message format**:
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, no logic change)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### 6. Push and Create Pull Request
```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:
- **Clear title**: Describe what the PR does
- **Description**: Explain why the change is needed
- **Screenshots**: Include for UI changes
- **Testing**: Describe how you tested the changes
- **Related Issues**: Link to related issues (e.g., "Closes #123")

### 7. Code Review
- Respond to review comments
- Make requested changes
- Push updates to the same branch
- Request re-review when ready

## 💻 Code Style Guidelines

### Python (Backend)
- Follow [PEP 8](https://pep8.org/)
- Use [Black](https://black.readthedocs.io/) for formatting
- Use type hints for function signatures
- Maximum line length: 100 characters
- Docstrings for all public functions/classes

Example:
```python
from typing import Optional

def generate_document(
    template_id: str,
    user_data: dict,
    lawyer_review: Optional[bool] = False
) -> dict:
    """
    Generate a legal document from a template.
    
    Args:
        template_id: Unique identifier for the document template
        user_data: Dictionary containing user-provided information
        lawyer_review: Whether to request lawyer review
        
    Returns:
        Dictionary with document_id and download_url
        
    Raises:
        TemplateNotFoundError: If template_id doesn't exist
        ValidationError: If user_data is incomplete
    """
    # Implementation
    pass
```

### TypeScript/React (Frontend)
- Follow [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)
- Use [Prettier](https://prettier.io/) for formatting
- Use functional components with hooks
- Use TypeScript for type safety
- Maximum line length: 100 characters

Example:
```typescript
interface DocumentGeneratorProps {
  templateId: string;
  onComplete: (documentId: string) => void;
  isLawyerReviewEnabled?: boolean;
}

export const DocumentGenerator: React.FC<DocumentGeneratorProps> = ({
  templateId,
  onComplete,
  isLawyerReviewEnabled = false,
}) => {
  const [loading, setLoading] = useState(false);
  
  // Implementation
  
  return (
    <div className="document-generator">
      {/* JSX */}
    </div>
  );
};
```

### Bahasa Indonesia Content
- Use formal but accessible language
- Avoid legal jargon when possible
- Provide examples to clarify complex concepts
- Use consistent terminology throughout

## 🧪 Testing Guidelines

### Unit Tests
- Test individual functions/components in isolation
- Mock external dependencies
- Aim for >80% code coverage

### Integration Tests
- Test API endpoints with database
- Test UI flows with backend integration
- Use fixtures for test data

### E2E Tests
- Test critical user journeys
- Use Playwright or Cypress for frontend
- Test in staging environment before production

### Test Naming Convention
```python
def test_should_generate_rental_agreement_when_valid_data():
    # Given
    template_id = "rental_agreement_v1"
    user_data = {"landlord": "John", "tenant": "Jane"}
    
    # When
    result = generate_document(template_id, user_data)
    
    # Then
    assert result["document_id"] is not None
    assert result["status"] == "generated"
```

## 🔒 Security Guidelines

### Sensitive Data
- Never commit API keys, passwords, or secrets
- Use environment variables for configuration
- Use Azure Key Vault for production secrets

### Authentication & Authorization
- Always validate user permissions
- Use HTTPS for all API calls
- Implement rate limiting
- Hash passwords with bcrypt

### Input Validation
- Validate all user input on both frontend and backend
- Sanitize HTML to prevent XSS
- Use parameterized queries to prevent SQL injection
- Validate file uploads (type, size, content)

### Reporting Security Vulnerabilities
- **Do not** create public GitHub issues for security bugs
- Email security@hukumai.id with details
- We'll respond within 48 hours
- Follow responsible disclosure practices

## 🌍 Internationalization (i18n)

### Adding Translations
1. Add keys to `frontend/locales/id.json` (Bahasa Indonesia)
2. Add corresponding keys to `frontend/locales/en.json` (English)
3. Use the `useTranslation` hook in components

Example:
```typescript
// locales/id.json
{
  "document": {
    "title": "Dokumen Hukum Anda",
    "generate": "Buat Dokumen"
  }
}

// Component
import { useTranslation } from 'next-i18next';

export const DocumentPage = () => {
  const { t } = useTranslation('common');
  
  return (
    <h1>{t('document.title')}</h1>
  );
};
```

## 📄 License

By contributing to AI Lawyer, you agree that your contributions will be licensed under the MIT License.

## 🤝 Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

## 💬 Communication

### Channels
- **GitHub Issues**: Bug reports, feature requests
- **GitHub Discussions**: Questions, ideas, general discussion
- **Discord**: Real-time chat (link coming soon)
- **Email**: dev@hukumai.id for private inquiries

### Getting Help
- Check the [documentation](./docs/)
- Search existing GitHub issues
- Ask in GitHub Discussions
- Join our Discord community

## 🎉 Recognition

Contributors will be:
- Listed in README.md acknowledgments
- Credited in release notes
- Invited to contributor events
- Eligible for swag and rewards (when available)

## 📅 Release Cycle

- **Weekly**: Bug fixes and minor improvements
- **Monthly**: New features and enhancements
- **Quarterly**: Major releases with breaking changes

## ❓ Questions?

If you have questions about contributing, please:
1. Check this guide
2. Search GitHub Discussions
3. Create a new Discussion topic
4. Email dev@hukumai.id

---

**Thank you for helping us make legal services accessible to all Indonesians!** 🇮🇩⚖️

*Hukum untuk Semua* (Law for Everyone)
