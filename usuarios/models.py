from django.db import models

STATUS_GENERO = [
    ("FEMININO", "Feminino"),
    ("MASCULINO", "Masculino"),
    ("OUTROS", "Outros"),
]

STATUS_ESTADOCIVIL = [
    ("SOLTEIRO", "Solteiro(a)"),
    ("CASADO", "Casado(a)"),
    ("DIVORCIADO", "Divorciada(a)"),
    ("VIUVO", "Viúvo(a)"),
]

STATUS_ESCOLARIDADE = [
    ("EFI", "Ensino Fundamental incompleto"),
    ("EFC", "Ensino Fundamental completo"),
    ("EMI", "Ensino Médio incompleto"),
    ("EMC", "Ensino Médio completo"),
    ("ESI", "Ensino Superior incompleto"),
    ("ESC", "Ensino Superior completo"),
]

class Pessoa(models.Model):

    nome_completo = models.CharField(
        verbose_name = "Nome completo",
        max_length = 194,
    )

    email = models.CharField(
        verbose_name = "E-mail",
        max_length = 194,
    )

    cpf = models.CharField(
        verbose_name = "CPF",
        max_length = 14,
        unique = True
    )

    data_nascimento = models.DateField(
        verbose_name = "Data de nascimento",
        auto_now = False,
        auto_now_add = False,
    )

    status_genero = models.CharField(
        verbose_name = "Sexo",
        max_length = 20,
        choices = STATUS_GENERO,
    )

    naturalidade = models.CharField(
        verbose_name = "Naturalidade",
        max_length = 50,
    )

    status_escolaridade = models.CharField(
        verbose_name = "Escolaridade",
        max_length = 50,
        choices = STATUS_ESCOLARIDADE,
    )

    status_estadocivil = models.CharField(
        verbose_name = "Estado Civil",
        max_length = 50,
        choices = STATUS_ESTADOCIVIL,
    )

    profissao = models.CharField(
        verbose_name = "Profissão",
        max_length = 50,
    )

    pais = models.CharField(
        verbose_name = "País",
        max_length = 50,
    )

    cep = models.CharField(
        verbose_name = "CEP",
        max_length = 14,
    )

    estado = models.CharField(
        verbose_name = "Estado",
        max_length = 50,
    )

    cidade = models.CharField(
        verbose_name = "Cidade",
        max_length = 50,
    )

    endereco = models.CharField(
        verbose_name = "Endereço",
        max_length = 120,
    )

    telefone = models.CharField(
        verbose_name = "Telefone",
        max_length = 50,
    )

    celular = models.CharField(
        verbose_name = "Celular",
        max_length = 50,
    )

    data_cadastro = models.DateField(
        verbose_name = "Data de Cadastro",
        max_length = 50,
        auto_now_add = True,
    )

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        db_table = "pessoa"

    def __str__(self):
        return self.nome_completo


class Gerente(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE, verbose_name="Pessoa")

    class Meta:
        verbose_name = "Gerente"
        verbose_name_plural = "gerentes"
        db_table = "gerente"

    def __str__(self):
        return self.pessoa.nome_completo


class Empresa(models.Model):

    nome_empresa = models.CharField(
        verbose_name = "Nome Empresa",
        max_length = 150,
    )

    telefone = models.CharField(
        verbose_name = "Telefone",
        max_length = 20,
    )

    pais = models.CharField(
        verbose_name = "País",
        max_length = 50,
    )

    cep = models.CharField(
        verbose_name = "CEP",
        max_length = 14,
    )

    estado = models.CharField(
        verbose_name = "Estado",
        max_length = 50,
    )

    cidade = models.CharField(
        verbose_name = "Cidade",
        max_length = 50,
    )

    endereco = models.CharField(
        verbose_name = "Endereço",
        max_length = 150,
    )

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "empresas"
        db_table = "empresa"

    def __str__(self):
        return self.nome_empresa



class Vendedor(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE, verbose_name="Pessoa")
    empresa = models.ForeignKey(Empresa, on_delete = models.CASCADE, verbose_name="Empresa")

    class Meta:
        verbose_name = "Vendedor"
        verbose_name_plural = "vendedores"
        db_table = "vendedor"

    def __str__(self):
        return self.pessoa.nome_completo


