# Full System Setup Guide

## Cloud setup steps

1. [Create a google cloud project](https://console.cloud.google.com/projectcreate) and note down the project id

2. Follow the [database setup guide](./backend/database/setup-cloud-sql.md) and note down the database credentials

3. Follow the [image storage bucket setup guide](./backend/image-storage-bucket/setup-image-storage-bucket.md) and note down the bucket url

4. Follow the [image function setup guide](./backend/image-function/setup-image-function.md) and note down the image function url

5. Follow the [microservices setup guide](./backend/microservices/setup-microservices.md) and note down the created service urls

6. Follow the [API gateway setup guide](./backend/api-gateway/setup-api-gateway.md) and note down the api gateway vm ip address

7. Follow the [frontend VM setup guide](./frontend/frontend-vm/setup-frontend-vm.md)

8. Follow the [frontend VM load balancer setup guide](./frontend/frontend-vm-load-balancer/setup-frontend-vm-load-balancer.md) and note down the load balancer IP address

9. Follow the [load generator setup guide](./load-generator/setup-load-generator.md) and run tests by hitting the load balancer and API Gateway VM IP addresses

## Local setup with Docker Compose

1. Create a Google Cloud project and note down the project name

2. [Setup the image storage bucket](./backend/image-storage-bucket/setup-image-storage-bucket.md) and note down the bucket name

3. [Setup the image function](./backend/image-function/setup-image-function.md) and note down the function url

4. Create an `.env.local` file in each microservice source directory

Add the following to the `.env.local` file

```txt
DB_NAME=ovatify
DB_USER=postgres
DB_PASSWORD=Test123.
DB_HOST=host.docker.internal
CLOUD_FUNCTION_URL=your-function-url-here
STORAGE_BUCKET_NAME=your-bucket-name-here
PROJECT_ID=your-project-id-here
```

5. Create an `.env` file in `frontend/ovatify-frontend`

Add the following to the `.env` file

```txt
PUBLIC_BASE_URL=http://localhost:8000
```

6. Run

```bash
docker compose up --remove-orphans --detach
```

7. Once the services are up and running, connect to the database and restore the backup

```bash
psql -U postgres -d ovatify -f backend/database/backup.sql
```

8. In your browser, navigate to `http://localhost:5000/` for the frontend app or `http://localhost:7000/` for the load generator
