FROM alpine:3.7
COPY maclookup.py /mac_lookup/
WORKDIR /mac_lookup
RUN apk update
RUN apk add python
RUN apk add py-requests
ENTRYPOINT [ "python", "/mac_lookup/maclookup.py" ]
