import sys
sys.path.insert(0, 'c:/Users/mu451/OneDrive/Desktop/agro_system')
from app import app
from models.db import get_db

with app.app_context():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT COUNT(*) as count FROM crop_rates WHERE is_active = 1')
    result = cursor.fetchone()
    print(f'Active rates in database: {result["count"]}')
    
    cursor.execute('SELECT id, crop_name, rate_per_kg_pkr FROM crop_rates WHERE is_active = 1 LIMIT 5')
    rates = cursor.fetchall()
    print('\nFirst 5 rates:')
    for rate in rates:
        print(f'  ID: {rate["id"]}, Crop: {rate["crop_name"]}, Rate: {rate["rate_per_kg_pkr"]}')
