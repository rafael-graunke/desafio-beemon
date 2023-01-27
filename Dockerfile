FROM python:3.10-slim

RUN apt-get update && apt-get -y install cron vim

WORKDIR /app

COPY . .

COPY crontab /etc/cron.d/crontab

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod 0644 /etc/cron.d/crontab

RUN /usr/bin/crontab /etc/cron.d/crontab

CMD ["cron", "-f"]