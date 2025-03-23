# XML Invoice Processing Script

## General Description
This Python script enables processing and analysis of invoices in XML format. The program is designed to load data from the `faktury.xml` file, which contains information about accounting documents, their issuers, amounts, and other financial details.

## Functionality

The script defines a `puzzle_invoices` class implementing the following functions:

- `import_xml()` - loads the XML file with invoices
- A series of `get_*` methods for extracting specific data from documents:
  - `get_data_wystawienia()` - retrieves invoice issue dates
  - `get_termin()` - retrieves payment due dates
  - `get_numer()` - retrieves invoice numbers
  - `get_NIP()` - retrieves contractor tax identification numbers
  - `get_nazwa_kontrahenta()` - retrieves contractor names
  - `get_adres_kontrahenta()` - retrieves contractor addresses
  - `get_kwota()` - retrieves payment amounts
  - `get_skala_VAT()` - retrieves VAT scale information
  - `get_netto()` - retrieves net amounts
  - `get_VAT()` - retrieves VAT amounts
  - `get_status()` - retrieves payment status information

## XML Data Structure

The script handles XML documents with the following structure:

```xml
<paczka wersja="11" miesiac="2021-01">
  <dokument dekret="sprz">
    <data>...</data>
    <data_wystawienia>...</data_wystawienia>
    <termin>...</termin>
    <numer>...</numer>
    <kontrahent>
      <NIP>...</NIP>
      <nazwa>...</nazwa>
      <adres>...</adres>
    </kontrahent>
    <ksieguj>
      <kwota>...</kwota>
    </ksieguj>
    <rejVAT>
      <skala>...</skala>
      <suma stawka="podst">
        <netto>...</netto>
        <VAT>...</VAT>
      </suma>
    </rejVAT>
    <zaplata/>
  </dokument>
</paczka>
```

## Usage

The main functionality of the script includes:

1. Creating an instance of the `puzzle_invoices` class
2. Loading XML data from the `faktury.xml` file
3. Extracting selected data into a list
4. Attempting to compare data with information from a bank statement file (`wyciag.csv`)

## Dependencies

The script uses the following libraries:
- `xml.etree.ElementTree` - for parsing XML files
- `pandas` - for data manipulation and reading CSV files

## Notes

The code contains a commented-out `get_data()` method, which was an earlier implementation for retrieving all document data simultaneously, as well as unfinished functionality for comparing data with bank statements.
