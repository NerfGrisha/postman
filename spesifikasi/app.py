from flask import Flask, jsonify, request
from flask import Flask, jsonify, request, render_template
import mysql.connector

app = Flask(__name__)


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="spesifikasi" 
)


cursor = mydb.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS spesifikasi (
        spesifikasi_id INT AUTO_INCREMENT PRIMARY KEY,
        laptop_id INT,
        processor VARCHAR(255),
        RAM VARCHAR(255),
        penyimpanan VARCHAR(255)
    )
""")
mydb.commit()

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def add():
    laptop_id = request.form['laptop_id']
    processor = request.form['processor']
    RAM = request.form['RAM']
    penyimpanan = request.form['penyimpanan']

    sql = "INSERT INTO spesifikasi (laptop_id, processor, RAM, penyimpanan) VALUES (%s, %s, %s, %s)"
    sql_insert = (laptop_id, processor, RAM, penyimpanan)

    cursor.execute(sql, sql_insert)
    mydb.commit()

    respond = jsonify('Data Berhasil Tersimpan!') if cursor.rowcount == 1 else jsonify('Data Gagal Tersimpan!')
    respond.status_code = 200 if cursor.rowcount == 1 else 500

    return respond

@app.route('/edit', methods=['PUT'])
def edit():
    spesifikasi_id = request.args.get("spesifikasi_id")
    laptop_id = request.args.get('laptop_id')
    processor = request.args.get('processor')
    RAM = request.args.get('RAM')
    penyimpanan = request.args.get('penyimpanan')

    sql = "UPDATE spesifikasi SET laptop_id = %s, processor = %s, RAM = %s, penyimpanan = %s WHERE spesifikasi_id = %s"
    sql_insert = (laptop_id, processor, RAM, penyimpanan, spesifikasi_id)

    cursor.execute(sql, sql_insert)
    mydb.commit()

    respond = jsonify('Data Berhasil Diubah!') if cursor.rowcount == 1 else jsonify('Data Gagal Diubah!')
    respond.status_code = 200 if cursor.rowcount == 1 else 500

    return respond

@app.route('/delete', methods=['DELETE'])
def delete():
    spesifikasi_id = request.args.get('spesifikasi_id')

    sql = "DELETE FROM spesifikasi WHERE spesifikasi_id = %s"
    cursor.execute(sql, (spesifikasi_id,))
    mydb.commit()

    respond = jsonify('Data Berhasil Dihapus!') if cursor.rowcount else jsonify('Data Gagal Dihapus!')
    respond.status_code = 200 if cursor.rowcount else 500

    return respond

@app.route('/showdata', methods=['GET'])
def showdata():
    spesifikasi_id = request.args.get('spesifikasi_id')

    sql = "SELECT * FROM spesifikasi WHERE spesifikasi_id = %s"
    cursor.execute(sql, (spesifikasi_id,))

    spesifikasi_data = cursor.fetchone()
    respond = jsonify(spesifikasi_data) if spesifikasi_data else jsonify('Data tidak ditemukan!')
    respond.status_code = 200 if spesifikasi_data else 404

    return respond

if __name__ == "__main__":
    app.run(port=8080)
