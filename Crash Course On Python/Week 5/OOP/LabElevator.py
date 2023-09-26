class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom=bottom
        self.top=top
        self.current=current
        pass
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current+1<self.top:
            self.current+=1
        pass
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current-1>self.bottom:
            self.current-=1        
        pass
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
        pass
    def __str__(self):
        return "Current floor: {}".format(self.current)
        pass
    
elevator = Elevator(-1, 10, 0)


# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1

elevator.go_to(5)
print(elevator)