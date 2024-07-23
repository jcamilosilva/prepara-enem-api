from ninja import ModelSchema, Schema
from typing import List, Optional

class AssuntoSchema(Schema):
    nome: str

class AnoSchema(Schema):
    ano: int

class MateriaSchema(Schema):
    nome: str

class QuestaoSchema(Schema):
    numero: int
    ano: AnoSchema
    materia: MateriaSchema
    assuntos: List[AssuntoSchema]  # Deve ser uma lista de AssuntoSchema
    enunciado: str
    imagem: Optional[str]
    alternativa_a: str
    alternativa_b: str
    alternativa_c: str
    alternativa_d: str
    alternativa_e: str
    alternativa_correta: str


class NotFoundSchema(Schema):
    message: str