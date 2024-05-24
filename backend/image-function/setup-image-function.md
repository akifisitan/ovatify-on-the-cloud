# Image Function Setup

## Creating Image Serverless Function

This creates a Cloud Function that handles Image Moderation API and Compression endpoint. The files that should be uploaded to the Cloud Function are already created, this just shows how to set up the Cloud Function.

_**!IMPORTANT!**_ For this to work properly, you must enable the [Cloud Vision API](https://console.cloud.google.com/apis/library/vision.googleapis.com) from GCP.

1. Go to [Cloud Functions - GCP Console](https://console.cloud.google.com/functions)

2. Click Create Function

3. Choose a name and region for the serverless function to be run (Belgium is preferred)

4. Leave trigger type as default and check `Allow unauthenticated invocations`

5. Adjust Runtime etc. according to your needs
   (_**Concurrency and number of instances are important**_)

6. Click Next

7. You should see the function creation screen now. Choose `Python 3.11` as runtime from the dropdown , modify the entry point to `compress_and_check_image`, and update `main.py` and `requirements.txt` with the files provided under the [src folder](./src/) in this directory

8. Click deploy, then copy the access URL for the function. Make sure to note it down
