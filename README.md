в файле task1.py выполненное задание 1

### Описание

API проекта магазина продуктов с использованием Django Rest Framework

- Python 3.12
- Django 6.0.2
- Django REST framework 3.16.1

### Функционал

- Авторизация по токенам:
    - `/api/auth/register/` - регистрация нового пользователя
    - `/api/auth/login/` - авторизация существующего пользователя
    - `/api/auth/logout/` - выход пользователя 

- Просмотр категорий с подкатегориями, продуктов :
    - `/api/catalog/categories/` - все категории с вложенными подкатегориями, поддерживается пагинация
    - `/api/catalog/products/` - продукты с полями наименование, slug, категория, подкатегория, цена, список изображений
- Управление корзиной (только для авторизованных пользователей):
    - `/api/cart/` - GET-запрос для просмотра содержимого корзины с подсчётом количества товаров и общей суммы
    - `/api/cart/` - POST-запрос добавление продукта в корзину или изменение его количества
    - `/api/cart/{id}/` - PUT/PATCH – обновление количества конкретного продукта
    - `/api/cart/{id}/` - DELETE – удаление конкретного продукта из корзины
    - `/api/cart/clear/` – DELETE – полная очистка корзины
    - `/api/cart/summary/` – вывод количества товаров и общей суммы корзины
- Документация Swagger:
    - `/api/schema/` - OpenAPI схема
    - `/api/docs/` - документация Swagger UI
    - 
### Установка

Далее все команды приведины для Windows.

Клонируйте репозиторий с GitHub
```bash
git clone https://github.com/belokopytova/test-shop.git

```

Перейдите в директорию **shop**:
```bash
cd shop/
```
Создайте и активируйте виртуальное окружение.

```bash
python -m venv venv

```

Установите зависимости:
```bash
pip install -r requirements.txt
```


Выполните миграции:
```bash
python manage.py migrate
```

Наполните БД данными из фикстур:

Расположение фикстур `catalog/fixtures/products.json`
```bash
python manage.py loaddata
```

Запустите проект:
```bash
python manage.py runserver
```

Для использования панели администратора следует создать суперпользователя:
```bash
python manage.py createsuperuser
```

### Тестирование

Для выполнения автотестирования, находясь в папке `shop/`, выполните команду:
```bash
pytest
```

### Настройка токенов JWT

Можно настроить срок действия токенов в settings.py:

```bash
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),   
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),  
}
```

`ACCESS_TOKEN_LIFETIME` – короткоживущий JWT-токен 

`REFRESH_TOKEN_LIFETIME` – токен, с помощью которого можно получить новый access-токен.

_______________

Документация по API доступна онлайн на GitHub Pages:  

[Просмотреть Swagger UI](https://belokopytova.github.io/) 
