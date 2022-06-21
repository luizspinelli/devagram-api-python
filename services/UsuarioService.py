

from models.UsuarioModel import UsuarioCriarModel
from repositories.UsuarioRepository import (
    listar_usuarios,
    atualizar_usuario,
    buscar_usuario_por_id,
    buscar_usuario_por_email,
    criar_usuario
)
from utils.AuthUtil import gerar_senha_criptografada


async def registrar_usuario(usuario: UsuarioCriarModel):
    try:
        usuario_encontrado = await buscar_usuario_por_email(usuario.email)

        if usuario_encontrado:
            return {
                "messagem": f'E-mail {usuario.email} não está disponível',
                "dados": "",
                "status": 400
            }
        else:
            usuario.senha = gerar_senha_criptografada(usuario.senha)

            novo_usuario = await criar_usuario(usuario)

            return {
                "messagem": "Usuario cadastrado com sucesso",
                "dados": novo_usuario,
                "status": 201
            }
    except Exception as error:
        return {
            "messagem": "Erro interno do servidor",
            "dados": str(error),
            "status": 500
        }


async def buscar_usuario(id: str):
    try:
        usuario = await buscar_usuario_por_id(id)

        if usuario:
            return {
                "messagem": "Usuario encontrado",
                "dados": usuario,
                "status": 200
            }
        else:
            return {
                "messagem": "Usuario não encontrado",
                "dados": "",
                "status": 404
            }
    except:
        return {
            "messagem": "Erro interno do servidor",
            "dados": "",
            "status": 500
        }
