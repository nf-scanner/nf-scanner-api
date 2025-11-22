"""Rotas da API do NF Scanner."""

from nf_scanner_api.routes.document import router as document_router
from nf_scanner_api.routes.health import router as health_router

__all__ = ["document_router", "health_router"]
