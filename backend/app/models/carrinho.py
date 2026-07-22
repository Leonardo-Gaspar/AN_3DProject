from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

class Carrinho(Base):
    __tablename__ = "carrinhos"

    id: Mapped[int] = mapped_column(primary_key=True)

    id_usuario: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id", ondelete="CASCADE"),
        unique=True,
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

    usuario: Mapped["Usuario"] = relationship(
        back_populates="carrinho"
    )

    itens: Mapped[list["ItemCarrinho"]] = relationship(
        back_populates="carrinho",
        cascade="all, delete-orphan"
    )