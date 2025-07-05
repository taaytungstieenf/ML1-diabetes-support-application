import mysql.connector
from datetime import datetime
from .database_config import DB_CONFIG


def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)


def execute_query(query, params=None, fetch=False):
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params or ())
            if fetch:
                return cursor.fetchall()
            conn.commit()
            return cursor.lastrowid if query.strip().lower().startswith("insert") else None


def init_db():
    create_tables = [
        '''
        CREATE TABLE IF NOT EXISTS patients (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            dob DATE
        )
        ''',
        '''
        CREATE TABLE IF NOT EXISTS predictions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            patient_id INT,
            gender INT,
            age FLOAT,
            hypertension INT,
            heart_disease INT,
            smoking_history INT,
            bmi FLOAT,
            HbA1c_level FLOAT,
            blood_glucose_level FLOAT,
            prediction INT,
            timestamp DATETIME,
            FOREIGN KEY (patient_id) REFERENCES patients(id)
        )
        '''
    ]
    for query in create_tables:
        execute_query(query)


def get_or_create_patient(name, dob):
    select_query = "SELECT id FROM patients WHERE name = %s AND dob = %s"
    result = execute_query(select_query, (name, dob), fetch=True)
    if result:
        return result[0][0]

    insert_query = "INSERT INTO patients (name, dob) VALUES (%s, %s)"
    return execute_query(insert_query, (name, dob))


def save_prediction(data: dict, prediction: int):
    patient_id = get_or_create_patient(data["name"], data["dob"])
    insert_query = '''
        INSERT INTO predictions (
            patient_id, gender, age, hypertension, heart_disease,
            smoking_history, bmi, HbA1c_level, blood_glucose_level,
            prediction, timestamp
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    params = (
        patient_id, data["gender"], data["age"], data["hypertension"],
        data["heart_disease"], data["smoking_history"], data["bmi"],
        data["HbA1c_level"], data["blood_glucose_level"],
        prediction, datetime.now()
    )
    execute_query(insert_query, params)


def get_predictions_from_db():
    query = '''
        SELECT p.id, pt.name, pt.dob, p.age, p.gender, p.bmi, p.blood_glucose_level,
               p.HbA1c_level, p.prediction, p.timestamp
        FROM predictions p
        JOIN patients pt ON p.patient_id = pt.id
        ORDER BY p.timestamp DESC
        LIMIT 4
    '''
    return execute_query(query, fetch=True)


def delete_all_predictions():
    execute_query("DELETE FROM predictions")
    execute_query("DELETE FROM patients")

init_db()