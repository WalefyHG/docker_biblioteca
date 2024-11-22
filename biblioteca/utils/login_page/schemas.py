from ninja import Schema



class LoginSchemaIn(Schema):
    email: str
    password: str


class LoginSchemaResponse(Schema):
    access_token: str
    refresh_token: str

class Message(Schema):
    message: str
    data: dict = None

