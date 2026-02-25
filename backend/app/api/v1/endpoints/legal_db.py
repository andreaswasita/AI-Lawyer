"""
Legal Database Endpoint
Search and browse the Indonesian legal reference database.
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import Optional

from app.services.legal_database import legal_db, LegalReference

router = APIRouter()


class LegalReferenceResponse(BaseModel):
    id: str
    law_name: str
    short_name: str
    category: str
    description: str
    keywords: list[str]
    url: Optional[str] = None
    articles: list[str]


def _to_response(ref: LegalReference) -> LegalReferenceResponse:
    return LegalReferenceResponse(
        id=ref.id,
        law_name=ref.law_name,
        short_name=ref.short_name,
        category=ref.category,
        description=ref.description,
        keywords=ref.keywords,
        url=ref.url,
        articles=ref.articles,
    )


@router.get("/", response_model=list[LegalReferenceResponse])
async def list_legal_references(
    category: Optional[str] = Query(None, description="Filter by legal category"),
):
    """
    List all Indonesian legal references.
    Optionally filter by category (e.g. perceraian, bisnis, ketenagakerjaan).
    """
    if category:
        refs = legal_db.get_by_category(category)
        if not refs:
            raise HTTPException(
                status_code=404, detail=f"No legal references found for category '{category}'"
            )
        return [_to_response(r) for r in refs]
    return [_to_response(r) for r in legal_db.list_all()]


@router.get("/search", response_model=list[LegalReferenceResponse])
async def search_legal_references(
    q: str = Query(..., min_length=2, description="Search query"),
    limit: int = Query(5, ge=1, le=20, description="Maximum results to return"),
):
    """
    Search the Indonesian legal knowledge base by keyword.
    Returns the most relevant legal references for the given query.
    """
    results = legal_db.search(q, limit=limit)
    return [_to_response(r) for r in results]


@router.get("/categories", response_model=list[str])
async def list_categories():
    """List all available legal categories in the database."""
    return legal_db.list_categories()


@router.get("/{ref_id}", response_model=LegalReferenceResponse)
async def get_legal_reference(ref_id: str):
    """Get a specific legal reference by its ID."""
    ref = legal_db.get_by_id(ref_id)
    if not ref:
        raise HTTPException(status_code=404, detail=f"Legal reference '{ref_id}' not found")
    return _to_response(ref)
