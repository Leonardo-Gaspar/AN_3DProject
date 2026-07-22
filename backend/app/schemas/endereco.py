from datetime import datetime

from pydantic import BaseModel, ConfigDict

class EnderecoBase(BaseModel):
    cep: str
    logradouro: str
    numero: str
    complemento: str | None = None
    bairro: str | None = None
    cidade: str
    estado: str
    pais: str = "Brasil"
    principal: bool = False

class EnderecoCreate(EnderecoBase):
    id_usuario: int

class EnderecoUpdate(BaseModel):
    cep: str | None = None
    logradouro: str | None = None
    numero: str | None = None
    complemento: str | None = None
    bairro: str | None = None
    cidade: str | None = None
    estado: str | None = None
    pais: str | None = None
    principal: bool | None = None

class EnderecoResponse(EnderecoBase):
    id: int
    id_usuario: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )