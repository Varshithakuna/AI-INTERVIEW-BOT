from database.db import get_connection


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    # ==========================================
    # Interviews Table
    # ==========================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interviews (

        id SERIAL PRIMARY KEY,

        candidate_name VARCHAR(100) NOT NULL,

        role VARCHAR(100) NOT NULL,

        experience VARCHAR(50),

        interview_type VARCHAR(50),

        difficulty VARCHAR(50),

        resume_text TEXT,

        overall_score INTEGER,

        technical_score INTEGER,

        communication_score INTEGER,

        problem_solving_score INTEGER,

        confidence_score INTEGER,

        strengths TEXT,

        weaknesses TEXT,

        suggestions TEXT,

        recommendation TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    );
    """)

    conn.commit()

    cursor.close()
    conn.close()

    print("✅ Interviews table created successfully!")


if __name__ == "__main__":
    create_tables()