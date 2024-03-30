from fpdf import FPDF

class PDF(FPDF):
    def shirt(self, s):
        self.image("shirtificate.png",10,70,190,190)
        self.set_font("Arial",size=25)
        self.set_text_color(255,255,255)
        self.cell(0,130,f"{s} took CS50",align="C")

    def background(self):
        self.set_font("Arial","B",size=50)
        self.cell(0,60,"CS50 Shirtificate",align="C", ln=True)

def main():
    s = input("Name: ")
    pdf = PDF()
    pdf.add_page()
    pdf.background()
    pdf.shirt(s)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
