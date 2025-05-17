# AI Doctor VoiceBot 🩺🗣️

A multimodal medical assistant that combines speech recognition, image analysis, and text-to-speech to provide interactive doctor consultations.



## Features ✨

- **Voice Consultation**: Speak naturally to describe symptoms
- **Image Diagnosis**: Upload images for visual analysis
- **AI Doctor Responses**: Get professional-style medical insights
- **Multimodal Integration**: Combines GROQ AI, Whisper ASR, and Amazon Polly
- **Gradio Interface**: User-friendly web UI

## Technologies Used 🛠️

| Component          | Technology |
|--------------------|------------|
| Speech-to-Text     | Whisper (via GROQ API) |
| Image Analysis     | LLaVA (via GROQ API) |
| Text-to-Speech     | Amazon Polly |
| Web Interface      | Gradio |
| Backend            | Python |

##Project Structure
ai-doctor-voicebot/
├── app.py                 # Main Gradio application
├── doctor_brain.py        # Image analysis module
├── patient_voice.py       # Speech recognition module
├── doctor_voice.py        # Text-to-speech module
├── requirements.txt       # Dependencies
├── .env.example           # Environment template
└── README.md              # This file
