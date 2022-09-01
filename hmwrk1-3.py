x_coord = int(input("Введите X: "))
y_coord = int(input("Введите Y: "))
if x_coord > 0 :
    if y_coord > 0 :
        print (f"Точка ({x_coord},{y_coord}) находится в I четверти ")
    else:
        print (f"Точка ({x_coord},{y_coord}) находится в II четверти ")
elif y_coord > 0 :
    print (f"Точка ({x_coord},{y_coord}) находится в IV четверти ")
else:
    print (f"Точка ({x_coord},{y_coord}) находится в III четверти ")
