# m5-capstone-kenzie-commerce - Grupo 23

Repositorio do nosso projeto de final de modulo utilizando o rest-framework do django para desenvolver as funcionalidades.

## Instruções:

### Crie o ambiente virtual

```
python -m venv venv
```

### Ative o venv

```bash
# linux:
source venv/bin/activate
# windows:
.\venv\Scripts\activate
```

### Instale as dependências

```
pip install -r requirements.txt
```

### Execute as migrações

```
python manage.py migrate
```

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

### Criação de primiero admin

POST /admin/

Rota cria um administrador automaticamente e a partir dele se consegue criar outros administradores.

username: admin
password: 1234

Não necessita autorização

#### Respostas Da Resquisição: <br/>

Modelo de resposta caso de certo:

```
{
	"username": "admin",
	"email": "admin@admin.com"
}
```

Modelo de resposta caso de errado:

`{"Descrição do erro"}`

<br/>

### Criação de admin

POST /users/admin

Rota para criar outros administradores a partir do criado a cima

Necessita token de admin

Modelo de requisição

{
"username": "AdminCriadoPorAdmin",
"email": "AdminCriadoPorAdmin@mail.com",
"password": "1234"
}

#### Respostas Da Resquisição: <br/>

Modelo de resposta caso de certo:

```
{
	"id": 7,
	"username": "AdminCriadoPorAdmin",
	"email": "AdminCriadoPorAdmin@mail.com",
	"is_seller": false
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

### List Users

GET /users/

Apenas Administradores

Requisição sem corpo

#### Respostas Da Resquisição: <br/>

Modelo de resposta caso de certo:

```
{
	"count": 3,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"username": "verdureiro",
			"email": "verdureiro@hotmail.com",
			"is_seller": true
		},
		{
			"id": 2,
			"username": "user",
			"email": "user@mail.com",
			"is_seller": false
		},
		{
			"id": 3,
			"username": "joao",
			"email": "joao@mail.com",
			"is_seller": true
		}
	]
}
```

Modelo de resposta caso de errado:
`{"Descrição do erro"}`

### Create Address

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

### Create Product

POST /products/

Necessita de autorização de vendedor

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

### Update Product

PATCH /products/

Necessita de autorização de vendedor

Modelo de Requisição:

```
{
   "name": "Maçã updated"
}
```

#### Respostas Da Resquisição: <br/>

Modelo de resposta caso de certo:

```
{
	"id": 17,
	"name": "Maçã updated",
	"category": "fruta",
	"price": "1.00",
	"in_stock": 5,
	"is_available": true,
	"seller": 1
}

