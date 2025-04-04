from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=64, null=False, blank=True)
    additional = models.TextField(null=True, blank=True)


class Suppliers(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    cnpj = models.CharField(max_length=14, null=False, blank=False)
    phone = models.CharField(max_length=32, null=True, blank=True)
    email = models.CharField(max_length=64, null=True, blank=True)
    additional = models.TextField(null=True, blank=True)


class Manufactorers(models.Model):
    name = models.CharField(max_length=64, null=False, blank=True)    
    cnpj = models.CharField(max_length=14, null=False, blank=False)
    phone = models.CharField(max_length=32, null=True, blank=True)
    email = models.CharField(max_length=64, null=True, blank=True)
    additional = models.TextField(null=True, blank=True)


class Brands(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    additional = models.TextField(null=True, blank=True)


class UnityMeasures(models.Model):
    name = models.CharField(max_length=16, null=False, blank=False)
    abbreviation = models.CharField(max_length=3, null=False, blank=False)
    additional = models.TextField(null=True, blank=True)


class Products(models.Model):
    barcode = models.CharField(max_length=64, null=False, blank=False)
    name = models.CharField(max_length=64, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey('Brands', on_delete=models.CASCADE, null=True, blank=True)
    stock_quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    unity_measure = models.ForeignKey('UnityMeasures', on_delete=models.CASCADE) #TODO: A alterar como PK, quando da implementação da app Stock
    cost_price = models.DecimalField(max_digits=8, decimal_places=2)
    sale_price = models.DecimalField(max_digits=8, decimal_places=2)
    expiration_date = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    batch_number = models.CharField(max_length=16, null=True, blank=True)
    supplier = models.ForeignKey('Suppliers', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


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