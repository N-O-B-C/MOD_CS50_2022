from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 50)
        self._pdf.cell(0,60, "cs50 shitificate", new_x="LMARGIN", new_y="NEXT", align="C")
        self._pdf.image("shirtificate.jpg", w= self._pdf.epw)
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(225,225,225)
        self._pdf.text(x=81,y= 140,txt=name)

    def save(self, name):
        self._pdf.output(name)


name = input("Name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")