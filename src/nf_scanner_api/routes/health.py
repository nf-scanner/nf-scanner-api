from fastapi import APIRouter
from ..schemas.health import HealthResponse

router = APIRouter(prefix="/health", tags=["Health"])


@router.get(
    "", response_model=HealthResponse, summary="Verifica se a API está funcionando"
)
async def health_check() -> HealthResponse:
    """Verifica se a API está funcionando.

    Returns:
        HealthResponse: Status da API
    """
    return HealthResponse(status="ok")
