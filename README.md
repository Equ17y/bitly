# Обрезка ссылок с помощью VK

Программа работы с API VK сервиса сжатия (укорачивания) ссылок


## Окружение и установка

Python должен быть установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2)  для установки зависимостей:

### Инструкция по созданию токена API VK: 

[Сервисный токен приложения](https://id.vk.ru/about/business/go/docs/ru/vkid/latest/vk-id/connection/tokens/service-token)

### Создание виртуальной среды
```bash
  python3 -m venv env
  source env/bin/activate
```

### Требования к установке
```bash
  pip install -r requirements.txt
```

### Создайте файл .env и укажите в нём свой токен API VK
```python
VK_API_TOKEN=вставьте_свой_токен_сюда
```

## Обрезка ссылок с помощью Битли

Допустим, вы хотите сократить эту ссылку: [https://dvmn.org/](ttps://dvmn.org/)
Таким образом, вам нужно запустить main.py, указав этот URL в качестве аргумента.
```bash
  python main.py https://dvmn.org/
```

Теперь у вас есть ссылка `Bitly`.
```bash
  https://vk.cc/cx0cHv
```

Для статистки переходов по вашей ссылке. Просто запустите main.py, указав в качестве аргумента свою `Bitly`.
```bash
  python main.py https://vk.cc/cx0cHv
```

И ответ таков:

Количество кликов по ссылке: 2



