import ParkingBarrierGate as parking
import ParkingTicketDatabase as database
import time

parking.init()

while True:             
    parking_id = input('Enter your ticket number: ')
    db = database.open_tickets()       
    if parking_id in db:
        print('Thanks, you can go, Bye!')
        print('Opening the gate...')
        parking.control_gate_arm("up")
        print('Waiting for the car to cross the barrier...')
        time.sleep(5)
        print('Closing the gate...')
        parking.control_gate_arm("down")            
    else:           
        print('Input invalid, Try again!')