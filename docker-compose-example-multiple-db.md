```
version: "3.9"

services:
  postgres-db-1:
    image: postgres:15
    container_name: postgres-db-1
    environment:
      POSTGRES_USER: user1
      POSTGRES_PASSWORD: password1
      POSTGRES_DB: database1
    ports:
      - "5433:5432"
    volumes:
      - postgres_data_1:/var/lib/postgresql/data

  postgres-db-2:
    image: postgres:15
    container_name: postgres-db-2
    environment:
      POSTGRES_USER: user2
      POSTGRES_PASSWORD: password2
      POSTGRES_DB: database2
    ports:
      - "5434:5432"
    volumes:
      - postgres_data_2:/var/lib/postgresql/data

  postgres-db-3:
    image: postgres:15
    container_name: postgres-db-3
    environment:
      POSTGRES_USER: user3
      POSTGRES_PASSWORD: password3
      POSTGRES_DB: database3
    ports:
      - "5435:5432"
    volumes:
      - postgres_data_3:/var/lib/postgresql/data

  mysql-db:
    image: mysql:8.0
    container_name: mysql-db
    environment:
      MYSQL_ROOT_PASSWORD: root_password
      MYSQL_USER: mysql_user
      MYSQL_PASSWORD: mysql_password
      MYSQL_DATABASE: mysql_database
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql

  duckdb:
    image: mwirkk/duckdb:latest
    container_name: motherduck
    command: ["tail", "-f", "/dev/null"] # Keep the container running
    volumes:
      - duckdb_data:/duckdb
    ports:
      - "8000:8000" # Example port for future services if needed

volumes:
  postgres_data_1:
  postgres_data_2:
  postgres_data_3:
  mysql_data:
  duckdb_data:
```
