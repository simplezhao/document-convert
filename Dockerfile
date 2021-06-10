FROM document-convert:base
RUN mkdir /root/convert

WORKDIR /root/convert

COPY ./ ./

ADD ./deploy/tini /tini
RUN chmod +x /tini

EXPOSE 5000

ENTRYPOINT ["/tini", "--", "./entrypoint.sh"]



