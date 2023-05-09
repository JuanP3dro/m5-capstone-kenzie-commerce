# m5-capstone-kenzie-commerce - Grupo 23

Repositorio do nosso projeto de final de modulo utilizando o rest-framework do django para desenvolver as funcionalidades.

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

POST /users/login/

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
