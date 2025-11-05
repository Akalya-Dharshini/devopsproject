from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Database configuration
db = mysql.connector.connect(
    host="localhost",      # your MySQL host
    user="root",           # your MySQL username
    password="yourpassword",  # your MySQL password
    database="devops_project"
)
cursor = db.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    message TEXT
)
""")
db.commit()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    cursor.execute("INSERT INTO feedback (name, email, message) VALUES (%s, %s, %s)", (name, email, message))
    db.commit()
    return jsonify({"status": "success", "message": "Thank you for your feedback!"})

@app.route('/get_feedback', methods=['GET'])
def get_feedback():
    cursor.execute("SELECT name, message FROM feedback ORDER BY id DESC")
    results = cursor.fetchall()
    feedback_list = [{"name": r[0], "message": r[1]} for r in results]
    return jsonify(feedback_list)

if __name__ == '__main__':
    app.run(debug=True)
