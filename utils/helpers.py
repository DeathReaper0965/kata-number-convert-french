from .constants import UnitsFrenchForm


def remove_zero_and_join(word_list, delimiter = "-"):
    return delimiter.join([_ for _ in word_list if _ not in [UnitsFrenchForm.ZERO.value, ""]])
