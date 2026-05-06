"""
Database module for the Anonymous Suggestions System.

This module handles all interactions with the SQLite database, including:
- Creating the suggestions table
- Inserting new suggestions
- Retrieving suggestions (all and filtered)
- Updating suggestion statuses

Separating database logic improves maintainability and supports scalability.
"""

import sqlite3
from services import calculate_priority

# Name of the SQLite database file
DB_NAME = "suggestions.db"


def get_connection():
    """
    Creates and returns a connection to the SQLite database.

    Returns:
        sqlite3.Connection: Database connection object
    """
    return sqlite3.connect(DB_NAME)


def create_table():
    """
    Creates the 'suggestions' table if it does not already exist.

    The table stores:
    - Unique ID for each suggestion
    - Suggestion text
    - Category and urgency
    - Current status
    - Calculated priority score
    """
    conn = get_connection()
    cursor = conn.cursor()

    # SQL command to create table structure
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
    """
    Inserts a new suggestion into the database.

    Automatically calculates a priority score before insertion.

    Parameters:
        text (str): Suggestion content
        category (str): Selected category
        urgency (str): Selected urgency level
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Calculate priority score based on urgency and category
    priority = calculate_priority(urgency, category)

    # Insert new suggestion with default status "New"
    cursor.execute("""
        INSERT INTO suggestions (text, category, urgency, status, priority)
        VALUES (?, ?, ?, ?, ?)
    """, (text, category, urgency, "New", priority))

    conn.commit()
    conn.close()


def get_all_suggestions():
    """
    Retrieves all suggestions from the database.

    Suggestions are sorted by priority (highest first).

    Returns:
        list of tuples: Each tuple represents a suggestion record
    """
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
    """
    Retrieves only suggestions with status 'New'.

    This allows users to focus on unreviewed suggestions.
    Results are sorted by priority.

    Returns:
        list of tuples: Filtered suggestion records
    """
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
    """
    Updates the status of a specific suggestion.

    Parameters:
        suggestion_id (int): ID of the suggestion to update
        new_status (str): New status value (e.g. "Accepted", "Rejected")
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Update status field for the selected suggestion
    cursor.execute("""
        UPDATE suggestions
        SET status = ?
        WHERE id = ?
    """, (new_status, suggestion_id))

    conn.commit()
    conn.close()