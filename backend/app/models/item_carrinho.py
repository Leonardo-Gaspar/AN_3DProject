from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

class ItemCarrinho(Base):
    __tablename__ = "itens_carrinho"

    id: Mapped[int] = mapped_column(primary_key=True)

    id_carrinho: Mapped[int] = mapped_column(
        ForeignKey("carrinhos.id", ondelete="CASCADE"),
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

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    carrinho: Mapped["Carrinho"] = relationship(
        back_populates="itens"
    )

    produto_cor: Mapped["ProdutoCor"] = relationship(
        back_populates="itens_carrinho"
    )