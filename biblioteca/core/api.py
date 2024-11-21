from ninja import NinjaAPI
from livros.views import router as LivroRouter

api = NinjaAPI(title="Biblioteca API", version="1.0.0")


api.add_router('/livros', LivroRouter, tags=["Rota dos livros"])