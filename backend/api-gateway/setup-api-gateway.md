# NGINX API Gateway Setup Instructions

## Config Files Overview

`nginx.conf`

- Contains the upstream services, imports all necessary configs

`location_proxy_shared.conf`

- Contains directives shared by different service routes

`service_config/<service-name>_service_routes.conf`

- Contains routes for each service. Mono service is the catch all service with just a single route "/" meaning any unmatched request is forwarded to it.

## Setting up API Gateway on a VM

1. Ensure all the services are hosted.

2. Modify the upstream servers in the `nginx.conf` file. Make sure to modify both the upstream and the corresponding host variable specified in the server block

Example:

Suppose auth service is hosted on https://ovtf-service.a.run.app/

Modify nginx.conf as follows:

```txt
    upstream auth_service {
        server ovtf-service.a.run.app:443;
    }

    # ...remaining services

    server {
        listen 80;

        set $auth_service_host ovtf-service.a.run.app;
        # ...remaining services

        include /etc/nginx/conf.d/auth_service.conf;
        # ...remaining services
    }
```

3. Install nginx and make

```bash
sudo apt update && sudo apt install nginx -y && sudo apt install make
```

4. Clone this directory somewhere then cd into it

Run the `copy` command from the makefile

```bash
make copy
```

This command will:

- Copy all the config files to the correct place
- Check if the nginx config has any syntax errors
- Restart the nginx service

## Optional: Setting up API Gateway using Docker

1. Ensure all the services are hosted.

2. Modify the upstream servers with their corresponding service host in the `nginx.conf` file. Make sure to modify both the upstream and the corresponding host variable specified in the server block

Example:

Suppose auth service is hosted on https://ovtf-service.a.run.app/

Modify nginx.conf as follows:

```txt
    upstream auth_service {
        server ovtf-service.a.run.app:443;
    }

    # ...remaining services

    server {
        listen 80;

        set $auth_service_host ovtf-service.a.run.app;
        # ...remaining services

        include /etc/nginx/conf.d/auth_service.conf;
        # ...remaining services
    }
```

3. Build the image

```bash
docker build -t api-gateway-nginx .
```

4. Run the image

```bash
docker run -d --name api-gateway -p 5000:80 api-gateway-nginx
```
