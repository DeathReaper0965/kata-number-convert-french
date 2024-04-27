import logging
from typing import Dict

from . import *

from utils.constants import FrenchStyle

from .base import BaseParser

logger = logging.getLogger(__name__)


class Hundreds(BaseParser):
    """
        Inherited from BaseParser class, defines a way to represent numbers that are above hundred by following the french rules.
    """

    def __init__(self, 
                 number: int, 
                 french_style: str = FrenchStyle.FRANCE_FRENCH.value, 
                 thousands_up_form: Dict = None) -> None:
        """
            Declares all the necessary attributes for the base parser along with helpers for correctly defining number in hundreds.

            Parameters
            -----------
                Same as Base Parser

            Returns
            -------
                Class object initialized with all required arguments.
        """
        self.hundredth_place = number // 100

        super().__init__(number, french_style, thousands_up_form)

    def process(self) -> str:
        """
            Defines the processing logic for converting the hundredth part of the given number.
            
            Returns
            -------
                A string representation of the hundredth part of the number
        """
        if self.hundredth_place == 0:
            return UnitsFrenchForm.ZERO.value # base case, return `zéro` if hundredth place is 0
        
        if self.hundredth_place == 1:
            return HundredFrenchForm.HUNDRED.value # base case, return without plurality if hundredth place is 1
        
        hundreds_value = self.hundreds_forms[self.hundredth_place-1]

        if self.initial_number % 100 == 0: # checking the number's tens and unit place for adding plurality.
            logger.info("Adding Plurality to Hundreds")
            hundreds_value += "s"
        
        return hundreds_value
