from __future__ import annotations

from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id: Mapped[int] = mapped_column(primary_key=True)

    id_pedido: Mapped[int] = mapped_column(
        ForeignKey("pedidos.id", ondelete="CASCADE"),
        nullable=False
    )

    id_produto_cor: Mapped[int] = mapped_column(
        ForeignKey("produtos_cores.id"),
        nullable=False
    )

    quantidade: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    valor_unitario: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    valor_total: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    pedido: Mapped["Pedido"] = relationship(
        back_populates="itens"
    )

    produto_cor: Mapped["ProdutoCor"] = relationship(
        back_populates="itens_pedido"
    )