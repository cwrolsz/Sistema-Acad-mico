from django.db import models

class Usuario(models.Model):
    nome_do_pai = models.CharField(max_length=100, verbose_name="Nome do Pai")
    nome_da_mae = models.CharField(max_length=100, verbose_name="Nome da Mãe")
    cpf = models.CharField(max_length=100, verbose_name="CPF do usuário")
    dat_nasc = models.CharField(max_length=100, verbose_name="Data de Nascimento")
    email = models.CharField(max_length=100, verbose_name="Email do Usuário")
    nome = models.CharField(max_length=100, verbose_name="Nome do Usuário")
    cidade = models.ForeignKey('Cidade', on_delete=models.CASCADE, verbose_name="Cidade do Usuário")
    ocupacao = models.ForeignKey('Ocupacao', on_delete=models.CASCADE, verbose_name="Ocupação do Usuário")

    def __str__(self):
        return f"{self.nome}, {self.email}, {self.cidade}, {self.ocupacao}"

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Ocupação da Pessoa")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"

class Instituicao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Instituição")
    site = models.CharField(max_length=100, verbose_name="Site da Instituição")
    telefone = models.CharField(max_length=100, verbose_name="Telefone")
    cidade = models.ForeignKey('Cidade', on_delete=models.CASCADE, verbose_name="Cidade do Usuário")

    def __str__(self):
        return f"{self.nome}, {self.site}, {self.telefone}, {self.cidade}"

    class Meta:
        verbose_name = "Instituição"

class Areas(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Área do Saber")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Áreas do Saber"

class Cursos(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Curso")
    carga_hor_total = models.CharField(max_length=100, verbose_name="Carga Horária Total do Curso")
    duracao_meses = models.CharField(max_length=100, verbose_name="Duração em Meses do Curso")
    area_saber = models.ForeignKey('Areas', on_delete=models.CASCADE, verbose_name="Área do Saber")
    instituicao = models.ForeignKey('Instituicao', on_delete=models.CASCADE, verbose_name="Instituição")

    def __str__(self):
        return f"{self.nome}, {self.carga_hor_total}, {self.duracao_meses}, {self.area_saber}, {self.instituicao}"

    class Meta:
        verbose_name_plural = "Cursos"

class Periodos(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Período do Curso")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Períodos de Cursos"

class Disciplinas(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Disciplina")
    area_saber = models.ForeignKey('Areas', on_delete=models.CASCADE, verbose_name="Área do Saber")

    def __str__(self):
        return f"{self.nome}, {self.area_saber}"

    class Meta:
        verbose_name_plural = "Disciplinas"

class Matriculas(models.Model):
    instituicao = models.ForeignKey('Instituicao', on_delete=models.CASCADE, verbose_name="Instituição do Usuário")
    cursos = models.ForeignKey('Cursos', on_delete=models.CASCADE, verbose_name="Cursos da Instituição")
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, verbose_name="Nome do Usuário")
    data_inicio = models.CharField(max_length=100, verbose_name="Data de Início do Curso")
    data_prev_termino = models.CharField(max_length=100, verbose_name="Data de Término do Curso")

    def __str__(self):
        return f"{self.instituicao}, {self.cursos}, {self.usuario}, {self.data_inicio}, {self.data_prev_termino}"

    class Meta:
        verbose_name_plural = "Matrículas"

class Avaliacoes(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    cursos = models.ForeignKey('Cursos', on_delete=models.CASCADE, verbose_name="Cursos")
    disciplinas = models.ForeignKey('Disciplinas', on_delete=models.CASCADE, verbose_name="Disciplina")

    def __str__(self):
        return f"{self.descricao}, {self.cursos}, {self.disciplinas}"

    class Meta:
        verbose_name_plural = "Avaliações"

class Frequencia(models.Model):
    cursos = models.ForeignKey('Cursos', on_delete=models.CASCADE, verbose_name="Cursos")
    disciplinas = models.ForeignKey('Disciplinas', on_delete=models.CASCADE, verbose_name="Disciplina")
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, verbose_name="Nome do Usuário")
    num_faltas = models.CharField(max_length=100, verbose_name="Número de Faltas")

    def __str__(self):
        return f"{self.cursos}, {self.disciplinas}, {self.usuario}, {self.num_faltas}"

    class Meta:
        verbose_name = "Frequência"

class Turmas(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    turno = models.CharField(max_length=100, verbose_name="Turno")

    def __str__(self):
        return f"{self.nome}, {self.turno}"

    class Meta:
        verbose_name_plural = "Turmas"

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name_plural = "Cidades"

class Ocorrencias(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição da Ocorrência")
    data = models.CharField(max_length=100, verbose_name="Data da Ocorrência")
    cursos = models.ForeignKey('Cursos', on_delete=models.CASCADE, verbose_name="Cursos")
    disciplinas = models.ForeignKey('Disciplinas', on_delete=models.CASCADE, verbose_name="Disciplina")
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, verbose_name="Nome do Usuário")

    def __str__(self):
        return f"{self.descricao}, {self.data}, {self.cursos}, {self.disciplinas}, {self.usuario}"

    class Meta:
        verbose_name_plural = "Ocorrências"

class Disciplina_Curso(models.Model):
    disciplinas = models.ForeignKey('Disciplinas', on_delete=models.CASCADE, verbose_name="Disciplina")
    carga_horaria = models.CharField(max_length=100, verbose_name="Carga Horária do Curso")
    cursos = models.ForeignKey('Cursos', on_delete=models.CASCADE, verbose_name="Cursos")
    periodos = models.ForeignKey('Periodos', on_delete=models.CASCADE, verbose_name="Período do Curso")

    def __str__(self):
        return f"{self.disciplinas}, {self.carga_horaria}, {self.cursos}, {self.periodos}"

    class Meta:
        verbose_name_plural = "Disciplinas por Curso"

class TipoAvaliacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")

    def __str__(self):
        return self.nome
