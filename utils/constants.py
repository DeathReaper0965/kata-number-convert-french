from enum import Enum


class FrenchStyle(Enum):
    """
        Types of French Styles currently supported for easier access and definition.
    """

    FRANCE_FRENCH = 'France-French'
    BELGIUM_FRENCH = 'Belgium-French'


class UnitsFrenchForm(Enum):
    """
        Enum for the unit form constants of each number to French forms.
    """

    ZERO = 'zéro'
    ONE = 'un'
    TWO = 'deux'
    THREE = 'trois'
    FOUR = 'quatre'
    FIVE = 'cinq'
    SIX = 'six'
    SEVEN = 'sept'
    EIGHT = 'huit'
    NINE = 'neuf'
    TEN = 'dix'
    
    # We will also add the 11-19 case here as they are constants as well
    ELEVEN = 'onze'
    TWELVE = 'douze'
    THIRTEEN = 'treize'
    FOURTEEN = 'quatorze'
    FIFTEEN = 'quinze'
    SIXTEEN = 'seize'
    SEVENTEEN = 'dix-sept'
    EIGHTEEN = 'dix-huit'
    NINETEEN = 'dix-neuf'


class TensFrenchForm(Enum):
    """
        Enum for the Tens form of 10-90 in all french styles.
        Also provides easier access if a new french style is added in the future. 
        Moreover, this is handled automatically in the BaseParser class.
    """

    TEN = 'dix'
    TWENTY = 'vingt'
    THIRTY = 'trente'
    FOURTY = 'quarante'
    FIFTY = 'cinquante'
    SIXTY = 'soixante'
    SEVENTY = {
        FrenchStyle.FRANCE_FRENCH.value: 'soixante-dix', 
        FrenchStyle.BELGIUM_FRENCH.value: 'septante'
    }
    EIGHTY = {
        FrenchStyle.FRANCE_FRENCH.value: 'quatre-vingt', 
        FrenchStyle.BELGIUM_FRENCH.value: 'huitante'
    }
    NINETY = {
        FrenchStyle.FRANCE_FRENCH.value: 'quatre-vingt-dix', 
        FrenchStyle.BELGIUM_FRENCH.value: 'nonante'
    }
    

class HundredFrenchForm(Enum):
    """
        Representation of hundred in its french form. 
        Declared separately here as conditions vary for numbers greater than hundered and below thousand.
    """

    HUNDRED = 'cent'


class ThousandsAndUpFrenchForm(Enum):
    """
        Representation of numbers that are thousands and up.
        Provides a very easy one-stop way to register higher numbers.
        Just define the required higher number here and you're good to go.
    """

    THOUSAND = {
        'text': 'mille',
        'modulus': 10**3
    }

    MILLION = {
        'text': 'million',
        'modulus': 10**6
    }

    MILLIARD = {
        'text': 'milliard',
        'modulus': 10**9
    }


class OutputType(Enum):
    """
        Types of output desired by the user.
    """

    JSON = 'JSON'
    LIST = 'LIST'
