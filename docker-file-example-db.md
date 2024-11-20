# Custom Dockerfile for PostgreSQL

## Dockerfile
```dockerfile
# Use the official PostgreSQL image as the base
FROM postgres:15

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydatabase

# Expose PostgreSQL's default port
EXPOSE 5432
```

## Steps to Use the Custom Dockerfile

1. **Save the Dockerfile**:
   Save the above `Dockerfile` in a folder. If using an `init.sql` file, ensure it’s in the same directory.

2. **Build the Docker Image**:
   Build the custom image:
   ```bash
   docker build -t custom-postgres .
   ```

3. **Run the Container**:
   Use the custom image to start a PostgreSQL container:
   ```bash
   docker run -d \
     --name my-custom-postgres \
     -p 5432:5432 \
     custom-postgres
   ```

4. **Verify the Container is Running**:
   Check the running containers:
   ```bash
   docker ps
   ```

5. **Access the PostgreSQL Database**:
   Connect to the database using a PostgreSQL client, like `psql`:
   ```bash
   psql -h localhost -U myuser -d mydatabase
   ```

6. **Stop and Remove the Container (Optional)**:
   ```bash
   docker stop my-custom-postgres
   docker rm my-custom-postgres
   ```

---

This approach allows for custom database initialization and reusable configurations.
