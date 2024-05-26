# Frontend VM Load Balancer Setup Instructions

This documentation provides a step-by-step guide to setting up a load balancer for three virtual machines (VMs) running front-end applications on Google Cloud Platform (GCP).

## Prerequisites
- A Google Cloud account
- Billing enabled on your GCP project
- Basic knowledge of Google Cloud Console and command-line interface
- Completing [frontend VM setup guide](./frontend/frontend-vm/setup-frontend-vm.md)

## Steps Overview
1. Create an instance template.
2. Create instance groups.
3. Set up the VMs.
4. Create the load balancer.


## Step 1: Create Instance Template

1. **Navigate to Compute Engine:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Navigate to `Compute Engine` > `Images`.
   - Click `Create Image`.
   - In the `Name` field, provide a name for your image.
   - Choose the `Source Disk` as your Frontend VM's disk which was created at [frontend VM setup](./frontend/frontend-vm/setup-frontend-vm.md).
   - Click `Create` to initiate the image creation process.

2. **Create Instance Template:**
   - Click on `Create Instance Template`.
   - Configure your instance template (name, machine type, etc.).
   - Under `Boot disk`, select the image you created at step 1.
   - Click `Create` to save the template.

## Step 2: Create Instance Groups

1. **Navigate to `Compute Engine` > `Instance groups`**

2. **Create Instance Group:**
   - Click on `Create Instance Group`.
   - Configure your instance group (name, location, etc.).
   - Specify the instance template created above.
   - Configure Auto-scaling as you wish.
   - Click `Create`.

## Step 3: Create Load Balancer

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
