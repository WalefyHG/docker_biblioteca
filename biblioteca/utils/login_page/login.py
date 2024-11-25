from ninja import Form
from ninja_extra import api_controller, route, status
from ninja_jwt.tokens import AccessToken, RefreshToken
from django.contrib.auth.hashers import check_password
from ninja_jwt.schema import TokenObtainPairInputSchema, TokenObtainPairOutputSchema
from ninja_jwt.controller import TokenObtainPairController
from .schemas import *
from user.models import User

@api_controller(
    "login/",
    tags=["Rota de Login"],
    auth=None
)

class LoginController(TokenObtainPairController):

    @route.post('', auth=None, response=Message)
    def login(self, request, payload: Form[TokenObtainPairInputSchema]):
        try:
            user = User.objects.get(email=payload.email)

            if check_password(payload.password, user.password):
                access_token = AccessToken.for_user(user)
                refresh_token = RefreshToken.for_user(user)

                return status.HTTP_200_OK, Message(
                    message="Login efetuado com sucesso",
                    data={
                        "access_token": str(access_token),
                        "refresh_token": str(refresh_token)
                    }
                )
            return status.HTTP_401_UNAUTHORIZED
        except User.DoesNotExist:
            return LoginSchemaResponse(
                message="Usuário não encontrado"
            )
        