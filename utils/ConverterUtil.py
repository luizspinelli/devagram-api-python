class ConverterUtil:
    def usuario_converter(self, usuario):
        print('usuario_helper', usuario)

        return{
            "id": str(usuario["_id"]) if "_id" in usuario else "",
            "nome": usuario["nome"] if "nome" in usuario else "",
            "email": usuario["email"] if "email" in usuario else "",
            "senha": usuario["senha"] if "senha" in usuario else "",
            "foto": usuario["foto"] if "foto" in usuario else "",
        }

    def postagem_converter(self, postagem):
        print('postagem_helper', postagem)

        return{
            "id": str(postagem["_id"]) if "_id" in postagem else "",
            "usuario": postagem["usuario"] if "usuario" in postagem else "",
            "foto": postagem["foto"] if "foto" in postagem else "",
            "legenda": postagem['legenda'] if "legenda" in postagem else "",
            "data": postagem['data'] if "data" in postagem else "",
            "curtidas": postagem['curtidas'] if "curtidas" in postagem else "",
            "comentarios": postagem['comentarios'] if "comentarios" in postagem else "",
        }
