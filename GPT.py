from openai import OpenAI
from time import time

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="sk-vSNSmOgCwAtIPfc8G0PVh1skulT6ZbEcJj96DjpVIfk0pJNE",
    base_url="https://api.chatanywhere.tech/v1"
)




def print_color(text, color):
    color_codes = {
        "black": "30", "red": "31", "green": "32", "yellow": "33", "blue": "34",
        "magenta": "35", "cyan": "36", "white": "37"
    }
    color_code = color_codes.get(color.lower(), "37")
    print(f"\033[{color_code}m{text}\033[0m",end = "")



# 非流式响应
def gpt_35_api(messages: list):
    """为提供的对话消息创建新的回答

    Args:
        messages (list): 完整的对话消息
    """
    completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    print(completion.choices[0].message.content)

def gpt_35_api_stream(messages: list):
    """为提供的对话消息创建新的回答 (流式传输)

    Args:
        messages (list): 完整的对话消息
    """
    stream = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=messages,
        stream=True,
    )
    try:
      for chunk in stream:
          #if (chunk.choices[0],delta.content != None):
            print_color(chunk.choices[0].delta.content,"blue")
            #sleep(0.1)
    except IndexError:
        pass


if __name__ == '__main__':
    while 1:
        user_massage = input()
        if (user_massage == "$"):
            while user_massage == "$":
                user_massage = user_massage + input()
        messages = [{'role': 'user','content': user_massage},]
        # 非流式调用
        # gpt_35_api(messages)
        # 流式调
        gpt_35_api_stream(messages)
        print()