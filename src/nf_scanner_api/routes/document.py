from fastapi import APIRouter, UploadFile, File, Depends, Query
from ..services.document_service import DocumentService
from ..schemas.document import NFSeResponse

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post(
    "/process_nfse",
    response_model=NFSeResponse,
    summary="Processar NFSe",
    description="Processa uma Nota Fiscal de Serviço Eletrônica (NFSe) e extrai seus dados estruturados",
    response_description="Dados extraídos da NFSe",
)
async def process_nfse(
    document: UploadFile = File(
        ..., description="Arquivo PDF ou Imagem da NFSe a ser processada"
    ),
    ai_extraction: bool = Query(
        default=False, description="Se True, usa IA para extração; se False, usa OCR"
    ),
    ai_parse: bool = Query(
        default=False,
        description="Se True, usa IA para parsear os dados; se False, usa parseamento manual",
    ),
) -> NFSeResponse:
    """
    Processa uma Nota Fiscal de Serviço Eletrônica (NFSe).

    O endpoint recebe um arquivo PDF ou Imagem contendo uma NFSe e retorna
    os dados estruturados extraídos do documento.

    Parameters:
        document: Arquivo da NFSe (PDF ou Imagem)

    Returns:
        NFSe: Objeto contendo os dados estruturados da NFSe

    Raises:
        HTTPException: Quando o documento não pode ser processado ou está em formato inválido
    """
    return NFSeResponse(
        nfse=await DocumentService(
            ai_extraction=ai_extraction, ai_parse=ai_parse
        ).process_nfse(document)
    )
