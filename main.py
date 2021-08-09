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

    def get_data(self, root):
        for dokument in root.findall('dokument'):
            data = dokument.find('data').text
            print(data)
            data_wystawienia=dokument.find('data_wystawienia').text
            print(data_wystawienia)
            termin = dokument.find('termin').text
            print(termin)
            numer = dokument.find('numer').text
            print(numer)
            kontrahent = dokument.find('kontrahent')
            for nip in kontrahent.iter('nip'):
                numer_nip = nip.text
                print(numer_nip)
            for nazwa in kontrahent.iter('nazwa'):
                nazwa_kontrahenta = nazwa.text
                print(nazwa_kontrahenta)
            for adres in kontrahent.iter('adres'):
                adres_kontrahenta = adres.text
                print(adres_kontrahenta)
            ksieguj=dokument.find('ksieguj')
            for kwota in ksieguj.iter('kwota'):
                naleznosc = kwota.text
                print(naleznosc)
            rejvat = dokument.find('rejvat')
            # for skala in rejvat.iter('skala'):
            #     skala_vat= skala.text
            #     print(skala_vat)
            # for suma in rejvat.iter('suma'):
            #     suma_vat = suma.text
            #     print(suma_vat)
            #     for netto in suma.iter('netto'):
            #         kwota_netto = netto.text
            #         print(kwota_netto)
            #     for vat in suma.iter('vat'):
            #         kwota_vat = vat.text
            #         print(kwota_vat)
            for zaplata in dokument.iter('zaplata'):
                zaplacono = zaplata.text
                print(zaplacono)
        return (data, data_wystawienia, termin, numer , nazwa_kontrahenta, numer_nip, suma_vat, kwota_netto, kwota_vat)


def main():
    faktury=puzzle_invoices()
    root=faktury.import_xml()
    faktury.get_data(root)

if __name__ == "__main__":
    main()