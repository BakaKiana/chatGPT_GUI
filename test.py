import openai
import asyncio
import tkinter as tk
import time

openai.api_key = "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"

async def run_openai(str):
    # 调用openai的接口
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=str,
        temperature=0.6,
        max_tokens=2048,
        n=1,
    )
    # 打印返回的结果
    # print(response["choices"][0]["text"])
    for c in response["choices"][0]["text"]:
        text.insert(tk.END, c)
        text.see(tk.END)  # 使文本框滚动到最后一行
        window.update()  # 更新窗口
        time.sleep(0.1)  # 等待0.1秒



# 创建一个窗口
window = tk.Tk()
window.geometry('600x400+100+100')
window.title("Openai")

# 创建一个输入框
input_field = tk.Entry(window,width=80)
input_field.config(width=None)

input_field.pack()

def getTextInput():
    result = input_field.get()  # 获取文本输入框的内容
    text.delete("1.0", "end")
    # 异步执行
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_openai(result))
# 创建一个按钮
text_variable = tk.StringVar()
button1 = tk.Button(window, text="查询",command = getTextInput)
button1.pack()
text = tk.Text(window,wrap="word")
text.pack()
# 运行窗口
window.mainloop()

