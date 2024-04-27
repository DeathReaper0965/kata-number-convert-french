from utils.constants import *


class BaseParser:
    def __init__(self, number, french_style=FrenchStyle.FRANCE_FRENCH.value, thousands_up_form=None):
        self.initial_number = number
        self.french_style = french_style
        self.thousands_up_form = thousands_up_form

        self.units = [_.value for _ in UnitsFrenchForm]
        
        self.tens = [_.value[self.french_style] if isinstance(_.value, dict) else _.value for _ in TensFrenchForm]

        self.hundreds_forms = [HundredFrenchForm.HUNDRED.value]

        for idx, unit_val in enumerate(UnitsFrenchForm):
            if idx >=2 and idx <=9:
                self.hundreds_forms.append(unit_val.value + "-" + HundredFrenchForm.HUNDRED.value)

    def process(self):
        pass
