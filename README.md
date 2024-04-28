# Kata: Number to French Converter

This repo presents an adventure of approaches for converting a number to french format strings(words).

Made using [Gradio](https://www.gradio.app/) for two main reasons:
1. Gradio provides an excellet UI for easily accessing the application with required parameters.
2. For integrating the Speech Recognition([Whisper-Base](https://huggingface.co/openai/whisper-base)) and Text-To-Speech([Google TTS](https://gtts.readthedocs.io/en/latest/)) models for converting the spoken numbers to their french audio representations.


## Features
This application has TWO core functionalities. Their details are as follows:

### First Tab - Accepts the input numbers as a string and returns their french form as outputs 

1. **Input List of numbers:** [MANDATORY] This is a comma separated string that is splitted internally to process one number at a time.
2. **French Style**: [OPTIONAL] Currently two French Styles are followed, select from either of `France-French` or `Belgium-french`. Defaults to `France-French`.
3. **Output Type**: [OPTIONAL] Either of `JSON` or `LIST`. Defaults to `JSON`.
    - if `JSON` is selected, a Dictionary of values corresponding to each input number is displayed.
    - if `LIST` is selected, a List of values are displayed in the given order of the input.

### Second Tab - Accepts the input numbers as Speech and returns the French Form of them as a Speech

1. **Record**: [MANDATORY] Speak through your microphone in the form of "Convert the numbers << Some Numbers here >> to their French Form"
   - Example: "Convert the numbers 45 and 999 to their French Forms"
2. **French Style**: [OPTIONAL] Currently two French Styles are followed, select from either of `France-French` or `Belgium-french`. Defaults to `France-French`.


## Installation
Follow the below steps to run the application in your local machine:
1. Clone the repo: `git clone https://github.com/DeathReaper0965/kata-number-convert-french.git`
2. Navigate to the repo: `cd kata-number-convert-french`
3. Create a new python 3.11 environment using: `conda create -n kata python=3.11` (This is helpful for separating the application's dependencies from system dependencies)
4. Activate the environment: `conda activate kata`
5. Install all required dependencies: `pip install -r requirements.txt`
6. For supporting Speech, we have to install just one more dependency of `ffmpeg` as it helps us in captuning audio from Microphone. Install it from this page: https://www.ffmpeg.org/download.html

**TIP**: All the steps from 3-5 can also be done by just executing `sh install.sh` from terminal. However, you still have to download `ffmeg` separately.

#### That's it, we're all done with the installation and all that's left is to start the app.

## Start the Application
To start the [Gradio](https://www.gradio.app/) app, just execute the below command from the root folder of the repo.<br>
`python app.py`
<br>

Once started, just head over to [http://localhost:7860/](http://localhost:7860/) in any browser of your choice to see the application in action 😄

**NOTE:** For the very first call, it may take time for the output as Gradio initializes some necessary cache, downloades the HuggingFace Models, etc. However, all the subsequent calls will be very fast (often within fraction of seconds).


## Executing Tests
UnitTest cases are added under the folder `tests/`. From root folder, execute the test cases using the following command:<br>
`python -m unittest discover tests "*.py" -v`


## Demo Images Using Text

1. An example with a choice of French-Style as "France" and Output type as "Json"
![Example-france-french-json](https://github.com/DeathReaper0965/kata-number-convert-french/blob/main/demo_images/Example-france-french-json.png?raw=true)

2. An example showcasing large numbers (upto Milliards/Billions)
![Example-Milliards](https://github.com/DeathReaper0965/kata-number-convert-french/blob/main/demo_images/Example-Milliards.png?raw=true)

3. An example with a choice of French-Style as "Belgium" and Output type as "Json"
![Example-belgium-french-json](https://github.com/DeathReaper0965/kata-number-convert-french/blob/main/demo_images/Example-belgium-french-json.png?raw=true)

4. An example with a choice of French-Style as "France" and Output type as "List"
![Example-france-french-list](https://github.com/DeathReaper0965/kata-number-convert-french/blob/main/demo_images/Example-france-french-list.png?raw=true)

5. An example showcasing long inputs (large number of numbers to be converted)
![Example-Long-Inputs](https://github.com/DeathReaper0965/kata-number-convert-french/blob/main/demo_images/Example-Long-Inputs.png?raw=true)


## Demo Videos Using Speech
1. An example with only a Single Input Number in Spoken Input Audio
![Example-Single-Numbers-In-Speech](https://github.com/DeathReaper0965/kata-number-convert-french/blob/main/demo_videos/Example-Single-Numbers-In-Speech.mp4?raw=true)

2. An example with Multiple Input Numbers in Spoken Input Audio
![Example-Multiple-Numbers-In-Speech](https://github.com/DeathReaper0965/kata-number-convert-french/blob/main/demo_videos/Example-Multiple-Numbers-In-Speech.mp4?raw=true)

3. An example with NO Numbers in Spoken Input Audio
![Example-No-Numbers-In-Speech](https://github.com/DeathReaper0965/kata-number-convert-french/blob/main/demo_images/Example-No-Numbers-In-Speech.mp4?raw=true)


### Current Limitations and Next Steps
1. Currently supports only the numerical part conversion. 
2. Decimal part and Fractional numbers conversion to be added.
