#  Разворачивание окружения

```
1. Docker-compose build
2. Docker-compose run billing_back_1 python manage.py migrate
3. Docker-compose run -d
```

# Основные методы:

1. Создание продавца:
```
POST /customer

Content-Type: application/x-www-form-urlencoded

name:<Название продавца>
company:<Название компании>
secret:<Ключ для обращении к сущности созданного продавца>
```

2. Просмотр продавца:
```
GET /customer?customer_id=<id продавца>&secret=<ключ продавца>
```
3. Создание продукта:
```
POST /customer

Content-Type: application/x-www-form-urlencoded

name:<Название продукта>
customer_id:<id продавца>
secret:<Ключ продавца>
currency:<Валюта(RUB, USD)>
value:<Стоимость продукта>
```
4. Инициация платежа:
```
POST /payment

Content-Type: application/x-www-form-urlencoded

customer_id:<id продавца>
secret:<Ключ продавца>
currency:<Валюта(RUB, USD)>
order:<Номер заказа>
product_id:<id продукта по которой производится оплата>
amount:<Сумма платежа>
```
5. Просмотр транзакции:
```
GET /transaction?order=<Номер заказа>&secret=<Ключ продавца>&customer_id=<id продавца> 
```
