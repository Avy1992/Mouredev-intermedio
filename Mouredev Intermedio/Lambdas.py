### Lambdas ###

sum_two_values = lambda first_value, second_value: print(first_value + second_value)
sum_two_values('1', '2')

multiply_values = lambda first_val, second_val: first_val * second_val
print(multiply_values(3, 6))

def sum_three_values(value):
    return lambda first_val, second_val : first_val + second_val + value
print(sum_three_values(5)(1,4))