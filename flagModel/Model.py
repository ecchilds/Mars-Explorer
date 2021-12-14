class Model():
    def select(self):
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self, name, address, service, phone, stars, active):
        """
        Inserts entry into database
        :param name: String
        :param address: String
        :param service: String
        :param phone: Int
        :param stars: Int
        :param active: Int
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass
