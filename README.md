# m5-capstone-kenzie-commerce - Grupo 23

## Models

### Model User

| Atributos | Propriedades                            |
| --------- | --------------------------------------- |
| username  | CharField(max_length=127, unique=True)  |
| email     | EmailField(max_length=127, unique=True) |
| password  | CharField(max_length=127)               |
| user_type | ChoiceField(default='client',choices=)  |

### Model Address

| Atributos  | Propriedades                                     |
| ---------- | ------------------------------------------------ |
| cep        | CharField(max_length=127)                        |
| street     | CharField(max_length=127)                        |
| number     | IntegerField(max_length=127)                     |
| complement | CharField()                                      |
| user_id    | OneToOneField('users.user', ON_DELETE = CASCADE) |

### Model Products

| Atributos | Propriedades                                 |
| --------- | -------------------------------------------- |
| name      | CharField(max_length=127, unique=True)       |
| category  | CharField(max_length=100)                    |
| price     | DecimalField(max_digits=5, decimal_places=2) |
| in_stock  | PositiveSmallIntegerField()                  |
| seller_id | FK()                                         |

### Model Cart

| Atributos | Propriedades                                     |
| --------- | ------------------------------------------------ |
| products  | ManyToManyField()                                |
| user_id   | OneToOneField('users.user', ON_DELETE = CASCADE) |

### Model Order

| Atributos | Propriedades  |
| --------- | ------------- |
| status    | ChoiceField() |
| products  | ...           |
| time      | ...           |
