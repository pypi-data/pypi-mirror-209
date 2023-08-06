from fastapi import (
    Depends,
    FastAPI,
)
from fastapi.security import HTTPAuthorizationCredentials

from src.validate.validate_jwt import (
    security,
    validate_jwt_scopes,
)

app = FastAPI()


@app.get('/jungle')
@validate_jwt_scopes(required_scopes=['block-storage.read'])
async def jungle(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):

    return {'message': 'WELCOME TO THE JUNGLE !!!!'}
