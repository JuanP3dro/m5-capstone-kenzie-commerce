# m5-capstone-kenzie-commerce - Grupo 23

## Models

### Model User

| Atributos | Propiedades                             |
| --------- | --------------------------------------- |
| username  | CharField(max_length=127, unique=True)  |
| email     | EmailField(max_length=127, unique=True) |
| password  | CharField(max_length=127)               |
| user_type | BooleanField()                          |

### Adress

| Atributos  | Propiedades                  |
| ---------- | ---------------------------- |
| cep        | CharField(max_length=127)    |
| street     | CharField(max_length=127)    |
| number     | IntegerField(max_length=127) |
| complement | CharField()                  |
| user_id    | OneToOneField('Vem do user') |

### Model Products

| Atributos | Propiedades                                  |
| --------- | -------------------------------------------- |
| name      | CharField(max_length=127, unique=True)       |
| category  | CharField(max_length=100)                    |
| price     | DecimalField(max_digits=5, decimal_places=2) |
| in_stock  | PositiveSmallIntegerField()                  |
