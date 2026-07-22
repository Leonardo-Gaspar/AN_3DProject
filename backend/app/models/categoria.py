from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(primary_key=True)

    codigo: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False
    )

    nome: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    descricao: Mapped[str | None] = mapped_column(nullable=True)

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

    produtos: Mapped[list["Produto"]] = relationship(
        back_populates="categoria"
    )