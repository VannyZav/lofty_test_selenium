## тестовое задание
Задача No1:</br>
Разработать парсер YouTube с использованием Selenium и PostgreSQL.</br>
Описание задачи:</br>
Скрипт должен:</br>
1. Переходить по каждой ссылке на канал, используя Selenium.(см. Приложение 1.1)
2. Собирать все ссылки на видео, доступные на странице (без scroll).
3. Сохранять данные в базу данных PostgreSQL (video_id, channel_username, video_href). Подсказки:
- video_id = все, что после "/watch?v=" в ссылке на видео.
Требования:</br>
- Версия Selenium == 4.14.0.
- Использование Chromedriver.
- Для хранения данных использовать PostgreSQL.
- Использование сырых SQL-запросов.
- Для запуска приложения использовать Docker-compose
- Использование Docstring в функциях с объяснением функционала.
- Выполнить Задачу No2, она не является обязательной

Приложение:</br>
1.1 - https://www.youtube.com/@raily
- https://www.youtube.com/@adorplayer
- https://www.youtube.com/@soderlingoc
- https://www.youtube.com/@sodyan
- https://www.youtube.com/@restlgamer
- https://www.youtube.com/@drozhzhin
- https://www.youtube.com/@empatia_manuchi
- https://www.youtube.com/@barsikofficial
- https://www.youtube.com/@diodand
- https://www.youtube.com/@nedohackerslite