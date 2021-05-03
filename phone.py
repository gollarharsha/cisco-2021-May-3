class Phone:
    def __init__(self, id_number):
        self.id_number = id_number
        self.call_history = []

    def call(self, phone_number):
        if phone_number.isdigit():
            self.call_history.append(phone_number)
            return 'OK'

        raise ValueError('Bad phone number')
