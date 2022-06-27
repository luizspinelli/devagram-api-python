
from pickle import NONE
from bson import ObjectId
import motor.motor_asyncio
from decouple import config
from models.UsuarioModel import UsuarioCriarModel
from utils.ConverterUtil import ConverterUtil

MONGODB_URL = config("MONGODB_URL")

cliente = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

database = cliente.devagram

usuario_collection = database.get_collection("usuario")

converterUtil = ConverterUtil()


class UsuarioRepository:

    async def criar_usuario(self, usuario: UsuarioCriarModel):

        usuario_criado = await usuario_collection.insert_one(usuario.__dict__)

        novo_usuario = await usuario_collection.find_one({"_id": usuario_criado.inserted_id})

        return converterUtil.usuario_converter(novo_usuario)

    async def listar_usuarios(self):
        return await usuario_collection.find()

    async def buscar_usuario_por_email(self, email: str) -> dict:
        usuario_encontrado = await usuario_collection.find_one({"email": email})
        print("usuario_encontrado", usuario_encontrado)

        if usuario_encontrado:
            return converterUtil.usuario_converter(usuario_encontrado)
        else:
            return usuario_encontrado

    async def buscar_usuario_por_id(self, id: str) -> dict:
        usuario_encontrado = await usuario_collection.find_one({"_id": ObjectId(id)})

        if usuario_encontrado:
            return converterUtil.usuario_converter(usuario_encontrado)
        else:
            return usuario_encontrado

    async def atualizar_usuario(self, id: str, dados_usuario: UsuarioCriarModel):
        print("atualizar_usuario")
        usuario = await usuario_collection.find_one({"_id": ObjectId(id)})
        print("usuario", usuario)
        if usuario:

            await usuario_collection.update_one(
                {"_id": ObjectId(id)}, {"$set": dados_usuario}
            )

            usuario_atualizado = await usuario_collection.find_one({"_id": ObjectId(id)})

        return converterUtil.usuario_converter(usuario_atualizado)

    async def deletar_usuario(self, id: str):
        usuario = await usuario_collection.find_one({"_id": ObjectId(id)})

        if usuario:
            usuario_atualizado = await usuario_collection.delete_one({"_id": ObjectId(id)})

        return converterUtil.usuario_converter(usuario_atualizado)
