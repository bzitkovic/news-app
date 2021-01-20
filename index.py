import tkinter as tk
import requests
import webbrowser

globalUrl = ''


def callback(url):
    webbrowser.open_new(url)

# Reads Source, Author, URL From Object


def get_response(article):
    global globalUrl
    name = article['articles'][0]['source']['name']
    author = article['articles'][0]['author']
    url = article['articles'][0]['url']
    globalUrl = url

    finalStr = f'Source:  {name}\n Author:  {author}\n\n URL\n {url}'

    return finalStr

# Reads Content From The Object


def get_response_text(article):
    content = article['articles'][0]['content']
    finalStr = f'Content Of The Article\n\n {content}\n\n <-- For More Click On The URL'

    return finalStr

# Gets Spec. Object


def get_article(subject):
    url = f'https://newsapi.org/v2/everything?q={subject}&apiKey=9fdc9907b75f4de791da3bda6272302f'
    api_key = '9fdc9907b75f4de791da3bda6272302f'
    response = requests.get(url)
    article = response.json()
    label['text'] = get_response(article)
    label2['text'] = get_response_text(article)


# GUI
root = tk.Tk()

# Maximize Window
root.state('zoomed')

canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)

bg_image = tk.PhotoImage(file='paperIm2.png')
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Frames
first_frame = tk.Frame(root, bg='#1E555C')
first_frame.place(relx=0.43, rely=0.1, relwidth=0.30, relheight=0.1, anchor='n')

second_frame = tk.Frame(root, bg='#00195c', bd=3)
second_frame.place(relx=0.20, rely=0.35, relwidth=0.3, relheight=0.5, anchor='n')

third_frame = tk.Frame(root, bg='#00195c', bd=3)
third_frame.place(relx=0.7, rely=0.35, relwidth=0.5, relheight=0.5, anchor='n')

buttonFrame = tk.Frame(root, bg='#1E555C')
buttonFrame.place(relx=0.43, rely=0.2, relwidth=0.30, relheight=0.1, anchor='n')

# Content Of The App
entry = tk.Entry(first_frame, bg='#2FA170', bd=2, font=('Times New Roman', 20), justify='center')
entry.insert(0, 'Enter Your Search Term')
entry.bind("<FocusIn>", lambda args: entry.delete('0', 'end'))
# entry.focus()
entry.place(relwidth=1, relheight=1)

button = tk.Button(buttonFrame, text='Search', bg='#2FA170', font=(
    'Times New Roman', 20), command=lambda: get_article(entry.get()))
button.place(relwidth=1, relheight=1)

labelCR = tk.Label(root, height=1, width=25, bg='#2FA170')
labelCR['text'] = "Powered By News API"
labelCR.place(relx=0.88, rely=0.97)

label = tk.Label(second_frame, font=('Times New Roman', 17,), bg='#C4C7E3',
                 cursor='hand2', wraplength=300, anchor='center')
label.place(relwidth=1, relheight=1)
label.bind("<Button-1>", lambda e: callback(globalUrl))

label2 = tk.Label(third_frame, font=('Times New Roman', 17), bg='#C4C7E3', wraplength=500)
label2.place(relwidth=1, relheight=1)

root.mainloop()
