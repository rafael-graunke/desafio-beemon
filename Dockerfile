FROM python:3.10-alpine

WORKDIR /app

COPY . .

COPY crontab /etc/cron.d/crontab

RUN apk add --no-cache libstdc++

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod 0644 /etc/cron.d/crontab

RUN /usr/bin/crontab /etc/cron.d/crontab

CMD ["/usr/sbin/crond", "-f"]