# #VoiceBot UI with gradio

# import os 
# import gradio as gr

# from doctor_brain_1 import encode_image, analyze_image_with_groq

# from patient_voice_2 import transcribe_audio_with_groq,record_audio

# from doctor_voice_3 import text_to_speech_with_gtts, text_to_speech_with_polly

# system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose. 
#             What's in this image?. Do you find anything wrong with it medically? 
#             If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
#             your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
#             Donot say 'In the image I see' but say 'With what I see, I think you have ....'
#             Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
#             Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""


# def process_inputs(audio_filepath, image_filepath):
#     # 1. Transcribe audio
#     transcription = transcribe_audio_with_groq(
#         file_path=audio_filepath,
#         model="whisper-large-v3"
#     )
    
#     # 2. Analyze image (if provided)
#     if image_filepath:
#         doctor_response = analyze_image_with_groq(
#             query=system_prompt + transcription,
#             image_path=image_filepath,
#             model="meta-llama/llama-4-scout-17b-16e-instruct"
#         )
#     else:
#         doctor_response = "No image provided for analysis"
    
#     # 3. Convert to speech
#     tts_path = "doctor_response.mp3"
#     text_to_speech_with_polly(
#         input_text=doctor_response,
#         output_path=tts_path
#     )
    
#     # Return THREE values (not a dictionary)
#     return transcription, doctor_response, tts_path  
    
# # Create the interface
# iface = gr.Interface(
#     fn=process_inputs,
#     inputs=[
#         gr.Audio(sources=["microphone"], type="filepath"),
#         gr.Image(type="filepath")  # For image upload
#     ],
#     outputs=[
#         gr.Textbox(label="Patient Speech"),
#         gr.Textbox(label="Doctor Diagnosis"), 
#         gr.Audio(label="Doctor Voice", autoplay=True)
#     ],
#     title="AI Doctor Chatbot",
#     allow_flagging="never"
# )

# iface.launch()
import os
import gradio as gr
import uuid
from doctor_brain_1 import encode_image, analyze_image_with_groq
from patient_voice_2 import transcribe_audio_with_groq, record_audio
from doctor_voice_3 import text_to_speech_with_polly

# System prompt for the AI doctor
system_prompt = """You have to act as a professional doctor, i know you are not but this is for learning purpose. 
What's in this image?. Do you find anything wrong with it medically? 
If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
Donot say 'In the image I see' but say 'With what I see, I think you have ....'
Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""

# Create temp directory if it doesn't exist
os.makedirs("temp_audio", exist_ok=True)

def process_inputs(audio_filepath, image_filepath):
    # 1. Transcribe audio
    try:
        transcription = transcribe_audio_with_groq(
            file_path=audio_filepath,
            model="whisper-large-v3"
        )
    except Exception as e:
        print(f"Error in transcription: {e}")
        transcription = "Could not transcribe audio"

    # 2. Analyze image (if provided)
    try:
        if image_filepath:
            doctor_response = analyze_image_with_groq(
                query=system_prompt + transcription,
                image_path=image_filepath,
                model="meta-llama/llama-4-scout-17b-16e-instruct"
            )
        else:
            doctor_response = "No image provided for analysis"
    except Exception as e:
        print(f"Error in image analysis: {e}")
        doctor_response = "Could not analyze image"

    # 3. Generate unique filename for each response
    tts_path = f"temp_audio/response_{uuid.uuid4().hex}.mp3"
    
    # 4. Convert to speech
    try:
        text_to_speech_with_polly(
            input_text=doctor_response,
            output_path=tts_path
        )
    except Exception as e:
        print(f"Error in text-to-speech: {e}")
        tts_path = None

    # Clean up old audio files (keep last 5)
    audio_files = sorted(os.listdir("temp_audio"), key=lambda x: os.path.getmtime(os.path.join("temp_audio", x)))
    for old_file in audio_files[:-5]:
        os.remove(os.path.join("temp_audio", old_file))

    return transcription, doctor_response, tts_path if tts_path else None

# Create the Gradio interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath", label="Record your symptoms"),
        gr.Image(type="filepath", label="Upload medical image (optional)")
    ],
    outputs=[
        gr.Textbox(label="Your Symptoms"),
        gr.Textbox(label="Doctor's Diagnosis"), 
        gr.Audio(label="Doctor's Voice Response", autoplay=True)
    ],
    title="AI Doctor VoiceBot 🩺",
    description="Describe your symptoms or upload an image for medical advice",
    allow_flagging="never"
)

# Launch the app
if __name__ == "__main__":
    iface.launch(server_port=7860, share=False)