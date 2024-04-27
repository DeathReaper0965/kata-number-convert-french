from typing import Dict, List

from . import *

from utils.constants import FrenchStyle
from utils.helpers import remove_zero_and_join

from .base import BaseParser


class TensUnits(BaseParser):
    """
        Inherited from BaseParser class, defines a way to represent numbers that are below hundred by following the french rules.
    """

    def __init__(self, 
                 number: int, 
                 french_style: str = FrenchStyle.FRANCE_FRENCH.value, 
                 thousands_up_form: Dict = None) -> None:
        """
            Declares all the necessary attributes for the base parser along with helpers for correctly defining number below hundred.

            Parameters
            -----------
                Same as Base Parser

            Returns
            -------
                Class object initialized with all required arguments.
        """
        super().__init__(number, french_style, thousands_up_form)


    def process(self) -> str:
        """
            Defines the processing logic for converting the below hundredth part of the given number.
            
            Returns
            -------
                A string representation of the tens and units part of the number.

            NOTE: 
                1. We consider the number in its hundred's form here due to the constraint of the french conversion for numbers other than [1, 11, 81, 91].
                2. Considering the hundred's form also helps us in organizing a more modular code with not much variable exchanges.

        """

        if self.initial_number%100 == 0:
            return UnitsFrenchForm.ZERO.value # base case, return `zéro` if hundredth place is 0
        
        self.tens_units_num = self.initial_number % 100

        tens_place = self.tens_units_num // 10

        # Handling the case, when the values are in the ranges of 11-19 or 70-79 or 90-99
        if tens_place in [1, 7, 9]:
            tens_place -= 1

        tens_reminder = self.tens_units_num - (tens_place * 10)

        curr_tens = UnitsFrenchForm.ZERO.value if tens_place == 0 else self.tens[tens_place-1]

        curr_units = self.units[tens_reminder]

        processed_value = remove_zero_and_join([curr_tens, curr_units])

        if processed_value.endswith("vingt") and len(processed_value) > len("vingt"):
            processed_value += "s" # Check to make the convertion to be plural

        if self.initial_number % 100 not in [1, 11, 81, 91]: # Check to add `-et` for to the required places where number ends with "1"
            processed_value = processed_value.replace("-un", "-et-un").replace("-onze", "-et-onze")

        return processed_value
        