from fastapi import APIRouter, Body, HTTPException
from models.UsuarioModel import UsuarioLoginModel
from services.AuthService import decode_jwt, gerar_token_jwt, login_service

router = APIRouter()


@router.post('/login', response_description="")
async def rota_logar_usuario(usuario: UsuarioLoginModel = Body(...)):
    resultado = await login_service(usuario)
    if not resultado['status'] == 200:
        raise HTTPException(
            status_code=resultado['status'], detail=resultado['messagem'])
    del resultado['dados']['senha']

    token = gerar_token_jwt(resultado['dados']['id'])

    resultado['token'] = token

    return resultado