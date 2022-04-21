def add(expression):
    try:
        if expression[0] == "/":
            prefixes = list(expression[2:expression.find('\n')])
            input_vals_as_str = expression[expression.find('\n')+1:]
            input_vals = []
            current_value = ''
            for char in input_vals_as_str:
                if char in prefixes:
                    input_vals.append(current_value)
                    current_value = ''
                else:
                    current_value += char
            input_vals.append(current_value)
        else:
            if ";" in expression:
                input_vals = expression.split(';')
            else:
                input_vals = expression.split(',')
        values = []
        for val in input_vals:
            values.append(float(val))
        total = sum(values)
        if int(total) == total:
            return int(total)
        else:
            return total
    except (ValueError, AttributeError, TypeError):
        return -1
