import os
from datetime import date

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from middlewares.JWTMIddleware import verificar_token
from models.PostagemModel import PostagemCriarModel

router = APIRouter()


@router.post('/', response_description="Rota para criar uma nova postagem")
async def rota_criar_postagem(file: UploadFile, postagem: PostagemCriarModel = Depends(PostagemCriarModel)):
    caminho_arquivo = f'files/foto-{date.today().strftime("%H-%M-%S")}.png'

    with open(caminho_arquivo, 'wb') as arquivo:
        arquivo.write(file.file.read())

    resultado = await registrar_usuario(usuario, caminho_arquivo)

    os.remove(caminho_arquivo)

    if not resultado['status'] == 201:
        raise HTTPException(
            status_code=resultado['status'], detail=resultado['messagem'])

    del resultado['dados']['senha']

    return resultado
