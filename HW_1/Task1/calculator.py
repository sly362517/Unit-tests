def calculate(first_operand: int, second_operand: int, operator: str) -> int | float:  
    match operator:
        case '+':
            result = first_operand + second_operand
        case '-':
            result = first_operand - second_operand
        case '*':
            result = first_operand * second_operand
        case '/':
            if second_operand != 0:
                result = first_operand / second_operand
            else:
                raise ArithmeticError("нельзя, ну нельзя делить на 0")
        case _:
            raise ValueError("не известный оператор, выберите другое значение: " + operator)
    return result



def calculate_discount(purchase_amount: float, discount_amount: int) -> float:
    if discount_amount < 0:
        raise ArithmeticError("Скидка не может быть меньше нуля")
    elif discount_amount > 100:
        raise ArithmeticError("Скидка не может превышать 100")
    return purchase_amount - (purchase_amount * discount_amount) / 100



if __name__ == "__main__":
    print(calculate(2, 7, '-'))
    print(calculate(5, 15, '*'))
    print(calculate(5, 5, '/'))
    print(calculate_discount(1250, 95))
    print(calculate_discount(4527, 50))