import tkinter as tk
from tkinter import font
from tkinterdnd2 import TkinterDnD, DND_FILES
import subprocess
from .GUIsetting import *

root = TkinterDnD.Tk()

#窗口颜色
BLACK = "#353535"
GREEN = "#3C6E71"
GREY = "#D9D9D9"
WHITE = "#FFFFFF"
BLUE = "#284B63"
LIGHTBLUE = "#68C3FF"

INPUT_TEXT_COLOR = GREEN
INPUT_TEXT_BG_COLOR = WHITE
HIGHLIGHT_COLOR = LIGHTBLUE

APPLICANTS_FILE_HINT = "(拖拽txt/xlsx文件或手动输入路径)"
ACTIVITY_SUBJECT_HINT = "(选填)"

THEMES={
    "Light":{
        "WINDOW_BG_COLOR":WHITE,
        "INPUT_LABEL_COLOR":GREEN,
        "INPUT_HIGHLIGHT_BG_COLOR":GREEN,
        "BUTTON_OUTLINE_COLOR":BLUE,
        "BUTTON_FOCUS_COLOR":GREEN,
        "OUTPUT_BG_COLOR":BLACK,
        "OUTPUT_TEXT_COLOR":WHITE,
        "OUTPUT_HIGHLIGHT_BACKGROUND":GREY,
    },
    "Dark":{
        "WINDOW_BG_COLOR":GREEN,
        "INPUT_LABEL_COLOR":WHITE,
        "INPUT_HIGHLIGHT_BG_COLOR":BLUE,
        "BUTTON_OUTLINE_COLOR":BLACK,
        "BUTTON_FOCUS_COLOR":BLUE,
        "OUTPUT_BG_COLOR":BLACK,
        "OUTPUT_TEXT_COLOR":WHITE,
        "OUTPUT_HIGHLIGHT_BACKGROUND":GREY,
    }
}

#获取系统主题模式
current_theme = THEMES[theme]

#平台定制
WINDOW_WIDTH = appearance["WindowWidth"]
WINDOW_HEIGHT = 400
HIGHLIGHT_THICKNESS = 3

tkdnd_path = 'tkdnd2.8'
root.tk.eval(f'global auto_path; lappend auto_path "{tkdnd_path}"')
root.tk.eval('package require tkdnd')
root.title("活动抽签")
root.configure(bg = current_theme["WINDOW_BG_COLOR"])
root.resizable(False, False)
POSITION_TOP = int(root.winfo_screenheight() / 2 - WINDOW_HEIGHT / 2)
POSITION_RIGHT = int(root.winfo_screenwidth() / 2 - WINDOW_WIDTH / 2)
root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{POSITION_RIGHT}+{POSITION_TOP}')

CUSTOM_FONT = font.Font(family="宋体", size=appearance["FontSize"], weight="normal") 
BOLD_FONT = font.Font(family="宋体", size=appearance["FontSize"], weight="bold")

INTERVALY:int = 34
INTERVALX:int = 104
STARTX:int = 10
STARTY:int = 10
INPUT_WIDTH:int = 36
SPECIAL_WIDTH:int = 6
INTERVALX:int = appearance["IntervalX"]
SPECIAL_INTERVAL_X:int = 160
LABEL_WIDTH = appearance["LabelWidth"]

tk.Label(root, text="活动主题", bg=current_theme["WINDOW_BG_COLOR"], fg = current_theme["INPUT_LABEL_COLOR"], font = BOLD_FONT, width = LABEL_WIDTH, anchor='e').place(x=STARTX, y=STARTY + 2)
activitySubject_entry = tk.Entry(root, width = INPUT_WIDTH, highlightbackground = current_theme["INPUT_HIGHLIGHT_BG_COLOR"], highlightcolor=HIGHLIGHT_COLOR, highlightthickness=HIGHLIGHT_THICKNESS, relief=tk.FLAT, bg = INPUT_TEXT_BG_COLOR, fg = INPUT_TEXT_COLOR, font = CUSTOM_FONT, insertbackground=BLACK)
activitySubject_entry.place(x=STARTX + INTERVALX, y=STARTY)

tk.Label(root, text="活动时间", bg=current_theme["WINDOW_BG_COLOR"], fg = current_theme["INPUT_LABEL_COLOR"], font = BOLD_FONT, width = LABEL_WIDTH, anchor='e').place(x=STARTX+SPECIAL_INTERVAL_X, y=STARTY + 2+INTERVALY)
activityTime_entry = tk.Entry(root, width = 20, highlightbackground = current_theme["INPUT_HIGHLIGHT_BG_COLOR"], highlightcolor=HIGHLIGHT_COLOR, highlightthickness=HIGHLIGHT_THICKNESS, relief=tk.FLAT, bg = INPUT_TEXT_BG_COLOR, fg = INPUT_TEXT_COLOR, font = CUSTOM_FONT, insertbackground=BLACK)
activityTime_entry.place(x=STARTX + INTERVALX+SPECIAL_INTERVAL_X, y= STARTY+INTERVALY)

