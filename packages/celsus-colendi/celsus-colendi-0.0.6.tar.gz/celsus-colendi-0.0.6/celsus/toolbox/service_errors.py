from  werkzeug.exceptions import HTTPException

class ScoreNotFound(HTTPException):
    errorCode = 4001
    code = 404
    message = 'Score not found.'
    name = 'ScoreNotFound'
    time = 1

class ConfigNotFound(HTTPException):
    errorCode = 4002
    code = 404
    message = 'Config is not registered for the application.'
    name = 'ConfigNotFound'
    time = 1

class MissingPathParameter(HTTPException):
    errorCode = 4004
    code = 400
    message = 'Path parameter is missing.'
    name = 'MissingPathParameter'
    time = 1

class MissingHeaderParameter(HTTPException):
    errorCode = 4005
    code = 400
    message = 'Header parameter is missing.'
    name = 'MissingHeaderParameter'
    time = 1

class AuthorizationError(HTTPException):
    errorCode = 4006
    code = 401
    message = 'Not authorized.'
    name = 'AuthorizationError'
    time = 1

class ConnectionLost(HTTPException):
    errorCode = 4007
    code = 404
    message = 'DB connection lost'
    name = 'ConnectionLost'
    time = 15
    
class GetLimitConfigLost(HTTPException):
    errorCode = 4008
    code = 404
    message = 'There is error in DB connection for getting limit config'
    name = 'GetLimitConfigLost'
    time = 15
    
class UndifinedLimitConfig(HTTPException):
    errorCode = 4009
    code = 404
    message = 'Limit config is not defined for the app_id or score_group'
    name = 'UndifinedLimitConfig'
    time = 15

class ScoreCalculationError(HTTPException):
    errorCode = 4010
    code = 404
    message = 'Error occurs in the score calculation process.'
    name = 'ScoreCalculationError'
    time = 1
    
class TimeoutError(HTTPException):
    errorCode = 4011
    code = 408
    message = 'Timeout error occurs.'
    name = 'TimeoutError'
    time = 0.15
    
class RedisError(HTTPException):
    errorCode = 4012
    code = 408
    message = 'Redis error occurs.'
    name = 'RedisError'
    time = 1