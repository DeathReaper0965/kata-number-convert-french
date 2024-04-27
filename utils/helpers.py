from typing import List

from .constants import UnitsFrenchForm


def remove_zero_and_join(word_list: List[str], delimiter: str = "-") -> str:
    """
        Removes any 0's present and joins them using the french specific delimiter ("-") or any other of our choice.

        Parameters
        ----------
            word_list: List[str]
                A list of french words to the analysed and joined
            delimiter: str
                The french delimiter for joining the words. Defaults to "-"

        Returns
        -------
            A string representation of the joined words.
    """
    
    return delimiter.join([_ for _ in word_list if _ not in [UnitsFrenchForm.ZERO.value, ""]])
