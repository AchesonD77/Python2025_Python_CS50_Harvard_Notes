"""
CS50 Shirtificate

FPDF coordinate system: origin (0,0) is the top-left, units are mm; A4 is 210×297 mm.

add_page() creates Page 1.

cell(w, h, text, ln, align) writes text; using w=0 makes the cell span the width of the page; align="C" centers it.

ln=1 moves to the next line after the cell.

image(path, x, y, w) draws the image.
We pass w=page_w to stretch it to the full width; that guarantees it’s horizontally centered (x=0).

Drawing order matters: anything added later appears on top of earlier content.
So we add the image first, then draw the white name text to overlay it.

set_text_color(255,255,255) makes the name white so it’s visible on the shirt.

set_auto_page_break(False) prevents FPDF from inserting automatic page breaks that might shift

Tip: If your name is very long and looks cramped, drop the font size to 28 or 26,
or replace cell with multi_cell (but the spec says you don’t need to wrap).

"""

# pip install fpdf2

from fpdf import FPDF


def make_shirtificate(name: str) -> None:
    # A4, and Portrait PDF
    pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
    pdf.set_auto_page_break(False)  # nothing pushes our layout around
    pdf.add_page()

    # title
    pdf.set_font('helvetica', 'B', 24)
    pdf.cell(0, 18, 'CS50 Shirtificate', ln=1, align='C')

    # shirt imagine, centered horizontally
    # use full page width so it's automatically centered
    page_w = pdf.w  # 210mm on A4
    # put the image a bit below the title
    pdf.image('shirtificate.png', x=0, y=55, w=page_w)

    # name text on top of the shirt, white color
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('helvetica', 'B', 32)
    # center the text
    pdf.set_y(120)
    pdf.cell(0, 12, f"{name} took CS50", align = 'C')

    # save
    pdf.output('shirtificate.pdf')


def main():
    name = input("Name: ").strip()
    make_shirtificate(name)


if __name__ == '__main__':
    main()