tk.Label(root, text="报名名单", bg=current_theme["WINDOW_BG_COLOR"], fg = current_theme["INPUT_LABEL_COLOR"], font = BOLD_FONT, width = LABEL_WIDTH, anchor='e').place(x=STARTX, y=STARTY + 2 + INTERVALY*2)
applicantsFile_entry = tk.Entry(root, width = INPUT_WIDTH, highlightbackground = current_theme["INPUT_HIGHLIGHT_BG_COLOR"], highlightcolor=HIGHLIGHT_COLOR, highlightthickness=HIGHLIGHT_THICKNESS, relief=tk.FLAT, bg = INPUT_TEXT_BG_COLOR, fg = INPUT_TEXT_COLOR, font = CUSTOM_FONT, insertbackground=BLACK)
applicantsFile_entry.place(x=STARTX + INTERVALX, y=STARTY + INTERVALY*2)

tk.Label(root, text="缴费链接", bg=current_theme["WINDOW_BG_COLOR"], fg = current_theme["INPUT_LABEL_COLOR"], font = BOLD_FONT, width = LABEL_WIDTH, anchor='e').place(x=STARTX, y= STARTY + 2 + INTERVALY*3)
chargeLink_entry = tk.Entry(root, width = INPUT_WIDTH, highlightbackground = current_theme["INPUT_HIGHLIGHT_BG_COLOR"], highlightcolor=HIGHLIGHT_COLOR, highlightthickness=HIGHLIGHT_THICKNESS, relief=tk.FLAT, bg = INPUT_TEXT_BG_COLOR, fg = INPUT_TEXT_COLOR, font = CUSTOM_FONT, insertbackground=BLACK)
chargeLink_entry.place(x=STARTX + INTERVALX, y=STARTY + INTERVALY*3)

tk.Label(root, text="活动人数", bg=current_theme["WINDOW_BG_COLOR"], fg = current_theme["INPUT_LABEL_COLOR"], font = BOLD_FONT, width = LABEL_WIDTH, anchor='e').place(x=STARTX, y=STARTY + 2 + INTERVALY)
N_entry = tk.Entry(root, width = 6, highlightbackground = current_theme["INPUT_HIGHLIGHT_BG_COLOR"], highlightcolor=HIGHLIGHT_COLOR, highlightthickness=HIGHLIGHT_THICKNESS, relief=tk.FLAT, bg = INPUT_TEXT_BG_COLOR, fg = INPUT_TEXT_COLOR, font = CUSTOM_FONT, insertbackground=BLACK)
N_entry.place(x=STARTX + INTERVALX, y=STARTY + INTERVALY)

tk.Label(root, text="缴费截止时间", bg=current_theme["WINDOW_BG_COLOR"], fg = current_theme["INPUT_LABEL_COLOR"], font = BOLD_FONT, width = LABEL_WIDTH, anchor='e').place(x=STARTX, y=STARTY + 2 + INTERVALY*5)
timeLimit_entry = tk.Entry(root, width = INPUT_WIDTH, highlightbackground = current_theme["INPUT_HIGHLIGHT_BG_COLOR"], highlightcolor=HIGHLIGHT_COLOR, highlightthickness=HIGHLIGHT_THICKNESS, relief=tk.FLAT, bg = INPUT_TEXT_BG_COLOR, fg = INPUT_TEXT_COLOR, font = CUSTOM_FONT, insertbackground=BLACK)
timeLimit_entry.place(x=STARTX + INTERVALX, y=STARTY + INTERVALY*5)

tk.Label(root, text="微信号", bg=current_theme["WINDOW_BG_COLOR"], fg = current_theme["INPUT_LABEL_COLOR"], font = BOLD_FONT, width = LABEL_WIDTH, anchor='e').place(x=STARTX+SPECIAL_INTERVAL_X, y=STARTY + 2 + INTERVALY*4)
contactWechatID_entry = tk.Entry(root, width = 20, highlightbackground = current_theme["INPUT_HIGHLIGHT_BG_COLOR"], highlightcolor=HIGHLIGHT_COLOR, highlightthickness=HIGHLIGHT_THICKNESS, relief=tk.FLAT, bg = INPUT_TEXT_BG_COLOR, fg = INPUT_TEXT_COLOR, font = CUSTOM_FONT, insertbackground=BLACK)
contactWechatID_entry.place(x=STARTX + INTERVALX + SPECIAL_INTERVAL_X, y=STARTY + INTERVALY*4)

