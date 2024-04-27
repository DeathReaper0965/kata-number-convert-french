from . import *

from utils.constants import FrenchStyle

from .base import BaseParser


class TensUnits(BaseParser):
    def __init__(self, number, french_style=FrenchStyle.FRANCE_FRENCH.value, thousands_up_form=None):
        super().__init__(number, french_style, thousands_up_form)


    def process(self):
        if self.initial_number%100 == 0:
            return UnitsFrenchForm.ZERO.value
        
        self.tens_units_num = self.initial_number % 100

        tens_place = self.tens_units_num // 10

        # Handling the case, when the values are in the ranges of 11-19 or 70-79 or 90-99
        if tens_place in [1, 7, 9]:
            tens_place -= 1

        tens_reminder = self.tens_units_num - (tens_place * 10)

        curr_tens = UnitsFrenchForm.ZERO.value if tens_place == 0 else self.tens[tens_place-1]

        curr_units = self.units[tens_reminder]

        processed_value = self.combine_values([curr_tens, curr_units])

        if (processed_value.endswith("vingt") and len(processed_value) > len("vingt")):
            processed_value += "s"

        if self.initial_number % 100 not in [1, 11, 81, 91]:
            processed_value = processed_value.replace("-un", "-et-un").replace("-onze", "-et-onze")

        return processed_value


    def combine_values(self, values) -> str:
        processed_value = []

        for _ in values:
            if _ != UnitsFrenchForm.ZERO.value:
                processed_value.append(_)

        processed_value = "-".join(processed_value)

        return str(processed_value)

        