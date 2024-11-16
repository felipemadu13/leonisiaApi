from django.db import models

class Servico(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Servico(nome={self.nome}, descricao={self.descricao[:30]}..., preco={self.preco})"

class ServicoRealizado(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.SET_NULL, blank=True, null=True, related_name='servicos_realizados')
    
    id = models.AutoField(primary_key=True)
    data = models.DateField()

    def __str__(self):
        return (
            f"Serviço: {self.servico.nome}, "
            f"Preço: R${self.servico.preco:.2f}, "
            f"Data: {self.data.strftime('%d/%m/%Y')}"
        )
