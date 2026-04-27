class Payroll:
    def __init__(self):
        self.staff_category_pay_schedules = {"Manager": "1st"}

    def get_staff_category_pay_schedule(self, staff_category):
        return self.staff_category_pay_schedules[staff_category]

    def set_staff_category_pay_schedule(self, staff_category, pay_date):
        self.staff_category_pay_schedules[staff_category] = pay_date