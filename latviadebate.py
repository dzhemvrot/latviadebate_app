import tkinter
import tkinter.filedialog
import os
import webbrowser
from tkinter import *
from tkinter import messagebox
from os import getcwd
from datetime import datetime, timedelta

root = Tk()
root.option_add("*Font", "Verdana 10")


#########################################################################

def load():
    try:
        fn = datetime.now().strftime("%d-%m-%Y")
        artic = NText.get('1.0', 'end')
        artic = artic.replace("\n", "<br>")
        artna = Name.get()
        regl = Regist.get()
        dienl = Dienas.get()
        phots = photo()
        if phots is None:
            return
        whfi = """<!doctype html>
    <html lang="lv-LV">
            <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <meta name="keywords" content="">"""+f"""
                    <title>Latvia Debate — {artna}</title>"""+'''
                    <link rel="icon" sizes="192x192" href="logo.png">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous"> 
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
                    <link rel="stylesheet" type="text/css" href="style.css">
            </head>
      
            <body>
                    <nav class="navbar navbar-light navbar-og navbar-expand-lg">
                      <div class="container-fluid">
                            <a class="navbar-brand" href="index.html"><img src="shapka.png" alt="Latvia Debate logo" width="250" height="auto"></a>
                            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                              <span class="navbar-toggler-icon"></span>
                            </button>
                            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                              <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                                    <li class="nav-item">
                                      <a class="nav-link" aria-current="page" href="index.html">Galvenā</a>
                                    </li>
                                    <li class="nav-item">
                                            <a class="nav-link" href="https://www.facebook.com/pg/LatviaDebate/photos">Foto</a>
                                      </li>

                              </ul>
                            </div>
                      </div>
                    </nav>
            <div class="row" style="margin-top: 15px;">
            <div class="col-sm-auto"></div>
            <div class="col p-4 border border-4 border-light justify-content-center" style="background-color: #3D2C2A">'''+f"""<h1>
                {artna}
                 </h1>
            <p>{artic}"""+f"""
               <a href="{regl}">Reģistrācija</a>
               <br><a href="{dienl}">Dienas kartība</a></p>"""+"""<hr>
           <img src="{phots}" class="img-fluid rounded" width="800px" height="auto"><hr>
            
               <div id="disqus_thread"></div>"""+"""
               <script>
                   /**
                   *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
                   *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables    */
                   /*
                   var disqus_config = function () {"""+f"""
                   this.page.url = latviadebate/pages/{fn};  // Replace PAGE_URL with your page's canonical URL variable
                   this.page.identifier = {fn};"""+""" // Replace PAGE_IDENTIFIER with your page's unique identifier variable
                   };
                   */
                   (function() { // DON'T EDIT BELOW THIS LINE
                   var d = document, s = d.createElement('script');
                   s.src = 'https://latviadebate-1.disqus.com/embed.js';
                   s.setAttribute('data-timestamp', +new Date());
                   (d.head || d.body).appendChild(s);
                   })();
               </script>
               <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
            
            </div>

            <div class="col-sm-auto"></div>
            </div>


            <br>
                    <div class="row p-4 justify-content-center" style="background-color: #D68624;"><p style="text-align: center;">Kļūsti par mūsu sociālo mediju sekotāju:</p>
                    <div class="col justify-content-center"></div>
                    <div class="col justify-content-center"><a href="https://www.facebook.com/LatviaDebate/"><img src="../images/fb.png" alt="Facebook logo" width="25" height="auto"></a></div>
                    <div class="col justify-content-center"><a href="https://www.instagram.com/latvia.debate/"><img src="../images/in.png" alt="Instagram logo" width="25" height="auto"></a></div>
            </div>
            </body>
    </html>
    """
        open(fn+".html", "wt", encoding='utf-8').write(whfi)
        webbrowser.open('https://github.com/dzhemvrot/latviadebate', new=2)
        messagebox.showinfo("Успех!", "Статья сохранена!")
    except Exception as e:
        print(e)
        messagebox.showerror("Ошибка!", f"Что-то пошло не так!\nПовторите попытку!\n\nОшибка: {e}\nСообщите ошибку создателю программы!")

def on_closing():
    if messagebox.askokcancel("Выход", "Вы точно хотите выйти?"):
        root.destroy()

def helps():
    win = Toplevel()
    win.title('О программе')
    message = """Программа создана Тимуром Бесарабом в 2023 году в рамках проекта по информатике (datorika).
Для получения дополнительной информации нажмите на кнопку "Помощь"."""
    HelpLab = Label(win, text=message)
    HelpLab.grid(row=0, column=1)
    HelpBut = Button(win, text='Помощь', command=helpweb)
    HelpBut.grid(row=1, column=0)
    ClBut = Button(win, text='Закрыть', command=win.destroy)
    ClBut.grid(row=1, column=2)
    win.resizable(False, False)

def helpweb():
    webbrowser.open('https://github.com/dzhemvrot/latviadebate_app/blob/main/README.md', new=2)

def photo():
    ftypes = [('.PNG', '*.png'), ('.JPG', '*.jpg'), ('.WEBP', '*.webp'), ('All files', '*')] 
    photo = tkinter.filedialog.Open(root, filetypes = ftypes).show()
    if photo == '':
        return
    print(photo)
    return photo
    
#########################################################################

menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar,tearoff=0)

file_menu.add_command(label='Сохранить', command = load)
file_menu.add_separator()

file_menu.add_command(
    label='Выход',
    command=on_closing
)

menubar.add_cascade(
    label="Файл",
    menu=file_menu
)

menubar.add_command(label='О программе', command = helps)

#########################################################################

NLabel = Label(root, text = "Название статьи:")
NLabel.grid(row=0, column=1)

Name = Entry(root)
Name.grid(row=0, column=2)

NText = Text(root)
NText.grid(row = 1, column = 0, columnspan = 5)

Regist = Entry(root)
Regist.grid(row=2, column=1)

#PhotoB = Button(root, text = "Фото", width = 8, command = photo)
#PhotoB.grid(row = 2, column = 2, padx=20, pady=10)

Dienas = Entry(root)
Dienas.grid(row=2, column=4)

ClearB = Button(root, text = "Очистить", width = 8)
ClearB.grid(row = 3, column = 1, padx=20, pady=10)

UplB = Button(root, text = "Сохранить", width = 8, command = load)
UplB.grid(row = 3, column = 4, padx=20, pady=10)

scrollbar = Scrollbar(root, orient='vertical', command=Text.yview)
scrollbar.grid(row=1, column=5, sticky=NS)

NText['yscrollcommand'] = scrollbar.set


try:
    root.iconbitmap('icon.ico')
except:
    pass
root.title(u'Latvia Debate - Написатель статей')
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
