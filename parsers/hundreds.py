from . import *

from utils.constants import FrenchStyle

from .base import BaseParser


class Hundreds(BaseParser):
    def __init__(self, number, french_style=FrenchStyle.FRANCE_FRENCH.value, thousands_up_form=None):
        self.hundredth_place = number // 100

        super().__init__(number, french_style, thousands_up_form)

    def process(self):
        if self.hundredth_place == 0:
            return UnitsFrenchForm.ZERO.value
        
        if self.hundredth_place == 1:
            return HundredFrenchForm.HUNDRED.value
        
        hundreds_value = self.hundreds_forms[self.hundredth_place-1]

        if self.initial_number % 100 == 0:
            hundreds_value += "s"
        
        return hundreds_value
