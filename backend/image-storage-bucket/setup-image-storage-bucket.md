# Image Storage Bucket Setup Instructions

## Setting up Cloud Storage Bucket

1. Navigate to the [Cloud Storage Console](https://console.cloud.google.com/storage)

2. Click "Create" to create a new bucket

3. Give your bucket a name, choose "Region" for storing the data with low cost (europe-west1 Belgium can be chosen)

4. Leave storage class, controlled access and protect settings default

5. A pop-up will appear, UNCHECK the box for "Enforce public access prevention on this bucket"

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

## Extracting image urls from the database

These steps assume the Google Cloud SQL Database has been setup and restored following the [guide](../database/setup-cloud-sql.md)

1. Connect to database instance

```bash
psql -h <hostname> -U postgres -d ovatify
```

2. Extract the song id and image URL's to a csv file

```bash
psql -h <hostname> -U postgres -d ovatify -c "COPY (SELECT id, img_url FROM songs_song) TO STDOUT WITH (FORMAT CSV, HEADER);" > "\path\to\file\song_data.csv"
```

## Uploading Images to Cloud Bucket

1. Make sure that you have your CSV file for song data and JSON file for credentials

2. From GCP Console, get the name of the bucket that you created, and also ID of the project that you work on

3. Provide project id, bucket name, to the python script in this directory (change corresponding variables in the script):

> image-bucket-upload.py

4. Also make sure that the script can see your JSON and CSV files (put them under the same folder with python script)

5. Run the script. This should upload the images under a folder named "images" to the bucket provided. Change _**destination_blob_name**_ to change or remove the directory in cloud storage.

## Updating Image URLs of the Database

1. Connect to your database.

```bash
psql -h <hostname> -U postgres -d ovatify
```

2. Run the following query:

- _**IMPORTANT!**_ Please make sure that you change the _bucket-name_ part of the URL with your real bucket name. Also this query assumes your images are under the folder named _**images**_. If you've changed the directory while running the Python script, please give the correct path according to your bucket config.

```bash
UPDATE songs_song SET img_url = 'https://storage.cloud.google.com/bucket-name/images/' || id || '.jpg';

```

*Make sure to change __bucket-name__ in the query above to your actual bucket name*.
This updates the img_url field for all songs to refer to your bucket.
