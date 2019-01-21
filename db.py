import cx_Oracle

class DB():
    def __init__(self, name="",pas ="", link=""):
        self.name = "test"
        self.pas = "test123"

        self.link =  "localhost/xe"

        self.connect = cx_Oracle.connect(self.name, self.pas, self.link)
        self.cursor  = self.connect.cursor()

def dodajOglas(ime, link, cena, datum, stran_ime, stran_id, slika, iskalni_niz):
    #shraniVSez()
    connect = cx_Oracle.connect("test", "test123", "localhost/xe")
    cursor = connect.cursor()
    try:
        cursor.execute("""
                        INSERT INTO oglasi
                        (id, ime, link, cena,datum,stran_ime,stran_id, slika, iskalni_niz)
                        values
                        (oglas_id.nextval,:p_ime, :p_link, :cena, to_date(:datum,'YYYY-MM-DD hh24:mi:ss'), :stran_ime, :stran_id, :slika, :iskalni_niz)
                        """,p_ime = ime, p_link = link, cena = cena, datum = datum, stran_ime = stran_ime, stran_id = stran_id, slika = slika, iskalni_niz = iskalni_niz)
    except cx_Oracle.DatabaseError, exception:
        print("Napaka dodajOglas")
        print(exception)
    cursor.close()
    connect.commit()
