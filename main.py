from modul_lemn_fasonat import AchizitiiLemnFasonat, IesiriLemnFasonat
from modul_adauga_stoc_partida import AchizitiiLemnPePicior
from modul_iesiri_stocuri import IesiriLemnPePicior
from baza_de_date_prodfor import Conexiune_bd

conexiune_noua=Conexiune_bd("baza_de_date_prodfor.db")


class Menu_principal_lemn_picior:
    def __init__(self) -> None:
        self.intrari_lemn_pe_picior=AchizitiiLemnPePicior(conexiune_noua)
        self.conexiune=conexiune_noua
        self.conexiune.connect_baza_de_date()
        
    def adauga_depozit(self):
        self.intrari_lemn_pe_picior.adauga_depozit(ID=(input("Introduce-ti ID-ul:")), numar_partida=input("Introduce-ti partida:"))
        self.conexiune.disconnect_baza_de_date()
        
        
    def adauga_apv(self):
        self.intrari_lemn_pe_picior.adauga_apv(ID=(input("Introduce-ti ID-ul:")), numar_partida=input("Introduce-ti partida:"), Sortiment=input("Introduce-ti sortimentul:"), Subsortiment=input("Introduce-ti subsortimentul: "), Volum=float(input("Introduce-ti volumul: ")))
        self.conexiune.disconnect_baza_de_date()
        
        
    def modifica_apv(self):
        self.intrari_lemn_pe_picior.modifica_apv(ID=(input("Introduce-ti ID-ul: ")), numar_partida=input("Introduce-ti partida: "), sortiment=input("Introduce-ti sortimentul: "), subsortiment=input("Introduce-ti subsortimentul: "), volum=float(input("Introduce-ti volumul: ")))
        self.conexiune.disconnect_baza_de_date()
        
    def adauga_autorizatie(self):
        self.intrari_lemn_pe_picior.adauga_autorizatie(numar_partida=input("Introduce-ti partida: "), data_infiintare=input("Introduce-ti data autorizarii: "), data_desfiintare=input("Introduce-ti data limita de exploatare: "))
        self.conexiune.disconnect_baza_de_date()
        
    def modifica_autorizatie(self):
        self.intrari_lemn_pe_picior.modifica_autorizatie(numar_partida=input("Introduce-ti partida: "), data_infiintare=input("Introduce-ti data autorizarii: "), data_desfiintare=input("Introduce-ti data limita de exploatare: "))
        self.conexiune.disconnect_baza_de_date()
        
    def prelungire_autorizatie(self):
        self.intrari_lemn_pe_picior.adauga_prelungire_autorizatie(prelungire_autorizatie=input("Introduce-ti prelungirea termenului de exploatare: "), numar_partida=input("Introduce-ti partida: "))
        self.conexiune.disconnect_baza_de_date()
        
    def stergere_apv_autorizatie_depozit(self):
        self.intrari_lemn_pe_picior.sterge( ID=(input("Introduce-ti ID-ul: ")), partida=input("Introduce-ti partida: "))
        self.conexiune.disconnect_baza_de_date()
        
    def adauga_partida_in_lucru(self):
        self.intrari_lemn_pe_picior.adauga_partida_in_lucru(ID=(input("Introduce-ti ID-ul partidei:")))
        self.conexiune.disconnect_baza_de_date()
        
    def sterge_partida_in_lucru(self):
        self.intrari_lemn_pe_picior.sterge_partida_in_lucru(numar_partida=input("Introduce-ti partida: "))
        self.conexiune.disconnect_baza_de_date()
        
