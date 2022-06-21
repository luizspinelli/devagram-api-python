from fastapi import Header, HTTPException
from decouple import config

from services.AuthService import decode_jwt

JWT_SECRET = config('JWT_SECRET')


async def verificar_token(Authorization: str = Header(default="")):
    try:

        if not Authorization.split(' ')[0] == 'Bearer':
            raise HTTPException(
                status_code=401, detail='Necessário token para autenticação')

        token = Authorization.split(' ')[1]

        payload = decode_jwt(token)

        if not payload:
            raise HTTPException(status_code=401, detail='Token inválido')

        Header.id = payload['usuario_id']

        return payload

    except Exception as erro:
        print('erro', erro)
        raise HTTPException(status_code=401, detail='Token inválido')
