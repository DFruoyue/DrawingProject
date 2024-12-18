from library import *
import os
"""获取资源文件的绝对路径"""
BASE_DIR = os.path.dirname(__file__)

ParticipantsExcelFile = None

def run_activity() -> None:
    try:
        global ParticipantsExcelFile
        if ParticipantsExcelFile is not None:
            output("请先发送邮件\n")
            return
        if check_input_valid():
            activity = Activity(activityTime = activityTime_entry.get(),  
                                N = int(N_entry.get()), 
                                applicantsFile =applicantsFile_entry.get(), 
                                baseDir=BASE_DIR)
            ParticipantsExcelFile = activity.draw(GuaranteeEnable=enable_guaranteed_pool_var.get())
            output("抽签完成，可以发送邮件\n")
    except SystemExit as e:
        pass
    except Exception as e:
        output(f"错误: {str(e)}\n")


def send_email() -> None:
    try:
        global ParticipantsExcelFile
        if ParticipantsExcelFile is None:
            output("请先抽签\n")
            return
        email = Email(paymentLink = chargeLink_entry.get(), 
                      paymentDeadline = timeLimit_entry.get(), 
                      activitySubject = activitySubject_entry.get(),
                      contactName = contactName_entry.get(),
                      contactWehcatID = contactWechatID_entry.get(),
                      emailConfigFile = os.path.join(BASE_DIR, "data", "email_config.json"))
        email.send(ParticipantsExcelFile)
        output("邮件发送完成\n")
        if platform.system() == 'Windows':
            subprocess.run(["start", "excel", ParticipantsExcelFile], shell=True)
        else:
            subprocess.run(["open", "-a", "Microsoft Excel", ParticipantsExcelFile])
        ParticipantsExcelFile = None
    except SystemExit as e:
        pass
    except Exception as e:
        output(f"错误: {str(e)}\n")


draw_button.tag_bind(draw_triangle, "<Button-1>", lambda event: on_click_button(event, draw_button, draw_triangle, run_activity))
draw_button.tag_bind(draw_triangle, "<ButtonRelease-1>", lambda event: on_release_buttion(event, draw_button, draw_triangle))
send_email_button.tag_bind(send_email_circle, "<Button-1>", lambda event: on_click_button(event, send_email_button, send_email_circle, send_email))
send_email_button.tag_bind(send_email_circle, "<ButtonRelease-1>", lambda event: on_release_buttion(event, send_email_button, send_email_circle))

# 运行主循环
root.mainloop()