"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
1. Add an import: from my_app import views
2. Add a URL to urlpatterns: path('', views.home, name='home')
Class-based views
1. Add an import: from other_app.views import Home
2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')
Including another URLconf
1. Import the include() function: from django.urls import include, path
2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
path('admin/', admin.site.urls),
path('', TemplateView.as_view(template_name='index.html'), name='index'),
path('pessoa/', PessoasView.as_view(), name='pessoa'),
path('ocupacao/', OcupacaoView.as_view(), name='ocupacao'),
path('instituicao/', InstituicaoView.as_view(), name='instituicao'),
path('areas/', AreasView.as_view(), name='area'),
path('cursos/', CursosView.as_view(), name='curso'),
path('periodos/', PeriodosView.as_view(), name='periodo'),
path('disciplinas/', DisciplinasView.as_view(), name='disciplina'),
path('matriculas/', MatriculasView.as_view(), name='matricula'),
path('avaliacoes/', AvaliacoesView.as_view(), name='avaliacao'),
path('frequencia/', FrequenciaView.as_view(), name='frequencia'),
path('turmas/', TurmasView.as_view(), name='turma'),
path('cidades/', CidadesView.as_view(), name='cidade'),
path('ocorrencias/', OcorrenciasView.as_view(), name='ocorrencia'),
path('manter_disciplinas/', Disciplina_cursoView.as_view(), name='manter_disciplina'),
path('manter_avaliacoes/', TipoAvaliacaoView.as_view(), name='manter_avaliacao'),
]