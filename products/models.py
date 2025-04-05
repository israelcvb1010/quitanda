from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=64, null=False, blank=True, unique=True)
    additional = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Categoria"

    def __str__(self):
        return self.name


class Suppliers(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    cnpj = models.CharField(max_length=14, null=False, blank=False, unique=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    email = models.CharField(max_length=64, null=True, blank=True)
    additional = models.TextField(null=True, blank=True)


class Manufactorers(models.Model):
    name = models.CharField(max_length=64, null=False, blank=True, unique=True)
    cnpj = models.CharField(max_length=14, null=False, blank=False, unique=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    email = models.CharField(max_length=64, null=True, blank=True)
    additional = models.TextField(null=True, blank=True)


class Brands(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    additional = models.TextField(null=True, blank=True)


class UnityMeasures(models.Model):
    name = models.CharField(max_length=16, null=False, blank=False, unique=True)
    abbreviation = models.CharField(max_length=3, null=False, blank=False, unique=True)
    additional = models.TextField(null=True, blank=True)


class Products(models.Model):
    barcode = models.CharField("Código de barras", max_length=64, null=False, blank=False, unique=True)
    name = models.CharField("Nome do produto", max_length=64, null=False, blank=False, unique=True)
    description = models.TextField("Descrição", null=True, blank=True)
    category = models.ForeignKey('Categories', verbose_name="Categoria", on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey('Brands', verbose_name="Marca", on_delete=models.CASCADE, null=True, blank=True)
    stock_quantity = models.PositiveIntegerField("Quantidade no estoque", default=0, null=True, blank=True)
    unity_measure = models.ForeignKey('UnityMeasures', verbose_name="Unidade", on_delete=models.CASCADE) #TODO: A alterar como PK, quando da implementação da app Stock
    cost_price = models.DecimalField("Preço de custo", max_digits=8, decimal_places=2)
    sale_price = models.DecimalField("Preço de venda", max_digits=8, decimal_places=2)
    expiration_date = models.DateField("Data de validade", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    batch_number = models.CharField("Número do lote", max_length=16, null=True, blank=True)
    supplier = models.ForeignKey('Suppliers', verbose_name="Fornecedor", on_delete=models.CASCADE)
    is_active = models.BooleanField("Ativo", default=True)

    class Meta:
        verbose_name = "Produto"


# Diagram
"""
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│  categorias │       │   marcas    │       │ fornecedores│
├─────────────┤       ├─────────────┤       ├─────────────┤
│ id (PK)     │       │ id (PK)     │       │ id (PK)     │
│ nome        │       │ nome        │       │ nome        │
│ descricao   │       └─────────────┘       │ cnpj        │
└─────────────┘              │              │ telefone    │
       │                     │              └─────────────┘
       │                     │                     │
       ▼                     ▼                     ▼
┌───────────────────────────────────────────────────────┐
│                      produtos                         │
├───────────────────────────────────────────────────────┤
│ id (PK)                                              │
│ nome                                                 │
│ codigo_barras                                        │
│ descricao                                            │
│ categoria_id (FK) ───────────────────────┐           │
│ marca_id (FK) ───────────────────┐       │           │
│ quantidade_estoque               │       │           │
│ unidade_medida                   │       │           │
│ preco_custo                      │       │           │
│ preco_venda                      │       │           │
│ data_validade                    │       │           │
│ lote                             │       │           │
│ fornecedor_id (FK) ──────────────┘       │           │
│ ativo                                   │           │
└─────────────────────────────────────────┘           │
"""