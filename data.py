import scipy.io as spio
import pandas as pd
from PIL import Image, ImageTk
import tkinter as tk

def load_list_action(matdata):
    
    t = matdata['list_action']
    column_names = ["object", "interaction"]

    df = pd.DataFrame(columns = column_names)

    for i in range(600):
        df.loc[i] = [t[i,0]['nname'][0]] + [t[i,0]['vname_ing'][0]]
    return df
    
def clicked(value):
    global pre
    pre = value	 

def load_anno(matdata,name):
    t = matdata['anno_' + name]
    df = pd.DataFrame(data=t)
    return df

def getIndexes(x,pre):
    if(pre == '../images/test2015/HICO_test2015_0000'):
        ex = test.loc[test[x-1] == 1]
        amb = test.loc[test[x-1] == 0]
        n_ex = test.loc[test[x-1] == -1]
    else:
        ex = train.loc[train[x-1] == 1]
        amb = train.loc[train[x-1] == 0]
        n_ex = train.loc[train[x-1] == -1]
    return ex.index.tolist(), amb.index.tolist(), n_ex.index.tolist()

def displayImage(image):
    zeros = ""
    
    if (pre == '../images/test2015/HICO_test2015_0000'):
        for i in range(4-len(image)):
            zeros += "0"
    else:
        for i in range(5-len(image)):
            zeros += "0"
    
    path = pre + zeros + str(image) + past
    im = Image.open(path)
    
    img = ImageTk.PhotoImage(im)
    
    width, height = im.size

    panel = tk.Label(root, image = img)

    panel.pack(side = "bottom", fill = "none", expand = "no", anchor='sw',
               padx=(700 - width)/2, pady=(700 - height)/2)
    labels.append(panel)
    root.mainloop()

def displayHOI():
    image = e.get()
    try:
        val = int(image)
    except ValueError:
        return
    
    if (val < 1):
        return
    elif (pre == '../images/test2015/HICO_test2015_0000' and val > 9658):
        return
    elif (pre == '../images/train2015/HICO_train2015_000' and val > 38116):
        return
    
    for label in labels: 
        label.destroy()
    
    ex_ind,amb_ind,n_ex_ind = getIndexes(int(image),pre)
     
    object = inter.iat[n_ex_ind[0], 0]
    name = tk.Label(root, text=object, font=("Arial",30), fg='blue')
    name.pack()
    name.place(relx=0.5, y=200, anchor='n')
    labels.append(name)
    
    i = 0
    if(len(ex_ind) != 0):
        for i in range(len(ex_ind)):
            hoi = tk.Label(root, text=inter.iat[ex_ind[i], 1], font=("Arial",20))
            hoi.pack()
            hoi.place(x = 900, rely=0.22+(i*0.1), anchor='e')
            labels.append(hoi)
            im = Image.open(check)
            display = ImageTk.PhotoImage(im)
            label = tk.Label(root, image=display)
            label.display = display
            label.place(x = 950, rely=0.22+(i*0.1), anchor='e')   
            labels.append(label)
        i += 1
    
    k=0
    if(len(amb_ind) != 0):
        for k in range(len(amb_ind)):
            hoi = tk.Label(root, text=inter.iat[amb_ind[k], 1], font=("Arial",20))
            hoi.pack()
            hoi.place(x = 900, rely=0.22+((k+i)*0.1), anchor='e')
            labels.append(hoi)
            im = Image.open(quest)
            display = ImageTk.PhotoImage(im)
            label = tk.Label(root, image=display)
            label.display = display
            label.place(x = 935, rely=0.22+((k+i)*0.1), anchor='e')   
            labels.append(label)
        k += 1
        
    l=0
    if(len(n_ex_ind) != 0):
        for l in range(len(n_ex_ind)):
            hoi = tk.Label(root, text=inter.iat[n_ex_ind[l], 1], font=("Arial",20))
            hoi.pack()
            hoi.place(x = 900, rely=0.22+((k+l+i)*0.1), anchor='e')
            labels.append(hoi)
            im = Image.open(cross)
            display = ImageTk.PhotoImage(im)
            label = tk.Label(root, image=display)
            label.display = display
            label.place(x = 950, rely=0.22+((k+l+i)*0.1), anchor='e')   
            labels.append(label)
    
    displayImage(image)    


pre = "../images/test2015/HICO_test2015_0000"
past = ".jpg"
check = "check.png"
cross = "cross.png"
quest = "questionmark.png" 

labels = []

matfile = '../anno.mat'
matdata = spio.loadmat(matfile)      

inter = load_list_action(matdata)  
train = load_anno(matdata,'train')
test = load_anno(matdata,'test')

root = tk.Tk()
root.title('HICO-DET viewer')
root.geometry("1200x950")

select = tk.Label(root, text='Please type in the picture number', font=("Arial",23))
select.place(relx=0.5, rely=0.0, anchor='n')

obj = tk.Label(root, text='Object in the picture:', font=("Arial",23))
obj.place(relx=0.5, y=150, anchor='n')

e = tk.Entry(root, width=12, font=("Arial",23), justify='center')
e.place(relx=0.5, rely=0.05, anchor='n')

confirm = tk.Button(root, text='Confirm',command=displayHOI, font=("Arial",14))
confirm.place(relx=0.5, rely=0.1, anchor='n')

r = tk.StringVar()
r.set(pre)
tk.Radiobutton(root, text="Training data", variable=r, 
               value="../images/train2015/HICO_train2015_000", font=("Arial",15), 
               command=lambda: clicked(r.get())).pack(side="top", anchor="w")
tk.Radiobutton(root, text="Testing data", variable=r, 
               value="../images/test2015/HICO_test2015_0000", font=("Arial",15), 
               command=lambda: clicked(r.get())).pack(side="top", anchor="w")

root.mainloop()





