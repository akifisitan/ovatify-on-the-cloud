# Microservices Setup Instructions

## Creating a repository in artifact registry to push docker images

1. Navigate to [Artifact Registry Console](https://console.cloud.google.com/artifacts)

2. Click create repository

3. Give it a name, select Docker as format, select the region and click create

4. Once created, click on it and copy its url. Make sure to note it down

5. Click on setup instructions and copy the Configure Docker command, then run it

6. Now you will be able to push images to this registry

Example:

```bash
gcloud auth configure-docker europe-west1-docker.pkg.dev
```

## Building docker images and pushing them to a repository to use on Google Cloud Run

1. Install Docker

    For each service

2. Navigate to the service source code where the Dockerfile is

3. Create `.env` file and add needed config values written at `.env.example`

4. Run

```bash
docker build -t <service-image-name> .
```

Example:

```bash
docker build -t ovtf-auth-srv .
```

4. Once it is built, tag the image with the repository url you noted down

```bash
docker tag <service-image-name> <repository-url>/<service-image-name>
```

Example:

```bash
docker tag ovtf-auth-srv europe-west1-docker.pkg.dev/my-project-name/my-test-registry/ovtf-auth-srv
```

5. Push the tagged image to the repository with

```bash
docker push <repository-url>/<service-image-name>
```

```bash
docker push europe-west1-docker.pkg.dev/my-project-name/my-test-registry/ovtf-auth-srv
```

Do these steps for each service

## Creating Google Cloud Run Services

1. Ensure the service images are pushed to the image repository

2. Navigate to the [Google Cloud Run Console](https://console.cloud.google.com/run)

3. Click on create service

4. Click on "Select" to select the container image URL, then select the image of the service you wish

5. Set service name and region

6. Check "Allow unauthenticated invocations"

7. Modify CPU and scaling parameters as necessary

8. Click on Container(s), Volumes, Networking, Security. Set the container port to 8000, modify memory and cpu as necessary

9. Click on Variables & Secrets, then add the required environment variables specified in the service's `.env.example` file

10. Modify the request timeout, max concurrent requests per instance, min and max number of instances as necessary

11. Click create

12. Once created, copy the service URL. Make sure to note it down

Do these steps for each service and obtain each service's url
