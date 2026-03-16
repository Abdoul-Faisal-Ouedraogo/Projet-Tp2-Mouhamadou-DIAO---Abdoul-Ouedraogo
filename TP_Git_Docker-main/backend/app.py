import os
import psycopg2
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Permet au frontend de communiquer avec le back

# Configuration BDD via variables d'environnement
def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD']
    )
    return conn

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, content FROM tasks;')
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{'id': t[0], 'content': t[1]} for t in tasks])

@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.json['content']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO tasks (content) VALUES (%s) RETURNING id;', (new_task,))
    task_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'id': task_id, 'content': new_task}), 201

if __name__ == '__main__':
    # Le port 5000 est standard pour Flask
    app.run(host='0.0.0.0', port=5000)