from django.shortcuts import render
from django.http import HttpResponse

from .models import Reservatorio, HistoricoVazoes, HistoricoEvaporacao


def index(request):
	query_reservatorio = Reservatorio.objects.all()
	if request.method == 'POST':
		id_nome = request.POST.get('name_list')
		query_vazao = HistoricoVazoes.objects.filter(reservatorio=id_nome)
		query_reservatorio = Reservatorio.objects.filter(id=id_nome)
		nome_reservatorio = query_reservatorio[0].nome
		return render(request, 'app/index.html', {'query_reservatorio': query_reservatorio, 'query_vazao': query_vazao})
	else:
		return render(request, 'app/index.html', {'query_reservatorio': query_reservatorio})


def index2(request):
	if request.method == 'POST':
		id = request.POST.get('name_list')
	else:
		id = 1

	query_reservatorio_all = Reservatorio.objects.all()
	query_vazao = HistoricoVazoes.objects.filter(reservatorio=id)
	query_reservatorio = Reservatorio.objects.filter(id=id)
	name = query_reservatorio[0].nome

	vaz_mensal = list(range(12))
	for q in query_vazao:
		if q.vazao != -999:
			if q.data.month == 1:
				vaz_mensal[0] += q.vazao
			if q.data.month == 2:
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

	for i in range(12):
		vaz_mensal[i] = vaz_mensal[i]/100

	series_1 = [{								# Gráfico vazão mensal.
		"name": name,
		"data": vaz_mensal
	}]

	vaz_anual = []								# Lista para armazenar as vazões.
	for x in query_vazao:						# Atribui o query a lista vazão.
		if x.vazao != -999:						# Verifica se o dado é válido.
			vaz_anual.append(x.vazao)			# Atribui a lista.

	series_2 = [{								# Grafico_2 Vazao Anual.
		"name": name,
		"data": vaz_anual
	}]

	return render(request, 'app/highchart_example.html', {'series_1': series_1, 'series_2': series_2, 'query_reservatorio_all': query_reservatorio_all})


def index3(request):
	""" Apresenta 3 gráficos, Vazão e Evaporação mensal, e vazão annual de um reservatório selecionado.
	"""

	if request.method == 'POST':							# Verifica se houve requisição
		id = request.POST.get('name_list')					# Pega o reservatório selecionado.
	else:
		id = 1												# Id padrão para abertura da página.

	query_reservatorio_all = Reservatorio.objects.all()		# Pega todos os reservatórios.
	query_reservatorio = Reservatorio.objects.filter(id=id)	# Pega o reservatório da id selecionada.
	
	name = query_reservatorio[0].nome						# Pega o nome do reservatório.

	vaz_mensal = HistoricoVazoes.getVazaoMensal(id=id)		# Retorna uma lista com a média da vazão mensal.
	vaz_anual = HistoricoVazoes.getVazaoAnual(id=id)		# Retorna uma lista com a vazão anual.
	evap = HistoricoEvaporacao.getEvapMensal(id=id)			# Retorna uma lista com a evaporação mensal.

	series_1 = [{											# Dicionário de dados para o Gráfico_1 vazão mensal.
		"name": name,
		"data": vaz_mensal
	}]

	series_2 = [{											# Grafico_2 Vazao Anual.
		"name": name,
		"data": vaz_anual
	}]

	series_3 = [{											# Grafico_3 Evaporação Mensal.
		"name": name,
		"data": evap
	}]

	return render(request, 'app/highchart_example.html', {'series_1': series_1, 'series_2': series_2, 'series_3': series_3, 'query_reservatorio_all': query_reservatorio_all})


def highchart_ex(request):
	query_vazao = HistoricoVazoes.objects.filter(reservatorio=1)
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
