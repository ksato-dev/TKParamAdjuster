import tkinter
import time

# ウィンドウのタイトル名
root = tkinter.Tk()
root.title("test")
root.geometry("300x150")
# キャンバスエリアの設定
canvas = tkinter.Canvas(root,width=300,height=150,bg="black")
canvas.pack()

def on_Scale(self):
    # 図形の削除
    canvas.delete("Time")
    # 初期タイムの変更
    canvas.create_text(150,40,text=s.get(),font=("Helvetica",30,"bold"),fill="white",tag="Time",anchor="c")

def startButtonClick():
    # グローバル変数の設定
    global endTime

    endTime=time.time() + s.get()
    root.after(50,update)

def update():
    # 図形の削除
    canvas.delete("Time")

    elapsedTime=endTime-time.time()
    if elapsedTime > 0:
        # 残り時間を０になるまで表示
        canvas.create_text(150,40,text=round(elapsedTime,1),font=("Helvetica",30,"bold"),fill="white",tag="Time",anchor="c")
        root.after(50,update)
    else:
        # 残り時間が０になれば「OK」を表示
        canvas.create_text(150,40,text="OK",font=("Helvetica",30,"bold"),fill="white",tag="Time",anchor="c")

# 初期タイムを設定
var = tkinter.IntVar(master=root,value=3,)
# スケール（スライダー）の作成
s = tkinter.Scale(root, orient='h',showvalue=False,variable=var,from_=1, to=10,length=160,command=on_Scale)
s.place(x=70, y=68)
# ボタンを作成
b = tkinter.Button(root,text="スタート",command=startButtonClick,width=8,font=("",14))
b.place(x=110, y=100)
# テキストを作成
canvas.create_text(150,40,text=s.get(),font=("Helvetica",30,"bold"),fill="white",tag="Time",anchor="c")

root.mainloop()
