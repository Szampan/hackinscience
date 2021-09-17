def battery_charge(battery):   
    
    n = round((battery) / 10)
    stripes = (" " * 10).replace(" ", "❚", n)
   
    print(f"[{stripes}]")
    print(f"{battery}%")

for i in range(20):
    battery_charge(i)
    print()