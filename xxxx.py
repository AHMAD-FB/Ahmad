import requests
import json

# کلیلێ لێرە دانە
API_KEY = "AIzaSyDPXHVFMbItSRgVpXdVLvdcvM546Jie4yY"

# بەکارهێنانا مۆدێلێ Gemini 3.1 Flash Lite کو د لیستێ دا هەبوو
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite-preview:generateContent?key={API_KEY}"

def check_with_gemini(text_input):
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{
            "parts": [{
                "text": f"Analyze this text: '{text_input}'. If it contains insults or bad words in Kurdish, reply 'BAD'. Else reply 'GOOD'. Just one word."
            }]
        }]
    }

    try:
        response = requests.post(URL, headers=headers, data=json.dumps(data))
        result = response.json()
        
        if response.status_code == 200:
            answer = result['candidates'][0]['content']['parts'][0]['text'].strip().upper()
            return answer
        else:
            return f"Error: {result['error']['message']}"
    except Exception as e:
        return f"Exception: {str(e)}"

# تاقیکرن ل تێرمینالێ
print("--- Gemini 3.1 Moderator ---")
while True:
    user_text = input("\nنڤیسینێ بنڤیسە: ")
    if user_text.lower() == 'exit': break
    print(f"Result: {check_with_gemini(user_text)}")
