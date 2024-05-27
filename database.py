import sqlite3

connection = sqlite3.connect('car.database')
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cars 
    (
        id INTEGER PRIMARY KEY,
        uid TEXT,
        make TEXT,
        model TEXT,
        price INTEGER,
        mileage INTEGER,
        link TEXT,
        photo_link TEXT
    );
    """)


def insert_car(car):
    q = ('INSERT INTO cars (uid,make,model,price,mileage,link,photo_link)'
         'VALUES (?,?,?,?,?,?,?)')

    cursor.execute(q, [car.uid, car.make, car.model, car.price, car.mileage, car.link, car.photo])
    connection.commit()


def check_car_exists(car):
    q = 'SELECT * FROM cars WHERE uid=?'
    data = cursor.execute(q, [car.uid]).fetchone()
    if data:
        return True
    else:
        return False
