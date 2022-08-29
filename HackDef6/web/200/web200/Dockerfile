FROM silintl/php8:8.1

ARG document_root=/etc/apache2/sites-enabled/
COPY vhost-config.conf $document_root

RUN mkdir -p /data
VOLUME ["/data"]

ADD Challenge/ /data/

WORKDIR /data
EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]
