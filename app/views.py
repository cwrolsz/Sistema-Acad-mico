from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    
class PessoasView(View):
  def get(self, request, *args, **kwargs):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoa.html', {'pessoa': pessoas})

class OcupacaoView(View):
  def get(self, request, *args, **kwargs):
    ocupacao = Ocupacao.objects.all()
    return render(request, 'ocupacao.html',{'ocupacao': ocupacao})
  
class InstituicaoView(View):
  def get(self, request, *args, **kwargs):
    instituicoes = InstituicaoEnsino.objects.all()
    return render(request, 'instituicao.html', {'instituicao': instituicoes})
  
class AreasView(View):
  def get(self, request, *args, **kwargs):
    areas = Area.objects.all()
    return render(request, 'areas.html', {'area': areas})
  
class CursosView(View):
  def get(self, request, *args, **kwargs):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html',{'curso': cursos})
  
class PeriodosView(View):
  def get(self, request, *args, **kwargs):
    periodos = Periodo.objects.all()
    return render(request, 'periodos.html',{'periodo': periodos})

class DisciplinasView(View):
  def get(self, request, *args, **kwargs):
    disciplinas = Disciplina.objects.all()
    return render(request, 'disciplinas.html', {'disciplina': disciplinas})
  
class MatriculasView(View):
  def get(self, request, *args, **kwargs):
    matriculas = Matricula.objects.all()
    return render(request, 'matriculas.html', {'matricula': matriculas})
  
class AvaliacoesView(View):
  def get(self, request, *args, **kwargs):
    avaliacoes = Avaliacao.objects.all()
    return render(request, 'avaliacoes.html', {'avaliacao': avaliacoes})
  
class FrequenciaView(View):
  def get(self, request, *args, **kwargs):
    frequencia = Frequencia.objects.all()
    return render(request, 'frequencia.html', {'frequencia': frequencia})
  
class TurmasView(View):
  def get(self, request, *args, **kwargs):
    turmas = Turma.objects.all()
    return render(request, 'turmas.html', {'turma': turmas})
  
class CidadesView(View):
  def get(self, request, *args, **kwargs):
    cidades = Cidade.objects.all()
    return render(request, 'cidades.html', {'cidade': cidades})
  
class OcorrenciasView(View):
  def get(self, request, *args, **kwargs):
    ocorrencias = Ocorrencia.objects.all()
    return render(request, 'ocorrencias.html', {'ocorrencia': ocorrencias})
  
class ManterDisciplinasView(View):
  def get(self, request, *args, **kwargs):
    manter_disciplinas = DisciplinaporCurso.objects.all()
    return render(request, 'manter_disciplinas.html', {'manter_disciplina': manter_disciplinas})
  
class ManterAvaliacoesView(View):
  def get(self, request, *args, **kwargs):
    manter_avaliacoes = TipoAvaliacao.objects.all()
    return render(request, 'manter_avaliacoes.html', {'manter_avaliacao': manter_avaliacoes})
