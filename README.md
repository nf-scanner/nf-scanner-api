# nf-scanner-api

API para processamento de notas fiscais utilizando a biblioteca nf-scanner-core.

## Funcionalidades

- **Processamento de NFSe via API**: Endpoint para processamento de documentos NFSe em formato PDF ou imagem.
- **Integração com nf-scanner-core**: Utiliza a biblioteca core para extração e análise dos dados.
- **API RESTful**: Interface HTTP para integração com outros sistemas.
- **Documentação Swagger**: Interface de documentação interativa para facilitar o uso da API.

## Arquitetura

A API segue uma **Arquitetura em Camadas (Layered Architecture)**, baseando-se no **Clean Architecture**:

```ascii
┌─────────────────────────────────┐
│         Interface HTTP          │
│      (FastAPI Endpoints)        │
├─────────────────────────────────┤
│         Camada Aplicação        │
│     (Serviços e Use Cases)      │
├─────────────────────────────────┤
│          Camada Domínio         │
│     (Modelos e Entidades)       │
├─────────────────────────────────┤
│      Camada Infraestrutura      │
│  (Integração nf-scanner-core)   │
└─────────────────────────────────┘
```

### Principais Componentes

1. **Endpoints API**: Pontos de entrada da API para processamento de documentos.
   - Aceita uploads de arquivos via multipart/form-data
   - Retorna dados estruturados em formato JSON

2. **Módulos**:
   - **routes/**: Contém os endpoints da API
   - **services/**: Implementa a lógica de negócios
   - **models/**: Define os modelos de dados e schemas
   - **utils/**: Funções utilitárias para a API

3. **Princípios de Design**:
   - **API First**: Design orientado à API com documentação automática
   - **Separação de Responsabilidades**: Cada módulo tem uma função específica
   - **Extensibilidade**: Facilidade para adicionar novos endpoints e funcionalidades

## Instalação

### Dependências

O projeto utiliza UV como gerenciador de pacotes e ambientes virtuais. Por isso, é necessário instalar o UV antes de instalar as dependências do projeto. Requisitos para dependências:

- Python 3.12 ou superior
- UV

### Instalação do UV

Para instalar o UV, siga os passos da [documentação oficial](https://docs.astral.sh/uv/getting-started/installation/).

### Configuração do Ambiente

Clone o repositório

```bash
git clone https://github.com/nf-scanner/nf-scanner-api.git
cd nf-scanner-api
```

Crie um ambiente virtual com UV

```bash
uv venv
```

Ative o ambiente virtual

```bash
# Linux/macOS
source .venv/bin/activate
```

Instale as dependências do projeto

```bash
uv pip install -e ".[dev]"
```

## Desenvolvimento

### Configuração de Variáveis de Ambiente

O projeto utiliza arquivos `.env` para gerenciar as configurações da API e chaves de integração.

1. Crie um arquivo `.env` na raiz do projeto (você pode copiar o arquivo `env.example`)

```bash
cp env.example .env
```

2. Edite o arquivo `.env` e adicione suas configurações

```
CLAUDE_API_KEY=sua-chave-api-aqui
CLAUDE_API_ID=claude-sonnet-4-5-20250929
CLAUDE_API_ALIAS=claude-sonnet-4-5
```

3. A API carregará automaticamente as configurações do arquivo `.env`

> **IMPORTANTE**: Nunca compartilhe ou comite o arquivo `.env` com suas chaves. O arquivo `.env` está incluído no `.gitignore`.

### Pré-commit hooks

O projeto utiliza pre-commit hooks para garantir a qualidade do código. Para configurá-los:

Instale as dependências de desenvolvimento

```bash
uv pip install -e ".[dev]"
```

Instale os hooks do pre-commit

```bash
pre-commit install
```

Os seguintes hooks serão executados automaticamente antes de cada commit:

- **Black**: Formata automaticamente o código python
- **uv-build**: Executa o build do projeto

## Uso da API

### Iniciar o servidor

Para iniciar o servidor da API:

```bash
api-start
```

A API estará disponível em http://localhost:8000.

### Documentação da API

A documentação interativa da API está disponível em:

- Swagger UI: http://localhost:8000/docs

### Endpoints Principais

#### Verificação de saúde

```bash
curl -X GET http://localhost:8000/health
```

Resposta:

```json
{
  "status": "ok"
}
```

#### Processar NFSe

```bash
curl -X POST http://localhost:8000/documents/process_nfse \
  -H "Content-Type: multipart/form-data" \
  -F "document=@/caminho/para/nfse.pdf" \
  -F "ai_extraction=false" \
  -F "ai_parse=false"
```

### Exemplos de Uso

#### Exemplo 1: Processamento básico

```python
import requests

url = "http://localhost:8000/documents/process_nfse"
files = {"document": open("caminho/para/nfse.pdf", "rb")}

response = requests.post(url, files=files)
nfse_data = response.json()

print(f"Número da NFSe: {nfse_data['numero_nfse']}")
print(f"Valor total: {nfse_data['valores']['valor_servicos']}")
```

#### Exemplo 2: Processamento com IA

```python
import requests

url = "http://localhost:8000/documents/process_nfse"
files = {"document": open("caminho/para/nfse.jpg", "rb")}
data = {"use_ai": "true"}

response = requests.post(url, files=files, data=data)
nfse_data = response.json()

print(f"Dados processados com IA: {nfse_data}")
```

## Testes

O projeto não possui testes automatizados, porém está considerado na lista de pendências para implementação futura.

## Custo

A API utiliza o nf-scanner-core para processamento, que pode usar a API do Claude para extração e análise com os seguintes custos aproximados:

| Operação                                    | Modelo     | Custo por NFSe |
| ------------------------------------------- | ---------- | -------------- |
| Parse do texto (AI Parse)                   | Claude 4.5 | U$0,02         |
| Extração do texto da imagem (AI Extraction) | Claude 4.5 | U$0,03         |
| Extração + Parse combinados                 | Claude 4.5 | U$0,03         |

**Observações:**
- Os valores são aproximados e podem variar de acordo com o tamanho do documento
- A extração de imagens já inclui o parse dos dados no padrão de saída
- A extração de PDFs não utiliza IA e não gera custos adicionais