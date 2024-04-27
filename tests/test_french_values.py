import unittest

from app import convert_to_french
from utils.constants import *


class TestNumberToFrenchConversion(unittest.TestCase):
    """
        Testcases ranging from basics to large numbers.
    """

    def test_units_basics(self) -> None:
        """
            Tests if the Units Form is converted correctly.
        """

        converted_values = []
        original_values = []

        for idx, unit in enumerate(UnitsFrenchForm):
            temp_converted = convert_to_french(nums_str=str(idx), 
                                               french_style=FrenchStyle.FRANCE_FRENCH.value, 
                                               output_type=OutputType.LIST.value)[0]
            
            converted_values.append(temp_converted)
            original_values.append(unit.value)

        self.assertEqual(converted_values, original_values)


    def test_tens_hundreds_basics(self) -> None:
        """
            Tests if the Tens and Hundreds Form is converted correctly.
        """

        converted_values = []
        original_values = []

        for num, ten in zip([10, 20, 30, 40, 50, 60, 70, 80, 90], TensFrenchForm):
            temp_converted = convert_to_french(nums_str=str(num), 
                                               french_style=FrenchStyle.FRANCE_FRENCH.value, 
                                               output_type=OutputType.LIST.value)[0]
            
            converted_values.append(temp_converted)

            if isinstance(ten.value, dict):
                if ten.name == "EIGHTY":
                    original_values.append(ten.value[FrenchStyle.FRANCE_FRENCH.value] + "s")
                else:
                    original_values.append(ten.value[FrenchStyle.FRANCE_FRENCH.value])
            else:
                original_values.append(ten.value)

        converted_values.append(convert_to_french(nums_str=str(100), 
                                                  french_style=FrenchStyle.FRANCE_FRENCH.value, 
                                                  output_type=OutputType.LIST.value)[0])
        original_values.append(HundredFrenchForm.HUNDRED.value)
        
        self.assertEqual(converted_values, original_values)


    def test_thousands_and_up(self):
        """
            Tests if the Thousands and Above Form is converted correctly.
        """

        converted_values = []
        original_values = []

        for num, t_and_up in zip([1000, 1000000, 1000000000], ThousandsAndUpFrenchForm):
            temp_converted = convert_to_french(nums_str=str(num), 
                                               french_style=FrenchStyle.FRANCE_FRENCH.value, 
                                               output_type=OutputType.LIST.value)[0]
            
            converted_values.append(temp_converted)
            original_values.append(t_and_up.value["text"] if num == 1000 else UnitsFrenchForm.ONE.value + "-" + t_and_up.value["text"])

        self.assertEqual(converted_values, original_values)


    def test_json_output(self):
        """
            Tests if the output is generated as JSON as specified in the parameter.
        """

        expected_output_type = type(convert_to_french(nums_str=str(754), 
                                                      french_style=FrenchStyle.FRANCE_FRENCH.value, 
                                                      output_type=OutputType.JSON.value))
        
        self.assertEqual(expected_output_type, dict)


    def test_list_output(self):
        """
            Tests if the output is generated as LIST as specified in the parameter.
        """

        expected_output_type = type(convert_to_french(nums_str=str(754), 
                                                      french_style=FrenchStyle.FRANCE_FRENCH.value, 
                                                      output_type=OutputType.LIST.value))
        
        self.assertEqual(expected_output_type, list)

    
    def test_given_input(self):
        """
            Tests if the given large input is correctly converted.
        """

        given_input = [0, 1, 5, 10, 11, 15, 20, 21, 30, 35, 50, 51, 68, 70, 75, 99, 100, 101, 105, 111, 123, 168, 171, 175, 199, 200, 201, 555, 999, 1000, 1001, 1111, 1199, 1234, 1999, 2000, 2001, 2020, 2021, 2345, 9999, 10000, 11111, 12345, 123456, 654321, 999999]
        actual_result = ['zéro', 'un', 'cinq', 'dix', 'onze', 'quinze', 'vingt', 'vingt-et-un', 'trente', 'trente-cinq', 'cinquante', 'cinquante-et-un', 'soixante-huit', 'soixante-dix', 'soixante-quinze', 'quatre-vingt-dix-neuf', 'cent', 'cent-un', 'cent-cinq', 'cent-onze', 'cent-vingt-trois', 'cent-soixante-huit', 'cent-soixante-et-onze', 'cent-soixante-quinze', 'cent-quatre-vingt-dix-neuf', 'deux-cents', 'deux-cent-un', 'cinq-cent-cinquante-cinq', 'neuf-cent-quatre-vingt-dix-neuf', 'mille', 'mille-un', 'mille-cent-onze', 'mille-cent-quatre-vingt-dix-neuf', 'mille-deux-cent-trente-quatre', 'mille-neuf-cent-quatre-vingt-dix-neuf', 'deux-milles', 'deux-mille-un', 'deux-mille-vingt', 'deux-mille-vingt-et-un', 'deux-mille-trois-cent-quarante-cinq', 'neuf-mille-neuf-cent-quatre-vingt-dix-neuf', 'dix-milles', 'onze-mille-cent-onze', 'douze-mille-trois-cent-quarante-cinq', 'cent-vingt-trois-mille-quatre-cent-cinquante-six', 'six-cent-cinquante-quatre-mille-trois-cent-vingt-et-un', 'neuf-cent-quatre-vingt-dix-neuf-mille-neuf-cent-quatre-vingt-dix-neuf']

        converted_values = []

        for num in given_input:
            converted_values.append(
                convert_to_french(nums_str=str(num), 
                                  french_style=FrenchStyle.FRANCE_FRENCH.value, 
                                  output_type=OutputType.LIST.value)[0]
            )

        self.assertEqual(converted_values, actual_result)


    def test_large_inputs(self):
        """
            Tests if the large inputs (more than millions) are converted correctly
        """

        given_input = [67125476547, 253821224, 96467212531, 8926486267]
        actual_result = ["soixante-sept-milliard-cent-vingt-cinq-million-quatre-cent-soixante-seize-mille-cinq-cent-quarante-sept", 
                         "deux-cent-cinquante-trois-million-huit-cent-vingt-et-un-mille-deux-cent-vingt-quatre", 
                         "quatre-vingt-seize-milliard-quatre-cent-soixante-sept-million-deux-cent-douze-mille-cinq-cent-trente-et-un", 
                         "huit-milliard-neuf-cent-vingt-six-million-quatre-cent-quatre-vingt-six-mille-deux-cent-soixante-sept"]

        converted_values = []

        for num in given_input:
            converted_values.append(
                convert_to_french(nums_str=str(num), 
                                  french_style=FrenchStyle.FRANCE_FRENCH.value, 
                                  output_type=OutputType.LIST.value)[0]
            )

        self.assertEqual(converted_values, actual_result)

