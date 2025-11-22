"""Esquemas para documentos da API do NF Scanner."""

from pydantic import BaseModel, Field
from typing import Dict, Any


class DocumentResponse(BaseModel):
    """Esquema para resposta de processamento de documento."""
    
    document_id: str = Field(..., description="Identificador único do documento")
    content: Dict[str, Any] = Field(..., description="Conteúdo extraído do documento")
    
    class Config:
        json_schema_extra = {
            "example": {
                "document_id": "123e4567-e89b-12d3-a456-426614174000",
                "content": {
                    "numero": "123456",
                    "data_emissao": "2023-01-01",
                    "valor_total": 100.0,
                    # Campos adicionais aqui
                }
            }
        }
