# # step1 : setup audio recorder (ffmpeg & portaudio)
# import logging
# import speech_recognition  as sr
# from pydub import AudioSegment
# from io import BytesIO

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# def record_audio(file_path, timeout=20, phrase_time_limit=None):
#     """
#     Simplified function to record audio from the microphone and save it as an MP3 file.

#     Args:
#     file_path (str): Path to save the recorded audio file.
#     timeout (int): Maximum time to wait for a phrase to start (in seconds).
#     phrase_time_lfimit (int): Maximum time for the phrase to be recorded (in seconds).
#     """
#     recognizer = sr.Recognizer()
    
#     try:
#         with sr.Microphone() as source:
#             logging.info("Adjusting for ambient noise...")
#             recognizer.adjust_for_ambient_noise(source, duration=1)
#             logging.info("Start speaking now...")
            
#             # Record the audio
#             audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
#             logging.info("Recording complete.")
            
#             # Convert the recorded audio to an MP3 file
#             wav_data = audio_data.get_wav_data()
#             audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
#             audio_segment.export(file_path, format="mp3", bitrate="128k")
            
#             logging.info(f"Audio saved to {file_path}")

#     except Exception as e:
#         logging.error(f"An error occurred: {e}")
# audio_file_path = "patient_voice_test.mp3"
# record_audio(file_path= audio_file_path)

# # step2 : setup speech to text - STT - momdel for transcription
# from groq import Groq
# GROQ_API_KEY = "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"
# client = Groq(api_key=GROQ_API_KEY)
# stt_model = "whisper-large-v3"
# audio_file = open(audio_file_path,"rb")
# transcription = client.audio.transcriptions.create(
#     model=stt_model,
#     file= audio_file,
#     language="en" 
# )

# print(transcription.text)



import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
from groq import Groq

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize GROQ client
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)


def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """
    Record audio from microphone and save it as an MP3 file.

    Args:
        file_path (str): Path to save the MP3 file.
        timeout (int): Time to wait for speech to start.
        phrase_time_limit (int): Max duration of the phrase to capture.
    """
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")
            
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")
            
            # Save audio as MP3
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occurred during recording: {e}")


def transcribe_audio_with_groq(file_path, model="whisper-large-v3", language="en"):
    """
    Transcribe audio file using Groq's Whisper model.

    Args:
        file_path (str): Path to the audio file.
        model (str): Whisper model version.
        language (str): Language of the speech in the audio.

    Returns:
        str: Transcribed text.
    """
    try:
        with open(file_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model=model,
                file=audio_file,
                language=language
            )
        return transcription.text

    except Exception as e:
        logging.error(f"An error occurred during transcription: {e}")
        return None