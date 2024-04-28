import re
import logging
from uuid import uuid4
from typing import Any

import gradio as gr

from transformers import pipeline

import numpy as np

from gtts import gTTS

from utils.constants import FrenchStyle, UnitsFrenchForm

from french_converter import FrenchConverter

from parsers import *

logger = logging.getLogger(__name__)


transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base.en")


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

    print(f"Given Input, french-style and output-type: {nums_str}, {french_style}, {output_type}")
    logger.info("Extracting numbers from string, replacing rudimentary symbols and splitting")
    original_values = nums_str.replace("[", "").replace("]", "").replace('"', "").replace("'", "").split(",")

    nums_list = [int(_) if _.strip().isnumeric() else None for _ in original_values]

    french_converted_list = []
    french_converted_json = {}

    logger.info("Loop through the extracted numbers and convert them to french form!")
    for idx, num in enumerate(nums_list):
        if num is None or len(str(num)) > 12:
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

    print(f"Generated Output: {french_converted_json}\n")

    if output_type == OutputType.JSON.value:
        return french_converted_json
    
    return french_converted_list


def recognize_speech_and_tts(audio: gr.Audio, french_style: str) -> str:
    """
        Function that takes the input audio and then transcribes, extracts numbers, converts to french form for the numbers and generates the French Audio accordingly.

        Parameters
        ----------
        audio: gr.Audio
            Speech spoken through a Microphone by the user.
        french_style: str
            The type of french to use for conversion. See Enum `FrenchStyle` in `constants.py` file for more details.

        Returns
        -------
            A string specifying the location of the generated audio file.
        
    """

    logger.info("Extracting sampling rate and raw speech from the spoken audio!")
    sampling_rate, raw = audio
    
    raw = raw.astype(np.float32)
    raw /= np.max(np.abs(raw))

    file_random_uuid = uuid4().__str__().split("-")[-1]
    audio_file_name = f"generated_audio/audio-{file_random_uuid}.wav"

    speech_output = transcriber(
        {
            "sampling_rate": sampling_rate, 
            "raw": raw
        }
    )
    
    speech_output_txt = speech_output["text"]

    logger.info("Converted Audio and now Extracting Numbers")

    recognized_nums = re.findall(r'\b\d+\b', speech_output_txt)

    if len(recognized_nums) == 0:
        print("No Numbers found, returning back with sorry message!")

        speech_prompt = SpeechOutputs.SORRY_MSG.value
        generated_speech = gTTS(text=speech_prompt, 
                                lang=SpeechLangs.EN.value, 
                                slow=True, 
                                tld=SpeechLangs.FR.value)
        generated_speech.save(audio_file_name)

        return audio_file_name
    
    print("Calling `convert_to_french` from Speech function!")
    converted_nums = convert_to_french(nums_str=", ".join(recognized_nums), 
                                       french_style=french_style, 
                                       output_type=OutputType.LIST.value)
    
    converted_nums = [_.replace("-", " ") for _ in converted_nums]

    converted_nums_str = SpeechOutputs.AND_CONNECTOR.value.join(converted_nums)

    speech_prompt = SpeechOutputs.SUCCESS_MSG.value + converted_nums_str

    print(f"Generating the speech of the constructed prompt: {speech_prompt}\n\n")

    generated_speech = gTTS(text=speech_prompt, 
                            lang=SpeechLangs.FR.value, 
                            slow=True, 
                            tld=SpeechLangs.FR.value
                        )
    generated_speech.save(audio_file_name)

    return audio_file_name


def main():
    # Initializes the Gradio App

    with gr.Blocks(title="Kata: Number to French Converter") as gradio_app:
        gr.Markdown(
        """
        # Kata: Number to French Converter
        """
        )

        with gr.Tab("Using Text"):
            input_numbers_txt = gr.Text(
                label="Input List of Numbers (Comma Separated, as shown in placeholder)", 
                placeholder="[0, 10]"
            )

            french_style_dropdown_txt = gr.Dropdown(
                choices=[_.value for _ in FrenchStyle], 
                label="Select a French Style", 
                value=FrenchStyle.FRANCE_FRENCH.value
            )

            output_type_dropdown_txt = gr.Dropdown(
                choices=[_.value for _ in OutputType],
                label="Desired Output Type",
                value=OutputType.JSON.value
            )

            text_buttton = gr.Button("Convert to French Form", 
                                     variant="primary", 
                                     scale=0)

            output_json = gr.Json(label="French Form of the input number list")

            text_buttton.click(convert_to_french, 
                               inputs=[input_numbers_txt, 
                                       french_style_dropdown_txt, 
                                       output_type_dropdown_txt], 
                               outputs=output_json)
            
        with gr.Tab("Using Speech"):
            audio_input = gr.Audio(sources=["microphone"], 
                                   label="Click on `Record` to speak through your Microphone and press `Stop` when done", 
                                   show_download_button=True)

            french_style_dropdown_speech = gr.Dropdown(
                choices=[_.value for _ in FrenchStyle], 
                label="Select a French Style", 
                value=FrenchStyle.FRANCE_FRENCH.value
            )

            speech_button = gr.Button("Recognize Numbers and Generate French Form Audio", 
                                      variant="primary", 
                                      scale=0)
            
            audio_output = gr.Audio(autoplay=True, 
                                    label="Generated Speech", 
                                    show_download_button=True)
            
            speech_button.click(recognize_speech_and_tts, 
                                inputs=[audio_input, french_style_dropdown_speech], 
                                outputs=audio_output)

        logger.info("Launching Gradio App Interface for accepting inputs!") 
        gradio_app.launch()


if __name__ == '__main__':
    main()
