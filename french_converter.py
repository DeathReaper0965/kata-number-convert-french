from parsers import *

from utils.helpers import remove_zero_and_join


class FrenchConverter:
    def __init__(self, num, french_style):
        self.curr_num = num
        self.req_french_values = []
        self.french_style = french_style
        self.registered_thousand_and_up = [
            ThousandsAndUpFrenchForm.MILLIARD.value,
            ThousandsAndUpFrenchForm.MILLION.value, 
            ThousandsAndUpFrenchForm.THOUSAND.value
        ]

    def convert(self):

        for thousands_up_form in self.registered_thousand_and_up:
            thousands_up_obj = ThousandsAndUp(self.curr_num, french_style=self.french_style, thousands_up_form=thousands_up_form)
            thousands_up_value = thousands_up_obj.process()

            self.req_french_values.append(thousands_up_value)
            self.curr_num = thousands_up_obj.remaining_num

        hundreds_obj = Hundreds(thousands_up_obj.remaining_num, french_style=self.french_style)
        hundreds_value = hundreds_obj.process()
        self.req_french_values.append(hundreds_value)

        fnum_obj = TensUnits(thousands_up_obj.remaining_num, french_style=self.french_style)
        fnum_value = fnum_obj.process()
        self.req_french_values.append(fnum_value)
        
        return remove_zero_and_join(self.req_french_values)
