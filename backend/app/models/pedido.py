from __future__ import annotations

from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

class Pedido(Base):
    __tablename__ = "pedidos"

    id: Mapped[int] = mapped_column(primary_key=True)

    codigo: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False
    )

    id_usuario: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id"),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    valor_total: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
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
        back_populates="pedidos"
    )

    itens: Mapped[list["ItemPedido"]] = relationship(
        back_populates="pedido",
        cascade="all, delete-orphan"
    )