tickets = []

def add_ticket(item):
    tickets.append(item)

def remove_ticket(item):
    tickets.remove(item)

def count_tickets():
    return len(tickets)

def list_tickets():
    #print('Listing the tickets...')
    for ticket in tickets:
        print(ticket)

def save_tickets():
    #print('Save database')
    with open("tickets.db", 'w') as f:
        for t in tickets:
            f.write(str(t) + '\n')

def open_tickets():
    #print('Open database')
    with open("tickets.db", 'r') as f:
        tickets = [line.rstrip('\n') for line in f]
    return tickets    
