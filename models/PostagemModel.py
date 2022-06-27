from pydantic import BaseModel, Field
from typing import List

from models.ComentarioModel import ComentarioModel
from models.UsuarioModel import UsuarioModel


class PostagemModel (BaseModel):
    id: str = Field(...)
    usuario: UsuarioModel = Field(...)
    foto: str = Field(...)
    legenda: str = Field(...)
    data: str = Field(...)
    curtidas: int = Field(...)
    comentarios: List[ComentarioModel] = Field(...)

    class Config:
        schema_extra = {
            "postagem": {
                "id": "",
                "usuario": "",
                "foto": "",
                "legenda": "",
                "data": "",
                "curtidas": "",
                "comentarios": "",
            }
        }


class PostagemCriarModel (BaseModel):
    usuario: UsuarioModel = Field(...)
    foto: str = Field(...)
    legenda: str = Field(...)

    class Config:
        schema_extra = {
            "postagem": {
                "usuario": "",
                "foto": "",
                "legenda": "",
            }
        }
