def get_spiral_value(x: int, y: int) -> int:
    
    x_value = 0
    y_value = 0
    number = 1
    vector = "right"
    do = 1
    already_do = 0
    points = 0

    while x_value != x or y_value != y:
        
        if points == 2:
            points = 0
            do += 1

        points += 1

        
        if vector == "top":
            while do != already_do:
                if x_value == x and y_value == y:
                    break
                y_value +=1
                number += 1
                already_do +=1
            

            vector = "left"
            already_do = 0

        elif vector == "bottom":
            while do != already_do:
                if x_value == x and y_value == y:
                    break
                
                y_value -=1
                number += 1
                already_do +=1
            

            vector = "right"
            already_do = 0

        elif vector == "left":
            while do != already_do:
                if x_value == x and y_value == y:
                    break
                
                x_value -=1
                number += 1
                already_do +=1
            

            vector = "bottom"
            already_do = 0

        elif vector == "right":
            while do != already_do:
                if x_value == x and y_value == y:
                    break
                
                x_value +=1
                number += 1
                already_do +=1
            

            vector = "top"
            already_do = 0
    return (number)
