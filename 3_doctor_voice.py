# step1a : setup Text to speech - TTS- model with gTTs 
from gtts import gTTS
def text_to_speech_with_gtts_old(input_text,output_path):
    language = "en"
    
    audioObj = gTTS(
        text=input_text,
        lang = language,
        slow=False
    )
    audioObj.save(output_path)
    
# text_to_speech_with_gtts_old(input_text=input_text,output_path="gtts_testing.mp3")

# step1b : setup Text to speech - TTS- model with  amazon polly
import boto3

def text_to_speech_with_polly_old(input_text, output_path):
    polly_client = boto3.Session(
        aws_access_key_id='AKIAR4WHYKSIZU7AQFO2',
        aws_secret_access_key='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',
        region_name='us-east-1'
    ).client('polly')

    response = polly_client.synthesize_speech(
        Text=input_text,
        OutputFormat='mp3',
        VoiceId='Stephen',     # ✅ Valid voice
        Engine='neural'        # ✅ lowercase, valid engine
    )

    with open(output_path, 'wb') as file:
        file.write(response['AudioStream'].read())

    print(f"Audio saved to {output_path}")


# text_to_speech_with_polly_old(input_text=input_text,output_path= "polly_output.mp3")

# step2 : use Model to Text output to voice automatically 

import subprocess
import platform
from playsound import playsound

def text_to_speech_with_gtts(input_text,output_path):
    language = "en"
    
    audioObj = gTTS(
        text=input_text,
        lang = language,
        slow=False
    )
    audioObj.save(output_path)
    
    
    
    os_name = platform.system()
    try:
        if os_name =="Windows":
            subprocess.run(['powershell','-c',f'(New-Object Media.SoundPlayer "{output_path}").PlaySync();'])
        else:
            raise OSError("Unsupported Operating system!")
    except Exception as e : 
        print(f"An Error Occured while trying to play the audio: {e}")
    
input_text = "Hi this is mahmudul using artifical machine learning.This is the new version , testing."

# text_to_speech_with_gtts(input_text=input_text,output_path="gtts_testing.mp3")


def text_to_speech_with_polly(input_text, output_path):
    polly_client = boto3.Session(
        aws_access_key_id='AKIAR4WHYKSIZU7AQFO2',
        aws_secret_access_key='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',
        region_name='us-east-1'
    ).client('polly')

    response = polly_client.synthesize_speech(
        Text=input_text,
        OutputFormat='mp3',
        VoiceId='Stephen',     # ✅ Valid voice
        Engine='neural'        # ✅ lowercase, valid engine
    )

    # Save to MP3
    with open(output_path, 'wb') as file:
        file.write(response['AudioStream'].read())

    print(f"Audio saved to {output_path}")

    # Play MP3 directly
    playsound(output_path)
    
    
    # os_name = platform.system()
    # try:
    #     if os_name =="Windows":
    #         subprocess.run(['powershell','-c',f'(New-Object Media.SoundPlayer "{output_path}").PlaySync();'])
    #     else:
    #         raise OSError("Unsupported Operating system!")
    # except Exception as e : 
    #     print(f"An Error Occured while trying to play the audio: {e}")

# text_to_speech_with_gtts(input_text=input_text,output_path="gtts_testing_autoPlay_testing.wav")
text_to_speech_with_polly(input_text=input_text,output_path="Polly_testing_autoPlay_testing.mp3")