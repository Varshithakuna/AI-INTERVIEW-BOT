from database.db import get_connection


try:
    conn = get_connection()

    print("✅ Connected to Neon PostgreSQL successfully!")

    conn.close()

except Exception as e:

    print("❌ Connection Failed")
    print(e)