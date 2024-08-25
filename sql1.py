import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('fitness_center.db')
cursor = conn.cursor()

# Create the Members table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Members (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
''')

# Create the WorkoutSessions table
cursor.execute('''
CREATE TABLE IF NOT EXISTS WorkoutSessions (
    session_id INTEGER PRIMARY KEY,
    member_id INTEGER,
    session_date DATE,
    session_time TEXT,
    activity TEXT,
    FOREIGN KEY (member_id) REFERENCES Members(id)
)
''')

# Commit the changes
conn.commit()

# Task 1: SQL Data Insertion with Existence Check
def insert_data():
    # Insert records into the Members table
    cursor.execute("SELECT COUNT(*) FROM Members WHERE id = 1")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO Members (id, name, age) VALUES (1, 'Jane Doe', 28)")

    cursor.execute("SELECT COUNT(*) FROM Members WHERE id = 2")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO Members (id, name, age) VALUES (2, 'John Smith', 35)")

    cursor.execute("SELECT COUNT(*) FROM Members WHERE id = 3")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO Members (id, name, age) VALUES (3, 'Alice Johnson', 22)")

    # Insert records into the WorkoutSessions table
    cursor.execute("SELECT COUNT(*) FROM WorkoutSessions WHERE session_id = 1")
    if cursor.fetchone()[0] == 0:
        cursor.execute('''INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity)
                          VALUES (1, 1, '2024-08-01', '07:00 AM', 'Yoga')''')

    cursor.execute("SELECT COUNT(*) FROM WorkoutSessions WHERE session_id = 2")
    if cursor.fetchone()[0] == 0:
        cursor.execute('''INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity)
                          VALUES (2, 2, '2024-08-02', '06:00 PM', 'Cardio')''')

    cursor.execute("SELECT COUNT(*) FROM WorkoutSessions WHERE session_id = 3")
    if cursor.fetchone()[0] == 0:
        cursor.execute('''INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity)
                          VALUES (3, 3, '2024-08-03', '08:00 AM', 'Weight Training')''')

    conn.commit()
    print("Data inserted successfully.")

# Task 2: SQL Data Update
def update_workout_session():
    # Update Jane Doe's workout session time from morning to evening
    cursor.execute('''
        UPDATE WorkoutSessions
        SET session_time = '06:00 PM'
        WHERE member_id = (SELECT id FROM Members WHERE name = 'Jane Doe')
    ''')

    conn.commit()
    print("Workout session updated successfully.")

# Task 3: SQL Data Deletion
def delete_member():
    # Delete John Smith's workout sessions
    cursor.execute('''
        DELETE FROM WorkoutSessions
        WHERE member_id = (SELECT id FROM Members WHERE name = 'John Smith')
    ''')

    # Delete John Smith's record from the Members table
    cursor.execute('''
        DELETE FROM Members
        WHERE name = 'John Smith'
    ''')

    conn.commit()
    print("Member and related workout sessions deleted successfully.")

# Running the tasks
insert_data()
update_workout_session()
delete_member()

# Close the connection
conn.close()
