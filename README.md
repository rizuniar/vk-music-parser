# vk-music-parser
Скрипт на Python для парсинга списка аудиозаписей из ВКонтакте. Использует Selenium для имитации действий пользователя и BeautifulSoup4 для быстрого извлечения данных из атрибутов страницы.

## 🛠 Требования
1.  **Python 3.x**
2.  **Geckodriver** (драйвер для Firefox):
    ```bash
    sudo pacman -S geckodriver
    ```

## ⚙️ Настройка
Перед запуском убедись, что путь к твоему профилю Firefox и ссылка на музыку в ВК в коде указаны верно. Путь можно найти, введя `about:support` в адресной строке браузера.

```python
profile_path = "/home/your_user/.mozilla/firefox/your_profile.default-release"
driver.get("https://vk.com/your_audio")
```

> [!IMPORTANT]
> Перед запуском скрипта необходимо **полностью закрыть Firefox**, иначе возникнет ошибка блокировки профиля.

## 📖 Использование
1. Склонируй репозиторий:
   ```bash
   git clone https://github.com/rizuniar/vk-music-parser.git
   cd vk-music-parser
   ```

2. Сделай виртаульное пространство и установи зависимости:
   ```bash
   python -m venv env
   . env/bin/activate
   pip install requirements.txt
   ```
3. Запусти скрипт:
   ```bash
   python main.py
   ```
4. По завершении в директории появится файл `vk_playlist.txt` со списком в формате `Исполнитель - Название`.

## 📂 Структура проекта
* `main.py` — основной скрипт парсера.
* `vk_playlist.txt` — результат работы.
* `README.md` — описание проекта.

## ⚠️ Дисклеймер
Данный проект создан исключительно в образовательных целях для изучения инструментов автоматизации браузера. Помните о правилах использования сторонних сервисов.
