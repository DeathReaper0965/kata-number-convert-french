from typing import Dict, Any

from utils.constants import *


class BaseParser:
    """
        The Base Parser class which is the Parent class for all parsers.
        This has the important information that sets the initial number that's to be converted to French format along with 
        multiple french styles (currently supported, France-French and Belgian-French).
    """

    def __init__(self, 
                 number: int, 
                 french_style: str = FrenchStyle.FRANCE_FRENCH.value, 
                 thousands_up_form: Dict = None) -> None:
        """
            Constructs all the necessary attributes for initializing the base parser.

            Parameters
            -----------
                number: int
                    The base number initiazed to be converted to french which may undergo transformation in the child classes.
                french_style: str
                    Type of french style to be used for converting the number. Refer to `constants.py` file for more. Defaults to `France-French`.
                thousands_up_form: Dict
                    A dictionary of the french representation for numbers greater than thousand. Refer to `constants.py` file for more. Defaults to `None`.

            Returns
            -------
                Class object initialized with all required arguments.
        """

        self.initial_number = number
        self.french_style = french_style
        self.thousands_up_form = thousands_up_form

        self.units = [_.value for _ in UnitsFrenchForm]
        
        self.tens = [_.value[self.french_style] if isinstance(_.value, dict) else _.value for _ in TensFrenchForm]

        self.hundreds_forms = [HundredFrenchForm.HUNDRED.value]

        for idx, unit_val in enumerate(UnitsFrenchForm):
            if idx >=2 and idx <=9:
                self.hundreds_forms.append(unit_val.value + "-" + HundredFrenchForm.HUNDRED.value)

    def process(self) -> Any:
        """
            Method definition to be initized in the child classes.
            
            Returns
            -------
                Any: Can return anything based on the method definition in the child.
        """
        pass
