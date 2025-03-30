import openai
openai.api_key = "你的_API_KEY"  # 請替換成你的 API Key

functions_description = '''
你是 TurtleBot4 控制專家。以下是可用函式：
1. move_forward(distance=1.0, speed=0.2)
2. turn(angle_deg=90, angular_speed=0.5)
請將中文指令轉為上述格式的函式呼叫。
'''

def language_to_code(text):
    prompt = functions_description + f"\n使用者指令：「{text}」\n對應函式："
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()
