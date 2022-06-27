import os
from datetime import date

from fastapi import APIRouter, Body, Depends, Header, HTTPException, UploadFile
from middlewares.JWTMIddleware import verificar_token
from models.UsuarioModel import UsuarioCriarModel
from services.AuthService import AuthService
from services.UsuarioService import UsuarioService

router = APIRouter()

usuarioService = UsuarioService()
authService = AuthService()


@router.post('/', response_description="Rota para criar um novo usuário")
async def rota_criar_usuario(file: UploadFile, usuario: UsuarioCriarModel = Depends(UsuarioCriarModel)):
    caminho_arquivo = f'files/foto-{date.today().strftime("%H-%M-%S")}.png'

    with open(caminho_arquivo, 'wb') as arquivo:
        arquivo.write(file.file.read())

    resultado = await usuarioService.registrar_usuario(usuario, caminho_arquivo)

    print("resultado", resultado)

    os.remove(caminho_arquivo)

    if not resultado['status'] == 201:
        raise HTTPException(
            status_code=resultado['status'], detail=resultado['messagem'])

    del resultado['dados']['senha']

    return resultado


@router.get(
    '/me',
    response_description="Rota para buscar as informações do usuário logado",
    dependencies=[Depends(verificar_token)]
)
async def buscar_info_usuario_logado(Authorization: str = Header(default="")):
    try:
        token = Authorization.split(' ')[1]

        payload = authService.decode_jwt(token)

        usuario_id = payload['usuario_id']

        usuario = await usuarioService.buscar_usuario(usuario_id)

        del usuario['dados']['senha']

        return usuario
    except:
        raise HTTPException(
            status_code=500, detail='Erro ao buscar informações do usuário logado')
