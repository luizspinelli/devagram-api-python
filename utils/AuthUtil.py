from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])


def gerar_senha_criptografada(senha: str):
    return pwd_context.hash(senha)


def verificar_senha(senha: str, senha_criptografada: str):
    return pwd_context.verify(senha, senha_criptografada)
