from parsers import FrenchStyle

from utils.constants import FrenchStyle
from utils.helpers import remove_zero_and_join

from .tens_units import *

from .hundreds import *


class ThousandsAndUp(Hundreds, TensUnits):
    """
        Multiple Inheritance from both the Hundreds and TensUnits classes for defining a way to represent numbers that are above thousand.

    """

    def __init__(self, 
                 number: int, 
                 french_style: str = FrenchStyle.FRANCE_FRENCH.value, 
                 thousands_up_form: Dict = None) -> None:
        """
            Declares all the necessary attributes along with helpers for correctly defining number above thousand.

            Parameters
            -----------
                Same as Base Parser, as this follows a multiple inheritance approach.

            Returns
            -------
                Class object initialized with all required arguments.
        """

        # Here, `remaining_num` is used for further processing of the numbers in an iterative fashion

        self.thousand_up_num_div, self.remaining_num = divmod(number, thousands_up_form["modulus"]) # Refer to Enum `ThousandsAndUpFrenchForm` for the meaning of modulus, basically defines the ten's representatin of a number for french conversion
        self.french_style = french_style

        super().__init__(self.thousand_up_num_div, self.french_style, thousands_up_form)

    def process(self) -> str:
        """
            Defines the processing logic for converting the thousands and above part of the given number.
            
            Returns
            -------
                A string representation of the above thousand part of the number defined by `thousands_up_form`

        """

        if self.thousand_up_num_div == 0:
            return UnitsFrenchForm.ZERO.value # base case, return `zéro` if `thousand_up_num_div` place is 0

        if self.thousand_up_num_div == 1: # base case, return one's form when `thousand_up_num_div` place is 1
            if self.thousands_up_form["text"] == ThousandsAndUpFrenchForm.THOUSAND.value["text"]:
                return self.thousands_up_form["text"]
            else:
                return "-".join([UnitsFrenchForm.ONE.value, self.thousands_up_form['text']])

        hundreds_value = super().process() # base case, Calls the `Hundreds` class for capturing the hundredth part
        tens_units_value = super(Hundreds, self).process() # base case, Calls the `TensUnits` class for capturing the Tens and Units part

        thousands_and_up_value = remove_zero_and_join([hundreds_value, tens_units_value, self.thousands_up_form["text"]])

        if self.remaining_num == 0:
            thousands_and_up_value += "s" # Check and add if number if plural, as defined by french rules

        return thousands_and_up_value
