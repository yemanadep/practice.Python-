class Train:
    def __init__(self,name,seats,fare):
        self.name = name 
        self.seats = seats
        #self.status = status
        self.fare = fare

    def getStatus(self):
        print(f"The name of Train is {self.name} and the Available seats are {self.seats}")

    def fareInfo(self):
        print(f"The Fare of train is {self.fare}")

    def bookTicket(self):
        if (self.seats) > 0:
            print(f"Your Ticket has been booked with Ticket number {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Seats are full , please try Tatkal Booking")

        
    def cancelTicket(self):
        if self.seats == 300:
            pass
        else:
            self.seats = self.seats + 1

Devgiri = Train("Devgiri",297, 150)
Devgiri.getStatus()
Devgiri.fareInfo()
Devgiri.cancelTicket()
Devgiri.getStatus()
