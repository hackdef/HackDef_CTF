FROM ubuntu:20.10

RUN apt-get -qq update && apt-get install -qq --no-install-recommends xinetd

COPY chal/mini-shellcoding /
COPY flag.txt /

COPY service.conf /service.conf
COPY banner_fail /banner_fail
COPY wrapper /wrapper

EXPOSE 4000
CMD ["/usr/sbin/xinetd", "-filelog", "/dev/stderr", "-dontfork", "-f", "/service.conf"]
