from baza_de_date_prodfor import Conexiune_bd, conexiune_bd


class AchizitiiLemnPePicior:
    def __init__(self, conexiune_bd : Conexiune_bd):
        self.conexiune_bd=conexiune_bd
        return
    
    def adauga_depozit(self, ID, numar_partida):
        self.conexiune_bd.connect_baza_de_date()
        self.conexiune_bd.cursor.execute(f"INSERT INTO tabel_depozit ('ID', 'Numar_partida') VALUES {ID, numar_partida}")
        self.conexiune_bd.conexiune.commit()
        print("Depozit adaugat cu succes.")
        self.conexiune_bd.disconnect_baza_de_date()
            
    def adauga_apv(self, ID, numar_partida, Sortiment, Subsortiment, Volum):
        self.conexiune_bd.connect_baza_de_date()
        self.conexiune_bd.cursor.execute("SELECT ID FROM tabel_depozit WHERE Numar_partida=?", (numar_partida, ))
        id_partida=self.conexiune_bd.cursor.fetchall()
        for id in id_partida:
            if id[0] == ID:
                self.conexiune_bd.cursor.execute("INSERT INTO tabel_APV ('ID', 'Numar_partida', 'Sortiment', 'Subsortiment', 'Volum') VALUES (?, ?, ?, ?, ?)", (ID, numar_partida, Sortiment, Subsortiment, Volum))
                self.conexiune_bd.conexiune.commit()
                print("Adaugare reusita.")
            else:
                print("Introduce-ti un ID valid.")
            
    def modifica_apv(self, ID, numar_partida, sortiment, subsortiment, volum):
        self.conexiune_bd.connect_baza_de_date()
        self.conexiune_bd.cursor.execute("SELECT ID FROM tabel_depozit WHERE Numar_partida=?", (numar_partida, ))
        id_partida=self.conexiune_bd.cursor.fetchall()
        for id in id_partida:
            if id[0] == ID:
                self.conexiune_bd.cursor.execute("UPDATE tabel_APV SET Numar_partida=?, Sortiment=?, Subsortiment=?, Volum=? WHERE ID=?", (numar_partida, sortiment, subsortiment, volum, ID, ))
                self.conexiune_bd.conexiune.commit()
                print("APV modificat cu succes.")
            else:
                print("ID invalid.")
        self.conexiune_bd.disconnect_baza_de_date()
            
    def adauga_autorizatie(self, numar_partida, data_infiintare, data_desfiintare):
        self.conexiune_bd.connect_baza_de_date()
        self.conexiune_bd.cursor.execute("SELECT SUM(Volum) FROM tabel_APV WHERE Numar_partida=?", (numar_partida, ))
        volum_depozit=self.conexiune_bd.cursor.fetchone()
        if volum_depozit[0] is not None:
            self.conexiune_bd.cursor.execute("INSERT INTO tabel_autorizatii ('Numar_partida', 'Data_infiintare', 'Data_desfiintare') VALUES (?, ?, ?)", (numar_partida, data_infiintare, data_desfiintare))
            self.conexiune_bd.cursor.execute("UPDATE tabel_autorizatii SET Volum_total=? WHERE Numar_partida=?", (volum_depozit[0], numar_partida, ))
            self.conexiune_bd.conexiune.commit()
            print("Autorizatie adaugata cu succes.")
        else:
            print("Volum indisponibil.")
        self.conexiune_bd.disconnect_baza_de_date()
        
    def modifica_autorizatie(self, numar_partida, data_infiintare, data_desfiintare):
        self.conexiune_bd.connect_baza_de_date()
        self.conexiune_bd.cursor.execute("SELECT SUM(Volum) FROM tabel_APV WHERE Numar_partida=?", (numar_partida, ))
        volum_depozit=self.conexiune_bd.cursor.fetchone()
        if volum_depozit[0] is not None:
            self.conexiune_bd.cursor.execute("UPDATE tabel_autorizatii SET Data_infiintare=?, Data_desfiintare=? WHERE Numar_partida=?", (data_infiintare, data_desfiintare, numar_partida, ))
            self.conexiune_bd.cursor.execute("UPDATE tabel_autorizatii SET Volum_total=? WHERE Numar_partida=?", (volum_depozit[0], numar_partida, ))
            self.conexiune_bd.conexiune.commit()
            print("Autorizatie actualizata.")
        else:
            print("Volum indisponibil.")
        self.conexiune_bd.disconnect_baza_de_date()
        
    def adauga_prelungire_autorizatie(self, prelungire_autorizatie, numar_partida):
        self.conexiune_bd.connect_baza_de_date()
        self.conexiune_bd.cursor.execute("SELECT Numar_partida FROM tabel_depozit WHERE Numar_partida=?", (numar_partida, ))
        depozit=self.conexiune_bd.cursor.fetchall()
        if depozit[0] == numar_partida:
            self.conexiune_bd.cursor.execute("UPDATE tabel_autorizatii SET Prelungit_pana_la=? WHERE Numar_partida=?", (prelungire_autorizatie, numar_partida, ))
            self.conexiune_bd.conexiune.commit()
            print("Autorizatie prelungita cu succes.")
        else:
            print("Depozit inexistent! Incerca-ti din nou.")
        self.conexiune_bd.disconnect_baza_de_date()
        
    def sterge(self, ID, partida):
        self.conexiune_bd.connect_baza_de_date()
        self.conexiune_bd.cursor.execute("SELECT Numar_partida FROM tabel_depozit WHERE ID=?", (ID, ))
        numar_partida=self.conexiune_bd.cursor.fetchall()
        id_valid=False
        for nume in numar_partida:
            if nume is not None:
                id_valid=True
                break
        if id_valid:
            self.conexiune_bd.cursor.execute("DELETE FROM tabel_autorizatii WHERE Numar_partida=?", (partida, ))
            self.conexiune_bd.cursor.execute("DELETE FROM tabel_APV WHERE Numar_partida=?", (partida, ))
            self.conexiune_bd.cursor.execute("DELETE FROM tabel_depozit WHERE Numar_partida=?", (partida, ))
            self.conexiune_bd.conexiune.commit()
            print("Ati sters cu succes partida.")
        else:
            print("Partida nu exista..")
            
        self.conexiune_bd.disconnect_baza_de_date()
        
    def adauga_partida_in_lucru(self, ID):
        self.conexiune_bd.connect_baza_de_date()
        self.conexiune_bd.cursor.execute("SELECT tabel_depozit.Numar_partida , tabel_APV.Sortiment, tabel_APV.Subsortiment, tabel_APV.Volum FROM tabel_depozit INNER JOIN tabel_APV ON tabel_depozit.ID = tabel_APV.ID WHERE tabel_depozit.ID=?", (ID,))
        afiseaza_date=self.conexiune_bd.cursor.fetchall()
        for element in afiseaza_date:
            if afiseaza_date is not None:
                self.conexiune_bd.cursor.execute("INSERT INTO tabel_parchet_in_lucru (Numar_partida, Sortiment, Subsortiment, Volum) VALUES(?, ?, ?, ?)",(element[0], element[1], element[2], element[3]))
                self.conexiune_bd.conexiune.commit()
                print("Partida adaugata in lucru.")
            else:
                print("Partida nu exista.")
        self.conexiune_bd.disconnect_baza_de_date()
        
    def sterge_partida_in_lucru(self, numar_partida):
        self.conexiune_bd.connect_baza_de_date()
        self.conexiune_bd.cursor.execute("SELECT Numar_partida FROM tabel_parchet_in_lucru WHERE Numar_partida=?", (numar_partida, ))
        parchet_in_lucru=self.conexiune_bd.cursor.fetchall()
        partida=False
        for nume in parchet_in_lucru:
            if nume is not None:
                partida=True
                break
        if partida:
            self.conexiune_bd.cursor.execute("DELETE FROM tabel_parchet_in_lucru WHERE Numar_partida=?", (numar_partida, ))
            self.conexiune_bd.conexiune.commit()
            print("Partida a fost stearsa.")
        else:
            print("Partida nu exista.")
        self.conexiune_bd.disconnect_baza_de_date()
        
        
stocuri=AchizitiiLemnPePicior(conexiune_bd)