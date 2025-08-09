# user -> /register -> UserLoginAndRegister(email, password) -> create_user -> hash_password -> DB(сохранение пользователя) регистрация
# user -> /auth/token -> UserLoginAndRegister(email, password) -> create_access_token -> JWT токен -> аутентификация -> авторизация

# user_with_token -> /me -> get_current_user(проверка токена) -> UserResponse(id, email, is_superuser) аутентификация
# user_with_token -> /products(POST) -> get_current_user(проверка токена) -> ProductCreate( name, price, description) -> DB(сохранение продукта) создание продукта
