# Frontend VM Load Balancer Setup Instructions

This documentation provides a step-by-step guide to setting up a load balancer for three virtual machines (VMs) running front-end applications on Google Cloud Platform (GCP).

## Prerequisites
- A Google Cloud account
- Billing enabled on your GCP project
- Basic knowledge of Google Cloud Console and command-line interface

## Steps Overview
1. Create an instance template.
2. Create instance groups.
3. Set up the VMs.
4. Create the load balancer.


## Step 1: Create Instance Template

1. **Navigate to Compute Engine:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Navigate to `Compute Engine` > `Instance templates`.

2. **Create Instance Template:**
   - Click on `Create Instance Template`.
   - Configure your instance template (name, machine type, etc.).
   - Under `Boot disk`, select your desired operating system, such as Ubuntu 22.04.
   - Click `Create` to save the template.

## Step 2: Create Instance Groups

1. **Navigate to `Compute Engine` > `Instance groups`**

2. **Create Instance Group:**
   - Click on `Create Instance Group`.
   - Configure your instance group (name, location, etc.).
   - Specify the instance template created above.
   - Turn off Auto-scaling and set the number of instances to 3.
   - Click `Create`.

## Step 3: Set Up the VMs

1. **Deploy Front-End Application:**
   - Navigate to `Compute Engine` > `VM Instances`.
   - SSH into each of the three VMs.
   - Follow the [frontend/frontend-vm/setup-frontend-vm.md](https://github.com/akifisitan/ovatify-on-the-cloud/blob/main/frontend/frontend-vm/setup-frontend-vm.md) instructions to set up the front-end application on each VM.

## Step 4: Create Load Balancer

1. **Navigate to `Network services` > `Load balancing`**

2. **Create Load Balancer:**
   - Click on `Create Load Balancer`.
   - Select `HTTP(S) Load Balancing` and click `Start configuration`.
   - Select `Global Load Balancer`.
   
3. **Configure the Frontend:**
   - Under `New Frontend Configuration`, provide a name.
   - Select `HTTP` or `HTTPS`.
   - Configure the IP address and port (use port 80 for HTTP).
   
4. **Configure the Backend:**
   - Under `Backends`, click `Create a backend service`.
   - Provide a name for the backend service.
   - Select the instance group you created earlier.
   - Set the port number your application is running on (e.g., port 80).
   - Configure health checks (HTTP check on port 80).

5. **Finalize and Create:**
   - Review the configuration.
   - Click `Create`.


You have successfully set up a load balancer for your front-end applications on Google Cloud using three virtual machines. This setup ensures high availability and efficient distribution of traffic to your application.
