FROM python:3.7.3-alpine3.9
WORKDIR /app/syncip/api
COPY ./api /app/syncip/api
RUN echo '5 * * * * /usr/bin/python3.7 /app/syncip/api/main.py' > /etc/crontabs/root
RUN mkdir /var/log/syncip
RUN touch /var/log/syncip/api.log
CMD ["crond", "-f"]