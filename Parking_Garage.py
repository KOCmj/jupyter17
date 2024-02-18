class ParkingGarage():
    total_ticket = 100
    total_parking_spots = 100

    def __init__(self, tickets=[], parking_spaces = [],  current_ticket = {}): 
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = current_ticket
        
    def add_ticket(self):
        ticket = len(self.tickets)+1
        print('Thank you.')
        self.tickets.append(ticket)
        print(f"Remaining tickets available at this time: {self.total_ticket - len(self.tickets)}")
        self.current_ticket = {'ticket_num': ticket,'paid': False}
        #print(self.current_ticket)
        print('You can park right over there.')
        self.parking_spaces.append(ticket)
        print(f'Remaining parking spots available at this time: {self.total_parking_spots - len(self.parking_spaces)}')
        
        
    def pay_parking(self):
        pay= input("That will be 30buckaroos (Enter 'hand' to give the money): ")
        if pay.lower() == 'hand':
            self.current_ticket['paid']= True
            print('Your ticket has been paid, you now have 15 minutes timer starts now.')
            # just having fun/easter egg
        elif pay.lower() == 'no':
            print("Find out next time on coding temple.")
        else:
            print('Ticket not paid, do you want to try again?')

    def leaveGarage(self):
        if self.current_ticket['paid']==True:
            print('Thank you, enjoy the rest of your day.') 
            self.tickets.remove(self.current_ticket['ticket_num'])
            self.parking_spaces.remove(self.current_ticket['ticket_num'])
        else:
            print('You still need to pay: ')
    
my_ticket = ParkingGarage() 

def ParkG():
    while True:
        i= input("Do you want to: (add/pay/leave/quit)?: ")
        if i.lower() == 'add':
            my_ticket.add_ticket()
        elif i.lower() == 'pay':
            my_ticket.pay_parking()
        elif i.lower() == 'leave':
            my_ticket.leaveGarage()
        elif i.lower() == 'quit':
            print('Adios')
            break
        else:
            print('Choose another option')
ParkG()
