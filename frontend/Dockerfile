# Используем Node.js как базовый образ
FROM node:18-alpine

# Устанавливаем рабочую директорию
WORKDIR /frontend

# Открываем порт для dev-сервера
EXPOSE 3000

# Команда по умолчанию для разработки
CMD npm install && npm run dev -- -o