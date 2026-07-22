from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

class ProdutoCor(Base):
    __tablename__ = "produtos_cores"

    __table_args__ = (
        UniqueConstraint(
            "id_produto",
            "id_cor",
            name="uk_produto_cor"
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    id_produto: Mapped[int] = mapped_column(
        ForeignKey("produtos.id", ondelete="CASCADE"),
        nullable=False
    )

    id_cor: Mapped[int] = mapped_column(
        ForeignKey("cores.id"),
        nullable=False
    )

    quantidade_estoque: Mapped[int] = mapped_column(
        Integer,
        default=0,
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

    produto: Mapped["Produto"] = relationship(
        back_populates="cores"
    )

    cor: Mapped["Cor"] = relationship(
        back_populates="produtos"
    )

    itens_carrinho: Mapped[list["ItemCarrinho"]] = relationship(
        back_populates="produto_cor"
    )

    itens_pedido: Mapped[list["ItemPedido"]] = relationship(
        back_populates="produto_cor"
    )