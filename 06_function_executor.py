def func_executor(*args):
    result = ""
    for item in args:
        function_name = item[0]
        function_args = item[1]
        function_result = function_name(*function_args)
        result += f"{function_name.__name__} - {function_result}\n"
    return result




def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
