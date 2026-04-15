"""Pydantic schemas for the TCE-PA feature."""

from __future__ import annotations

from pydantic import BaseModel


class DiarioOficial(BaseModel):
    """Publicação no Diário Oficial do TCE-PA."""

    numero_publicacao: int | None = None
    publicacao: str | None = None
    data_publicacao: str | None = None
    tipo_ato: str | None = None
