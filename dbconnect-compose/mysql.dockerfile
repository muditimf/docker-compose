FROM mysql
ENV MYSQL_DATABASE users

COPY ./sql-scripts /docker-entrypoint-initdb.d/
