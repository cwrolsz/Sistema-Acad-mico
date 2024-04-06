# Create your models here.
from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    def __str__(self):
        return f"{self.nome}, {self.uf}"
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Ocupação")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Pessoa")
    nome_do_pai = models.CharField(max_length=100, verbose_name="Nome do Pai")
    nome_da_mae = models.CharField(max_length=100, verbose_name="Nome da Mãe")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF da Pessoa")
    data_nasc = models.DateField(verbose_name="Data de Nascimento")
    email = models.CharField(max_length=100, verbose_name="Email da Pessoa")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da Pessoa")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupação da Pessoa")
    def __str__(self):
        return f"{self.nome}, {self.nome_do_pai}, {self.nome_da_mae}, {self.cpf}, {self.data_nasc}, {self.email}, {self.cidade}, {self.ocupacao}"
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Instituição")
    site = models.CharField(max_length=100, verbose_name="Site da Instituição")
    telefone = models.CharField(max_length=11, verbose_name="Telefone da Instituição")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da Instituição")
    def __str__(self):
            return f"{self.nome}, {self.site}, {self.telefone}, {self.cidade}"
    class Meta:
        verbose_name = "Instituição de Ensino"
        verbose_name_plural = "Instituições de Ensino"


class Area(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Áreas do Saber")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Área"
    verbose_name_plural = "Áreas"


class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Curso")
    carga_horaria_total = models.CharField(max_length=100, verbose_name="Carga Horária")
    duracao_meses = models.CharField(max_length=2, verbose_name="Duração de Meses")
    area_saber = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Área do Saber")
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Nome da Instituição de Ensino")
    def __str__(self):
        return f"{self.nome}, {self.carga_horaria_total}, {self.duracao_meses}, {self.area_saber}, {self.instituicao}"
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"


class Periodo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Período")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Período"
    verbose_name_plural = "Períodos"


class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Disciplina")
    area_saber = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Área do Saber")
    def __str__(self):
        return f"{self.nome}, {self.area_saber}"
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"


class Matricula(models.Model):
    instituicao =  models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição de Ensino")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Nome da Pessoa")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_previsao_termino = models.DateField(verbose_name="Data de Término")
    def __str__(self):
        return f"{self.instituicao}, {self.curso}, {self.pessoa}, {self.data_inicio}, {self.data_previsao_termino}"
    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"


class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    def __str__(self):
            return f"{self.descricao}, {self.curso}, {self.disciplina}"
    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"


class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Nome da Pessoa")
    numero_faltas = models.CharField(max_length=100, verbose_name="Número de Faltas")
    def __str__(self):
            return f"{self.curso}, {self.disciplina}, {self.pessoa}, {self.numero_faltas}"
    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"


class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Turma")
    turno = models.CharField(max_length=100, verbose_name="Turno")
    def __str__(self):
        return f"{self.nome}, {self.turno}"
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"


class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    data = models.DateField(verbose_name="Data da Ocorrência")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Nome da Pessoa")
    def __str__(self):
            return f"{self.descricao}, {self.data}, {self.curso}, {self.disciplina}, {self.pessoa}"
    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"


class DisciplinaporCurso(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    carga_horaria = models.CharField(max_length=100, verbose_name="Carga Horária")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, verbose_name="Período")
    def __str__(self):
            return f"{self.disciplina}, {self.carga_horaria}, {self.curso}, {self.periodo}"
    class Meta:
        verbose_name = "Disciplina por Curso"
        verbose_name_plural = "Disciplinas por Curso"


class TipoAvaliacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Avaliação")
    def __str__(self):
            return self.nome
    class Meta:
        verbose_name = "Tipo de Avaliação"
        verbose_name_plural = "Tipos de Avaliação"

