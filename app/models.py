# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Reservatorio(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'reservatorio'
        

class HistoricoEvaporacao(models.Model):
    reservatorio = models.ForeignKey('Reservatorio', models.DO_NOTHING, blank=True, null=True)
    mes = models.CharField(max_length=30, blank=True, null=True)
    evaporacao = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historico_evaporacao'

    def getEvapMensal(id):            
        """ Retorna a evaporação mensal de um reservatório, se existir.
            id: (int) id do reservatório.
            return: (list) os dados da evaporação.
        """

        query_evap = HistoricoEvaporacao.objects.filter(reservatorio=id)# Query com o id do reservatório.
        evap = []   											        # Lista para armazenar a evaporação.
        for q in query_evap:								            # Verificação dos dados de evaporação.
            if q.evaporacao != -999:
                evap.append(q.evaporacao)

        return evap

class HistoricoVazao(models.Model):
    reservatorio = models.ForeignKey('Reservatorio', models.DO_NOTHING, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    vazao = models.FloatField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'historico_vazao'

    def getVazaoMensal(id):
        """ Calcula a média da vazão mensal de um reservatório.
            id: id do reservatório.
            return: (list) médias das vazões mensais, onde, indice 0 contém os valores de janeiro, índice 1, valores de fevereiro e assim por diante.
        """

        query_vazao = HistoricoVazao.objects.filter(reservatorio=id)   # Query com o id do resservatório.
        vaz_mensal = list(range(12))				                    # Lista para armazenar a vazão mensal.
        for q in query_vazao:
            if q.vazao != -999:                                         # Verifica se existe dado.
                if q.data.month == 1:                                   # Verifica qual o mês e relaciona com o indice da lista.
                    vaz_mensal[0] += q.vazao                            # Janeiro é o mês 1,
                if q.data.month == 2:                                   # Seus valores ficam no indice 0, e assim por diante.
                    vaz_mensal[1] += q.vazao
                if q.data.month == 3:
                    vaz_mensal[2] += q.vazao
                if q.data.month == 4:
                    vaz_mensal[3] += q.vazao
                if q.data.month == 5:
                    vaz_mensal[4] += q.vazao
                if q.data.month == 6:
                    vaz_mensal[5] += q.vazao
                if q.data.month == 7:
                    vaz_mensal[6] += q.vazao
                if q.data.month == 8:
                    vaz_mensal[7] += q.vazao
                if q.data.month == 9:
                    vaz_mensal[8] += q.vazao
                if q.data.month == 10:
                    vaz_mensal[9] += q.vazao
                if q.data.month == 11:
                    vaz_mensal[10] += q.vazao
                if q.data.month == 12:
                    vaz_mensal[11] += q.vazao

        for i in range(12):							                    # Calculo da média, 100 anos (1912 a 2012)
            vaz_mensal[i] = vaz_mensal[i]/100                           

        return vaz_mensal                                               # Retorna a lista.


    def getVazaoAnual(id):                           
        """ Pega todas as vazões de um reservatorio.
            id: id do reservatório.
            return: (list) dados das vazões.
        """
        
        query_vazao = HistoricoVazao.objects.filter(reservatorio=id)   # Query com o id do reservatorio.
        vaz_anual = []								                    # Lista para armazenar as vazões.
        for x in query_vazao:						                    # Atribui o query a lista vazão.
            if x.vazao != -999:						                    # Verifica se o dado é válido.
                vaz_anual.append(x.vazao)			                    # Atribui a lista.

        return vaz_anual                                                # Retorna a lista.


class Volume(models.Model):
    id = models.ForeignKey(Reservatorio, models.DO_NOTHING, db_column='id', primary_key=True)
    atual = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'volume'
