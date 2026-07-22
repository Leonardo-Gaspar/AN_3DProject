from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict

class UsuarioBase(BaseModel):
    codigo: str
    nome: str
    username: str
    email: EmailStr
    cpf_cnpj: str | None = None
    tipo: str
    ativo: bool = True

class UsuarioCreate(UsuarioBase):
    senha: str

class UsuarioUpdate(BaseModel):
    nome: str | None = None
    email: EmailStr | None = None
    cpf_cnpj: str | None = None
    tipo: str | None = None
    ativo: bool | None = None

class UsuarioResponse(UsuarioBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )