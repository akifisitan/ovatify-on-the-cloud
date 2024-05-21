# Google Cloud SQL Setup Instructions

## Creating a Cloud SQL Instance

1. Navigate to the [Cloud SQL Console](https://console.cloud.google.com/sql)

2. Click on create instance

3. Select PostgreSQL

4. Give it an id and password. Make sure to note down the password

5. Set database version to PostgreSQL 15

6. Select Enterprise

7. Select production or development depending on needs

8. Click on customize instance

9. In connections, add a new network as authorized network

```
name: allowall
network: 0.0.0.0/0
```

10. Click done

11. Click create instance

12. Wait for the instance to be created - this can take 5 to 10 minutes

13. Once its created, copy the public IP address. This will be used as host when connecting

## Restoring the database backup

1. Install [PostgreSQL 15](https://www.postgresql.org/download/) for the psql command line tool

2. Run

```bash
psql -h <public-ip-address> -U postgres -d postgres
```

3. Once connected, run the following command to create a new database

```sql
CREATE DATABASE ovatify;
```

4. Once the database has been created, run \q to exit

5. Navigate to the directory of the backup.sql file, then run

```bash
psql -h <public-ip-address> -U postgres -d ovatify -f backup.sql
```

6. Wait for the operation to complete

7. Connect to the database

```bash
psql -h <public-ip-address> -U postgres -d ovatify
```

8. Run a test query

```bash
SELECT COUNT(*) FROM users_user;
```

## Using database connection in .env files

```txt
DB_USERNAME: postgres
DB_NAME: ovatify
DB_PASSWORD: <database password>
DB_HOST: <database public IP address>
```
