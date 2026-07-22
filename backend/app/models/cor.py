from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

class Cor(Base):
    __tablename__ = "cores"

    id: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    codigo_hex: Mapped[str | None] = mapped_column(
        String(7),
        nullable=True
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

    produtos: Mapped[list["ProdutoCor"]] = relationship(
        back_populates="cor"
    )