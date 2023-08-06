from app.classes.stop_sheet import StopSheet
from pypdf import PdfMerger, PdfReader
from io import BytesIO
import os

def get_pwd():
    return os.getcwd()


def generate_sheets(players = [], print = False):
    merger = PdfMerger()
    for player in players:
        template = StopSheet(player.upper())
        pdf = template.generate_pdf()
        bytes = pdf.output()
        reader = PdfReader(BytesIO(bytes))
        merger.append(reader)

    if len(players) > 0:
        merger.write("sheets.pdf")
        merger.close()
        os.system("open sheets.pdf")





