from exhaust.exhaust import Exhaust
from utils import add_years_to_date


class SingleExitExhaust(Exhaust):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        date_which_exhaust_should_be_serviced_by = add_years_to_date(self.last_service_date, 3)
        if date_which_exhaust_should_be_serviced_by < self.current_date:
            return True
        else:
            return False
