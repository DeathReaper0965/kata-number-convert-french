from enum import Enum


class FrenchStyle(Enum):
    # Types of French Styles Present for easier access
    FRANCE_FRENCH = 'France-French'
    BELGIUM_FRENCH = 'Belgium-French'


class UnitsFrenchForm(Enum):
    # Initializing the unit forms of each number to French forms
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
    # Initializing the Tens form of 10-90 with both french styles as 
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
    HUNDRED = 'cent'

class PostHundredsFrenchForm(Enum):
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

