

from models.UsuarioModel import UsuarioCriarModel
from providers.AWSProvider import AWSProvider
from repositories.UsuarioRepository import UsuarioRepository

from utils.AuthUtil import gerar_senha_criptografada

awsProvider = AWSProvider()
usuarioRepository = UsuarioRepository()


class UsuarioService:

    async def registrar_usuario(self, usuario: UsuarioCriarModel, caminho_arquivo):
        try:
            usuario_encontrado = await usuarioRepository.buscar_usuario_por_email(usuario.email)

            if usuario_encontrado:
                return {
                    "messagem": f'E-mail {usuario.email} não está disponível',
                    "dados": "",
                    "status": 400
                }
            else:
                usuario.senha = gerar_senha_criptografada(usuario.senha)

                novo_usuario = await usuarioRepository.criar_usuario(usuario)

                url_foto = awsProvider.upload_arquivo_s3(
                    f'fotos-perfil/{novo_usuario["id"]}.png',
                    caminho_arquivo,
                )

                usuario_atualizado = await usuarioRepository.atualizar_usuario(
                    novo_usuario["id"], {"foto": url_foto})

                print("usuario_atualizado", usuario_atualizado)

                return {
                    "messagem": "Usuario cadastrado com sucesso",
                    "dados": usuario_atualizado,
                    "status": 201
                }
        except Exception as error:
            return {
                "messagem": "Erro interno do servidor",
                "dados": str(error),
                "status": 500
            }

    async def buscar_usuario(self, id: str):
        try:
            usuario = await usuarioRepository.buscar_usuario_por_id(id)

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
