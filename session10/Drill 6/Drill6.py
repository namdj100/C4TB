Huy = {
    'Name': 'Huy',
    'Role': 'Waiter',
    'Hours': 12,
    'Salary per Hour($)': 0.8,

}

Tung = {
    'Name': 'Tung',
    'Role': 'Cook',
    'Hours': 24,
    'Salary per Hour($)': 1.5,
}

MDuc = {
    'Name': 'MDuc',
    'Role': 'Manager',
    'Hours': 20,
    'Salary per Hour($)': 2,
}

Don = {
    'Name': 'Don',
    'Role': 'Waiter',
    'Hours': 12,
    'Salary per Hour($)': 0.9
}

HDuc = {
    'Name': 'HDuc',
    'Role': 'Waiter',
    'Hours': 14,
    'Salary per Hour($)': 0.7
}

Fastfood_restaurent = [Huy, Tung, MDuc, Don, HDuc]
print (Fastfood_restaurent)

x = 0
for i in Fastfood_restaurent:
    print("Luong cua ",i["Name"],":",i["Hours"]*i["Salary per Hour($)"])
    print("*"*20)

    x = x + i["Hours"]*i["Salary per Hour($)"]
print (x)
