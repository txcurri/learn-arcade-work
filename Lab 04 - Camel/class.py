class Address:
    pass

class Character:
    """class that represents the player character"""
    def __int__(self):
        """this a method that sets up the variables in the object"""
        self.name = ""
        self.outfit = ""
        self.max.hit_points = 0
        self.current_hit = 0
        self.armor_amount = 0
        self.max_speed = 0

    def main ():
        # create an address
        home_address = Address()

        home_address.name = "john smith"
        home_address.line1 = "701 N. C Street"
        home_address.line2 = "carver science building"
        home_address.city = "Roy"
        home_address.state = "UT"
        home_address.zip = "84067"

    main()