tk.Label(root, text="联系人姓名", bg=current_theme["WINDOW_BG_COLOR"], fg = current_theme["INPUT_LABEL_COLOR"], font = BOLD_FONT, width = LABEL_WIDTH, anchor='e').place(x=STARTX, y=STARTY + 2 + INTERVALY*4)
contactName_entry = tk.Entry(root, width = SPECIAL_WIDTH + 2, highlightbackground = current_theme["INPUT_HIGHLIGHT_BG_COLOR"], highlightcolor=HIGHLIGHT_COLOR, highlightthickness=HIGHLIGHT_THICKNESS, relief=tk.FLAT, bg = INPUT_TEXT_BG_COLOR, fg = INPUT_TEXT_COLOR, font = CUSTOM_FONT, insertbackground=BLACK)
contactName_entry.place(x=STARTX + INTERVALX, y=STARTY + INTERVALY*4)

enable_guaranteed_pool_var = tk.BooleanVar(value=True)
enable_guaranteed_pool_checkbox = tk.Checkbutton(root, text="启用保底池", variable=enable_guaranteed_pool_var, bg=current_theme["WINDOW_BG_COLOR"], fg=current_theme["INPUT_LABEL_COLOR"], font=BOLD_FONT)
enable_guaranteed_pool_checkbox.place(x=10, y=STARTY + INTERVALY*6 + 5)

def on_entry_click(event, entry:tk.Entry, default_text:str):
    if entry.get() == default_text:
        entry.delete(0, "end")  # 删除所有文本
        entry.config(fg=INPUT_TEXT_COLOR)  # 设置文本颜色为正常颜色
def on_focusout(event, entry:tk.Entry, default_text:str):
    if entry.get() == "":
        entry.insert(0, default_text)
        entry.config(fg="gray")
activitySubject_entry.configure(fg="gray")
activitySubject_entry.insert(0, ACTIVITY_SUBJECT_HINT)
activitySubject_entry.bind("<FocusIn>", lambda event: on_entry_click(event, activitySubject_entry, ACTIVITY_SUBJECT_HINT))
activitySubject_entry.bind("<FocusOut>", lambda event: on_focusout(event, activitySubject_entry, ACTIVITY_SUBJECT_HINT))
applicantsFile_entry.configure(fg="gray")
applicantsFile_entry.insert(0, APPLICANTS_FILE_HINT)
applicantsFile_entry.bind("<FocusIn>", lambda event: on_entry_click(event, applicantsFile_entry, APPLICANTS_FILE_HINT))
applicantsFile_entry.bind("<FocusOut>", lambda event: on_focusout(event, applicantsFile_entry, APPLICANTS_FILE_HINT))
def drop(event):
    file_path = event.data.strip('{}')
    applicantsFile_entry.delete(0, tk.END)
    applicantsFile_entry.configure(fg=INPUT_TEXT_COLOR)
    applicantsFile_entry.insert(0, file_path)
applicantsFile_entry.drop_target_register(DND_FILES)
applicantsFile_entry.dnd_bind('<<Drop>>', drop)

