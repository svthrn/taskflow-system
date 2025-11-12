from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    print("Starting TaskFlow server on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0')
