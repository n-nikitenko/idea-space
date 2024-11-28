# Используем Node.js как базовый образ
FROM node:18-alpine

# Устанавливаем рабочую директорию
WORKDIR /frontend

# Копируем package.json и package-lock.json для установки зависимостей
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем весь проект
COPY . .

# Открываем порт для dev-сервера
EXPOSE 3000

# Команда по умолчанию для разработки
CMD ["npm", "run", "dev"]
