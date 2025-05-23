# #step1:  setup GROQ API key
# import os 

# GROQ_API_KEY = "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"


# #step2:  convert image to required format
# import base64

# # image_path = "aimage.jpg"
# #image_file = open(image_path, "rb")
# # encoded_image = base64.b64encode(image_file.read()).decode("utf-8")


# def encode_image(image_path):
#     image_file = open(image_path,"rb")
    
#     return base64.b64encode(image_file.read()).decode("utf-8")
    



# #step3: setup Multimodal LLM 
# from groq import Groq

# client = Groq(api_key=GROQ_API_KEY)
# query = "is there anything wrong with my face ?"
# model = "meta-llama/llama-4-scout-17b-16e-instruct"
# messages=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text", 
#                     "text": query
#                 },
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": f"data:image/jpeg;base64,{encoded_image}",
#                     },
#                 },
#             ],
#         }]

# chat_completion = client.chat.completions.create(messages= messages, model=model)

# print(chat_completion.choices[0].message.content)


import os
import base64
from groq import Groq

# Step 1: Set your GROQ API key
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)


# Step 2: Encode the image to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Step 3: Analyze image with GROQ's multimodal LLM
def analyze_image_with_groq(image_path, query, model="meta-llama/llama-4-scout-17b-16e-instruct"):
    encoded_image = encode_image(image_path)

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }
    ]

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content


