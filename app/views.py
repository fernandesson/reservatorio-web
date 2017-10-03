from django.shortcuts import render
from django.http import HttpResponse
import csv

from .models import Reservatorio, HistoricoVazao, HistoricoEvaporacao


def index(request):
	""" Apresenta 3 gráficos, Vazão e Evaporação mensal, e vazão annual de um reservatório selecionado.
	"""

	if request.method == 'POST':												# Verifica se houve requisição
		id = request.POST.get('name_list')										# Pega o reservatório selecionado.
	else:
		id = 1																	# Id padrão para abertura da página.

	query_reservatorio_all = Reservatorio.objects.all()							# Pega todos os reservatórios.
	query_reservatorio = Reservatorio.objects.filter(id=id)						# Pega o reservatório da id selecionada.
	
	name = query_reservatorio[0].nome											# Pega o nome do reservatório.

	vaz_mensal = HistoricoVazao.getVazaoMensal(id=id)							# Retorna uma lista com a média da vazão mensal.
	vaz_anual = HistoricoVazao.getVazaoAnual(id=id)								# Retorna uma lista com a vazão anual.
	evap = HistoricoEvaporacao.getEvapMensal(id=id)								# Retorna uma lista com a evaporação mensal.

	series_1 = [{																# Dicionário de dados para o Gráfico_1 vazão mensal.
		"name": name,
		"data": vaz_mensal
	}]

	series_2 = [{																# Grafico_2 Vazao Anual.
		"name": name,
		"data": vaz_anual
	}]

	series_3 = [{																# Grafico_3 Evaporação Mensal.
		"name": name,
		"data": evap
	}]

	return render(request, 'app/index.html', {'series_1': series_1, 'series_2': series_2, 'series_3': series_3, 'query_reservatorio_all': query_reservatorio_all})

def download(request):
	""" Página para o Download dos dados.
	"""

	if request.method == 'POST':												# Verifica se houve requisição
		id = request.POST.get('name_list')										# Pega o reservatório selecionado.
	else:
		id = 1																	# Id padrão para abertura da página.

	query_reservatorio_all = Reservatorio.objects.all()							# Pega todos os reservatórios.
	query_reservatorio = Reservatorio.objects.filter(id=id)						# Pega o reservatório da id selecionada.
	
	name = query_reservatorio[0].nome											# Pega o nome do reservatório.


	return render(request, 'app/download.html', {'query_reservatorio_all': query_reservatorio_all})

def download_csv(request):
	""" Gera um .csv com os dados do reservatorio selecionado
	"""
	if request.method == 'POST':												# Verifica se houve requisição
		id = request.POST.get('name_list')										# Pega o reservatório selecionado.
	else:
		id = 1																	# Id padrão para abertura da página.
	
	query_reservatorio = Reservatorio.objects.filter(id=id)						# Pega o reservatório da id selecionada.
	query_vazao = HistoricoVazao.objects.filter(reservatorio=id)				# Pega o reservatório da id selecionada.
	query_evap = HistoricoEvaporacao.objects.filter(reservatorio=id)
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="dados_reservatorio.csv"'
	
	writer = csv.writer(response)
	writer.writerow([query_reservatorio[0].nome, "Dados da Evaporação e Volume no fim do arquivo"])
	writer.writerow(["Data", 'Vazao'])
	for q in query_vazao:
		writer.writerow([q.data, q.vazao])

	writer.writerow([''])
	writer.writerow(['Mes', 'Evaporação'])
	for q in query_evap:
		writer.writerow([q.mes, q.evaporacao])

	writer.writerow([''])
	writer.writerow(['Volume Atual', 'Volume Total'])
	for q in query_reservatorio:
		writer.writerow([q.volume_atual, q.volume_total])

	return response


def index3(request):
	""" Apresenta 3 gráficos, Vazão e Evaporação mensal, e vazão annual de um reservatório selecionado.
	"""

	if request.method == 'POST':												# Verifica se houve requisição
		id = request.POST.get('name_list')										# Pega o reservatório selecionado.
	else:
		id = 1																	# Id padrão para abertura da página.

	query_reservatorio_all = Reservatorio.objects.all()							# Pega todos os reservatórios.
	query_reservatorio = Reservatorio.objects.filter(id=id)						# Pega o reservatório da id selecionada.
	
	name = query_reservatorio[0].nome											# Pega o nome do reservatório.

	vaz_mensal = HistoricoVazao.getVazaoMensal(id=id)							# Retorna uma lista com a média da vazão mensal.
	vaz_anual = HistoricoVazao.getVazaoAnual(id=id)								# Retorna uma lista com a vazão anual.
	evap = HistoricoEvaporacao.getEvapMensal(id=id)								# Retorna uma lista com a evaporação mensal.

	series_1 = [{																# Dicionário de dados para o Gráfico_1 vazão mensal.
		"name": name,
		"data": vaz_mensal
	}]

	series_2 = [{																# Grafico_2 Vazao Anual.
		"name": name,
		"data": vaz_anual
	}]

	series_3 = [{																# Grafico_3 Evaporação Mensal.
		"name": name,
		"data": evap
	}]

	return render(request, 'app/highchart_example.html', {'series_1': series_1, 'series_2': series_2, 'series_3': series_3, 'query_reservatorio_all': query_reservatorio_all})


def highchart_ex(request):
	query_vazao = HistoricoVazao.objects.filter(reservatorio=1)
	query_reservatorio = Reservatorio.objects.filter(id=1)

	vaz_anual = []
	for x in query_vazao:
		vaz_anual.append(x.vaz_anual)

	name = query_reservatorio[0].nome

	series_1 = [{
		"name": "Teste",
		"data": vaz_anual
	}]

	return render(request, 'app/highchart_example.html', {'series_1':series_1})
