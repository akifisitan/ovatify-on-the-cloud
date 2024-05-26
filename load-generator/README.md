# Stress Test Instructions


## Prerequisites

1. Backend API Gateway Public IP
2. Frontend Load Balancer Public IP 
3. Create a firewall rule that accepts requests from public

## Backend

    Inside `load-generator` directory

1. Create a virtual environment for python
```bash 
python -m venv ENV
```
2. Run
```
pip install -r requirements.txt
```
3. `cd` into `backend-load-gen`
4. Run `locust`
5. Enter API Gateway IP as host and add your test values (e.g. 1000 users 15 ramp up)

## Frontend

    Inside `load-generator` directory. (Assuming you created virtual environment above)

1. Create a virtual environment for python

1. `cd` into `frontend-load-gen`
2. Run `locust`
3. Enter Load Balancer IP as host and add your test values (e.g. 1000 users 15 ramp up)
