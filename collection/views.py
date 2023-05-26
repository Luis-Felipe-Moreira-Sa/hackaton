from django.shortcuts import render
from django.views import View
from .models import TipoResiduo, LocalColeta

class TiposResiduosView(View):
    def get(self, request):
        tipos_residuos = TipoResiduo.objects.all()
        return render(request, 'tipos_residuos.html', {'tipos_residuos': tipos_residuos})

class CadastroLocalColetaView(View):
    def get(self, request):
        return render(request, 'cadastro_local_coleta.html')

    def post(self, request):
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        descricao = request.POST.get('descricao')
        tipos_residuos = request.POST.getlist('tipos_residuos')

        local_coleta = LocalColeta.objects.create(
            nome=nome,
            endereco=endereco,
            latitude=latitude,
            longitude=longitude,
            descricao=descricao
        )
        local_coleta.tipos_residuos.set(tipos_residuos)

        return render(request, 'cadastro_local_coleta.html', {'success_message': 'Local de coleta cadastrado com sucesso!'})


class BuscaLocalColetaView(View):
    def get(self, request):
        return render(request, 'busca_local_coleta.html')

    def post(self, request):
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        locais_coleta = LocalColeta.objects.all()
        # Lógica para buscar os locais de coleta mais próximos com base na latitude e longitude

        return render(request, 'resultado_busca.html', {'locais_coleta': locais_coleta})

class OrientacoesView(View):
    def get(self, request):
        # Lógica para obter as orientações sobre separação e armazenamento de resíduos
        orientacoes = '...'

        return render(request, 'orientacoes.html', {'orientacoes': orientacoes})

def ResultadoBuscaViews(request):
    # Lógica para buscar os locais de coleta com base nos parâmetros da busca
    #locais_coleta = # Obtenha os locais de coleta com base na busca

    context = {
        'locais_coleta':  'todos os locais_coleta',
    }

    return render(request, 'envicollection/resultado_busca.html', context)
