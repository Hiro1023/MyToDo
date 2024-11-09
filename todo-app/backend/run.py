from app import app

print("Starting Flask app...")  # デバッグメッセージ

if __name__ == "__main__":
    app.run(debug=True)
    print("Flask app is running")  # サーバーが起動したことを確認
