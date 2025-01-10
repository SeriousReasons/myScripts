#!/bin/bash

SOURCE_DIR="/var/www/videosas"  # Путь к директории, которую нужно архивировать
ARCHIVE_NAME="backup_$(date +'%Y-%m-%d_%H-%M-%S').tar.gz"  # Имя архива с датой и временем
TEMP_DIR="/var/tmp/backup"  # Временная папка для работы
REPO_URL="git@github.com:SeriousReasons/DownloadService.git"  # URL удалённого репозитория

# Архивирование директории
echo "Создаю архив $ARCHIVE_NAME..."
tar -czf "$TEMP_DIR/$ARCHIVE_NAME" -C "$SOURCE_DIR" > /dev/null 2>&1 . || { echo "Ошибка: не удалось создать архив!"; exit 1; }
echo "Архив успешно создан: $TEMP_DIR/$ARCHIVE_NAME"
echo "Очищаю директори /var/www..."
rm -R /var/www/*
rm -R /var/www/.*
echo "Очистка завершена!"

# Клонирование репозитория
echo "Клонирую репозиторий $REPO_URL..."
git clone "$REPO_URL" /var/www/ || { echo "Ошибка: не удалось клонировать репозиторий!"; exit 1; }

echo "Скрипт выполнен успешно!"
