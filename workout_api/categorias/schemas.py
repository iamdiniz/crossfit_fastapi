
from typing import Annotated
from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class Categoria(BaseSchema):
    nome: Annotated[str, Field(description="Nome da categoria", example='Musculação', max_length=10)]
    descricao: Annotated[str, Field(description="Descrição da categoria", example='Treinos de musculação', max_length=255)]