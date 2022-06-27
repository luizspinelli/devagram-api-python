from pydantic import BaseModel, Field
from typing import List

from models.UsuarioModel import UsuarioModel


class ComentarioModel (BaseModel):
    usuario: UsuarioModel = Field(...)
    comentario: str = Field(...)
