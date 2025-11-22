from fastapi import APIRouter, UploadFile, File, Depends
from ..services.document_service import DocumentService
from ..schemas.document import DocumentResponse

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.post("/process", response_model=DocumentResponse)
async def process_document(
    file: UploadFile = File(...),
    document_service: DocumentService = Depends(),
):
    """Processa um documento e extrai informações."""
    # Implementação será adicionada posteriormente
    pass
