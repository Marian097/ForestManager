from baza_de_date_prodfor import Conexiune_bd, conexiune_bd

class AchizitiiLemnFasonat:
    def __init__(self, conexiune_bd : Conexiune_bd):
        self.conexiune_bd=conexiune_bd
        return
    
    def adauga_achizitie(self, ID, ocol_silvic, contract, sortiment, subsortiment, volum, pret_achizitie, cont_bancar):
        self.conexiune_bd.connect_baza_de_date()
        valoare_totala=pret_achizitie * volum
        if len(cont_bancar) == 24:
            self.conexiune_bd.cursor.execute("INSERT INTO tabel_achizitii_lemn_fasonat (ID, Nume_Ocol_silvic, Contract, Sortiment, Subsortiment, Volum, Pret_achizitie, Valoare_totala, Cont_bancar) VALUES (?,?,?,?,?,?,?,?,?)", (ID, ocol_silvic, contract, sortiment, subsortiment, volum, pret_achizitie, valoare_totala, cont_bancar, ))
            self.conexiune_bd.conexiune.commit()
            print("Adaugare cu succes.")
        else:
            print("Contul bancar trebuie sa contina 24 de caractere.")
        self.conexiune_bd.disconnect_baza_de_date()
        
    def sterge_achizitie(self, ID, ocol_silvic):
        self.conexiune_bd.connect_baza_de_date()
        self.conexiune_bd.cursor.execute("SELECT Nume_Ocol_silvic FROM tabel_achizitii_lemn_fasonat WHERE ID=?", (ID, ))
        ocol=self.conexiune_bd.cursor.fetchall()
        try:
            if ocol[0] is not None:
                self.conexiune_bd.cursor.execute("DELETE FROM tabel_achizitii_lemn_fasonat WHERE ID=?", (ID, ))
                self.conexiune_bd.conexiune.commit()
                print("Operatiune reusita.")
            else:
                print("Operatiune esuata.")
        
        except IndexError as e:
            print(f"Parametrii gresiti: {e}")
        self.conexiune_bd.disconnect_baza_de_date()
                
    
    def actualizeaza_informatii(self, id, ocol_silvic, contract, sortiment, subsortiment, volum, pret_achizitie, cont_bancar):
        self.conexiune_bd.connect_baza_de_date()
        self.conexiune_bd.cursor.execute("SELECT Nume_Ocol_silvic FROM tabel_achizitii_lemn_fasonat")
        ocol_silvic=self.conexiune_bd.cursor.fetchall()
        valoare_totala=pret_achizitie * volum
        try:
            if ocol_silvic[0] == ocol_silvic:
                self.conexiune_bd.cursor.execute("UPDATE tabel_achizitii_lemn_fasonat SET Contract=?, Sortiment=?, Subsortiment=?, Volum=?, Pret_achizitie=?, Valoare_totala=?, Cont_bancar=? WHERE ID=? ", (contract, sortiment, subsortiment, volum, pret_achizitie, valoare_totala, cont_bancar, id, ))
                self.conexiune_bd.conexiune.commit()
                print("Actualizare reusita.")
            else:
                print("Operatiune esuata.")
        except IndexError as e:
            print(f"Informatii gresite: {e} ")
        self.conexiune_bd.disconnect_baza_de_date()
                
                
