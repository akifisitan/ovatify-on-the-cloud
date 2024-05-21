# Full System Setup Guide

1. [Database](./backend/database/setup-cloud-sql.md) => Get database credentials

2. [Image Storage Bucket](./backend/image-storage-bucket/setup-image-storage-bucket.md) => Get bucket url

3. [Image Function](./backend/image-function/setup-image-function.md) => Get function url

4. [Microservices](./backend/microservices/setup-microservices.md) => Setup microservices using the previous, get all of their urls

5. [API Gateway](./backend/api-gateway/setup-api-gateway.md) => Set all service urls, get VM ip

6. [Frontend VMs](./frontend/frontend-vm/setup-frontend-vm.md) => Set base_url env to API Gateway VM ip, get VM ips

7. [Frontend VM Load Balancer](./frontend/frontend-vm-load-balancer/setup-frontend-vm-load-balancer.md) => Set VM ips, get url

8. [Load Generator](./load-generator/setup-load-generator.md) => Run tests by hitting VM Load balancer and API Gateway IPs