BUTTON_HEIGHT = 24
BUTTON_WIDTH = 20
FOCUS_COLOR = GREEN
IsButtonPressed = False
hint_text = tk.Label(root, text="", bg=current_theme["WINDOW_BG_COLOR"], fg = current_theme["INPUT_LABEL_COLOR"], font = BOLD_FONT)
draw_button = tk.Canvas(root, width=BUTTON_WIDTH+HIGHLIGHT_THICKNESS*2, height=BUTTON_HEIGHT+HIGHLIGHT_THICKNESS*2, highlightthickness=0, bg = current_theme["WINDOW_BG_COLOR"])
draw_triangle = draw_button.create_polygon(HIGHLIGHT_THICKNESS, BUTTON_HEIGHT+HIGHLIGHT_THICKNESS, BUTTON_WIDTH+HIGHLIGHT_THICKNESS, BUTTON_HEIGHT/2+HIGHLIGHT_THICKNESS, HIGHLIGHT_THICKNESS, HIGHLIGHT_THICKNESS, fill=current_theme["WINDOW_BG_COLOR"], outline=current_theme["BUTTON_OUTLINE_COLOR"], width=HIGHLIGHT_THICKNESS)
draw_button.place(x=200, y=STARTY + INTERVALY*6 + 5)
send_email_button = tk.Canvas(root, width=BUTTON_HEIGHT+HIGHLIGHT_THICKNESS*2, height=BUTTON_HEIGHT+HIGHLIGHT_THICKNESS*2, highlightthickness=0, bg = current_theme["WINDOW_BG_COLOR"])
send_email_circle = send_email_button.create_oval(HIGHLIGHT_THICKNESS, HIGHLIGHT_THICKNESS, BUTTON_HEIGHT+HIGHLIGHT_THICKNESS, BUTTON_HEIGHT+HIGHLIGHT_THICKNESS, fill=current_theme["WINDOW_BG_COLOR"], outline=current_theme["BUTTON_OUTLINE_COLOR"], width=HIGHLIGHT_THICKNESS)
send_email_button.place(x=350, y=STARTY + INTERVALY*6 + 5)
def on_enter(event, button:tk.Canvas, shape, hint:str):
    button.itemconfig(shape, fill=current_theme["BUTTON_FOCUS_COLOR"])
    hint_text.configure(text = hint)
    hint_text.place(x=button.winfo_x() + button.winfo_width(), y=button.winfo_y() + HIGHLIGHT_THICKNESS)
def on_leave(event, button:tk.Canvas, shape):
    button.itemconfig(shape, fill=current_theme["WINDOW_BG_COLOR"])
    hint_text.place_forget()
    global IsButtonPressed
    if IsButtonPressed:
        button.move(shape, -1, -1)
        IsButtonPressed = False
        
draw_button.tag_bind(draw_triangle, "<Enter>", lambda event: on_enter(event, draw_button, draw_triangle, '抽签'))
draw_button.tag_bind(draw_triangle, "<Leave>", lambda event: on_leave(event, draw_button, draw_triangle))
send_email_button.tag_bind(send_email_circle, "<Enter>", lambda event: on_enter(event, send_email_button, send_email_circle, '发送邮件'))
send_email_button.tag_bind(send_email_circle, "<Leave>", lambda event: on_leave(event, send_email_button, send_email_circle))

Y:int = STARTY + INTERVALY*7 + 10
output_text = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED, font = BOLD_FONT, fg = current_theme["OUTPUT_TEXT_COLOR"], bg = current_theme["OUTPUT_BG_COLOR"], relief=tk.FLAT, highlightcolor= HIGHLIGHT_COLOR, highlightthickness=HIGHLIGHT_THICKNESS, highlightbackground=current_theme["OUTPUT_HIGHLIGHT_BACKGROUND"])
output_text.place(x=0, y=Y, width=WINDOW_WIDTH, height=WINDOW_HEIGHT-Y)
def output(message: str) -> None:
    output_text.config(state=tk.NORMAL)  # 允许插入文本
    output_text.insert(tk.END, str(message) + '\n')
    output_text.config(state=tk.DISABLED)  # 禁止用户输入
    output_text.see(tk.END)  # 确保最新消息可见
def clear_output() -> None:
    output_text.config(state=tk.NORMAL)  # 允许插入文本
    output_text.delete('1.0', tk.END)
    output_text.config(state=tk.DISABLED)  # 禁止用户输入
    output_text.see(tk.END)  # 确保最新消息可见


def on_close_window():
    root.destroy()


def on_release_buttion(event, canvas:tk.Canvas, shape):
    global IsButtonPressed
    if IsButtonPressed:
        canvas.move(shape, -1, -1)
        IsButtonPressed = False


def on_click_button(event, canvas:tk.Canvas, shape, function, *args):
    canvas.move(shape, 1, 1)
    global IsButtonPressed
    IsButtonPressed = True
    function(*args)


def check_input_valid()-> bool:
    activity_time = activityTime_entry.get()
    payment_link = chargeLink_entry.get()
    payment_deadline = timeLimit_entry.get()
    applicants_file = applicantsFile_entry.get()
    N:int = None
    if not activity_time:
        output("Error:活动时间为空")
        return False
    if not payment_link:
        output("Error:缴费链接为空")
        return False
    try:
        N = int(N_entry.get())
    except ValueError:
        # 处理输入不是整数的情况，例如显示错误消息
        output("Error:活动人数不是正整数")
        return False
    if N < 0:
        output("Error:活动人数是负数")
        return False
    if not payment_deadline:
        output("Error:缴费截止时间为空")
        return False
    if applicants_file == APPLICANTS_FILE_HINT:
        output("Error:参与抽奖名单为空")
        return False
    return True


root.protocol("WM_DELETE_WINDOW", on_close_window)