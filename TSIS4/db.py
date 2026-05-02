import psycopg2
from config import DB_CONFIG


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def run_schema():
    conn = get_connection()
    cur = conn.cursor()

    with open("schema.sql", "r", encoding="utf-8") as file:
        cur.execute(file.read())

    conn.commit()
    cur.close()
    conn.close()


def get_or_create_user(username):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM players WHERE username = %s;", (username,))
    user = cur.fetchone()

    if user:
        cur.close()
        conn.close()
        return user[0]

    cur.execute(
        "INSERT INTO players(username) VALUES(%s) RETURNING id;",
        (username,)
    )

    user_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return user_id


def save_score(username, score, level):
    user_id = get_or_create_user(username)

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO game_sessions(player_id, score, level_reached)
        VALUES(%s, %s, %s);
        """,
        (user_id, score, level)
    )

    conn.commit()
    cur.close()
    conn.close()


def get_top_scores():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT p.username, g.score, g.level_reached, g.played_at
        FROM game_sessions g
        JOIN players p ON g.player_id = p.id
        ORDER BY g.score DESC
        LIMIT 10;
    """)

    result = cur.fetchall()

    cur.close()
    conn.close()

    return result


def get_personal_best(username):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT MAX(g.score)
        FROM game_sessions g
        JOIN players p ON g.player_id = p.id
        WHERE p.username = %s;
    """, (username,))

    best = cur.fetchone()[0]

    cur.close()
    conn.close()

    return best if best is not None else 0