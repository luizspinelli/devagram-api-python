
from pickle import NONE
from bson import ObjectId
import motor.motor_asyncio
from decouple import config
from models.PostagemModel import PostagemCriarModel
from models.UsuarioModel import UsuarioCriarModel
from utils.ConverterUtil import ConverterUtil

MONGODB_URL = config("MONGODB_URL")

cliente = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

database = cliente.devagram

postagem_collection = database.get_collection("postagem")

converterUtil = ConverterUtil()


class PostagemRepository:

    async def criar_postagem(self, postagem: PostagemCriarModel):

        postagem_criada = await postagem_collection.insert_one(postagem.__dict__)

        nova_postagem = await postagem_collection.find_one({"_id": postagem_criada.inserted_id})

        return converterUtil.postagem_converter(nova_postagem)

    async def listar_postagens(self):
        return await postagem_collection.find()

    async def buscar_postagem_por_id(self, id: str) -> dict:
        postagem_encontrado = await postagem_collection.find_one({"_id": ObjectId(id)})

        if postagem_encontrado:
            return converterUtil.postagem_converter(postagem_encontrado)
        else:
            return postagem_encontrado

    async def atualizar_postagem(self, id: str, dados_postagem: UsuarioCriarModel):
        print("atualizar_postagem")
        postagem = await postagem_collection.find_one({"_id": ObjectId(id)})
        print("postagem", postagem)
        if postagem:

            await postagem_collection.update_one(
                {"_id": ObjectId(id)}, {"$set": dados_postagem}
            )

            postagem_atualizado = await postagem_collection.find_one({"_id": ObjectId(id)})

        return converterUtil.postagem_converter(postagem_atualizado)

    async def deletar_postagem(self, id: str):
        postagem = await postagem_collection.find_one({"_id": ObjectId(id)})

        if postagem:
            postagem_atualizado = await postagem_collection.delete_one({"_id": ObjectId(id)})

        return converterUtil.postagem_converter(postagem_atualizado)
