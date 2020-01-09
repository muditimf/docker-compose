FROM centos
RUN yum install httpd python36 -y
RUN pip3 install mysql-connector

COPY index.html /var/www/html/index.html

COPY py.cgi /var/www/cgi-bin/py.cgi
RUN chmod +x /var/www/cgi-bin/py.cgi
ENV MYSQL_HOST $MYSQL_HOST
EXPOSE 80
ENTRYPOINT httpd -DFOREGROUND
