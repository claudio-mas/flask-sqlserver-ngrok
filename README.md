# Flask + SQL Server + ngrok

A simple web dashboard to expose data from a **local SQL Server** database using **Flask** and **ngrok**.

Perfect for internal reports, demos, or secure data sharing — without exposing your database.

---

## 🚀 How to Run

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
    ```
2. **Update database credentials in app.py**
    ```python
    SERVER=your_server
    DATABASE=your_DB
    UID=your_user
    PWD=your_password
    ```
3. **Run the Flask app**
   ```bash
   python app.py
    ```
4. **Start ngrok tunnel**
   ```bash
   ngrok http --domain=yourapp.ngrok.io 5000
    ```
5. **Access your dashboard**
   Open: https://yourapp.ngrok.io
   🔗 Get a free fixed domain at ngrok.com 

🛠️ Requirements
Python 3.8+
SQL Server (local)
ngrok account with reserved domain
ODBC Driver 17 for SQL Server

🌍 Article (Medium)
Read the full story:
👉 How to Expose a Local SQL Server Database Online Using Flask and ngrok

🇧🇷 Versão em Português
Veja o artigo em português:
👉 Como Expor um Banco de Dados SQL Server Local na Internet