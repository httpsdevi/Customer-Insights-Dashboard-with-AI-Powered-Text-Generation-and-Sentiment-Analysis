from app import app

if __name__ == '__main__':
    print("Starting AI Text Analysis Dashboard...")
    print("Access the application at: http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
