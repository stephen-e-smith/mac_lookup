# mac_lookup
A simple MAC vendor lookup script.

# Building

    [root@localhost mac_lookup]# docker build -t mac_lookup .
    Sending build context to Docker daemon  35.33kB
    Step 1/7 : FROM alpine:3.7
    3.7: Pulling from library/alpine
    5d20c808ce19: Pull complete
    Digest: sha256:8421d9a84432575381bfabd248f1eb56f3aa21d9d7cd2511583c68c9b7511d10
    Status: Downloaded newer image for alpine:3.7
     ---> 6d1ef012b567
    ...
    OK: 56 MiB in 33 packages
    Removing intermediate container 2b76d7ae6408
     ---> d0c24e55f4a4
    Step 7/7 : ENTRYPOINT [ "python", "/mac_lookup/maclookup.py" ]
     ---> Running in 36ea09110ba7
    Removing intermediate container 36ea09110ba7
     ---> ccb9156d7790
    Successfully built ccb9156d7790
    Successfully tagged mac_lookup:latest

# Usage

    docker run -it mac_lookup -k <macaddress.io api key> -m <mac>

This returns the "companyName" field from the macaddress.io payload.
Some MAC addresses, while valid, are not registered and thus return a
blank line.

    [root@localhost mac_lookup]# docker run -it mac_lookup -k REDACTED -m 74:d4:35:64:8a:4e
    Giga-Byte Tech Co, Ltd

# Security

This application communicates with api.macaddress.io via HTTPS only.
In addition, no secrets are embedded in this image. You're required
to provide your own API key for macaddress.io (Free sign-up). 
