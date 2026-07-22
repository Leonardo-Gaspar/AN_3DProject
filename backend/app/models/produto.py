from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Produto(Base):
    __tablename__ = "produtos"

    id: Mapped[int] = mapped_column(primary_key=True)

    codigo: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False
    )

    id_categoria: Mapped[int] = mapped_column(
        ForeignKey("categorias.id"),
        nullable=False
    )

    nome: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    descricao: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    preco: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    peso: Mapped[float | None] = mapped_column(
        Numeric(8, 2),
        nullable=True
    )

    ativo: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
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
        onupdate=func.now(),
        nullable=False
    )

    categoria: Mapped["Categoria"] = relationship(
        back_populates="produtos"
    )

    cores: Mapped[list["ProdutoCor"]] = relationship(
        back_populates="produto",
        cascade="all, delete-orphan"
    )

    imagens: Mapped[list["ImagemProduto"]] = relationship(
        back_populates="produto",
        cascade="all, delete-orphan"
    )