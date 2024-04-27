from typing import Any

import gradio as gr

from utils.constants import FrenchStyle, UnitsFrenchForm

from french_converter import FrenchConverter

from parsers import *


def convert_to_french(nums_str: str, french_style: str, output_type: str) -> Any:
    """
        Function that initiates the conversion of the given numerical number to its french form

        Parameters
        ----------
        nums_str: str
            A comma-separated string of the numbers passed through Gradio input field.
        french_style: str
            The type of french to use for conversion. See Enum `FrenchStyle` in `constants.py` file for more details.
        output_type: str
            The type of output desired by user after conversion. See Enum `OutputType` in `constants.py` file for more details.

        Returns
        -------
            A dictonary/list conversion of each `valid` value in the input. Based on the selected `output_type`.
            If any of the value is not a number, `None` is produced as its conversion.


        Limitations:
            1. Currently supports only the numerical part conversion. 
            2. Decimal part and Fractional numbers conversion will be added in the future.
        
    """

    original_values = nums_str.replace("[", "").replace("]", "").replace('"', "").replace("'", "").split(",")

    nums_list = [int(_) if _.strip().isnumeric() else None for _ in original_values]

    french_converted_list = []
    french_converted_json = {}

    for idx, num in enumerate(nums_list):
        if num is None:
            french_converted_list.append(None)
            french_converted_json[original_values[idx]] = None
            continue

        if num == 0:
            converted_val = UnitsFrenchForm.ZERO.value
        else:
            fc_obj = FrenchConverter(num, french_style)
            converted_val = fc_obj.convert()
        
        french_converted_list.append(converted_val)
        french_converted_json[original_values[idx]] = converted_val

    if output_type == OutputType.JSON.value:
        return french_converted_json
    
    return french_converted_list


# initializes the Gradio App
gradio_app = gr.Interface(
    fn=convert_to_french,
    inputs=[
        gr.Text(label="Input List of Numbers (Comma Separated, as shown in placeholder)", placeholder="[0, 10]"), 
        gr.Dropdown(
            choices=[_.value for _ in FrenchStyle], 
            label="Select a French Style", 
            value=FrenchStyle.FRANCE_FRENCH.value),
        gr.Dropdown(
            choices=[_.value for _ in OutputType],
            label="Desired Output Type",
            value=OutputType.JSON.value
        )
    ],
    outputs=gr.Json(label="French Form of the input number list"), 
    allow_flagging="never",
    title="Kata: Number to French Converter"
)

gradio_app.launch()
