# Setup

## Local Development Setup

### Requirements
- Python 3.11
- Docker

Create a virtual environment and activate it
```bash
python -m venv venv
.\venv\Scripts\activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

Run the server
```bash
python manage.py runserver
```

Update/apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## Google Cloud Setup

install google cloud cli from
https://cloud.google.com/sdk/docs/install

europe-west-3 => frankfurt

## Database Setup

### Local

Install Docker

```bash
docker run -d --name pg -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=<your-password> -p 5432:5432 postgres
```

### Connect to database instance
```bash
psql -h 35.198.162.10 -U postgres -d postgres -p 5432
```
Enter the password and connect

### Create new database
Once connected, create a new database
```sql
> CREATE DATABASE ovatify;
```
Run the following to restore database from a backup file

```bash
psql -h 35.198.162.10 -U postgres -d ovatify -f backup.sql
```

## Backend Setup

Build the image locally with

```bash
docker build -t ovatify-backend . 
```

Run the image locally with
```bash
docker run -d --name ovatify --env-file .env -p 8000:8000 ovatify-backend 
```

Create new docker artifact registry from the [google artifact dashboard](https://console.cloud.google.com/artifacts) 
- Choose Docker as the format and Standard as the mode.
- Under Location Type, select Region and then choose the location europe-west-3

Configure auth for the registry you have created
```bash
gcloud auth configure-docker europe-west3-docker.pkg.dev
```

Tag the local image with the registry
```bash
docker tag ovatify-backend europe-west3-docker.pkg.dev/ascendant-bloom-417021/test-registry/ovatify-backend
```

Push the image to the registry with
```bash
docker push europe-west3-docker.pkg.dev/ascendant-bloom-417021/test-registry/ovatify-backend
```
# Steps

1. Open up Cloud SQL Postgres 15 instance with 1vCPU 614.4 MB 10 GB SSD 0.02$/hour [show](https://console.cloud.google.com/sql/instances/pg/edit?hl=en&organizationId=1045832606744&project=ascendant-bloom-417021) 
2. Setup Cloud Run from Artifact Registry



