from django.db import models

class Servico(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Servico(nome={self.nome}, descricao={self.descricao[:30]}..., preco={self.preco})"
    
class ServicoRealizado(models.Model):
    id = models.AutoField(primary_key=True)
    nome_servico = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return (
            f"Serviço: {self.nome_servico}, "
            f"Preço: R${self.preco:.2f}, "
            f"Data: {self.data.strftime('%d/%m/%Y')}"
        )