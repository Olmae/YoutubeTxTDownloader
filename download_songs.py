import os
import yt_dlp as youtube_dl

# Чтение списка песен из файла
with open('songs.txt', 'r', encoding='utf-8') as file:
    songs = file.readlines()

# Путь к папке "Плейлист" в репозитории
playlist_dir = os.path.join(os.path.dirname(__file__), 'Плейлист')
os.makedirs(playlist_dir, exist_ok=True)  # Создаем папку, если она не существует

# Настройки для yt-dlp
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Скачиваем лучшее видео и аудио
    'default_search': 'ytsearch',  # Поиск по названию
    'noplaylist': True,  # Отключаем скачивание плейлистов
    'outtmpl': os.path.join(playlist_dir, '%(title)s.%(ext)s'),  # Сохраняем файлы в папку "Плейлист"
    'ffmpeg_location': os.path.join(os.getcwd(), 'ffmpeg-7.0-full_build/bin'),  # Путь к ffmpeg
}

# Хранение уже скачанных треков для проверки дубликатов
downloaded_songs = set()

# Открываем файл для записи информации о скачанных треках
with open('downloaded_songs.txt', 'w', encoding='utf-8') as log_file:
    for song in songs:
        song = song.strip()  # Удаляем лишние пробелы и символы новой строки
        if not song:
            continue

        # Добавляем приписку "караоке" к названию
        search_query = f'{song} караоке'

        # Проверяем на дубликат
        if search_query in downloaded_songs:
            print(f'Трек уже скачан: {search_query}')
            continue

        print(f'Ищем и скачиваем: {search_query}')
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                # Поиск и скачивание видео
                result = ydl.extract_info(search_query, download=True)
                video_title = result.get('title', 'Без названия')
                video_url = result.get('webpage_url', 'Неизвестно')

                # Записываем информацию о треке в лог-файл
                log_file.write(f'Запрос: {song}\nНазвание: {video_title}\nСсылка: {video_url}\n\n')

                # Добавляем трек в список скачанных
                downloaded_songs.add(search_query)
            except Exception as e:
                print(f'Ошибка при скачивании {search_query}: {e}')
