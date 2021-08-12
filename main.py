# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# STRUKLTURA XML

# <paczka wersja="11" miesiac="2021-01">
# </dokument>
# 	<dokument dekret="sprz">
# 		<data>...</data>
# 		<data_wystawienia>...</data_wystawienia>
# 		<termin>...</termin>
# 		<numer>...</numer>
# 		<kontrahent>
# 			<NIP>...</NIP>
# 			<nazwa>S...</nazwa>
# 			<adres>...</adres>
# 		</kontrahent>
# 		<ksieguj>
# 			<kwota>...</kwota>
# 		</ksieguj>
# 		<rejVAT>
# 			<skala>...</skala>
# 			<suma stawka="podst">
# 				<netto>...</netto>
# 				<VAT>...</VAT>
# 			</suma>
# 		</rejVAT>
# 		<zaplata/>
# 	</dokument>
# </paczka>



class puzzle_invoices:

    def __init__(self):
        self.data = []

    directory='faktury.xml'

    def import_xml(self):
        import xml.etree.ElementTree as ET
        tree = ET.parse('faktury.xml')
        root = tree.getroot()
        return root

    # def get_data(self, root):
    #     for dokument in root.findall('dokument'):
    #         data = dokument.find('data').text
    #         print(data)
    #         data_wystawienia=dokument.find('data_wystawienia').text
    #         print(data_wystawienia)
    #         termin = dokument.find('termin').text
    #         print(termin)
    #         numer = dokument.find('numer').text
    #         print(numer)
    #         kontrahent = dokument.find('kontrahent')
    #         for nip in kontrahent.iter('NIP'):
    #             numer_nip = nip.text
    #             print(numer_nip)
    #         for nazwa in kontrahent.iter('nazwa'):
    #             nazwa_kontrahenta = nazwa.text
    #             print(nazwa_kontrahenta)
    #         for adres in kontrahent.iter('adres'):
    #             adres_kontrahenta = adres.text
    #             print(adres_kontrahenta)
    #         ksieguj=dokument.find('ksieguj')
    #         for kwota in ksieguj.iter('kwota'):
    #             naleznosc = kwota.text
    #             print(naleznosc)
    #         rejvat = dokument.find('rejVAT')
    #         for skala in rejvat.iter('skala'):
    #             skala_vat= skala.text
    #             print(skala_vat)
    #         for suma in rejvat.iter('suma'):
    #             suma_vat = suma.text
    #             print(suma_vat)
    #             for netto in suma.iter('netto'):
    #                 kwota_netto = netto.text
    #                 print(kwota_netto)
    #             for vat in suma.iter('VAT'):
    #                 kwota_vat = vat.text
    #                 print(kwota_vat)
    #         for zaplata in dokument.iter('zaplata'):
    #             zaplacono = zaplata.text
    #             print(zaplacono)
    #     faktury=[data, data_wystawienia, termin, numer , nazwa_kontrahenta, numer_nip, suma_vat, kwota_netto, kwota_vat]
    #     return (faktury)

    def get_data_wystawienia(self,root):

        data_wystawienia=[]
        for dokument in root.findall('dokument'):
            data_wystawienia.append(dokument.find('data_wystawienia').text)
        return (data_wystawienia)

    def get_termin(self,root):

        termin=[]
        for dokument in root.findall('dokument'):
            termin.append(dokument.find('termin').text)
        return termin

    def get_numer(self,root):

        numer_faktury=[]
        for dokument in root.findall('dokument'):
            numer_faktury.append(dokument.find('numer').text)
        return numer_faktury

    def get_NIP(self,root):
        numer_nip = []
        for dokument in root.findall('dokument'):
            kontrahent = dokument.find('kontrahent')
            for nip in kontrahent.iter('NIP'):
                numer_nip.append(nip.text)
        return numer_nip

    def get_nazwa_kontrahenta(self,root):
        nazwa_kontrahenta = []
        for dokument in root.findall('dokument'):
            kontrahent = dokument.find('kontrahent')
            for nazwa in kontrahent.iter('nazwa'):
                nazwa_kontrahenta.append(nazwa.text)
        return nazwa_kontrahenta

    def get_adres_kontrahenta(self,root):
        adres_kontrahenta = []
        for dokument in root.findall('dokument'):
            kontrahent = dokument.find('kontrahent')
            for adres in kontrahent.iter('adres'):
                adres_kontrahenta.append(adres.text)
        return adres_kontrahenta

    def get_kwota(self,root):
        naleznosc = []
        for dokument in root.findall('dokument'):
            ksieguj = dokument.find('ksieguj')
            for kwota in ksieguj.iter('kwota'):
                naleznosc.append(kwota.text)
        return naleznosc

    def get_skala_VAT(self,root):
        skala_VAT = []
        for dokument in root.findall('dokument'):
            rejvat = dokument.find('rejVAT')
            for skala in rejvat.iter('skala'):
                skala_VAT.append(skala.text)
        return skala_VAT

    def get_netto(self,root):
        kwota_netto = []
        for dokument in root.findall('dokument'):
            rejvat = dokument.find('rejVAT')
            for suma in rejvat.iter('suma'):
                for netto in suma.iter('netto'):
                    kwota_netto.append(netto.text)
        return kwota_netto

    def get_VAT(self,root):
        kwota_VAT = []
        for dokument in root.findall('dokument'):
            rejvat = dokument.find('rejVAT')
            for suma in rejvat.iter('suma'):
                for vat in suma.iter('VAT'):
                    kwota_VAT.append(vat.text)
        return kwota_VAT

    def get_status(self, root):
        status = []
        for dokument in root.findall('dokument'):
            for zaplata in dokument.iter('zaplata'):
                status.append(zaplata.text)
        return status



def main():
    import pandas as pd
    faktury=puzzle_invoices()
    root=faktury.import_xml()
    #print(faktury.get_netto(root))
    lista=[[faktury.get_data_wystawienia(root)],
           [faktury.get_termin(root)],
           [faktury.get_numer(root)],
           [faktury.get_nazwa_kontrahenta(root)],
           [faktury.get_kwota(root)]]
                 # columns = ["Data wystawienia" , "Termin płatności", "Numer faktury", "Nazwa kontrahenta", "Kwota"]
    nazwy=pd.Series(lista)


    print(lista)
    print(nazwy)
    # data_wystawienia=faktury.get_data_wystawienia(root)

if __name__ == "__main__":
    main()