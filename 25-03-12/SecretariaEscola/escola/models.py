from django.db import models

# TODO: add CEP, cpf validator


class Guardian(models.Model):
    TURMA_CHOICES = (
        ("1A", "1° Ano A"),
        ("1B", "1° Ano B"),
        ("1C", "1° Ano C"),
        ("2A", "2° Ano A"),
        ("2B", "2° Ano B"),
        ("2C", "2° Ano C"),
        ("3A", "3° Ano A"),
        ("3B", "3° Ano B"),
        ("3C", "3° Ano C"),
    )

    first_name = models.CharField(
        max_length=50, verbose_name="Primeiro nome do responsável"
    )
    last_name = models.CharField(
        max_length=50, verbose_name="Último nome do responsável"
    )
    phone_number = models.CharField(
        max_length=15, verbose_name="N° do celular do responsável (xx) xxxxx-xxxx"
    )
    email = models.EmailField(max_length=100, verbose_name="Email do responsável")
    adress = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    birthday = models.DateField()
    class_choices = models.CharField(
        max_length=2, choices=TURMA_CHOICES, blank=True, null=False
    )

    def __str__(self):
        return self.first_name


class Student(models.Model):
    TURMA_CHOICES = (
        ("1A", "1° Ano A"),
        ("1B", "1° Ano B"),
        ("1C", "1° Ano C"),
        ("2A", "2° Ano A"),
        ("2B", "2° Ano B"),
        ("2C", "2° Ano C"),
        ("3A", "3° Ano A"),
        ("3B", "3° Ano B"),
        ("3C", "3° Ano C"),
    )

    first_name = models.CharField(max_length=50, verbose_name="Primeiro nome do aluno")
    last_name = models.CharField(max_length=50, verbose_name="Último nome do aluno")
    phone_number = models.CharField(
        max_length=15, verbose_name="N° do celular do aluno (xx) xxxxx-xxxx"
    )
    email = models.EmailField(max_length=100, verbose_name="Email do aluno")
    adress = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    birthday = models.DateField()
    class_choices = models.CharField(
        max_length=2, choices=TURMA_CHOICES, blank=True, null=False
    )

    def __str__(self):
        return self.first_name


class Professor(models.Model):
    TURMA_CHOICES = (
        ("1A", "1° Ano A"),
        ("1B", "1° Ano B"),
        ("1C", "1° Ano C"),
        ("2A", "2° Ano A"),
        ("2B", "2° Ano B"),
        ("2C", "2° Ano C"),
        ("3A", "3° Ano A"),
        ("3B", "3° Ano B"),
        ("3C", "3° Ano C"),
    )

    first_name = models.CharField(
        max_length=50, verbose_name="Primeiro nome do Professor"
    )
    last_name = models.CharField(max_length=50, verbose_name="Último nome do Professor")
    phone_number = models.CharField(
        max_length=15, verbose_name="N° do celular do Professor (xx) xxxxx-xxxx"
    )
    email = models.EmailField(max_length=100, verbose_name="Email do Professor")
    adress = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    birthday = models.DateField()
    class_choices = models.CharField(
        max_length=2, choices=TURMA_CHOICES, blank=True, null=False
    )

    def __str__(self):
        return self.first_name
