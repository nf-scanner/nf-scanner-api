"""Esquemas para documentos da API do NF Scanner."""

from pydantic import BaseModel, Field
from nf_scanner_core.models.nfse import NFSe

from datetime import datetime
from nf_scanner_core.models.empresa import Empresa
from nf_scanner_core.models.endereco import Endereco
from nf_scanner_core.models.servico_detalhe import ServicoDetalhe
from nf_scanner_core.models.valores import Valores
from nf_scanner_core.models.tributos_federais import TributosFederais


class NFSeResponse(BaseModel):
    """Esquema para resposta de processamento de NFSe."""

    nfse: NFSe = Field(
        ...,
        description="Objeto NFSe com os dados extraídos",
        example=NFSe(
            data_hora_emissao=datetime.now(),
            competencia="2025-01",
            codigo_verificacao="1234567890",
            numero_rps="1234567890",
            local_prestacao="São Paulo",
            numero_nfse="1234567890",
            origem="São Paulo",
            orgao="Prefeitura Municipal de São Paulo",
            nfse_substituida="1234567890",
            prestador=Empresa(
                razao_social="Empresa de Serviços Ltda",
                cnpj="12345678901234",
                inscricao_municipal="12345678901234",
                inscricao_estadual="12345678901234",
                nome_fantasia="Empresa de Serviços Ltda",
                endereco=Endereco(
                    logradouro="Rua das Flores",
                    numero="123",
                    bairro="Centro",
                    cep="123456789012",
                    municipio="São Paulo",
                    uf="SP",
                ),
            ),
            tomador=Empresa(
                razao_social="Cliente Exemplo S.A.",
                cnpj="12345678901234",
                inscricao_municipal="12345678901234",
                inscricao_estadual="12345678901234",
                nome_fantasia="Cliente Exemplo S.A.",
                endereco=Endereco(
                    logradouro="Rua das Flores",
                    numero="123",
                    bairro="Centro",
                    cep="123456789012",
                    municipio="São Paulo",
                    uf="SP",
                ),
            ),
            servico=ServicoDetalhe(
                descricao="Serviços de informática",
                codigo_servico="1234567890",
                atividade_descricao="Atividade de informática",
                cnae="1234567890",
                cnae_descricao="Descrição da atividade",
                observacoes="Observações do serviço",
            ),
            valores=Valores(
                valor_servicos=100.0,
                desconto=0.0,
                valor_liquido=100.0,
                base_calculo=100.0,
                aliquota=0.0,
                valor_iss=100.0,
                outras_retencoes=0.0,
                retencoes_federais=0.0,
            ),
            tributos_federais=TributosFederais(
                pis=0.0, cofins=0.0, ir=0.0, inss=0.0, csll=0.0
            ),
        ),
    )
