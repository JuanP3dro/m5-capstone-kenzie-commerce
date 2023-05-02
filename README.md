# m5-capstone-kenzie-commerce - Grupo 23

## Requisições

### Cadastro

POST /users/

Não necessita autorização

Modelo de Requisição:

```
{
    "username": "João Borchoski"
    "email": "joao@joao.com",
    "password": "1212",
    "user_type": "ademiro"
}
```

#### Respostas Da Resquisição: <br/>

Modelo de resposta caso de certo:

```
{
    "id": 1
    "username": "João Borchoski"
    "email": "joao@joao.com",
    "user_type": "ademiro"
}
```

Modelo de resposta caso de errado:

`{"Descrição do erro"}`

<br/>

### Login

POST /login/

Não necessita de autorização

Modelo de Requisição:

```
{
    "username": "joao@joao.com",
    "password": "121212"
}
```

#### Respostas Da Resquisição: <br/>

Modelo de resposta caso de certo:

```
{
    "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvYW9Aam9hby5jb20iLCJpYXQiOjE2NzI3NjYwMTcsImV4cCI6MTY3Mjc2OTYxNywic3ViIjoiMSJ9",
    "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvYW9Aam9hby5jb20iLCJpYXQiOjE2NzI3NjYwMTcsImV4cCI6MTY3Mjc2OTYxNywic3ViIjoiMSJ9"
}
```

Modelo de resposta caso de errado:
`{"Descrição do erro"}`

<br/>

### Address

POST /address/

Necessita de autorização

Modelo de Requisição:

```
{
    "cep": "12345-678",
    "street": "ruazinha",
    "number": "1",
    "complement": "casa",
}
```

#### Respostas Da Resquisição: <br/>

Modelo de resposta caso de certo:

```
{
    "id": 1
    "cep": "12345-678",
    "street": "ruazinha",
    "number": "1",
    "complement": "casa",
    "user_id": 1
}
```

Modelo de resposta caso de errado:
`{"Descrição do erro"}`

<br/>

### Products

POST /products/

Necessita de autorização

Modelo de Requisição:

```
{
    "name": "manga",
    "category": "fruta",
    "price": "1",
    "in_stock": "10",
}
```

#### Respostas Da Resquisição: <br/>

Modelo de resposta caso de certo:

```
{
    "id": 1
    "name": "manga",
    "category": "fruta",
    "price": "1",
    "in_stock": "10",
    "seller_id": 1
}
```

Modelo de resposta caso de errado:
`{"Descrição do erro"}`

<br/>

### Order

POST /order/

Necessita de autorização

Requisição sem corpo

#### Respostas Da Resquisição: <br/>

Modelo de resposta caso de certo:

```
{
    "id": 1
    "status": "Pedido realizado",
    "created_at": "agora",
    "products": [
        {
            "id": 1
            "name": "manga",
            "category": "fruta",
            "price": "1",
            "seller_id": 1
        }
    ]
}
```

Modelo de resposta caso de errado:
`{"Descrição do erro"}`

<br/>

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

| Atributos  | Propriedades                     |
| ---------- | -------------------------------- |
| status     | ChoiceField()                    |
| created_at | DateTimeField(auto_now_add=True) |
