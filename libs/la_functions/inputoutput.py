class InputOutput:

    
    def input_int(self, messaggio, errore):
        """
        Intero
        """
        while True:
            try:
                return int(input(messaggio))
            except ValueError:
                print("{}".format(errore))

    
    def input_float(self, messaggio, errore):
        """
        Decimali
        """
        while True:
            try:
                return float(input(messaggio))
            except ValueError:
                print("{}".format(errore))

    
    def input_string(self, messaggio, errore):
        """
        Stringa
        """
        user_input = input(messaggio)
        while not user_input:
            print("{}".format(errore))
            user_input = input(messaggio)
        return user_input
