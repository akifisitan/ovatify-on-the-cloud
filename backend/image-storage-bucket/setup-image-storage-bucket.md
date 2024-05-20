# Image Storage Bucket Setup Instructions

## Database

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

## Cloud Bucket

### Bucket Setup Steps

1. From GCP Console, choose Cloud Storage, go to "Buckets" tab, and click "Create"

2. Give your bucket a name, choose "Region" for storing the data with low cost (europe-west1 Belgium can be chosen)

3. Leave storage class, controll access and protect settings default

4. A pop-up will appear, UNCHECK the box for "Enforce public access prevention on this bucket"

## Service Account Setup

### Steps

1. From GCP Console, choose "IAM & Admin", then select "Service Accounts" tab

2. Click "Create Service Account", give it a name

3. **IMPORTANT!** Grant 3 roles to the service account:

> - Storage Admin
> - Storage Object Admin
> - Storage Object Creator

4. Leave _"Grant User Access"_ part empty, click _"Done"_

5. Then, from the Service Accounts tab, choose your Service Account and choose _"Actions"_, then click _"Manage Keys"_

6. Click _"Add Key"_, and then _"Create new key"_, choose JSON and create

7. A JSON file with your credentials should begin to download.

# Uploading Images to Cloud Bucket

### Steps

1. Firstly, make sure that you have your CSV file for song data and JSON file for credentials

2. From GCP Console, get the name of the bucket that you created, and also ID of the project that you work on

3. Provide project id, bucket name, to the python script in this directory (change corresponding variables in the script):

> image-bucket-upload.py

4. Also make sure that the script can see your JSON and CSV files (put them under the same folder with python script)

5. Run the script. This should upload the images under a folder named "images" to the bucket provided. Change _**destination_blob_name**_ to change or remove the directory in cloud storage.

# Updating Image URLs of the Database

### Steps

1. Firstly, connect to your database.

```bash
psql -U postgres -d ovatify
```

2. Run the following query:

- _**IMPORTANT!**_ Please make sure that you change the _bucket-name_ part of the URL with your real bucket name. Also this query assumes your images are under the folder named _**images**_. If you've changed the directory while running the Python script, please give the correct path according to your bucket config.

```bash
UPDATE songs_song
SET img_url = CONCAT('https://storage.cloud.google.com/bucket-name/images/', id, '.jpg')
WHERE id = '<id_value>';
```

This updates the img_url field for all songs to refer to your bucket.
