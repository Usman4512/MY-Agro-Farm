import sys
sys.path.insert(0, 'c:/Users/mu451/OneDrive/Desktop/agro_system')
from app import app
from models.db import get_db
from werkzeug.security import generate_password_hash

with app.app_context():
    db = get_db()
    cursor = db.cursor()
    new_hash = generate_password_hash('admin123', method='scrypt')
    cursor.execute('UPDATE users SET password_hash = %s WHERE id = 1', (new_hash,))
    db.commit()
    print('Admin password updated successfully')
