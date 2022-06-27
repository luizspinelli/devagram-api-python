from pydantic import BaseModel, Field
from fastapi import Form


class UsuarioModel (BaseModel):
    id: str = Field(...)
    nome: str = Field(...)
    email: str = Field(...)
    senha: str = Field(...)

    class Config:
        schema_extra = {
            "usuario": {
                "nome": "Fulano de tal",
                "email": "fulano@gmail.com",
                "senha": "senha123",
                "foto": "fulano.png",
            }
        }


def form_body(cls):
    print(cls)
    cls.__signature__ = cls.__signature__.replace(
        parameters=[
            arg.replace(default=(Form(...)))
            for arg in cls.__signature__.parameters.values()
        ]
    )

    return cls


@form_body
class UsuarioCriarModel (BaseModel):
    nome: str = Field(...)
    email: str = Field(...)
    senha: str = Field(...)

    class Config:
        schema_extra = {
            "usuario": {
                "nome": "Fulano de tal",
                "email": "fulano@gmail.com",
                "senha": "senha123",
            }
        }


class UsuarioLoginModel (BaseModel):
    email: str = Field(...)
    senha: str = Field(...)

    class Config:
        schema_extra = {
            "usuario": {
                "email": "fulano@gmail.com",
                "senha": "senha123",
            }
        }
