# NGINX API Gateway

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

Run

```bash
sudo apt update && sudo apt install nginx -y && sudo apt install make
```

to install nginx and make.

Copy the `vm-api-gateway` directory somewhere then cd into it

Run

```bash
make copy
```

Should be ready to go!
