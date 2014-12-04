from Tkinter import *
class Check_in(object):
    root = Tk()
    box = Entry(root, width = 30)
    root1 = Tk()
    price = []
    count = 0
    def __init__(self):
        price = []
        head = Label(self.root, text="Welcome to 10 Tables Restaurant")
        head.pack()
        head1 = Label(self.root, text="Name")
        head1.pack()
        self.box.pack()
        self.b = Button(self.root, text="Reserve", width=10\
                        , command=self.monitor)
        self.b.pack()
        self.root.mainloop()

    def monitor(self):
        if self.count >= 10:
            print 'Table are full reserved now, please checking again in 10 minutes'
        else:
            list1 = ['Fried chicken $6', 'Rice $1', 'Noodle $8', 'Salad $5']
            self.name = self.box.get()
            head1 = Label(self.root1, text=self.name)
            head1.pack()
    ##        self.b = Button(self.root1, text="Order", width=10\
    ##                        , command=self.order_food)
    ##        self.b.pack()
            self.spindle = StringVar(self.root1)
            self.spindle.set(list1[0]) #default value
            s = OptionMenu(self.root1, self.spindle, *list1)
            s.pack()

            button = Button(self.root1, text="Submit", command=self.submit)
            button.pack()

            bill_button = Button(self.root1, text="Check Bill", command=self.check_bill)
            bill_button.pack()

            self.count += 1
            print self.name

    def submit(self):
        print self.spindle.get()
        self.price.append(int(self.spindle.get()[-1]))

    def check_bill(self):
        print sum(self.price)
        self.price = []
##    def order_food(self):
##        root2 = Tk()
##        self.b = Button(root2, text="Noodle", width=10\
##                        , command=self.monitor)
##        self.b.pack()
##        self.b = Button(root2, text="Fried chicken", width=10\
##                        , command=self.monitor)
##        self.b.pack()
##        self.b = Button(root2, text="Rice", width=10\
##                        , command=self.monitor)
##        self.b.pack()

Check_in()


