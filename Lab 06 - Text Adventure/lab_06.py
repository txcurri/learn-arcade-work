

class Room:
    """creates a room"""
    def __init__(self, p_description, p_north, p_east, p_south, p_west):
        self.description = p_description
        self.north = p_north
        self.east = p_east
        self.south = p_south
        self.west = p_west
def main ():
    """makes a room list"""
    room_list = []
    #room 0
    my_room = Room("bedroom2, there are doors to your north and east", 3, 1, None, None)
    room_list.append(my_room)
    #room 1
    my_room = Room("south hall, there are doors to your north, east and west", 4, 2, None, 0)
    room_list.append(my_room)
    #room 2
    my_room = Room("dinning room, there are doors to your north and west", 5, None, None, 1)
    room_list.append(my_room)
    #room 3
    my_room = Room("bedroom1, there are doors to your east and south", None, 4, 0, None)
    room_list.append(my_room)
    #room 4
    my_room = Room("north hall, there are doors in all directions", 6, 5, 1, 3)
    room_list.append(my_room)
    #room 5
    my_room = Room("kitchen, there are doors to your south and west", None, None, 2, 4)
    room_list.append(my_room)
    #room 5
    my_room = Room("balcony, there is a door to your south", None, None, 4, None)

    # adding rooms to room_list
    room_list.append(my_room)

    #varible for current room
    current_room = 0

    done = False

    while not done:
        print()
        print("You are now in ")
        print(room_list[current_room].description)

        user_choice: str = input("Where do you want to go? North (N), East (E), South(S) or West(W)?")
        my_result = user_choice.upper() == "N, E, S, W"

        if user_choice.upper() == "N":
            next_room = room_list[current_room].north
        elif user_choice.upper() == "E":
            next_room = room_list[current_room].east
        elif user_choice.upper() == "S":
            next_room = room_list[current_room].south
        elif user_choice.upper() == "W":
            next_room = room_list[current_room].west
        elif user_choice.upper() == "Q":
            done = True
            print("You have quit the game")
            break
        else:
            #eliminates the error if they choose something other that n,e,s,w,q
            next_room = None


        if next_room == None:
            print("you cannot go that way, choose again.")
        else:
            current_room = next_room

if __name__  ==  "__main__":

    main()



