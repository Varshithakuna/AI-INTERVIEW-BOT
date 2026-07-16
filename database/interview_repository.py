import json

from database.db import get_connection


def save_interview(report, candidate):
    """
    Save an interview evaluation into PostgreSQL.
    """

    conn = None
    cursor = None

    try:

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO interviews (

                candidate_name,
                role,
                experience,
                interview_type,
                difficulty,
                resume_text,
                overall_score,
                technical_score,
                communication_score,
                problem_solving_score,
                confidence_score,
                strengths,
                weaknesses,
                suggestions,
                recommendation

            )

            VALUES (

                %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s

            )
            """,

            (

                candidate.name,
                candidate.role,
                candidate.experience,
                candidate.interview_type,
                candidate.difficulty,
                candidate.resume_text,

                report["overall_score"],
                report["technical_score"],
                report["communication_score"],
                report["problem_solving_score"],
                report["confidence_score"],

                json.dumps(report["strengths"]),
                json.dumps(report["weaknesses"]),
                json.dumps(report["suggestions"]),

                report["recommendation"]

            )

        )

        conn.commit()

        print("✅ Interview saved successfully!")

    except Exception as e:

        if conn:
            conn.rollback()

        print("❌ Failed to save interview")
        print(e)

        raise

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()