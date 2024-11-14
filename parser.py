import PyPDF2
import pdfminer
import pdfminer.pdfparser
import pdfquery
import camelot
import pandas as pd
import sys
import traceback
import tabula

def extract_data_camelot(pdf_path, password, output_csv):

    tables=[]
    try:
        tables = camelot.read_pdf(pdf_path, pages='all', password=password, flavor='stream')
    except Exception:
        print(traceback.format_exc())

    # tables.export(output_csv, f="csv", compress=False)
    for i, table in enumerate(tables):
        df = table.df
        file_name = f"table_{i+1}.csv"
        df.to_csv('files/' + file_name, index=False)

        print(f"Table {i+1} saved as {file_name}")


def extract_data_pdfquery(pdf_path, password, output_xml):
    pdf = pdfquery.PDFQuery(pdf_path)
    pdf.load()
    pdf.tree.write(output_xml, pretty_print=True)

def extract_data_tabula(pdf_path, password, output_csv):
    tables = tabula.read_pdf(pdf_path, pages='all', password=password, stream=True, pandas_options={'header': None})
    for i, table in enumerate(tables):
        df = table
        file_name = f"table_{i+1}.csv"
        df.to_csv('files/' + file_name, index=False)
        # print(table)

        print(f"Table {i+1} saved as {file_name}")

# extract_data_pdfquery('files/statement1.pdf', '97505090901', 'files/output.xml')

# extract_data_camelot('files/statement1.pdf', '97505090901', 'files/output.csv')

extract_data_tabula('files/cc2.pdf', 'AASH3907', '/')