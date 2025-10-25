import sqlite3

# Este módulo gestiona todas las operaciones de la base de datos (creación, inserción, consulta).
def create_connection():
    conn = sqlite3.connect('test_manager.db')
    return conn

# Crea y devuelve una conexión a la base de datos SQLite.
def create_tables(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS test_cases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id INTEGER,
                name TEXT NOT NULL,
                description TEXT,
                steps TEXT,
                expected_result TEXT,
                priority TEXT,
                status TEXT,
                execution_result TEXT,
                FOREIGN KEY (project_id) REFERENCES projects (id)
            );
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Crea un nuevo proyecto en la base de datos.
def create_project(conn, name):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO projects (name) VALUES (?)", (name,))
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(e)
        return None

# Obtiene todos los proyectos de la base de datos.
def get_projects(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM projects")
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(e)
        return []

# Crea un nuevo caso de prueba en la base de datos.
def create_test_case(conn, test_case_data):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO test_cases (project_id, name, description, steps, expected_result, priority, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (test_case_data[0], test_case_data[1], test_case_data[2], test_case_data[3], test_case_data[4], test_case_data[5], "Pendiente"))
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(e)
        return None

# Obtiene todos los casos de prueba para un proyecto específico.
def get_test_cases_by_project(conn, project_id):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, priority, status, execution_result FROM test_cases WHERE project_id = ?", (project_id,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(e)
        return []

# Actualiza el resultado de la ejecución de un caso de prueba.
def update_test_case_result(conn, test_case_id, result):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE test_cases SET execution_result = ? WHERE id = ?", (result, test_case_id))
        conn.commit()
    except sqlite3.Error as e:
        print(e)