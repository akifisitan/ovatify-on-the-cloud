# Load Generator Setup Instructions

## Setting up VM for load generation

1. Create an Ubuntu VM

2. Create a [firewall rule](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies) for TCP port 8089 or whichever port the locust web interface will be run on

3. Install Python 3.10+

4. Create a virtual environment and activate it

5. Install dependencies

```bash
pip install -r requirements.txt
```

5. Change directory to `backend-load-gen` or `frontend-load-gen` depending on use-case and run

```bash
locust
```

6. Navigate to `http://<VM-ip:8089/` on your local machine to view the locust web interface and run tests
