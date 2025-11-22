"""Modelo de documento para a API do NF Scanner."""

class Document:
    """Modelo que representa um documento recebido."""

    def __init__(self, document_name: str, base64_content: str):
        """Construtor do modelo de documento.

        Args:
            document_name: Nome do documento
            base64_content: Conteúdo do documento em base64
        """
        self.document_name = document_name
        self.base64_content = base64_content

    def to_dict(self) -> dict:
        """Converte o modelo de documento para um dicionário."""
        return {
            "document_name": self.document_name,
            "base64_content": self.base64_content,
        }

