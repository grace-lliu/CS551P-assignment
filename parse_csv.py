import csv
import sqlite3
from faker import Faker

fake = Faker()

# open the connection to the database
conn = sqlite3.connect('app_store.db')
cur = conn.cursor()

conn.execute('DROP TABLE IF EXISTS app_store')
# create app_store table
cur.execute("""
    CREATE TABLE app_store (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        app_id INTEGER,
        track_name TEXT,
        size_bytes INTEGER,
        currency TEXT,
        price REAL,
        rating_count_tot INTEGER,
        rating_count_ver INTEGER,
        user_rating REAL,
        user_rating_ver REAL,
        ver TEXT,
        cont_rating TEXT,
        prime_genre TEXT,
        sup_devices_num INTEGER,
        ipadSc_urls_num INTEGER,
        lang_num INTEGER,
        vpp_lic INTEGER
    );
""")
print("table app_store created successfully");

conn.execute('DROP TABLE IF EXISTS app_store_desc')

# create app_store_desc table
cur.execute("""
    CREATE TABLE app_store_desc (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        app_id INTEGER,
        app_desc TEXT
    );
""")
print("table app_store_desc created successfully");

with open('app_store/AppleStore.csv', newline='', encoding='gbk') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    count = 0
    for row in reader:
        if count >= 3500:
            break

        try:
            app_id = row[1]
        except ValueError:
            app_id = 0
        try:
            track_name = fake.name()
        except ValueError:
            track_name = ""
        try:
            size_bytes = int(row[2])
        except ValueError:
            size_bytes = 0
        try:
            currency = row[3]
        except ValueError:
            currency = ""
        try:
            price = float(row[4])
        except ValueError:
            price = 0
        try:
            rating_count_tot = int(row[5])
        except ValueError:
            rating_count_tot = 0
        try:
            rating_count_ver = int(row[6])
        except ValueError:
            rating_count_ver = 0
        try:
            user_rating = float(row[7])
        except ValueError:
            user_rating = 0
        try:
            user_rating_ver = float(row[8])
        except ValueError:
            user_rating_ver = 0
        try:
            ver = row[9]
        except ValueError:
            ver = ""
        try:
            cont_rating = row[10]
        except ValueError:
            cont_rating = ""
        try:
            prime_genre = row[11]
        except ValueError:
            prime_genre = ""
        try:
            sup_devices_num = int(row[12])
        except ValueError:
            sup_devices_num = 0
        try:
            ipadSc_urls_num = int(row[13])
        except ValueError:
            ipadSc_urls_num = 0
        try:
            lang_num = int(row[14])
        except ValueError:
            lang_num = 0
        try:
            vpp_lic = int(row[15])
        except ValueError:
            vpp_lic = 0
            
        cur.execute('INSERT INTO app_store (app_id,track_name, size_bytes, currency, price, rating_count_tot, rating_count_ver, user_rating, user_rating_ver, ver, cont_rating, prime_genre, sup_devices_num, ipadSc_urls_num, lang_num, vpp_lic) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (app_id,track_name, size_bytes, currency, price, rating_count_tot, rating_count_ver, user_rating, user_rating_ver, ver, cont_rating, prime_genre, sup_devices_num, ipadSc_urls_num, lang_num, vpp_lic))
        conn.commit()
        count += 1

print("data app_store parsed successfully")

with open('app_store/AppleStore.csv', newline='') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row
    count = 0
    for row in reader:
        if count >= 3500:
            break
        try:
            app_id = int(row[1])
        except ValueError:
            app_id = 0
        
        app_desc = fake.text()
        
        cur.execute('INSERT INTO app_store_desc (app_id, app_desc) VALUES (?, ?)', (app_id, app_desc))
        conn.commit()
        count += 1

print("data app_store_desc parsed successfully")

conn.close()