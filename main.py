from utils import generate_column_numbers, generate_ticket, print_ticket
from fpdf import FPDF

tickets = [generate_ticket() for _ in range(200)]

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=8)


ticket_w = 110
ticket_h = 60
spacing_x = 1
spacing_y = 1
margin_x = 10
margin_y = 10
cell_h = 8
cell_w = (ticket_w - 2 * margin_x - 2 * spacing_x) / 9

tickets_per_page = 10
for page_start in range(0, len(tickets), tickets_per_page):
    pdf.add_page()
    pdf.set_font("Courier", size=10)
    for i in range(tickets_per_page):
        idx = page_start + i + 1
        if idx > len(tickets):
            break
        ticket = tickets[page_start + i]
        # Calculate position: 3 rows x 4 columns grid
        grid_row = i // 2
        grid_col = i % 2
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