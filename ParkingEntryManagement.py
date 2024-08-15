import ParkingTicket as ticket
import ParkingBarrierGate as parking
from time import sleep
import ParkingTicketDatabase as database

parking.init()

while True:
    button = input("Press 'o' to open the gate or 'l' to list the tickets: ")
    if button == 'o':
        print('Printing ticket...')
        ticket_number = ticket.generate_barcode()
        ticket.print_ticket(ticket_number)
        database.add_ticket(ticket_number)
        database.save_tickets()        
        print('Waiting for ticket...')
        sleep(3)
        print('Opening the gate...')
        parking.control_gate_arm("up")
        print('Waiting for the car to cross the barrier...')
        sleep(5)
        print("Closing the gate...")
        parking.control_gate_arm("down")
    elif button == 'l':
        print('Listing the tickets...')
        database.open_tickets()   
        database.list_tickets()
        print('End of the list')
    else:
        print('Input invalid')

# parking.show_demo1()

# Keep Turtle window open
parking.t.getscreen().mainloop()