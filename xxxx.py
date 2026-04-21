import requests
import json

def check_with_gemini(text_input):
    # کلیل و لینک ل ناڤ فۆنکشنێ بن دا تووشی ئیرۆرا 'not defined' نەبی
    API_KEY = "AIzaSyDPXHVFMbItSRgVpXdVLvdcvM546Jie4yY"
    api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite-preview:generateContent?key={API_KEY}"
    
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{
            "parts": [{
                "text": f"Analyze this text: '{text_input}'. If it contains insults or bad words in Kurdish, reply 'BAD'. Else reply 'GOOD'. Just one word."
            }]
        }]
    }

    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(data))
        result = response.json()
        
        if response.status_code == 200:
            answer = result['candidates'][0]['content']['parts'][0]['text'].strip().upper()
            return answer
        else:
            return f"Error: {result.get('error', {}).get('message', 'Unknown Error')}"
    except Exception as e:
        return f"Exception: {str(e)}"

# تاقیکرن
print("--- Gemini 3.1 Moderator ---")
while True:
    user_text = input("\nنڤیسینێ بنڤیسە: ")
    if user_text.lower() in ['exit', 'قەپات']: break
    if not user_text: continue
    print(f"Result: {check_with_gemini(user_text)}")
