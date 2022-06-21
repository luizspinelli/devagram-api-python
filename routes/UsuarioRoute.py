from email.header import Header
from fastapi import APIRouter, Body, HTTPException, Depends, Header
from middlewares.JWTMIddleware import verificar_token
from models.UsuarioModel import UsuarioCriarModel
from repositories.UsuarioRepository import buscar_usuario_por_id
from services.AuthService import decode_jwt
from services.UsuarioService import buscar_usuario, registrar_usuario

router = APIRouter()


@router.post('/', response_description="Rota para criar um novo usuário")
async def rota_criar_usuario(usuario: UsuarioCriarModel = Body(...)):
    resultado = await registrar_usuario(usuario)
    if not resultado['status'] == 201:
        raise HTTPException(
            status_code=resultado['status'], detail=resultado['messagem'])
    return resultado


@router.get(
    '/me',
    response_description="Rota para buscar as informações do usuário logado",
    dependencies=[Depends(verificar_token)]
)
async def buscar_info_usuario_logado(Authorization: str = Header(default="")):
    try:
        token = Authorization.split(' ')[1]

        payload = decode_jwt(token)

        usuario_id = payload['usuario_id']

        usuario = await buscar_usuario(usuario_id)

        del usuario['dados']['senha']

        return usuario
    except:
        raise HTTPException(
            status_code=500, detail='Erro ao buscar informações do usuário logado')
