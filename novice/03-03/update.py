try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="fitraqorina25")
    
    curs = conn.cursor()

    namaLama = "anggi"

    namaBaru= "angga"
    umurBaru= 24
    query = f"update siswa set nama= '{namaBaru}', umur={umurBaru} where nama='{namaLama}'"
   
    curs.execute(query)
    conn.commit()
    print("data berhasil diupdate")
except Exception as e:
    print(e)


