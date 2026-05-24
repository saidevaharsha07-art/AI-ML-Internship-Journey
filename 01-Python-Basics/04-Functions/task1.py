def food_order(name,item="Pizza",*extras):
    print("Customer Name:",name)
    print("Item:",item)
    if extras:
        print("Extras:",extras)
        for extra in extras:
            print("-",extra)
    else:
        print("No extras added.")
order1 = food_order("Harsha")
print()
order2 = food_order("Harsha","Burger")
print()
order3 = food_order("Harsha","Pasta","Dosa","Idly")
print()