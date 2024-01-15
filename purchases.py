from tkinter import *

purchases = Tk()
purchases.geometry("800x500")
purchases.title("Purchases")
purchases.configure(bg="#219ebc")

background_image = PhotoImage(file = r"c:\Users\hp\Desktop\secondbg.png")
background_label = Label(purchases, image=background_image)
background_label.place(relwidth=1, relheight=1)


head = Label(purchases, text="> Purchases",
              font=("Arial", 20, "bold"),
              fg="white",
              bg="orange",
              pady=20,
              width=300)
#313131
product_id = Label(purchases, text="Product ID", font=("Arial", 16), bg="black", fg="white")
supplier = Label(purchases, text="supplier", font=("Arial", 16), bg="black", fg="white")
phone = Label(purchases, text="phone", font=("Arial", 16), bg="black", fg="white")
product_name = Label(purchases, text="Product Name", font=("Arial", 16), bg="black", fg="white")
price = Label(purchases, text="Price", font=("Arial", 16), bg="black", fg="white")
quantity = Label(purchases, text="Quantity", font=("Arial", 16), bg="black", fg="white")

product_id_input = Entry(purchases)
supplier_input = Entry(purchases)
phone_input = Entry(purchases)
product_name_input = Entry(purchases)
price_input = Entry(purchases)
quantity_input = Entry(purchases)


head.place(x=150,y=30, anchor=CENTER)


product_id.place(x=140, y= 120, anchor=E)
product_id_input.place(x=280, y= 120, anchor=W, width=250, height=30)

supplier.place(x=114, y= 160, anchor=E)
supplier_input.place(x=280, y= 160, anchor=W, width=250, height=30)

phone.place(x=98, y= 200, anchor=E)
phone_input.place(x=280, y= 200, anchor=W, width=250, height=30)

product_name.place(x=100, y= 240, anchor=CENTER)
product_name_input.place(x=280, y= 240, anchor=W, width=250, height=30)

price.place(x=84, y= 280, anchor=E)
price_input.place(x=280, y= 280, anchor=W, width=250, height=30)

quantity.place(x=116, y= 320, anchor=E)
quantity_input.place(x=280, y= 320, anchor=W, width=250, height=30)




purchases.mainloop()
