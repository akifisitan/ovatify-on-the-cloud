# Database Setup

### Local

Install Docker, then run

```bash
docker run -d --name pg -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=<your-password> -p 5432:5432 postgres
```

Install psql cli tool, then run

### Connect to database instance
```bash
psql -h <hostname> -U postgres -d postgres -p 5432
```

Enter the password and connect

### Create new database
Once connected, create a new database

```sql
CREATE DATABASE ovatify;
```
Run the following to restore database from a backup file

```bash
psql -h <hostname> -U postgres -d ovatify -f backup.sql
```

### Extract the song id and image URL's to a csv file
```bash
psql -U postgres -d ovatify -c "COPY (SELECT id, img_url FROM songs_song) TO STDOUT WITH (FORMAT CSV, HEADER);" > "\path\to\file\song_data.csv"
```

# Cloud Bucket Setup

### Bucket Setup Steps

1. From GCP Console, choose Cloud Storage, go to "Buckets" tab, and click "Create" 

2. Give your bucket a name, choose "Region" for storing the data with low cost (europe-west1 Belgium can be chosen)

3. Leave storage class, controll access and protect settings default

4. A pop-up will appear, UNCHECK the box for "Enforce public access prevention on this bucket"

# Service Account Setup

### Steps

1. From GCP Console, choose "IAM & Admin", then select "Service Accounts" tab

2. Click "Create Service Account", give it a name 

3. __IMPORTANT!__ Grant 3 roles to the service account:

> - Storage Admin
> - Storage Object Admin
> - Storage Object Creator


4. Leave *"Grant User Access"* part empty, click *"Done"*

5. Then, from the Service Accounts tab, choose your Service Account and choose *"Actions"*, then click *"Manage Keys"*

6. Click *"Add Key"*, and then *"Create new key"*, choose JSON and create 

7. A JSON file with your credentials should begin to download.

# Uploading Images to Cloud Bucket

### Steps

1. Firstly, make sure that you have your CSV file for song data and JSON file for credentials 

2. From GCP Console, get the name of the bucket that you created, and also ID of the project that you work on

3. Provide project id, bucket name, to the python script in this directory (change corresponding variables in the script):

> image-bucket-upload.py 

4. Also make sure that the script can see your JSON and CSV files (put them under the same folder with python script)

5. Run the script. This should upload the images under a folder named "images" to the bucket provided. Change *__destination_blob_name__* to change or remove the directory in cloud storage.