```

Modelo de resposta caso de errado:
`{"Descrição do erro"}`

<br/>

### Delete Product

DELETE /products/:id/

Necessita de autorização de vendedor

Requisição sem corpo

#### Respostas Da Resquisição: <br/>

Modelo de resposta caso de certo:

Requisição sem resposta

Modelo de resposta caso de errado:
`{"Descrição do erro"}`

<br/>

### List Products

GET /products/

Não necessita de autorização

Requisição sem corpo

#### Respostas Da Resquisição: <br/>

Modelo de resposta caso de certo:

```
{
"count": 8,
"next": "http://localhost:8000/api/products/?page=2",
"previous": null,
"results": [
{
"id": 31,
"name": "alface",
"category": "vegetal",
"price": "10.00",
"in_stock": 500,
"is_available": true,
"seller": 3
},
{
"id": 32,
"name": "vagem",
"category": "vegetal",
"price": "10.00",
"in_stock": 500,
"is_available": true,
"seller": 8
},
{
"id": 33,
"name": "maçã",
"category": "fruta",
"price": "10.00",
"in_stock": 500,
"is_available": true,
"seller": 3
},
{
"id": 34,
"name": "pera",
"category": "fruta",
"price": "10.00",
"in_stock": 500,
"is_available": true,
"seller": 5
},
{
"id": 35,
"name": "alface americana",
"category": "verdura",
"price": "10.00",
"in_stock": 500,
"is_available": true,
"seller": 5
}
]
}
```

Modelo de resposta caso de errado:
`{"Descrição do erro"}`

<br/>

### Retriver Product

GET /products/:id/

Não necessita de autorização

Requisição sem corpo

#### Respostas Da Resquisição: <br/>

Modelo de resposta caso de certo:

```
{
"id": 31,
"name": "alface",
"category": "verdura",
"price": "10.00",
"in_stock": 500,
"is_available": true,
"seller": 3
}
```

Modelo de resposta caso de errado:
`{"Descrição do erro"}`

<br/>

### Create Cart

POST /cart/

Necessita de autorização

Modelo de Requisição:

```
{
    "name": "pepino",
	"quantity": 5
}
```

#### Respostas Da Resquisição: <br/>

Modelo de resposta caso de certo:

```
{
	"id": 43,
	"products": {
		"id": 36,
		"name": "pepino",
		"category": "verdura",
		"price": "10.00",
		"in_stock": 470,
		"is_available": true,
		"seller": 8
	},
	"cart": {
		"id": 10,
		"user": 3
	},
	"quantity": 5
}
```

Modelo de resposta caso de errado:
`{"Descrição do erro"}`

<br/>

### Update Cart

PATCH /cart/

Necessita de autorização

Descrição: Rota criada para diminuir a quantidade de itens passados na requisição.

Modelo de Requisição:

```
{
    "name": "fruta5",
	"quantity": 4
}
```

#### Respostas Da Resquisição: <br/>

Modelo de resposta caso de certo:

Requisição sem resposta

Modelo de resposta caso de errado:
`{"Descrição do erro"}`

<br/>

### Delete Cart

DELETE /cart/:id/

Necessita de autorização

Requisição sem corpo

#### Respostas Da Resquisição: <br/>

Modelo de resposta caso de certo:

Requisição sem resposta

Modelo de resposta caso de errado:
`{"Descrição do erro"}`

<br/>

### List Cart

GET /cart/

Necessita de autorização

Requisição sem corpo

#### Respostas Da Resquisição: <br/>

Modelo de resposta caso de certo:

```
[
{
"id": 44,
"products": {
"id": 36,
"name": "pepino",
"category": "verdura",
"price": "10.00",
"in_stock": 465,
"is_available": true,
"seller": 8
},
"cart": {
"id": 11,
"user": 5
},
"quantity": 5
},
{
"id": 45,
"products": {
"id": 31,
"name": "alface",
"category": "fruta",
"price": "10.00",
"in_stock": 500,
"is_available": true,
"seller": 3
},
"cart": {
"id": 11,
"user": 5
},
"quantity": 5
}
]

```

Modelo de resposta caso de errado:
`{"Descrição do erro"}`

<br/>

### Create Order

POST /order/

Necessita de autorização

Requisição sem corpo

#### Respostas Da Resquisição: <br/>

Modelo de resposta caso de certo:

```
{
	"orders": [
		{
			"id": 49,
			"status": "Pedido Realizado",
			"created_at": "2023-05-09T18:10:55.932522Z",
			"user": 5,
			"products": [
				{
					"product": {
						"name": "pepino",
						"category": "verdura",
						"price": "10.00"
					},
					"quantity": 5
				}
			]
		},
		{
			"id": 50,
			"status": "Pedido Realizado",
			"created_at": "2023-05-09T18:10:55.951474Z",
			"user": 5,
			"products": [
				{
					"product": {
						"name": "alface",
						"category": "fruta",
						"price": "10.00"
					},
					"quantity": 5
				}
			]
		}
	]
}
```

Modelo de resposta caso de errado:
`{"Descrição do erro"}`

### Patch Order

PATCH /order/:id/

Necessita de autorização

Modelo de requisição:

```
{
	"status": "Pedido em Andamento"
}
```

#### Respostas Da Resquisição: <br/>

Modelo de resposta caso de certo:

```
{
	"id": 28,
	"status": "Pedido em Andamento",
	"created_at": "2023-05-08T17:56:34.178626Z",
	"user": 3,
	"products": [
		29,
		30
	]
}
```

Modelo de resposta caso de errado:
`{"Descrição do erro"}`

<br/>

### List Order

GET /order/

Necessita de autorização

Requisição sem corpo

#### Respostas Da Resquisição: <br/>

Modelo de resposta caso de certo:

```
[
	{
		"id": 49,
		"status": "Pedido Realizado",
		"created_at": "2023-05-09T18:10:55.932522Z",
		"user": 5,
		"products": [
			36
		]
	},
	{
		"id": 50,
		"status": "Pedido Realizado",
		"created_at": "2023-05-09T18:10:55.951474Z",
		"user": 5,
		"products": [
			31
		]
	}
]
```

Modelo de resposta caso de errado:
`{"Descrição do erro"}`

<br/>
