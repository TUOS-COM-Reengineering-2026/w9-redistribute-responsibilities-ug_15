from Staff import Staff


class Branch:

    def __init__(self, location):
        self._location = location
        self._opening = "9:00"
        self._staff = []

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

    def get_opening(self):
        return self._opening

    def set_opening(self, opening):
        self._opening = opening

    def get_staff(self):
        return self._staff

    def add_staff_member(self, staff: Staff):
        self.get_staff().append(staff)

    def transfer_staff_member(self, to_branch, member):
        self.get_staff().remove(member)
        to_branch.get_staff().append(member)

    def transfer_all_staff(self, to_branch):
        while len(self.get_staff()) != 0:
            self.transfer_staff_member(to_branch, self.get_staff()[0])
