from django.db import models

class Equipe(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    regiao = models.CharField(max_length=50)
    data_fundacao = models.DateField()

    def __str__(self):
        return self.nome

class Jogador(models.Model):
    nickname = models.CharField(max_length=50, unique=True)
    rota = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    # Chave estrangeira exigida na rubrica
    equipe = models.ForeignKey(Equipe, related_name='jogadores', on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname