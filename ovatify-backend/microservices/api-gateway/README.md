# Readme

## Docker

```bash
docker build -t custom-nginx-reverse-proxy .
```

```bash
docker run -d -p 5000:80 --name api-gateway --rm custom-nginx-reverse-proxy
```
