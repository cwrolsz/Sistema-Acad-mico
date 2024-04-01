from django.db import models
# Create your models here.
class Usuario(models.Model):
    nome_do_pai = models.CharField(max_length=100, verbose_name="Nome do Pai")
    nome_da_mae = models.CharField(max_length=100, verbose_name="Nome da Mãe")
    cpf = models.CharField(max_length=100, verbose_name="CPF do usuário")
    dat_nasc = models.CharField(max_length=100, verbose_name="Data de Nascimento")
    email = models.CharField(max_length=100, verbose_name="Email do Usuário")
    nome = models.CharField(max_length=100, verbose_name="Nome do Usuário")
    Cidade = models.ForeignKey( Cidade, on_delete=models.CASCADE, verbose_name="Cidade do Usuário")
    Ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupação do Usuário")

    def __str__(self):
        return f"{self.nome}, {self.email}, {self.cidade}, {self.Ocupacao}"
    
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class Ocupacao(models.Model):
        nome = models.CharField(max_length=100, verbose_name="Ocupação da Pessoa")
        def __str__(self):
                return self.nome
        class meta:
                verbose_name = "Ocupação"

class Instituicao(models.Model):
        nome = models.CharField(max_length=100, verbose_name="Nome da Instituição")
        site = models.CharField(max_length=100, verbose_name="site da Instituição")
        telefone = models.CharField(max_length=100, verbose_name="Telefone")
        Cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade do Usuário")
        def __str__(self):
                return f"{self.nome}, {self.site}, {self.telefone}, {self.cidade}"
        class meta:
                verbose_name = "instituição"

class Areas(models.Model):
        nome = models.CharField(max_length=100, verbose_name="Nome da Área do saber")
        def __str__(self):
                return {self.nome}
        class meta:
                verbose_name_plural = "Areas do saber"

class Cursos(models.Model):
        nome = models.CharField(max_length=100, verbose_name="Nome do Curso")
        carga_hor_total = models.CharField(max_length=100, verbose_name="Carga Horaria total do Curso")
        duracao_meses = models.CharField(max_length=100, verbose_name="Duração em meses do curso")
        Areas = models.ForeignKey(Areas, on_delete=models.CASCADE, verbose_name="Area do saber")
        Instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Cidade do Usuário")

        def __str__(self):
                return f"{self.nome}, {self.carga_hor_total}, {self.duracao_meses}, {self.Areas}, {self.Instituicao}"
        class meta:
                verbose_name_plural = "Cursos"

class Periodos(models.Model):
        nome = models.CharField(max_length=100, verbose_name="Nome do Curso")
        def __str__(self):
                return {self.nome}
        class meta:
                verbose_name_plural = "Períodos de Cursos"

class Diciplinas(models.Model):
        nome = models.CharField(max_length=100, verbose_name="Nome do Curso")
        Areas = models.ForeignKey(Areas, on_delete=models.CASCADE, verbose_name="Area do saber")
        def __str__(self):
                return f"{self.nome}, {self.Areas}"
        class meta:
                verbose_name_plural = "Diciplinas"

class Matriculas(models.Model):
        Instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="instituição do Usuário")
        Cursos = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="cursos da instituição")
        Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Nome do Usuário")
        data_inicio = models.CharField(max_length=100, verbose_name="Data inicio do curso")
        data_prev_termino = models.CharField(max_length=100, verbose_name="Data término do Curso")

        def __str__(self):
                return f"{self.Instituicao}, {self.Cursos}, {self.Usuario}, {self.data_inicio}, {self.data_prev_termino}"
        class meta:
                verbose_name_plural = "Matrículas"

class Avaliacoes(models.Model):
        descricao = models.CharField(max_length=100, verbose_name="descrição")
        Cursos = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="cursos")
        Diciplinas = models.ForeignKey(Diciplinas, on_delete=models.CASCADE, verbose_name="diciplina")

        def __str__(self):
                return f"{self.descricao}, {self.Cursos}, {self.Diciplinas}"
        class meta:
                verbose_name_plural = "Avaliações"

class Frequencia(models.Model):
        Cursos = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="cursos")
        Diciplinas = models.ForeignKey(Diciplinas, on_delete=models.CASCADE, verbose_name="diciplina")
        Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="nome do usuário")
        num_faltas = models.CharField(max_length=100, verbose_name="Numero de faltas")
        
        def __str__(self):
                return f"{self.Cursos}, {self.Diciplinas}, {self.Usuario}, {self.num_faltas}"
        class meta:
                verbose_name= "Frequência"

class Turmas(models.Model):
        nome = models.CharField(max_length=100, verbose_name="Nome")
        turno = models.CharField(max_length=100, verbose_name="Turno")

        def __str__(self):
                return f"{self.nome}, {self.turno}"
        class meta:
                verbose_name_plural= "Turmas"

class Cidade(models.Model):
        nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
        uf = models.CharField(max_length=2, verbose_name="UF")

        def __str__(self):
                return f"{self.nome}, {self.uf}"
        class meta:
                verbose_name_plurar = "Cidades"

class Ocorrencias(models.Model):
        descricao = models.CharField(max_length=2, verbose_name="descrição da ocorrência")
        data = models.CharField(max_length=2, verbose_name="data da ocorrência")
        Cursos = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="cursos")
        Diciplinas = models.ForeignKey(Diciplinas, on_delete=models.CASCADE, verbose_name="diciplina")
        Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="nome do usuário")

        def __str__(self):
                return f"{self.descricao}, {self.data}, {self.Cursos}, {self.Diciplinas}, {self.Usuario}"
        class meta:
                verbose_name_plurar = "Ocorrências" 

class diciplina_curso(models.Model):
        Diciplinas = models.ForeignKey(Diciplinas, on_delete=models.CASCADE, verbose_name="diciplina")
        carga_hor = models.CharField(max_length=2, verbose_name="carga horaria do curso")
        Cursos = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="cursos")
        Periodos = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="Periodo do curso")

        def __str__(self):
                return f"{self.Diciplinas}, {self.carga_hor}, {self.Cursos}, {self.Periodos}"
        class meta:
                verbose_name_plurar = "Diciplinas por curso" 

class tipo_avaliacao(models.Model):
        nome = models.CharField(max_length=2, verbose_name="Nome")
        
        
