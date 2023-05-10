def say_hello(name):
    print(f"Hello {name}!!!")
def add_num(num1, num2):
    return num1 + num2
def check_even(num):
    return num % 2 == 0
def check_even_list(num_list):
    even_list = []
    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
    return even_list
work_hours = [('Abby', 100), ('Billy', 1000), ('Cassie', 800)]
def employee_check(work_hour):
    current_max = 0
    employee_of_month = ''
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
    return current_max, employee_of_month
def lesser_of_two_evens(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1, num2)
    else:
        return max(num1, num2)
def animal_crackers(text):
    wordlist = text.split()
    if len(wordlist) == 2:
        if wordlist[0][0] == wordlist[1][0]:
            return True
        else:
            return False
    else:
        return False
print(animal_crackers("Crackhead Llama"))
print(lesser_of_two_evens(2,5))
say_hello("Abcdefgh")
result = add_num(10, 20)
print(result)
print(check_even(21))
print(check_even_list([x for x in range(0, 15, 2)]))
# Tuple unpacking with functions
print(employee_check(work_hours))
