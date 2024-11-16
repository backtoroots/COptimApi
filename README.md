Тестовое приложение для тестовой Api:

<h4>Endpoints:</h4>
1. Выполнение get запроса

    Endpoint: /get
    Method: GET

Request Body

```json
  {
    "id": "UUID"
  }
```

Response

    Status Code: 200 OK
    Response Body:

```json
{
  "result": "str",
}
```

2. Выполнение post запроса

  Endpoint: /post
  Method: POST
    Endpoint: /post
    Method: POST

Request Body

```json
  {
    "palindrome": "bool"
  }
```

Response

    Status Code: 200 OK
    Response Body:

```json
{
  "id": "UUID",
  "result": "str",
}
```

Отображение результатов выполнения тестов выполнялось с помощью allure выполнением команды allure serve <Директория allure логов>.
