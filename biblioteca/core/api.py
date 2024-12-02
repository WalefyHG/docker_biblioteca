from ninja_extra import NinjaExtraAPI
from livros.views import LivroController
from utils.login_page.login import LoginController
from user.views import UserController
from ninja_jwt.authentication import JWTAuth
from .encoder import MyJSONRenderer


api = NinjaExtraAPI(title="Biblioteca API", version="1.0.0", auth=JWTAuth(), renderer=MyJSONRenderer())

api.register_controllers(LivroController)
api.register_controllers(LoginController)
api.register_controllers(UserController)