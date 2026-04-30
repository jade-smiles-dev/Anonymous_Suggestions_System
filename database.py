import sqlite3
from services import calculate_priority

DB_NAME = "suggestions.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS suggestions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            category TEXT NOT NULL,
            urgency TEXT NOT NULL,
            status TEXT NOT NULL,
            priority INTEGER
        )
    """)

    conn.commit()
    conn.close()


def add_suggestion(text, category, urgency):
    conn = get_connection()
    cursor = conn.cursor()

    priority = calculate_priority(urgency, category)

    cursor.execute("""
        INSERT INTO suggestions (text, category, urgency, status, priority)
        VALUES (?, ?, ?, ?, ?)
    """, (text, category, urgency, "New", priority))

    conn.commit()
    conn.close()


def get_all_suggestions():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, text, category, urgency, status, priority
        FROM suggestions
        ORDER BY priority DESC
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows


def get_new_suggestions():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, text, category, urgency, status, priority
        FROM suggestions
        WHERE status = 'New'
        ORDER BY priority DESC
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows


def update_suggestion_status(suggestion_id, new_status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE suggestions
        SET status = ?
        WHERE id = ?
    """, (new_status, suggestion_id))

    conn.commit()
    conn.close()