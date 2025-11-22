"""Modelo de documento para a API do NF Scanner."""

class Document:
    """Modelo que representa um documento processado."""
    
    def __init__(self, document_id: str, content: dict):
        """ ** Placeholder para criação da arquitetura
        """
        self.document_id = document_id
        self.content = content
