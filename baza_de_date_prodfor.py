import sqlite3

class Conexiune_bd:
    def __init__(self, baza_de_date) -> None:
        self.baza_de_date=baza_de_date
        self.conexiune=None
        self.cursor=None
        
    def connect_baza_de_date(self):
        self.conexiune=sqlite3.connect(self.baza_de_date)
        self.cursor=self.conexiune.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tabel_depozit (ID str, Numar_partida str)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tabel_APV (ID str, Numar_partida str,  Sortiment str, Subsortiment str, Volum float, FOREIGN KEY (ID) REFERENCES tabel_depozit(ID))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tabel_autorizatii (Numar_partida str, Data_infiintare str, Data_desfiintare str, Prelungit_pana_la str,  Volum_total float )")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tabel_nir (Cod_Aviz str, Data str,  Provenienta str, Specie str, Sortiment str, Volum_mc float)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tabel_parchet_in_lucru(Numar_partida str, Sortiment str, Subsortiment str , Volum float)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tabel_achizitii_lemn_fasonat ( ID str, Nume_Ocol_silvic str, Contract str, Sortiment str, Subsortiment str, Volum float, Pret_achizitie float, Valoare_totala float, Cont_bancar str)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tabel_NIR_lemn_fasonat (Ocol_silvic str, Cod_aviz str, Data str, Sortiment str,  Subsortiment str, Volum_mc real)")
        self.conexiune.commit()
        
    def disconnect_baza_de_date(self):
        if self.conexiune:
            self.conexiune.close()
            
            

conexiune_bd=Conexiune_bd("baza_de_date_prodfor.db")

conexiune_bd.connect_baza_de_date()
