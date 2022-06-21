
from pickle import NONE
import motor.motor_asyncio
from decouple import config
from models.UsuarioModel import UsuarioCriarModel

MONGODB_URL = config("MONGODB_URL")

cliente = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

database = cliente.devagram

usuario_collection = database.get_collection("usuario")


async def usuario_helper(usuario):
    print('usuario_helper', usuario)

    return{
        "id": str(usuario["_id"]),
        "nome": str(usuario["nome"]),
        "email": str(usuario["email"]),
        "senha": str(usuario["senha"]),
        "foto": str(usuario["foto"]),
    }


async def criar_usuario(usuario: UsuarioCriarModel):

    usuario_criado = await usuario_collection.insert_one(usuario.__dict__)

    novo_usuario = await usuario_collection.find_one({"_id": usuario_criado.inserted_id})

    return await usuario_helper(novo_usuario)


async def listar_usuarios():
    return await usuario_collection.find()


async def buscar_usuario_por_email(email: str) -> dict:
    usuario_encontrado = await usuario_collection.find_one({"email": email})
    print("usuario_encontrado", usuario_encontrado)

    if usuario_encontrado:
        return await usuario_helper(usuario_encontrado)
    else:
        return usuario_encontrado


async def atualizar_usuario(id: str, dados_usuario: UsuarioCriarModel):
    usuario = await usuario_collection.find_one({"_id": ObjectId(id)})

    if usuario:
        usuario_atualizado = await usuario_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": dados_usuario}
        )

    return usuario_helper(usuario_atualizado)


async def deletar_usuario(id: str):
    usuario = await usuario_collection.find_one({"_id": ObjectId(id)})

    if usuario:
        usuario_atualizado = await usuario_collection.delete_one({"_id": ObjectId(id)})

    return usuario_helper(usuario)
