from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Esquema para resposta de saúde da API."""

    status: str = Field(..., description="Status da API", example="ok")
