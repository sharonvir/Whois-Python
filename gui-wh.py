# Creator : MR.D3F417 > BLACK GUARD TM > 
# Discord : https://discord.gg/EZssbvh8UF
# Dont Copy kid
# pip install python-whois

from tkinter import *
import whois


# user define funtion
# for get domain information
def Domain_info():
	domain = whois.whois(str(e1.get()))
	server.set(domain.whois_server)
	exp_date.set(domain.expiration_date)
	reg_name.set(domain.name)
	org.set(domain.org)
	state.set(domain.state)
	city.set(domain.city)
	country.set(domain.country)


# object of tkinter
# and background set for Gray
master = Tk()
master.configure(bg='gray')

# Variable Classes in tkinter
server = StringVar()
exp_date = StringVar()
reg_name = StringVar()
org = StringVar()
state = StringVar()
city = StringVar()
country = StringVar()

# Creating label for each information
# name using widget Label
Label(master, text="[BG] Website URL : ", bg="Gray").grid(row=0, sticky=W)
Label(master, text="[BG] Server Name :", bg="Gray").grid(row=3, sticky=W)
Label(master, text="[BG] Expiration date :", bg="Gray").grid(row=4, sticky=W)
Label(master, text="[BG] Register name :", bg="Gray").grid(row=5, sticky=W)
Label(master, text="[BG] Origination :", bg="Gray").grid(row=6, sticky=W)
Label(master, text="[BG] State :", bg="Gray").grid(row=7, sticky=W)
Label(master, text="[BG] City :", bg="Gray").grid(row=8, sticky=W)
Label(master, text="[BG] Country :", bg="Gray").grid(row=9, sticky=W)

# Creating label for class variable
# name using widget Entry
Label(master, text="", textvariable=server,
	bg="Gray").grid(row=3, column=1, sticky=W)
Label(master, text="", textvariable=exp_date,
	bg="Gray").grid(row=4, column=1, sticky=W)
Label(master, text="", textvariable=reg_name,
	bg="Gray").grid(row=5, column=1, sticky=W)
Label(master, text="", textvariable=org, bg="Gray").grid(
	row=6, column=1, sticky=W)
Label(master, text="", textvariable=state,
	bg="Gray").grid(row=7, column=1, sticky=W)
Label(master, text="", textvariable=city,
	bg="Gray").grid(row=8, column=1, sticky=W)
Label(master, text="", textvariable=country,
	bg="Gray").grid(row=9, column=1, sticky=W)


e1 = Entry(master)
e1.grid(row=0, column=1)

# creating a button using the widget
# Button that will call the submit function
b = Button(master, text="Get", command=Domain_info, bg="white")
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5,)

mainloop()