class IesiriLemnFasonat:
    def __init__(self, conexiune_bd : Conexiune_bd):
        self.conexiune_bd=conexiune_bd
        return
    
    def adauga_nir(self, ID, ocol_silvic, cod_aviz, data,  sortiment, subsortiment, volum_aviz):
        self.conexiune_bd.connect_baza_de_date()
        self.conexiune_bd.cursor.execute("SELECT Volum FROM tabel_achizitii_lemn_fasonat WHERE Nume_Ocol_silvic=? AND Sortiment=? AND Subsortiment=? ", (ocol_silvic, sortiment, subsortiment, ))
        volum_initial=self.conexiune_bd.cursor.fetchone()
        self.conexiune_bd.cursor.execute("SELECT Pret_achizitie, Valoare_totala FROM tabel_achizitii_lemn_fasonat WHERE ID=?", (ID, ))
        pret_valoare=self.conexiune_bd.cursor.fetchone()
        try:
            if volum_initial is not None:
                valoare_actualizata=pret_valoare[0] * volum_aviz
                valoare_finala=pret_valoare[1]-valoare_actualizata
                volum_actualizat=volum_initial[0]-volum_aviz
                self.conexiune_bd.cursor.execute("INSERT INTO tabel_NIR_lemn_fasonat (Ocol_silvic, Cod_aviz , Data , Sortiment ,  Subsortiment , Volum_mc) VALUES (?, ?, ?, ?, ?, ?)", (ocol_silvic, cod_aviz, data, sortiment, subsortiment, volum_aviz, ))
                self.conexiune_bd.cursor.execute("UPDATE tabel_achizitii_lemn_fasonat SET Volum=?, Valoare_totala=? WHERE Nume_Ocol_silvic=? AND Sortiment=? AND Subsortiment=?", (volum_actualizat, valoare_finala, ocol_silvic, sortiment, subsortiment, ))
                self.conexiune_bd.conexiune.commit()
                print("NIR adaugat cu succes.")
            else:
                print('Operatiune esuata')
        except TypeError as e:
            print(f"Parametrii gresiti: {e}")
        self.conexiune_bd.disconnect_baza_de_date()
        
        
    def sterge_nir(self, ID,cod_aviz, Ocol_silvic, sortiment, subsortiment):
        self.conexiune_bd.connect_baza_de_date()
        self.conexiune_bd.cursor.execute("SELECT Volum FROM tabel_achizitii_lemn_fasonat WHERE Nume_Ocol_silvic=? AND Sortiment=? AND Subsortiment=?", (Ocol_silvic, sortiment, subsortiment, ))
        volum_initial=self.conexiune_bd.cursor.fetchone()
        self.conexiune_bd.cursor.execute("SELECT Volum_mc FROM tabel_NIR_lemn_fasonat WHERE Cod_aviz=? AND Sortiment=? AND Subsortiment=?", (cod_aviz, sortiment, subsortiment, ))
        volum_scazut=self.conexiune_bd.cursor.fetchone()
        self.conexiune_bd.cursor.execute("SELECT Pret_achizitie, Valoare_totala FROM tabel_achizitii_lemn_fasonat WHERE ID=?", (ID, ))
        pret_valoare=self.conexiune_bd.cursor.fetchone()
        try:
            if volum_scazut is not None:
                valoare_actualizata=pret_valoare[0] * volum_scazut[0]
                valoare_finala=pret_valoare[1] + valoare_actualizata
                volum_actualizat=volum_initial[0]+volum_scazut[0]
                self.conexiune_bd.cursor.execute("DELETE FROM tabel_NIR_lemn_fasonat WHERE Cod_aviz=?", (cod_aviz, ))
                self.conexiune_bd.cursor.execute("UPDATE tabel_achizitii_lemn_fasonat SET Volum=?, Valoare_totala=? WHERE Nume_Ocol_silvic=? AND Sortiment=? AND Subsortiment=?", ( volum_actualizat, valoare_finala, Ocol_silvic, sortiment, subsortiment, ))
                self.conexiune_bd.conexiune.commit()
                print("NIR sters cu succes.")
            else:
                print("Avizul nu exista.")
        except TypeError as e:
            print(f"Parametrii gresiti: {e}")
            
        self.conexiune_bd.disconnect_baza_de_date()
        
        
    def afiseaza_volum_ramas(self, ocol_silvic):
        self.conexiune_bd.connect_baza_de_date()
        self.conexiune_bd.cursor.execute("SELECT Nume_Ocol_Silvic, Sortiment, Subsortiment, Volum FROM tabel_achizitii_lemn_fasonat WHERE Nume_Ocol_silvic=?", (ocol_silvic, ))
        volum_ramas=self.conexiune_bd.cursor.fetchall()
        for elemente in volum_ramas:
            print(elemente)
        self.conexiune_bd.disconnect_baza_de_date()
            
        
            
            
            
            
            
achizitii_lemn_fasonat=AchizitiiLemnFasonat(conexiune_bd)
iesiri_lemn_fasonat=IesiriLemnFasonat(conexiune_bd)

            


    
                
                
    