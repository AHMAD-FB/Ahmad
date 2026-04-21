def check_with_gemini(text_input):
    # هەمی import کان ل ڤێرە دانە دا تووشی ئیرۆرا 'not defined' نەبی
    import requests
    import json

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
        if response.status_code == 200:
            result = response.json()
            return result['candidates'][0]['content']['parts'][0]['text'].strip().upper()
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Exception: {str(e)}"

# ئەڤ بەشە دێ مینیت وەک خۆ
print("--- Gemini 3.1 Moderator ---")
while True:
    user_text = input("\nنڤیسینێ بنڤیسە: ")
    if user_text.lower() in ['exit', 'quit']: break
    if not user_text: continue
    print(f"Result: {check_with_gemini(user_text)}")
