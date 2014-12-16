from Tkinter import *
from PIL import Image, ImageTk

class Check_in(object):
    '''This Class is use to keep all funtion for look easy
        This program is use to pre-reserve table in restaurant for easy
        and comfortable, now we can reserve about 5 tables. But in future
        we will develop this program for more table and more function. Thank you'''
    #main window
    root = Tk()
    root.title("Table-Reservation")
    root.geometry('800x700+230+40')
    root.resizable(width=FALSE, height=FALSE)
    #background
    bg_image = Image.open("red.bmp")
    bg_photo =  ImageTk.PhotoImage(bg_image)
    bg_pic = Label(root, image=bg_photo)
    bg_pic.pack()
    #photo
    logo_image = Image.open("logo6.jpg")
    logo_photo =  ImageTk.PhotoImage(logo_image)
    logo_pic = Label(root, image=logo_photo)
    logo_pic.place(x=319, y=75)
    #for reservation
    box = Entry(root, width = 50, bg = '#FFFFC2')
    count = 300 #count is use to fix position of button, other option and use to limit amount of tables
    listm = [] #listm is use to find position of name that empty and replaced it
    data1, data2, data3, data4, data5 = [], [], [], [], [] #database of meny that customer ordered
    total1, total2, total3, total4, total5 = [], [], [], [], [] #database of price in check bill function
    order_amount1, order_amount2, order_amount3, order_amount4, order_amount5 = {}, {}, {}, {}, {}
    
    def __init__(self):
        price = []
        about = Button(self.root, width = 115, text="About this program", command=self.detail)
        about.place(x=0, y=0)
        head = Label(self.root, text="Welcome to 5 Tables Restaurant", bg='#9C000F', fg='white')
        head.place(x=320, y=40)
        head1 = Label(self.root, text="Enter your name here", bg='#9C000F', fg='white')
        head1.place(x=340, y=180)
        self.box.place(x=250, y=210)
        self.b = Button(self.root, text="Reserve", width=10\
                        , command=self.monitor, bg = '#FDD017')
        self.b.place(x=360, y=240)
        self.root.mainloop()

    def monitor(self):
        '''This function is use to link all button and another option'''
        if self.count >= 500:
            root1 = Tk()
            caution = Label(root1, text="Table are full reserved now, please checking again in 10 minutes")
            caution.pack()
            exits = Button(root1, text='OK', command = root1.destroy, bg = '#92C7C7')
            exits.pack()

        else:
            position = 0
            for i in xrange(300, 461, 40):
                position += 1
                if i not in self.listm:
                    self.count = i
                    self.listm.append(i)
                    list1 = ['Fried chicken $6', 'Rice $1', 'Noodle $7', 'Salad $5', 'Pizza $9', 'Pasta $7', 'Juice $1', \
                             'Steak $9', 'Fried rice $2', 'Lasagna $9']
                    self.name = self.box.get()
                    head1 = Label(self.root, text='Table ' + str(position) + '   ' + self.name, bg='#9F000F',fg = 'white')
                    head1.place(x=50, y=self.count)

                    self.spindle = StringVar(self.root)
                    self.spindle.set('Pre-Order') #default value
                    s = OptionMenu(self.root, self.spindle, *list1)
                    s.place(x=250, y=self.count)

                    button_submit = Button(self.root, text="Submit", command=self.submit, bg = '#FFDB58')
                    button_submit.place(x=400, y=self.count)

                    button_calcel = Button(self.root, text="Cancel", command=self.cancel, bg = '#FFDB58')
                    button_calcel.place(x=450, y=self.count)


                    if self.count == 300:
                        bill_button = Button(self.root, text="Check Bill", command=self.check_bill1, bg = '#FDD017')
                        bill_button.place(x=650, y=self.count)
                        menu_list = Button(self.root, text="Your Ordered", command=self.menu_list1, bg = '#FFD801')
                        menu_list.place(x=550, y=self.count)
                    elif self.count == 340:
                        bill_button = Button(self.root, text="Check Bill", command=self.check_bill2, bg = '#FDD017')
                        bill_button.place(x=650, y=self.count)
                        menu_list = Button(self.root, text="Your Ordered", command=self.menu_list2, bg = '#FFD801')
                        menu_list.place(x=550, y=self.count)
                    elif self.count == 380:
                        bill_button = Button(self.root, text="Check Bill", command=self.check_bill3, bg = '#FDD017')
                        bill_button.place(x=650, y=self.count)
                        menu_list = Button(self.root, text="Your Ordered", command=self.menu_list3, bg = '#FFD801')
                        menu_list.place(x=550, y=self.count)
                    elif self.count == 420:
                        bill_button = Button(self.root, text="Check Bill", command=self.check_bill4, bg = '#FDD017')
                        bill_button.place(x=650, y=self.count)
                        menu_list = Button(self.root, text="Your Ordered", command=self.menu_list4, bg = '#FFD801')
                        menu_list.place(x=550, y=self.count)
                    elif self.count == 460:
                        bill_button = Button(self.root, text="Check Bill", command=self.check_bill5, bg = '#FDD017')
                        bill_button.place(x=650, y=self.count)
                        menu_list = Button(self.root, text="Your Ordered", command=self.menu_list5, bg = '#FFD801')
                        menu_list.place(x=550, y=self.count)

                    self.count += 40
                    break

    def submit(self):
        '''This function is use to command to save list of menu that customer ordered to this restaurant'''
        ##add price to data##
        if self.spindle.get() != 'Pre-Order': #this loop is use to find and keep data in each customer
            if self.count == 340: #add data to data1 and total1 for table1
                self.data1.append(self.spindle.get())
                self.total1.append(int(self.spindle.get()[-1]))
                if self.spindle.get() not in self.order_amount1:
                    self.order_amount1[self.spindle.get()] = 1
                else:
                    self.order_amount1[self.spindle.get()] += 1
            elif self.count == 380: #add data to data1 and total1 for table2
                self.data2.append(self.spindle.get())
                self.total2.append(int(self.spindle.get()[-1]))
                if self.spindle.get() not in self.order_amount2:
                    self.order_amount2[self.spindle.get()] = 1
                else:
                    self.order_amount2[self.spindle.get()] += 1
            elif self.count == 420: #add data to data1 and total1 for table3
                self.data3.append(self.spindle.get())
                self.total3.append(int(self.spindle.get()[-1]))
                if self.spindle.get() not in self.order_amount3:
                    self.order_amount3[self.spindle.get()] = 1
                else:
                    self.order_amount3[self.spindle.get()] += 1
            elif self.count == 460: #add data to data1 and total1 for table4
                self.data4.append(self.spindle.get())
                self.total4.append(int(self.spindle.get()[-1]))
                if self.spindle.get() not in self.order_amount4:
                    self.order_amount4[self.spindle.get()] = 1
                else:
                    self.order_amount4[self.spindle.get()] += 1
            elif self.count == 500: #add data to data1 and total1 for table5
                self.data5.append(self.spindle.get())
                self.total5.append(int(self.spindle.get()[-1]))
                if self.spindle.get() not in self.order_amount5:
                    self.order_amount5[self.spindle.get()] = 1
                else:
                    self.order_amount5[self.spindle.get()] += 1

    def cancel(self):
        '''This function is use to cancel things that customer change there mind'''
        if self.count == 340:
            if self.order_amount1[self.spindle.get()] > 0:
                self.order_amount1[self.spindle.get()] -= 1
            if self.order_amount1[self.spindle.get()] <= 0:
                self.data1.remove(self.spindle.get())
            self.total1.remove(int(self.spindle.get()[-1])) ##remove price in total1
        elif self.count == 380:
            if self.order_amount2[self.spindle.get()] > 0:
                self.order_amount2[self.spindle.get()] -= 1
            if self.order_amount2[self.spindle.get()] <= 0:
                self.data2.remove(self.spindle.get())
                self.total2.remove(int(self.spindle.get()[-1]))
            self.total2.remove(int(self.spindle.get()[-1])) ##remove price in total2
        elif self.count == 420:
            if self.order_amount3[self.spindle.get()] > 0:
                self.order_amount3[self.spindle.get()] -= 1
            if self.order_amount3[self.spindle.get()] <= 0:
                self.data3.remove(self.spindle.get())
            self.total3.remove(int(self.spindle.get()[-1])) ##remove price in total3
        elif self.count == 460:
            if self.order_amount4[self.spindle.get()] > 0:
                self.order_amount4[self.spindle.get()] -= 1
            if self.order_amount4[self.spindle.get()] <= 0:
                self.data4.remove(self.spindle.get())
            self.total4.remove(int(self.spindle.get()[-1])) ##remove price in total4
        elif self.count == 500:
            if self.order_amount5[self.spindle.get()] > 0:
                self.order_amount5[self.spindle.get()] -= 1
            if self.order_amount5[self.spindle.get()] <= 0:
                self.data5.remove(self.spindle.get())
            self.total5.remove(int(self.spindle.get()[-1])) ##remove price in total5

     ####################################apart all menu list for 5 customers####################################
    def menu_list1(self):
        '''This function is use to save list of menu that customer ordered'''
        line = 0
        rootm = Tk() #rootm is window of menu list
        rootm.resizable(width=FALSE, height=FALSE)
        Label(rootm, text='Amount').place(x=230, y=line)
        self.data1 = list(set(self.data1))
        for i in self.data1:
            line += 30
            Label(rootm, text=i).place(x=10, y=line)
            Label(rootm, text=self.order_amount1[i]).place(x=250, y=line)
        self.okbutton_menu_list(rootm, line)
    def menu_list2(self):
        '''This function is use to save list of menu that customer ordered'''
        line = 0
        rootm = Tk()
        rootm.resizable(width=FALSE, height=FALSE)
        Label(rootm, text='Amount').place(x=230, y=line)
        self.data2 = list(set(self.data2))
        for i in self.data2:
            line += 30
            Label(rootm, text=i).place(x=10, y=line)
            Label(rootm, text=self.order_amount2[i]).place(x=250, y=line)
        self.okbutton_menu_list(rootm, line)
    def menu_list3(self):
        '''This function is use to save list of menu that customer ordered'''
        line = 0
        rootm = Tk()
        rootm.resizable(width=FALSE, height=FALSE)
        Label(rootm, text='Amount').place(x=230, y=line)
        self.data3 = list(set(self.data3))
        for i in self.data3:
            line += 30
            Label(rootm, text=i).place(x=10, y=line)
            Label(rootm, text=self.order_amount3[i]).place(x=250, y=line)
        self.okbutton_menu_list(rootm, line)
    def menu_list4(self):
        '''This function is use to save list of menu that customer ordered'''
        line = 0
        rootm = Tk()
        rootm.resizable(width=FALSE, height=FALSE)
        Label(rootm, text='Amount').place(x=230, y=line)
        self.data4 = list(set(self.data4))
        for i in self.data4:
            line += 30
            Label(rootm, text=i).place(x=10, y=line)
            Label(rootm, text=self.order_amount4[i]).place(x=250, y=line)
        self.okbutton_menu_list(rootm, line)
    def menu_list5(self):
        '''This function is use to save list of menu that customer ordered'''
        line = 0
        rootm = Tk()
        rootm.resizable(width=FALSE, height=FALSE)
        Label(rootm, text='Amount').place(x=230, y=line)
        self.data5 = list(set(self.data5))
        for i in self.data5:
            line += 30
            Label(rootm, text=i).place(x=10, y=line)
            Label(rootm, text=self.order_amount5[i]).place(x=250, y=line)
        self.okbutton_menu_list(rootm, line)

    def okbutton_menu_list(self, rootm, line):
        '''This function is use to build ok button that use in many function above'''
        rootm.geometry(str(300)+'x'+str(line+60))
        exits = Button(rootm, text='OK', command = rootm.destroy, bg = '#FDD017')
        exits.place(x=140, y=line+30)

    ####################################apart all button check bill for 5 customers####################################
    def check_bill1(self):
        '''Keep database of Table1 and ready to calculate all the time'''
        rootb = Tk() #rootb is window of check bill
        rootb.resizable(width=FALSE, height=FALSE)
        line = 0
        Label(rootb, text='Amount').place(x=230, y=line)
        self.data1 = list(set(self.data1))
        for i in self.data1:
            line += 30
            Label(rootb, text=i).place(x=10, y=line)
            Label(rootb, text=self.order_amount1[i]).place(x=250, y=line)
        Label(rootb, text='Price   =   $' + str(sum(self.total1))).place(x=200, y=line+30)
        self.okbutton_check_bill(rootb, line)
        a = Label(self.root, text='                '*100, bg='#9C000F') ##use to replace customer who is already check bill
        a.place(y=300)
        a = Label(self.root, text='                '*100, bg='#9C000F') ##use to replace customer who is already check bill
        a.place(y=310)
        self.listm.remove(300)
        self.count -= 40
        self.data1, self.total1 = [], []
        self.order_amount1 = dict()

    def check_bill2(self):
        '''Keep database of Table2 and ready to calculate all the time'''
        rootb = Tk()
        rootb.resizable(width=FALSE, height=FALSE)
        line = 0
        Label(rootb, text='Amount').place(x=230, y=line)
        self.data2 = list(set(self.data2))
        for i in self.data2:
            line += 30
            Label(rootb, text=i).place(x=10, y=line)
            Label(rootb, text=self.order_amount2[i]).place(x=250, y=line)
        Label(rootb, text='Price   =   $' + str(sum(self.total2))).place(x=200, y=line+30)
        self.okbutton_check_bill(rootb, line)
        a = Label(self.root, text='                '*100, bg='#9C000F')
        a.place(y=340)
        a = Label(self.root, text='                '*100, bg='#9C000F')
        a.place(y=350)
        self.listm.remove(340)
        self.count -= 40
        self.data2, self.total2 = [], []
        self.order_amount2 = dict()
    def check_bill3(self):
        '''Keep database of Table3 and ready to calculate all the time'''
        rootb = Tk()
        rootb.resizable(width=FALSE, height=FALSE)
        line = 0
        Label(rootb, text='Amount').place(x=230, y=line)
        self.data3 = list(set(self.data3))
        for i in self.data3:
            line += 30
            Label(rootb, text=i).place(x=10, y=line)
            Label(rootb, text=self.order_amount3[i]).place(x=250, y=line)
        Label(rootb, text='Price   =   $' + str(sum(self.total3))).place(x=200, y=line+30)
        self.okbutton_check_bill(rootb, line)
        a = Label(self.root, text='                '*100, bg='#9C000F')
        a.place(y=380)
        a = Label(self.root, text='                '*100, bg='#9C000F')
        a.place(y=390)
        self.listm.remove(380)
        self.count -= 40
        self.data3, self.total3 = [], []
        self.order_amount3 = dict()

    def check_bill4(self):
        '''Keep database of Table4 and ready to calculate all the time'''
        rootb = Tk()
        rootb.resizable(width=FALSE, height=FALSE)
        line = 0
        Label(rootb, text='Amount').place(x=230, y=line)
        self.data4 = list(set(self.data4))
        for i in self.data4:
            line += 30
            Label(rootb, text=i).place(x=10, y=line)
            Label(rootb, text=self.order_amount4[i]).place(x=250, y=line)
        Label(rootb, text='Price   =   $' + str(sum(self.total4))).place(x=200, y=line+30)
        self.okbutton_check_bill(rootb, line)
        a = Label(self.root, text='                '*100, bg='#9C000F')
        a.place(y=420)
        a = Label(self.root, text='                '*100, bg='#9C000F')
        a.place(y=430)
        self.listm.remove(420)
        self.count -= 40
        self.data4, self.total4 = [], []
        self.order_amount4 = dict()

    def check_bill5(self):
        '''Keep database of Table4 and ready to calculate all the time'''
        rootb = Tk()
        rootb.resizable(width=FALSE, height=FALSE)
        line = 0
        Label(rootb, text='Amount').place(x=230, y=line)
        self.data5 = list(set(self.data5))
        for i in self.data5:
            line += 30
            Label(rootb, text=i).place(x=10, y=line)
            Label(rootb, text=self.order_amount5[i]).place(x=250, y=line)
        Label(rootb, text='Price   =   $' + str(sum(self.total5))).place(x=200, y=line+30)
        self.okbutton_check_bill(rootb, line)
        a = Label(self.root, text='                '*100, bg='#9C000F')
        a.place(y=460)
        a = Label(self.root, text='                '*100, bg='#9C000F')
        a.place(y=470)
        self.listm.remove(460)
        self.count -= 40
        self.data5, self.total5 = [], []
        self.order_amount5 = dict()

    def okbutton_check_bill(self, rootb, line):
        '''This function is use to build ok button that use in many function above'''
        rootb.geometry(str(300)+'x'+str(line+90))
        exits = Button(rootb, text='OK', command = rootb.destroy, bg = '#FDD017')
        exits.place(x=140, y=line+60)

    def detail(self):
        '''This function is use to explain about this program in short paragraph'''
        rootd = Tk() #rootd is window of detail about this program
        rootd.resizable(width=FALSE, height=FALSE)
        scrollb = Scrollbar(rootd)
        texture = Text(rootd, height=4, width=57)
        scrollb.pack(side=RIGHT, fill=Y)
        texture.pack(side=LEFT, fill=Y)
        scrollb.config(command=texture.yview)
        texture.config(yscrollcommand=scrollb.set)
        quote = """This program is use to reserve a table from another place. \
You can pre-order for more rapid and comfort in your dialy life. \
This program is help you that you haven't wait for food anymore \
if you pre-order to there restaurant, all foods that will come \
to your table in 5 minutes because we had cooked for you and boil \
all the time. When you ate already you can click check bill button. \
This program will calculate all price for you to pay. \
Attention!!! : Customer can submit or cancel menu until next customer \
come to submit over you."""
        texture.insert(END, quote)
        
        
Check_in()
