Создание ssh ключа:
	>> ssh-keygen -t ed25519 -C "your_email@example.com"
Добавление ключа в аккаунт на GitHub:
	1. Откройте настройки пользователя (Settings) и выберите раздел SSH and GPG keys, или перейдите по ссылке https://github.com/settings/keys. 
	2. Кликните на New SSH key или Add SSH key
	3. В поле «Title» добавьте описание нового ключа. Например, если вы используете Малинку под номером 5, вы можете написать «RaspberryPi #5».
	4. Вставьте ключ из буфера обмена в поле Key 
	5. Нажмите "Add SSH key". Если будет предложено, введите пароль для подтверждения
Клонирование репозитория:
	>> git clone git@github.com:username/repository.git