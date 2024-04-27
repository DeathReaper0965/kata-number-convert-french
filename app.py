import gradio as gr

from utils.constants import FrenchStyle, UnitsFrenchForm
from utils.helpers import remove_zero_and_join

from parsers import *


def convert_to_french(nums_list, french_style):
    nums_list = eval(nums_list)

    french_converted = []

    for num in nums_list:
        if num == 0:
            french_converted.append(UnitsFrenchForm.ZERO.value)
        else:
            curr_num = num
            req_french_values = []

            for thousands_up_form in [PostHundredsFrenchForm.MILLION.value, PostHundredsFrenchForm.THOUSAND.value]:
                thousands_up_obj = ThousandsAndUp(curr_num, french_style=french_style, thousands_up_form=thousands_up_form)
                thousands_up_value = thousands_up_obj.process()

                req_french_values.append(thousands_up_value)
                curr_num = thousands_up_obj.remaining_num

            hundreds_obj = Hundreds(thousands_up_obj.remaining_num, french_style=french_style)
            hundreds_value = hundreds_obj.process()
            req_french_values.append(hundreds_value)

            fnum_obj = TensUnits(thousands_up_obj.remaining_num, french_style=french_style)
            fnum_value = fnum_obj.process()
            req_french_values.append(fnum_value)
            
            french_converted.append(remove_zero_and_join(req_french_values))


    return french_converted


gradio_app = gr.Interface(
    fn=convert_to_french,
    inputs=[
        gr.Text(label="Input List of Numbers", placeholder="[0, 10]"), 
        gr.Dropdown(
            choices=[FrenchStyle.FRANCE_FRENCH.value, FrenchStyle.BELGIUM_FRENCH.value], 
            label="Select a French Style", 
            value=FrenchStyle.FRANCE_FRENCH.value)
        ],
    outputs=gr.Text(label="French Form of the input number list"), 
    allow_flagging="never"
)

gradio_app.launch()
