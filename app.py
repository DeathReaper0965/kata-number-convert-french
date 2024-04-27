import gradio as gr

from utils.constants import FrenchStyle, UnitsFrenchForm

from french_converter import FrenchConverter

from parsers import *


def convert_to_french(nums_list, french_style):
    nums_list = eval(nums_list)

    french_converted = []

    for num in nums_list:
        if num == 0:
            converted_val = UnitsFrenchForm.ZERO.value
        else:
            fc_obj = FrenchConverter(num, french_style)
            converted_val = fc_obj.convert()
        
        french_converted.append(converted_val)

    return french_converted


gradio_app = gr.Interface(
    fn=convert_to_french,
    inputs=[
        gr.Text(label="Input List of Numbers", placeholder="[0, 10]"), 
        gr.Dropdown(
            choices=[_.value for _ in FrenchStyle], 
            label="Select a French Style", 
            value=FrenchStyle.FRANCE_FRENCH.value)
        ],
    outputs=gr.Text(label="French Form of the input number list"), 
    allow_flagging="never",
    title="Kata: Number to French Converter"
)

gradio_app.launch()
