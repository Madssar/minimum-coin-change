import tkinter as tk

window = tk.Tk()

hasPound = tk.BooleanVar()
has50p = tk.BooleanVar()
has20p = tk.BooleanVar()
has10p = tk.BooleanVar() 
has5p = tk.BooleanVar()
has2p = tk.BooleanVar()
has1p = tk.BooleanVar()


window.title("Change Calculator")
window.configure(background='white')
window.geometry("600x400")


coins = {100:0,50:0,20:0,10:0,5:0,2:0,1:0}

def exitApp():
    print("Ending App...")
    window.destroy()



def exclude(n):
    '''take value of n from checkbuttons if checkbutton is true then exclude that coin from coins dictionary
    else add back into dictionary'''
    global coins
    
    c ={100:hasPound.get(),
         50:has50p.get(),
         20:has20p.get(),
         10:has10p.get(),
         5:has5p.get(),
          2:has2p.get()
     }.get(n)
    print(f"{n}: {c}")
    if  c:
        coins.pop(n)
    else:
        coins[n]=n
    print(f"Coins available {coins}")

    


#Change label
lblTitle =tk.Label(text="Change", 
                   font=('Time New Roman', 12,'bold'),
                   bg ='white',
                   fg='black'
                   ) 
lblTitle.grid(row=1,column=0)


#textbox
coinEntryBox = tk.Entry(
                    font=('Time New Roman', 12,'bold'),
                    border=2
                    ) 
coinEntryBox.grid(row=1,column=1, columnspan=6,pady=(5,5))

#value error label if you enter alphabet in textbox and press execute button then this label will be visible
checkTypelbl =tk.Label(text="", 
                   font=('Time New Roman', 12),
                   bg ='white',
                   fg='black'
                   ) 
checkTypelbl.place(x=400,y=1)

def coinChange():
    '''Return list of miminum coins required to make change and display it into lblResult area'''
    try:
        amount = int(coinEntryBox.get())
        if 100 in coins: #check the coin is excluded or not
            if amount >= 100:
                coins[100] = amount // 100
                # Reduce the amount by the value of the 1 pound added:
                amount = amount % 100
            
    
        if 50 in coins: #check the coin is excluded or not
            if amount >= 50:  # If the amount is enough to add 50p, add them:
                coins[50] = amount // 50
                # Reduce the amount by the value of the half added:
                amount = amount % 50
                
   
        if 20 in coins:
            if amount >= 20:
                coins[20] = amount // 20
                amount = amount % 20
            
   
        if 10 in coins:
            if amount >= 10:
                coins[10] = amount // 10
                amount = amount % 10
            
   
        if 5 in coins:
            if amount >= 5:
                coins[5] = amount // 5
                amount = amount % 5
    
        if 2 in coins:
            if amount >= 2:
                coins[2] = amount // 2
                amount = amount % 2
            
        if amount >= 1:
            coins[1] = amount
        
        #displaying the result
        lblResult.configure(text= f"""
        £: {coins[100] if 100 in coins else '0'}
        50p: {coins[50] if 50 in coins else '0'}
        20p: {coins[20] if 20 in coins else '0'}
        10p: {coins[10] if 10 in coins else '0'}
        5p: {coins[5] if 5 in coins else '0'}
        2p: {coins[2] if 2 in coins else '0'}
        1p: {coins[1] if 1 in coins else '0'}""")
    
    except ValueError:
        checkTypelbl.config(text='Please enter numbers only')


def clearDict():
    '''
    this function is used to clear all the values of coins dictionary and lblResult

    '''
    for key in coins:
        coins[key]=0
    lblResult.configure(text= f"""
    £: {coins[100] if 100 in coins else '0'}
    50p: {coins[50] if 50 in coins else '0'}
    20p: {coins[20] if 20 in coins else '0'}
    10p: {coins[10] if 10 in coins else '0'}
    5p: {coins[5] if 5 in coins else '0'}
    2p: {coins[2] if 2 in coins else '0'}
    1p: {coins[1] if 1 in coins else '0'}""")


#check boxes stars here
cbPound = tk.Checkbutton(window, text="1£", variable=hasPound,
                         font=('Time New Roman', 12,'bold'),
                         bg ='white',
                         fg='black',
                         command= lambda: exclude(100)) #call the exclude function and remove 100 from dictonery
cbPound.grid(row=3, column=1)
cb50p = tk.Checkbutton(window, text="50p", variable=has50p,
                       font=('Time New Roman', 12,'bold'),
                       bg ='white',
                       fg='black',
                       command= lambda: exclude(50)) 
cb50p.grid(row=3, column=2)

cb20p = tk.Checkbutton(window, text="20p",variable=has20p,
                      font=('Times New Roman',12,'bold'),
                      bg ='white',
                      fg='black',
                      command= lambda: exclude(20))
cb20p.grid(row=3, column=3)

cb10p = tk.Checkbutton(window, text="10p",variable=has10p,
                      font=('Times New Roman',12,'bold'),
                      bg ='white',
                      fg='black',
                      command= lambda: exclude(10))
cb10p.grid(row=3, column=4)

cb5p = tk.Checkbutton(window, text="5p",variable=has5p,
                      font=('Times New Roman',12,'bold'),
                      bg ='white',
                      fg='black',
                      command= lambda: exclude(5))
cb5p.grid(row=3, column=5)

cb2p = tk.Checkbutton(window, text="2p", variable=has2p,
                       font=('Time New Roman', 12,'bold'),
                       bg ='white',
                       fg='black',
                       command= lambda: exclude(2))
cb2p.grid(row=3, column=6)


#exclude label
excludeLabel = tk.Label(text="Exclude", 
                   font=('Time New Roman', 12,'bold'),
                   bg ='white',
                   fg='black')
excludeLabel.grid(row=3, column=7)


#Result Area start here
lblCoins = tk.Label(text="Coin break down:", 
                   font=('Time New Roman', 12,'bold'),
                   bg ='white',
                   fg='black') 
lblCoins.grid(row=5,column=0)

lblResult = tk.Label(text='', 
                   font=('Time New Roman', 12,'bold'),
                   bg ='white',
                   fg='black') 
lblResult.grid(row=6,column=0)


#Execute button
btnExe = tk.Button(text="Exec", command=coinChange,width=10,height=2)
btnExe.place(x=460,y=120)

#Clear Button
clearBtn = tk.Button(text="Clear",command=clearDict,width=10,height=2)
clearBtn.place(x=460,y=170)
#Quit button
btnQuit = tk.Button(text="Quit", command=exitApp, width=10,height=2)
btnQuit.place(x=460,y=220)

#mainloop() is an infinite loop used to run the application, 
#wait for an event to occur and process the event as long as the window is not closed
window.mainloop()


