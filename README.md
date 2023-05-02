# m5-capstone-kenzie-commerce - Grupo 23

## Models

<br/>

### Model User

| Atributos | Propiedades                             |
| --------- | --------------------------------------- |
| username  | CharField(max_length=127, unique=True)  |
| email     | EmailField(max_length=127, unique=True) |
| password  | CharField(max_length=127)               |
| user_type | BooleanField()                          |
