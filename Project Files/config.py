import google.generativeai as genai

# Configure API Key
API_KEY = "AIzaSyAvyqiMDkyZg1ugNo0NxlFhsPV0CEXLs7w"

genai.configure(api_key=API_KEY)

# Generation settings
GENERATION_CONFIG = {
    "temperature": 0.75,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
