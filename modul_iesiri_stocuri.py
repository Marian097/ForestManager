from baza_de_date_prodfor import Conexiune_bd, conexiune_bd
import sqlite3


class IesiriLemnPePicior:
    def __init__(self, conexiune_bd : Conexiune_bd):
        self.conexiune_bd=conexiune_bd
        return
    
    def adauga_nir(self, Cod_aviz, data, Provenienta, Specie, Subsortiment, Volum_mc ):
        self.conexiune_bd.cursor.execute("SELECT Numar_partida FROM tabel_parchet_in_lucru WHERE Numar_partida=?", (Provenienta, ))
        numar_partida=self.conexiune_bd.cursor.fetchall()
        self.conexiune_bd.cursor.execute("SELECT Volum FROM tabel_parchet_in_lucru WHERE Numar_partida=? AND Sortiment=? AND Subsortiment=?", (Provenienta, Specie, Subsortiment))
        volum=self.conexiune_bd.cursor.fetchone()
        volum_actualizat=volum[0]-Volum_mc
        lista_criterii=[numar_partida[0], volum[0], Provenienta, Specie, Subsortiment]
        valabilitate=False
        for detalii in lista_criterii:
            if detalii is not None:
                valabilitate=True
                break
        if valabilitate and Volum_mc <= volum[0]:
            self.conexiune_bd.cursor.execute("INSERT INTO tabel_nir (Cod_aviz, Data, Provenienta, Specie, Sortiment, Volum_mc) VALUES (?, ?, ?, ?, ?, ?)", (Cod_aviz, data, Provenienta, Specie, Subsortiment, Volum_mc))
            self.conexiune_bd.cursor.execute("UPDATE tabel_parchet_in_lucru SET Volum=? WHERE Numar_partida=? AND Sortiment=? AND Subsortiment=?", (volum_actualizat, Provenienta, Specie, Subsortiment))
            self.conexiune_bd.conexiune.commit()
            print("NIR adaugat.")
        else:
            print("Stoc epuizat")
            
    def sterge_nir(self, cod_aviz, Provenienta, Specie, Subsortiment):
        self.conexiune_bd.cursor.execute("SELECT Volum_mc FROM tabel_nir WHERE Cod_Aviz=? AND Provenienta=? AND Specie=? AND Sortiment=?", (cod_aviz, Provenienta, Specie, Subsortiment))
        volum_de_sters=self.conexiune_bd.cursor.fetchone()
        self.conexiune_bd.cursor.execute("SELECT Volum FROM tabel_parchet_in_lucru WHERE Numar_partida=? AND Sortiment=? AND Subsortiment=?", (Provenienta, Specie, Subsortiment))
        volum=self.conexiune_bd.cursor.fetchone()
        volum_actualizat=volum[0]+volum_de_sters[0]
        lista_criterii=[volum_de_sters[0], volum[0]]
        if lista_criterii is not None:
            self.conexiune_bd.cursor.execute("DELETE FROM tabel_nir WHERE Cod_Aviz=? AND Provenienta=? AND Specie=? AND Sortiment=?", (cod_aviz, Provenienta, Specie, Subsortiment))
            self.conexiune_bd.cursor.execute("UPDATE tabel_parchet_in_lucru SET Volum=? WHERE Numar_partida=? AND Sortiment=? AND Subsortiment=?", (volum_actualizat, Provenienta, Specie, Subsortiment))
            self.conexiune_bd.conexiune.commit()
            print("NIR sters.")
        else:
            print("Operatiune esuata.")
            
            
    def afiseaza_stoc_ramas(self, provenienta):
        self.conexiune_bd.cursor.execute("SELECT * FROM tabel_parchet_in_lucru WHERE Numar_partida=?", (provenienta, ))
        afiseaza_partida=self.conexiune_bd.cursor.fetchall()
        print("Stocuri ramase: ")
        for detalii in afiseaza_partida:
            if detalii is not None:
                print(detalii)
            else:
                print("Partida inexistenta")

    
    def afiseaza_stoc_initial(self, numar_partida):
        self.conexiune_bd.cursor.execute("SELECT Numar_partida, Volum_total FROM tabel_autorizatii WHERE Numar_partida=?", (numar_partida, ))
        stoc_initial=self.conexiune_bd.cursor.fetchall()
        print("Stoc initial: ")
        for informatii in stoc_initial:
            print(informatii)
            
            
            
                
                
                
iesiri=IesiriLemnPePicior(conexiune_bd)

