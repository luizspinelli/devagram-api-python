from distutils.command.config import config
import time

import jwt
from models.UsuarioModel import UsuarioLoginModel
from decouple import config

from repositories.UsuarioRepository import buscar_usuario_por_email
from utils.AuthUtil import verificar_senha

JWT_SECRET = config('JWT_SECRET')


def decode_jwt(token: str) -> dict:
    try:
        token_decodificado = jwt.decode(
            token, JWT_SECRET, algorithms=['HS256'])

        if token_decodificado['expires'] >= time.time():
            return token_decodificado
        else:
            return None

    except Exception as erro:
        print(erro)
        return None


def gerar_token_jwt(usuario_id: str) -> str:
    payload = {
        'usuario_id': usuario_id,
        'expires': time.time() + 600
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm='HS256')

    return token


async def login_service(usuario: UsuarioLoginModel):
    usuario_encontrado = await buscar_usuario_por_email(usuario.email)

    if not usuario_encontrado:
        return {
            "messagem": 'email ou senha incorretos',
            "dados": "",
            "status": 401
        }
    else:
        if verificar_senha(usuario.senha, usuario_encontrado['senha']):
            return {
                "messagem": 'Login realizado com sucesso',
                "dados": usuario_encontrado,
                "status": 200
            }
        else:
            return {
                "messagem": 'email ou senha incorretos',
                "dados": "",
                "status": 401
            }
