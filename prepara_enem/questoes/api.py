from ninja import NinjaAPI
from typing import Optional, List
from django.http import Http404
from questoes.models import Questao
from questoes.schema import QuestaoSchema

api = NinjaAPI()

@api.get("/questoes", response=List[QuestaoSchema])
def questoes(request, ano: Optional[int] = None, materia: Optional[str] = None, assunto: Optional[str] = None):
    questoes = Questao.objects.prefetch_related('assuntos', 'materia')

    if ano:
        questoes = questoes.filter(ano__ano=ano)
    if materia:
        questoes = questoes.filter(materia__nome__icontains=materia)  # Assumindo que 'nome' é o campo que você quer filtrar
    if assunto:
        questoes = questoes.filter(assuntos__nome__icontains=assunto)

    if not questoes.exists():
        raise Http404("Item não encontrado")

    return [QuestaoSchema.from_orm(questao) for questao in questoes]
