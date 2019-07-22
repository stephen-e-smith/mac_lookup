FROM alpine:3.7
COPY maclookup.py /tools/
WORKDIR /tools
RUN apk update
RUN apk add bash
RUN apk add python
RUN apk add py-requests
ENTRYPOINT [ "/bin/bash" ]
