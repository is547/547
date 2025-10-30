import tkinter as tk
import random
import threading
import time

# ---------- 数据 ----------
tips = ['我想你了', '今天过得开心吗', '早点休息', '天冷了，多穿衣','好好爱自己','少熬点夜',
        '今天有想我嘛','万事顺遂','乖乖，你超哇塞的','幸福，请降临你的手心', '愿所有烦恼都消失','最近过得好吗','有好好吃饭嘛','金榜题名','我们都会有光明的未来', '我的身边还是你',"每天都要元气满满"]
bg_colors = ["#C7EEFF", "#B8E0D2", "#95B8D1", "#E8D4D3", "#D8BFD5", "#BFA6CA"]

MAX_WIN = 250
alive = {}          # 存活着的窗口
count = 0           # 已弹数量

# ---------- 逻辑 ----------
def make_window():
    global count
    if count >= MAX_WIN:
        return
    count += 1

    top = tk.Toplevel(root)
    top.title("宝贝")
    w, h = 250, 60
    top.geometry(f"{w}x{h}+{random.randrange(0, top.winfo_screenwidth()-w)}"
                 f"+{random.randrange(0, top.winfo_screenheight()-h)}")
    top.attributes('-topmost', True)
    tk.Label(top,
             text=random.choice(tips),
             bg=random.choice(bg_colors),
             font=('楷体', 16),
             width=30, height=3).pack()

    alive[top] = True

    # 用户手动点×也清掉记录
    def on_close():
        alive.pop(top, None)
        top.destroy()
    top.protocol("WM_DELETE_WINDOW", on_close)

    # 最后一扇窗弹出 → 启动 30 秒后逐个消失
    if count == MAX_WIN:
        threading.Thread(target=vanish_one_by_one, daemon=True).start()

def vanish_one_by_one():
    """子线程：先睡 30 秒，再挨个销毁"""
    time.sleep(30)
    # 每隔 150 ms 关掉一扇窗（速度自己调）
    for w in list(alive.keys()):
        try:
            root.after(0, w.destroy)   # 抛回主线程
        except tk.TclError:
            pass                         # 窗口已被手动关闭
        time.sleep(0.15)
    root.after(0, root.quit)             # 全部关完退出

def pop_loop():
    for _ in range(MAX_WIN):
        root.after(0, make_window)
        time.sleep(0.05)   # 每 50 ms 弹一个

# ---------- 启动 ----------
root = tk.Tk()
root.withdraw()                     # 隐藏主窗口
threading.Thread(target=pop_loop, daemon=True).start()
root.mainloop()