from myapp.libs.error import APIException


class NotFound(APIException):
    code=404
    msg='the resource are not_found 0__0'
    error_code=1001

class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed'
    error_code = 1005