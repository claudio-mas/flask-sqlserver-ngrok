# app.py
from flask import Flask
import pyodbc

app = Flask(__name__)

# === CONFIGURE YOUR CREDENTIALS HERE ===
DATABASE = "your_DB"
TABLE = "your_table"
DB_USER = "your_user"
DB_PASSWORD = "your_password"

def get_db_connection():
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        f"DATABASE={DATABASE};"
        f"UID={DB_USER};"
        f"PWD={DB_PASSWORD};"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )
    return pyodbc.connect(conn_str)

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT TOP 50 * FROM {TABLE}")
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        conn.close()

        # Create HTML table
        html = """
        <html>
            <head>
                <title>SQL Server Dashboard</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 40px; }
                    table { border-collapse: collapse; width: 100%; }
                    th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
                    th { background-color: #f2f2f2; }
                    h1 { color: #333; }
                </style>
            </head>
            <body>
                <h1>📊 SQL Server Data</h1>
                <table>
                    <thead>
                        <tr>
        """
        for col in columns:
            html += f"<th>{col}</th>"
        html += "</tr></thead><tbody>"

        for row in rows:
            html += "<tr>"
            for cell in row:
                html += f"<td>{cell}</td>"
            html += "</tr>"

        html += """
                </tbody></table>
            </body>
        </html>
        """
        return html

    except Exception as e:
        return f"""
        <h1 style="color:red">❌ Error connecting to the DB</h1>
        <p><strong>{str(e)}</strong></p>
        <p>Check: credentials, SQL Server running, ngrok started.</p>
        """

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
