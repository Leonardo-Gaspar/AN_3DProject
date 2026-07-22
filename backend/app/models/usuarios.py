from __future__ import annotations
from datetime import datetime

from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)

    codigo: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False
    )

    nome: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False
    )

    senha_hash: Mapped[str] = mapped_column(
        nullable=False
    )

    cpf_cnpj: Mapped[str] = mapped_column(
        String(18),
        unique=True,
        nullable=False
    )

    tipo: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    ativo: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    enderecos: Mapped[list[Endereco]] = relationship(
        back_populates="usuario",
        cascade="all, delete-orphan"
    )

    carrinho: Mapped[Carrinho] = relationship(
        back_populates="usuario",
        uselist=False
    )

    pedidos: Mapped[list[Pedido]] = relationship(
        back_populates="usuario"
    )