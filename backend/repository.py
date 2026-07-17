from backend.database import get_connection


def save(table, column, value):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        f"INSERT OR IGNORE INTO {table}({column}) VALUES(?)",
        (value,)
    )

    conn.commit()
    conn.close()


def get_all(table, column):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        f"SELECT {column} FROM {table}"
    )

    rows = cursor.fetchall()

    conn.close()

    return [row[0] for row in rows]


def save_key_value(table, key, value):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"""
        INSERT INTO {table}(key,value)
        VALUES(?,?)
        ON CONFLICT(key)
        DO UPDATE SET value=excluded.value
    """, (key, value))

    conn.commit()
    conn.close()


def get_value(table, key):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        f"SELECT value FROM {table} WHERE key=?",
        (key,)
    )

    row = cursor.fetchone()

    conn.close()

    return row[0] if row else None