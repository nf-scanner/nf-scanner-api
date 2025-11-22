from fastapi import FastAPI
from .routes.document import router as document_router
from .routes.health import router as health_router

app = FastAPI(
    title="NF Scanner API",
    description="API para processamento de notas fiscais. Permite a extração de dados estruturados de documentos fiscais eletrônicos.",
    version="1.0.0",
)

app.include_router(health_router)
app.include_router(document_router)


def main():
    import uvicorn

    uvicorn.run("nf_scanner_api.app:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
