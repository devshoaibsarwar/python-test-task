import psycopg2

db_params = {
    "database": "python_test_task",
    "user": "postgres",
    "password": "password",
    "host": "localhost",
}

def create_connection():
    try:
        conn = psycopg2.connect(**db_params)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)
        return None

def execute_query(query, parameters=None, query_type=""):
    conn = create_connection()

    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(query, parameters)

            result = None
            if query_type == "fetchall":
                result = cursor.fetchall()
            elif query_type == "fetchone":
                result = cursor.fetchone()

            conn.commit()
            cursor.close()
            conn.close()

            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error:", error)
            return None
    else:
        return None

def check_configuration_table_exists():
    result = execute_query("""
        SELECT EXISTS (
            SELECT 1
            FROM information_schema.tables
            WHERE table_name = 'configuration_table'
        )
    """, {}, "fetchone")

    if result is None:
        return False

    return result[0]

def create_configuration_table():
    table_exists = check_configuration_table_exists()

    if not table_exists:
        result =  execute_query("""
            CREATE TABLE configuration_table (
                status VARCHAR(255) NOT NULL,
                action_type VARCHAR(255) NOT NULL,
                action VARCHAR(255) NOT NULL,
                order_number INT UNIQUE NOT NULL,
                CONSTRAINT unique_combination UNIQUE (status, action_type, action)
            );
        """)

        print(result)