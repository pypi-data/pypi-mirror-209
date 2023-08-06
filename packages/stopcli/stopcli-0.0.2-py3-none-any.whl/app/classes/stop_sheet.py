from fpdf import FPDF
from app.constants import LETTERS, HEADERS
from uuid import uuid4

class StopSheet:
    __player = ""
    __pdf = None
    __col_width = None
    __row_height = None
    width = None
    height = None

    def __init__(self, player):
        self.__player = player
        self.__pdf = FPDF()
        self.__configure_page()
        self.__row_height = 6
        self.__col_width = (self.__pdf.w - 20) / len(HEADERS)
        self.width = self.__pdf.w
        self.height = self.__pdf.h

    def __change_font(self, font="Helvetica", size=8, style="B"):
        self.__pdf.set_font(font, size=size, style=style)

    def __configure_page(self):
        self.__pdf.add_page(
            orientation="L",
            format="A4",
            same=False
        )
        self.__pdf.set_margin(5)
        self.__change_font()

    def __add_fecha(self):
        x = self.width - (10 + self.__col_width * 2)
        self.__pdf.set_xy(x, 5)
        self.__pdf.cell(self.__col_width, self.__row_height, txt="FECHA:", border=1, align="C")
        self.__pdf.cell(self.__col_width, self.__row_height, txt="", border=1, align="C")

    def __add_info(self):
        id = uuid4()
        self.__pdf.set_xy(10, 11)
        self.__pdf.cell(self.width / 2, self.__row_height, txt=f"JUGADOR: {self.__player}", border=1)
        self.__pdf.cell((self.width / 2) - 20, self.__row_height, txt=f"UUID: {id}", border=1)
    
    def __add_headers(self):
        self.__pdf.set_xy(10, 17)
        for header in HEADERS:
            self.__pdf.set_x(self.__pdf.x)
            self.__pdf.cell(self.__col_width, self.__row_height,  txt=header, border=1, align="C")

    def __add_letters(self):
        self.__pdf.set_xy(10, 17)
        for letter in LETTERS:
            pos_y = self.__pdf.y + self.__row_height
            self.__pdf.set_xy(10, pos_y)
            self.__pdf.cell(self.__col_width, self.__row_height , txt=letter, border=1, align="C")
    
    def __add_grid(self):
        for row in range(1, len(LETTERS) + 1):
            for col in range(1, len(HEADERS)):
                x = col * self.__col_width + 10
                y = row * self.__row_height + 17
                self.__pdf.rect(x, y, self.__col_width, self.__row_height)

    def __add_total(self):
        x = self.width - (10 + self.__col_width * 2)
        self.__pdf.set_xy(x, 185)
        self.__pdf.cell(self.__col_width, self.__row_height, txt="TOTAL", border=1, align="C")
        self.__pdf.cell(self.__col_width, self.__row_height, txt="", border=1, align="C")

    def generate_pdf(self):
        self.__add_fecha()
        self.__add_info()
        self.__add_headers()
        self.__add_letters()
        self.__add_grid()
        self.__add_total()
        return self.__pdf


# pdf.set_xy(pdf.w - pos_header * 2, 5)
# pdf.cell(0, CELL_HEIGHT, txt="FECHA:", border=1, align="C")

# pdf.set_xy(10, 12)


# pdf.cell(pdf.w - 20, CELL_HEIGHT, txt="JUGADOR:", border=1)

# # pdf.set_xy(10, 12)

# # for header in HEADERS:
# #     idx = HEADERS.index(header)
# #     pdf.set_x(pdf.x)
# #     pdf.cell(pos_header, CELL_HEIGHT,  txt=header, border=1, align="C")

# pdf.set_y(13)
# for letter in LETTERS:
#     idx = LETTERS.index(letter)
#     pos_y = pdf.y + CELL_HEIGHT - 1
#     pdf.set_xy(10, pos_y)
#     pdf.cell(pos_header, CELL_HEIGHT - 1, txt=letter, border=1, align="C")

# cell_width = pos_header
# cell_height = 6


# for row in range(1, len(LETTERS) + 1):
#     for col in range(1, len(HEADERS)):
#         x = col * cell_width + 10
#         y = row * cell_height + 13
#         pdf.rect(x, y, cell_width, cell_height)

# pdf.set_xy(pdf.w - (pos_header + 5) * 2, 181)
# pdf.cell(pos_header, CELL_HEIGHT, txt="TOTAL", border=1, align="C")
# pdf.set_xy(pdf.w - pos_header, 181)
# pdf.rect(pdf.w - pos_header - 10, 181, pos_header, CELL_HEIGHT)

# pdf.output("simple_demo.pdf")
