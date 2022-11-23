class Room:
    def __init__(self, rnumber, rfloor, rcapacity):
        self.room_number=rnumber
        self.room_floor=rfloor
        self.room_capacity=rcapacity
    def get_room_info(self):
        return (f"Room Number: {self.room_number}, Room floor: {self.room_floor}, Room capacity: {self.room_capacity}")


