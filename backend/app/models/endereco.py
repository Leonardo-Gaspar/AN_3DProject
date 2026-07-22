from __future__ import annotations
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

class Endereco(Base):
    __tablename__ = "enderecos"

    id: Mapped[int] = mapped_column(primary_key=True)

    id_usuario: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id", ondelete="CASCADE"),
        nullable=False
    )

    cep: Mapped[str] = mapped_column(
        String(9),
        nullable=False
    )

    logradouro: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    numero: Mapped[str] = mapped_column(
        String(15)
    )

    complemento: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True
    )

    bairro: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    cidade: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    estado: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    pais: Mapped[str] = mapped_column(
        String(50),
        default="Brasil",
        nullable=False
    )

    principal: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    usuario: Mapped[Usuario] = relationship(
        back_populates="enderecos"
    )