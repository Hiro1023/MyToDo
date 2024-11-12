from app import app

print("Starting Flask app...")  # デバッグメッセージ

if __name__ == "__main__":
    #from app import routes
    app.run(host="0.0.0.0", debug=True)
    print("Flask app is running")  # サーバーが起動したことを確認
