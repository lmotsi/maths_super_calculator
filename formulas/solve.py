def split_equation(equation):
    split_up = []
    current_num = ""
    for i in equation:
        print(i)
        if i.isdigit() :
            current_num += i
        elif i in ["*","-","/","+"]:
            split_up.append(current_num)
            split_up.append(i)
            current_num = ""
        else:
            return i + " not a valid operation"
    if not current_num:
        return split_up[-1] + " needs a number on the right hand side"
    split_up.append(current_num)
    return split_up

def solve(equation):
    print(equation)
    if len(equation) == 1:
        return equation[0]
    elif type(equation)==str:
        return equation
    else:
        try:
            multiply_index = equation.index("*")
            result = float(equation.pop(multiply_index-1))*float(equation.pop(multiply_index))
            equation.pop(multiply_index-1)
            equation.insert(multiply_index-1,result)
            return solve(equation)
        except ValueError:
            try:
                divide_index = equation.index("/")
                result = float(equation.pop(divide_index-1))/float(equation.pop(divide_index))
                equation.pop(divide_index-1)
                equation.insert(divide_index-1,result)
                return solve(equation)
            except ValueError:
                try:
                    add_index = equation.index("+")
                    result = float(equation.pop(add_index-1))+float(equation.pop(add_index))
                    equation.pop(add_index-1)
                    equation.insert(add_index-1,result)
                    return solve(equation)
                except ValueError:
                    try:
                        subtract_index = equation.index("-")
                        result = float(equation.pop(subtract_index-1))-float(equation.pop(subtract_index))
                        equation.pop(subtract_index-1)
                        equation.insert(subtract_index-1,result)
                        return solve(equation)
                    except:
                        return equation[0]
equation = split_equation("6*8+5+9-7/2")
print(solve(equation))