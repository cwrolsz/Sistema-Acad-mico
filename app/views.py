from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Ocupacao, Instituicao, Area, Curso, Periodo, Disciplina, Matricula, Avaliacao, Frequencia, Turma, Cidade, Ocorrencia, DisciplinaporCurso, TipoAvaliacao
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class PessoasView(View):
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        return render(request, 'usuario.html', {'usuarios': usuarios})

class OcupacaoView(View):
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacoes': ocupacoes})

class InstituicaoView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = Instituicao.objects.all()
        return render(request, 'instituicao.html', {'instituicoes': instituicoes})

class AreasView(View):
    def get(self, request, *args, **kwargs):
        areas = Area.objects.all()
        return render(request, 'areas.html', {'areas': areas})

class CursosView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'cursos.html', {'cursos': cursos})

class PeriodosView(View):
    def get(self, request, *args, **kwargs):
        periodos = Periodo.objects.all()
        return render(request, 'periodos.html', {'periodos': periodos})

class DisciplinasView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplinas.html', {'disciplinas': disciplinas})

class MatriculasView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        return render(request, 'matriculas.html', {'matriculas': matriculas})

class AvaliacoesView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes})
    
class FrequenciaView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencia.html', {'frequencias': frequencias})

class TurmasView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'turmas.html', {'turmas': turmas})

class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidades.html', {'cidades': cidades})

class OcorrenciasView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencias.html', {'ocorrencias': ocorrencias})

class DisciplinaCursoView(View):
    def get(self, request, *args, **kwargs):
        disciplinas_curso = DisciplinaporCurso.objects.all()
        return render(request, 'disciplinas_cursos.html', {'disciplinas_cursos': disciplinas_curso})

class TipoAvaliacoesView(View):
    def get(self, request, *args, **kwargs):
        tipo_avaliacoes = TipoAvaliacao.objects.all()
        return render(request, 'tipo_avaliacoes.html', {'tipo_avaliacoes': tipo_avaliacoes})
