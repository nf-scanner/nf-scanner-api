from fastapi import UploadFile
from nf_scanner_core.extractor import NFExtractor
from fastapi import HTTPException
import os


class DocumentService:
    """Serviço para processamento de documentos."""

    def __init__(self, ai_extraction: bool = False, ai_parse: bool = False):
        """Construtor do serviço de documentos."""
        """
        Args:
            ai_extraction: Se True, usa IA para extração; se False, usa OCR
            ai_parse: Se True, usa IA para parsear os dados; se False, usa parseamento manual
        """
        self.ai_extraction = ai_extraction
        self.ai_parse = ai_parse

    def _save_file(self, file: UploadFile):
        """Salva o arquivo em um diretório temporário."""
        os.makedirs("temp", exist_ok=True)
        with open(f"temp/{file.filename}", "wb") as f:
            f.write(file.file.read())
        return f"temp/{file.filename}"

    async def process_nfse(self, file: UploadFile):
        """Processa um documento PDF ou Imagem e extrai os dados estruturados da NFSe.

        Args:
            UploadFile: O arquivo do documento enviado (PDF ou Imagem)

        Returns:
            NFSe: Objeto contendo os dados estruturados da NFSe
        """
        saved_file = self._save_file(file)
        try:
            nfse = NFExtractor(saved_file, self.ai_extraction, self.ai_parse).extract()
            return nfse
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Erro ao processar o arquivo: {str(e)}"
            )
        finally:
            os.remove(saved_file)
