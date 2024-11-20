from dotenv import load_dotenv
import os
import psycopg2
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Environment variables for database connection
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")


# Establish a connection to the PostgreSQL database
def connect_to_db():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )

# Write the current time to the database
def log_time():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        # Create table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS time_log (
                id SERIAL PRIMARY KEY,
                timestamp TIMESTAMP NOT NULL
            );
        """)
        conn.commit()

        # Insert the current time
        now = datetime.now()
        cursor.execute("INSERT INTO time_log (timestamp) VALUES (%s)", (now,))
        conn.commit()
        print(f"Time logged: {now}")

        # Close the connection
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    log_time()
