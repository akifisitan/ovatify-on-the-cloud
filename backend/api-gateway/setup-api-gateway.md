# NGINX API Gateway Setup Instructions

## Modifying config files

`nginx.conf`
Contains the nginx configuration
You may modify the upstream servers in this file
Make sure to modify both the upstream and the corresponding host variable specified in the server block

`location_proxy_shared.conf`

Contains shared directives

## Docker Setup Instructions

```bash
docker build -t api-gateway-nginx .
```

```bash
docker run -d --name api-gateway -p 5000:80 api-gateway-nginx
```

## VM Setup Instructions

Install nginx and make

```bash
sudo apt update && sudo apt install nginx -y && sudo apt install make
```

Clone this directory somewhere then cd into it

Run `copy` command from makefile

```bash
make copy
```

Should be ready to go!
