import os
import openai
import pytesseract
from PIL import Image
from datetime import datetime

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

# OpenAI API密钥配置
openai.api_key = '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'

# 找到最新的截图文件
screenshot_dir = '/Users/zizhoutong/Desktop/testScreenShot'
latest_screenshot_file = max([os.path.join(screenshot_dir, f) for f in os.listdir(
    screenshot_dir) if f.endswith('.png')], key=os.path.getctime)

print(latest_screenshot_file)

# # 将截图转换为文本
# text = pytesseract.image_to_string(Image.open(
#     latest_screenshot_file), lang='eng+chi_sim')

# # 将转换后的文本保存在当前文件夹下的converted_text文件夹中
# converted_text_dir = '/Users/zizhoutong/Downloads/img2textgpt/converted_text'
# if not os.path.exists(converted_text_dir):
#     os.makedirs(converted_text_dir)

# now = datetime.now().strftime("%Y%m%d%H%M%S")
# converted_text_file = os.path.join(converted_text_dir, f"text_{now}.txt")
# with open(converted_text_file, 'w', encoding='utf-8') as file:
#     file.write(text)

# # 设置你的prompt，这里将最新的文本文件内容添加到prompt中
# prompt = f"你是产品/研发专家以及资深面试官。以下是一段文本,不要管错别字，忽略掉错别字的问题,帮助我来作答，用中文告诉我答案：\n{text}\n回答："

# # 使用OpenAI API发送请求并获取回答
# completion = openai.ChatCompletion.create(
#     model="gpt-4-0125-preview",
#     messages=[
#         # {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": prompt}
#     ]
# )

# # 打印ChatGPT的回答
# print(completion.choices[0].message.content.strip())

# # 获取ChatGPT的回答
# answer = completion.choices[0].message.content.strip()

# # 将回答追加到文件末尾
# response_file = '/Users/zizhoutong/Desktop/response.txt'
# with open(response_file, 'a', encoding='utf-8') as f:
#     f.write(answer + '\n')