class Exploatare:
    def __init__(self) -> None:
        self.conexiune=conexiune_noua
        self.iesiri=IesiriLemnPePicior(conexiune_noua)
        self.conexiune.connect_baza_de_date()
    
    def adauga_nir(self):
        self.iesiri.adauga_nir(Cod_aviz=input("Introduce-ti codul avizului: "), data=input("Introduce-ti data: "), Provenienta=input("Introduce-ti partida: "), Specie=input("Introduce-ti sortimentul: "), Subsortiment=input("Introduce-ti subsortimentul: "), Volum_mc=float(input("Introduce-ti volumul: ")))
        self.conexiune.disconnect_baza_de_date()
        
    def sterge_nir(self):
        self.iesiri.sterge_nir(cod_aviz=input("Introduce-ti codul avizului: "), Provenienta=input("Introduce-ti partida: "), Specie=input("Introduce-ti sortimentul: "), Subsortiment=input("Introduce-ti subsortimentul: "))
        self.conexiune.disconnect_baza_de_date()
        
    def afiseaza_stoc(self):
        self.iesiri.afiseaza_stoc_initial(numar_partida=input("Introduce-ti partida dorita: "))
        self.conexiune.disconnect_baza_de_date()
    
    def afiseaza_stoc_ramas(self):
        self.iesiri.afiseaza_stoc_ramas(provenienta=input("Introduce-ti partida: "))
        self.conexiune.disconnect_baza_de_date()
        
        
class Menu_lemn_fasonat:
    def __init__(self) -> None:
        self.conexiune=conexiune_noua
        self.achizitii_lemn_fasonat=AchizitiiLemnFasonat(conexiune_noua)
        self.conexiune.connect_baza_de_date()
        
    def adauga_contract(self):
        self.achizitii_lemn_fasonat.adauga_achizitie(ID=input("Introduce-ti ID: "), ocol_silvic=input("Introduce-ti ocol silvic: "), contract=input("Introduce-ti contract: "), sortiment=input("Introduce-ti sortiment: "), subsortiment=input("Introduce-ti subsortiment: "), volum=float(input("Introduce-ti volum: ")), pret_achizitie=float(input("Introduce-ti pretul de achizitie: ")), cont_bancar=input("Introduce-ti contul bancar: "))
        self.conexiune.disconnect_baza_de_date()
    
    def actualizeaza_contract(self):
        self.achizitii_lemn_fasonat.actualizeaza_informatii(ID=input("Introduce-ti ID: "), ocol_silvic=input("Introduce-ti ocol silvic: "), contract=input("Introduce-ti contract: "), sortiment=input("Introduce-ti sortiment: "), subsortiment=input("Introduce-ti subsortiment: "), volum=float(input("Introduce-ti volum: ")), pret_achizitie=float(input("Introduce-ti pretul de achizitie: ")), cont_bancar=input("Introduce-ti contul bancar: "))    
        self.conexiune.disconnect_baza_de_date()   
    
    def sterge_contract(self):
        self.achizitii_lemn_fasonat.sterge_achizitie(ID=input("Introduce-ti ID:"), ocol_silvic=input("Introduce-ti ocolul: "))
        self.conexiune.disconnect_baza_de_date()
        
        
class Nir_lemn_fasonat:
    def __init__(self) -> None:
        self.conexiune=conexiune_noua
        self.nir=IesiriLemnFasonat(conexiune_noua)
        self.conexiune.connect_baza_de_date()
        
    def adauga_nir(self):
        self.nir.adauga_nir(ID=input("Introduce-ti ID-ul obiectului de contract: "), ocol_silvic=input("Introduce-ti ocolul: "), cod_aviz=input("Introduce-ti codul avizului: "), data=input("Introduce-ti data: "), sortiment=input("Introduce-ti specia: "), subsortiment=input("Introduce-ti subsortimentul: "), volum_aviz=float(input("Introduce-ti volum: ")))
        self.conexiune.disconnect_baza_de_date()
        
    def sterge_nir(self):
        self.nir.sterge_nir( ID=input("Introduce-ti ID-ul obiectului de contract: "),cod_aviz=input("Introduce-ti codul avizului: "), Ocol_silvic=input("Introduce-ti ocolul: "), sortiment=input("Introduce-ti specia: "), subsortiment=input("Introduce-ti subsortimentul: "))
        self.conexiune.disconnect_baza_de_date()
        
    def afiseaza_volum_ramas(self):
        self.nir.afiseaza_volum_ramas(ocol_silvic=input("Introduce-ti ocolul: "))
        self.conexiune.disconnect_baza_de_date()
    

    
        
        


menu_principal=Menu_principal_lemn_picior()
exploatare=Exploatare()
menu_lemn_fasonat=Menu_lemn_fasonat()
iesiri_lemn_fasonat=Nir_lemn_fasonat()

# menu_lemn_fasonat.adauga_contract()
menu_lemn_fasonat.sterge_contract()