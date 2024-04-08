# Use a lightweight base image
FROM alpine:latest

# Install required packages and build dependencies
RUN apk add --no-cache bash netcat-openbsd fortune wget unzip perl

# Download and extract cowsay source code
RUN wget https://github.com/tnalpgge/rank-amateur-cowsay/archive/master.zip && \
    unzip master.zip && \
    rm master.zip

# Build and install cowsay
RUN cd rank-amateur-cowsay-master && \
    ./install.sh /usr/local && \
    cd .. && \
    rm -rf rank-amateur-cowsay-master

# Copy the script into the container
COPY wisecow.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/wisecow.sh

# Expose the port
EXPOSE 4499

# Set the script as the entrypoint
ENTRYPOINT ["/usr/local/bin/wisecow.sh"]

# ENTRYPOINT should be the path to the process that will be executed inside the container.
# CMD should be the default arguments to pass to that command (if any).

# Incorrectly setting CMD instead of ENTRYPOINT is a common mistake. While your image will usually still work—because 
# Docker defaults to using /bin/sh -c as the ENTRYPOINT—end users won’t be able to directly pass arguments to your binary using docker run. 
# They’ll need to pass the full path to the binary instead, as the container’s ENTRYPOINT process will be /bin/sh -c instead of your own app.