from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

class ImagemProduto(Base):
    __tablename__ = "imagens_produto"

    id: Mapped[int] = mapped_column(primary_key=True)

    id_produto: Mapped[int] = mapped_column(
        ForeignKey("produtos.id", ondelete="CASCADE"),
        nullable=False
    )

    arquivo: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    ordem: Mapped[int] = mapped_column(
        Integer,
        default=1,
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

    produto: Mapped["Produto"] = relationship(
        back_populates="imagens"
    )