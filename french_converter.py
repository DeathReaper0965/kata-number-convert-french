import logging
from parsers import *

from utils.helpers import remove_zero_and_join

logger = logging.getLogger(__name__)


class FrenchConverter:
    """
        A class that actually converts the given number by following all the steps iteratively to its french form.
    """

    def __init__(self, 
                 num: int, 
                 french_style: str) -> None:
        """
            Declares all the necessary attributes for the number conversion along with helpers wherever required.

            Parameters
            -----------
                num: int
                    An integer that is to be converted to french form
                french_style: str
                    Type of french style to be used for converting the number. Refer to `constants.py` file for more.

            Returns
            -------
                Class object initialized with all required arguments.
        """

        self.curr_num = num
        self.req_french_values = []
        self.french_style = french_style

        # A one-stop shop for defining all required forms that are thousand and above.
        # Just defining in this one place will automatically takes care of the conversion to any higher french representation
        # An Enum key in `ThousandsAndUpFrenchForm` in `constants.py` file and its declaration here are enough for auto-conversion
        self.registered_thousand_and_up = [
            ThousandsAndUpFrenchForm.MILLIARD.value,
            ThousandsAndUpFrenchForm.MILLION.value, 
            ThousandsAndUpFrenchForm.THOUSAND.value
        ]

    def convert(self) -> str:
        """
            French number conversion logic that follows the required rules and takes care of all registered thousands and up numbers.Currenlty added support till `Milliards`.

            Returns
            -------
            A French representation of the given number.
        """

        logger.info("Checking and Converting for thousands and above numbers")
        for thousands_up_form in self.registered_thousand_and_up: # Looping as there's little difference as we go higher than thousands 
            thousands_up_obj = ThousandsAndUp(self.curr_num, french_style=self.french_style, thousands_up_form=thousands_up_form)
            thousands_up_value = thousands_up_obj.process()

            self.req_french_values.append(thousands_up_value)
            self.curr_num = thousands_up_obj.remaining_num

        logger.info("Checking and Converting for Hundreds form of the number")
        hundreds_obj = Hundreds(thousands_up_obj.remaining_num, french_style=self.french_style)
        hundreds_value = hundreds_obj.process()
        self.req_french_values.append(hundreds_value)

        logger.info("Checking and Converting for Tens and Units form of the number")
        fnum_obj = TensUnits(thousands_up_obj.remaining_num, french_style=self.french_style) # NOTE: We're passing hundredth part here and taking care of it internally for consistency and also for adhering to French rules.
        fnum_value = fnum_obj.process()
        self.req_french_values.append(fnum_value)
        
        logger.info("Stitch all of them together and return!")
        return remove_zero_and_join(self.req_french_values)
