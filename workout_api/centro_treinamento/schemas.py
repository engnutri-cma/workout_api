from typing import Annotated
from pydantic import BaseModel, Field, UUID4
from workout_api.contrib.schemas import BaseSchema

class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento', example='Rua A, 123', max_length=60)]
    proprietario: Annotated[str, Field(description='Nome do proprietário do centro de treinamento', example='Carlos Silva', max_length=30)]


class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]    

class CentroTreinamentoAtleta(BaseModel):
    centro_id: int
    atleta_id: int