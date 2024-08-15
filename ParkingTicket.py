

def generate_barcode():
    from barcode import EAN13
    from barcode.writer import ImageWriter
    import random

    # Specify the code number as a string
    ticket_number = '7' + ''.join([str(random.randint(0, 9)) for _ in range(11)])

    # Create an EAN13 barcode object
    barcode = EAN13(ticket_number, writer=ImageWriter())   

    # Save the barcode as a PNG file
    barcode.save(ticket_number)
    return ticket_number
    

def print_ticket(ticket_number):
    show_ticket(ticket_number)


def show_ticket(ticket_number):
    from PIL import Image
    img = Image.open(ticket_number + ".png")
    img.show()    