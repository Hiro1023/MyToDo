from app import app

print("Starting Flask app...")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    print("Flask app is running")
