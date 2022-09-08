from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = psycopg2.connect(
        host="localhost",
        database="tugas",
        user="postgres",
        password="fitraqorina25"
    )
    curs = conn.cursor()
    if request.method == "POST":
        tanggal = request.form.get("tanggal")
        tempat = request.form.get("tempat")
        masuk = request.form.get("masuk")
        keluar = request.form.get("keluar")
        query = f"insert into uangkas(tanggal, tempat, masuk, keluar) values('{tanggal}', '{tempat}', '{masuk}', '{keluar}')"
        curs.execute(query)
        conn.commit()

    print(request.method)
    query = f"select * from uangkas"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    return render_template("index.html", context=data)

# @app.route("/masuk/<uangkas_id>")
# def masuk(uangkas_id):
#     conn = psycopg2.connect(
#         host="localhost",
#         database="tugas",
#         user="postgres",
#         password="fitraqorina25"
#     )
#     curs = conn.cursor()
#     query = f"select * from uangkas where id = {uangkas_id}"
#     curs.execute(query)
#     data = curs.fetchone()
#     curs.close()
#     conn.close()
#     print(data)
#     return render_template("masuk.html", context=data)

# @app.route("/keluar/<uangkas_id>")
# def keluar(uangkas_id):
#     conn = psycopg2.connect(
#         host="localhost",
#         database="tugas",
#         user="postgres",
#         password="fitraqorina25"
#         )
#     curs = conn.cursor()
#     # if request.method =="POST"
#     #       tanggal = request.form.get("tanggal")
#     #       tempat.request.form.get("tempat")
#     query = f"keluar from uangkas where id = {uangkas_id}"
#     curs.execute(query)
#     conn.commit()
#     curs.close()
#     conn.close()
#     return redirect("/")

if __name__ == "__main__":
    app.run()      