# Creating Image Serverless Function
This creates a Cloud Function that handles Image Moderation API and Compression endpoint. The files that should be uploaded to the Cloud Function are already created, this just shows how to set up the Cloud Function. 

*__!IMPORTANT!__* For this to work properly, you should enable Cloud Vision API from GCP. 

## Steps

1. Go to [Cloud Functions - GCP Console](https://console.cloud.google.com/functions)

2. Click Create Function

3. Choose a name and region for the serverless function to be run (Belgium is preferred)

4. Leave trigger type as defauly, *__allow for unauthenticated invocations__*

5. Adjust Runtime etc. according to your needs
(*__Concurrency and number of instances are important__*)

6. Click Next

7. You should see the function creation screen now. Choose Runtime as *__Python 3.11__*, entry point as *__compress_and_check_image__*, and change *__main.py__* and *__requirements.txt__* with the files provided under *__src__* folder in this directory

8. Click deploy, you will be given the access URL for the Function that will be accessible by any HTTP request.


