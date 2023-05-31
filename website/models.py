from django.db import models

class Item(models.Model):
    id_item = models.AutoField(primary_key=True)
    cod_item = models.IntegerField(unique=True, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return(f"({self.nome} {self.quantidade} {self.cod_item})")

class Consumidor(models.Model):
    id_consumidor = models.AutoField(primary_key=True)
    id_pessoa = models.CharField(unique= True,max_length=100, blank=True, null=True)
    email = models.CharField(unique= True,max_length=100, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)

class Funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    senha = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(unique= True,max_length=100, blank=True, null=True)
    login = models.CharField(unique= True,max_length=100, blank=True, null=True)

class HistoricoEmprestimo(models.Model):
    id_histemp = models.AutoField(db_column='id_histEmp', primary_key=True)  
    id_consumidor = models.ForeignKey('Consumidor', models.DO_NOTHING, db_column='id_consumidor', blank=True, null=True)
    id_funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='id_funcionario', blank=True, null=True)
    id_item = models.ForeignKey('Item', models.DO_NOTHING, db_column='id_item', blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)

class HistoricoConsumo(models.Model):
    id_histcons = models.AutoField(db_column='id_histCons', primary_key=True)
    id_item = models.ForeignKey('Item', models.DO_NOTHING, db_column='id_item', blank=True, null=True)
    id_funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='id_funcionario', blank=True, null=True)
    id_consumidor = models.ForeignKey('Consumidor', models.DO_NOTHING, db_column='id_consumidor', blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)