import yt_dlp as youtube_dl  # Используем yt-dlp вместо youtube_dl
import os
import shutil

# Путь к папке "Плейлист" в директории скрипта
playlist_folder = os.path.join(os.getcwd(), 'Плейлист')

# Создаём папку, если она не существует
if not os.path.exists(playlist_folder):
    os.makedirs(playlist_folder)

# Чтение списка песен из файла
with open('songs.txt', 'r', encoding='utf-8') as file:
    songs = file.readlines()

# Настройки для yt-dlp
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'default_search': 'ytsearch',  # Поиск по названию
    'noplaylist': True,  # Отключаем скачивание плейлистов
    'ffmpeg_location': os.path.join(os.getcwd(), 'ffmpeg-7.0-full_build', 'bin'),  # Путь к ffmpeg
    'outtmpl': os.path.join(playlist_folder, '%(title)s.%(ext)s'),  # Путь сохранения треков в папку "Плейлист"
}

downloaded_tracks = set()  # Множество для хранения названий уже скачанных треков

# Файл для записи логов скачивания
with open('download_log.txt', 'w', encoding='utf-8') as log_file:
    for song in songs:
        song = song.strip()  # Удаляем лишние пробелы и символы новой строки
        if not song:
            continue
        if song in downloaded_tracks:
            print(f'Трек уже скачан: {song}')
            continue  # Пропускаем трек, если он уже был скачан

        print(f'Ищем и скачиваем: {song}')
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                result = ydl.extract_info(song, download=True)  # Поиск и скачивание песни
                downloaded_tracks.add(song)  # Добавляем трек в множество скачанных

                # Получаем название трека и ссылку
                track_title = result.get('title', 'Unknown Title')
                track_url = result.get('webpage_url', 'Unknown URL')

                # Записываем информацию в лог
                log_file.write(f'{song} -> {track_title}: {track_url}\n')

        except Exception as e:
            print(f'Ошибка при скачивании {song}: {e}')
