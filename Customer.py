class Customer:
    def __init__(self, name: str):
        self._name = name
        self._adr = "NO ADDRESS"  # default address
        self._phone = "NO PHONE NUMBER"  # default phone number

    def set_name(self, name: str):
        self._name = name

    def get_name(self):
        return self._name

    def set_address(self, adr: str):
        self._adr = adr

    def get_address(self):
        return self._adr

    def set_phone(self, phone: str):
        self._phone = phone

    def get_phone(self):
        return self._phone

