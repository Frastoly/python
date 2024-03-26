class Personel:
    def __init__(self, adi, departmani, calisma_yili, maasi):
        self.adi = adi
        self.departmani = departmani
        self.calisma_yili = calisma_yili
        self.maasi = maasi

    def __str__(self):
        return f"{self.adi}, {self.departmani} departmanında, {self.calisma_yili} yıldır çalışıyor ve maaşı {self.maasi} TL."

class Firma:
    def __init__(self):
        self.personel_listesi = []

    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)



    def personel_listele(self):
        for personel in self.personel_listesi:
            print(personel)

    def maas_zammi(self, personel, zam_orani):
        yeni_maas = personel.maasi * (1 + zam_orani / 100)
        personel.maasi = round(yeni_maas, 2)  # Maaşı iki ondalık basamağa yuvarlar

    def personel_cikart(self, personel):
        if personel in self.personel_listesi:
            self.personel_listesi.remove(personel)

# Örnek kullanım:
personel1 = Personel("Ali", "Muhasebe", 5, 3000)
personel2 = Personel("Semih","Yazılımcı",3,15000)
firma = Firma()
firma.personel_ekle(personel1)
#firma.personel_cikart(personel1)
firma.maas_zammi(personel1, 15)  
firma.personel_ekle(personel2)
#firma.personel_cikart(personel2)
firma.personel_listele()
firma.maas_zammi(personel2,50)

