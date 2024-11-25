from .user_permission import BaseAcess

class UserPermission(BaseAcess):

    ROLE_USER = "user"


class AdminPermission(BaseAcess):

    ROLE_USER = "admin"


class EmployeePermission(BaseAcess):

    ROLE_USER = "employee"