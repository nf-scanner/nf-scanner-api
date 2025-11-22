from nf_scanner_core.models.nfse import NFSe as NFSeModel


class NFSe:
    """Modelo para equivalente a NFSe do nf-scanner-core."""

    def __init__(self, nfse: NFSeModel):
        """Construtor do modelo de NFSe."""
        self.nfse = nfse

    def to_dict(self) -> dict:
        """Converte o modelo de NFSe para um dicionário."""
        return self.nfse.to_dict()
