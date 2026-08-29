FROM n8nio/n8n:1.65.0

USER root

# 1. Устанавливаем системный Python, пакетный менеджер и виртуальные среды
RUN apk add --no-cache python3 py3-pip python3-dev build-base bash

# 2. Создаем изолированное виртуальное окружение в папке /opt/venv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV

# 3. Добавляем пути к виртуальному окружению в системный PATH контейнера
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# 4. Спокойно устанавливаем requests без каких-либо флагов и блокировок OS
RUN pip install --no-cache-dir requests

# 5. Возвращаем безопасного пользователя node для запуска самого n8n
USER node
