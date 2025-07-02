from utils import  generate_ticket
from fpdf import FPDF

tickets = [generate_ticket() for _ in range(300)]

pdf = FPDF(format='A4')
pdf.set_auto_page_break(auto=True, margin=8)

# A4 size in mm: 210 x 297
page_w = 210
page_h = 297

ticket_w = 90
ticket_h = 45
spacing_x = 5
spacing_y = 5
margin_x = 10
margin_y = 10
cell_h = 7
cell_w = (ticket_w - 2 * margin_x - 2 * spacing_x) / 9

tickets_per_page = 12
cols = 2
rows = 6

for page_start in range(0, len(tickets), tickets_per_page):
    pdf.add_page()
    pdf.set_font("Courier", size=10)
    for i in range(tickets_per_page):
        idx = page_start + i + 1
        if idx > len(tickets):
            break
        ticket = tickets[page_start + i]
        grid_row = i // cols
        grid_col = i % cols
        x = margin_x + grid_col * (ticket_w + spacing_x)
        y = margin_y + grid_row * (ticket_h + spacing_y)
        pdf.set_xy(x, y)
        pdf.set_font("Courier", size=10)
        pdf.cell(ticket_w, 8, f"Ticket #{idx}", ln=1, align='C')
        pdf.set_font("Courier", size=10)
        for row in ticket:
            pdf.set_x(x)
            for num in row:
                text = f"{num:2}" if num is not None else "  "
                pdf.cell(cell_w, cell_h, text, border=1, align='C')
            pdf.ln(cell_h)
        pdf.ln(1)
pdf.output(".\\bingo_tickets_files\\bingo_tickets.pdf")
print("PDF generated successfully.")