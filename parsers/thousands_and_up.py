from parsers import FrenchStyle

from utils.constants import FrenchStyle
from utils.helpers import remove_zero_and_join

from .tens_units import *

from .hundreds import *


class ThousandsAndUp(Hundreds, TensUnits):
    def __init__(self, number, french_style=FrenchStyle.FRANCE_FRENCH.value, thousands_up_form=None):
        self.thousand_num_div, self.remaining_num = divmod(number, thousands_up_form["modulus"])
        self.french_style = french_style

        super().__init__(self.thousand_num_div, self.french_style, thousands_up_form)

    def process(self):
        if self.thousand_num_div == 0:
            return UnitsFrenchForm.ZERO.value

        if self.thousand_num_div == 1:
            if self.thousands_up_form["text"] == ThousandsAndUpFrenchForm.THOUSAND.value["text"]:
                return self.thousands_up_form["text"]
            else:
                return "-".join([UnitsFrenchForm.ONE.value, self.thousands_up_form['text']])

        hundreds_value = super().process()
        tens_units_value = super(Hundreds, self).process()

        thousands_value = remove_zero_and_join([hundreds_value, tens_units_value, self.thousands_up_form["text"]])

        if self.remaining_num == 0:
            thousands_value += "s"

        return thousands_value
