# Setting Up a PostgreSQL Database with Docker

## 1. Pull the PostgreSQL Image
Download the official PostgreSQL image from Docker Hub:
docker pull postgres:15

## 2. Run the PostgreSQL Container
Start a PostgreSQL container with a custom database name, user, and password:
docker run --name my-postgres-db \
  -e POSTGRES_USER=myuser \
  -e POSTGRES_PASSWORD=mypassword \
  -e POSTGRES_DB=mydatabase \
  -p 5432:5432 \
  -d postgres:15

### Explanation:
- `--name my-postgres-db`: Names the container for easy reference.
- `-e`: Sets environment variables for the database (user, password, and name).
- `-p 5432:5432`: Maps the container's PostgreSQL port to your local machine's port.
- `-d`: Runs the container in detached mode.

## 3. Verify the Container is Running
List running containers:
docker ps
You should see your `my-postgres-db` container in the list.

## 4. Connect to PostgreSQL
Use `psql` or any PostgreSQL client tool to connect:
psql -h localhost -U myuser -d mydatabase

Or, access the container directly:
docker exec -it my-postgres-db psql -U myuser -d mydatabase

## 5. Stop the Container
To stop the running PostgreSQL container:
docker stop my-postgres-db

## 6. Remove the Container
To remove the container:
docker rm my-postgres-db
