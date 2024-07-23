from django.db import models

class Ano(models.Model):
    ano = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.ano)


class Materia(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Assunto(models.Model):
    nome = models.CharField(max_length=100)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Questao(models.Model):
    numero = models.IntegerField()
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    assuntos = models.ManyToManyField(Assunto)  # ManyToManyField
    enunciado = models.TextField()
    imagem = models.ImageField(upload_to='imagens_questoes/', blank=True, null=True)
    alternativa_a = models.CharField(max_length=500)
    alternativa_b = models.CharField(max_length=500)
    alternativa_c = models.CharField(max_length=500)
    alternativa_d = models.CharField(max_length=500)
    alternativa_e = models.CharField(max_length=500)
    alternativa_correta = models.CharField(max_length=1, choices=[
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E')
    ])

    class Meta:
        unique_together = ('numero', 'ano')

    def __str__(self):
        return f"Questão {self.numero} ({self.ano.ano})"
