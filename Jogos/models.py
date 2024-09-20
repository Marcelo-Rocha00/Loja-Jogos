from django.db import models


# criação dos models 


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
   
    
    def __str__(self):
        return self.nome

#na class jogos tem uma chave estrangeira que relaciona 1 desenvolvedor é 1 distribuidora a 1 jogo
class Jogo(models.Model):
    nome = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    data_lançamento = models.DateField()
    sobre_o_jogo = models.TextField()
    preço = models.FloatField(default=0)
    desenvolvedor = models.ForeignKey("Desenvolvedor",on_delete=models.CASCADE)
    distribuidora = models.ForeignKey("Distribuidora",on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nome} R${self.preço}'

#nesse class temos uma chave estrangeira que relaciona mais de um jogo a um desenvolvedor
class Desenvolvedor(models.Model):
    nome = models.CharField(max_length=255)
    jogos_lançados = models.ManyToManyField(
        Jogo,related_name='jogos_lançados', blank=True)
    sobre = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.nome



class Distribuidora(models.Model):
    nome = models.CharField(max_length=255)
    sobre = models.TextField(null=True, blank=True)
    jogo_distribuidos = models.ManyToManyField(
    Jogo, related_name= "jogo_distribuidora",blank=True)#criação de chave estrangeira muitos para muito para que 
    # distribuidora tenha mais de um jogo é mais de um desenvolvedor relacionado a ela
    desenvolvedores_associados = models.ManyToManyField(Desenvolvedor,related_name= "desenvolvedores_associados",blank=True)

    def __str__(self):
        return self.nome