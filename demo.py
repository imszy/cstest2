print("Hello, World!")

a = 5
b = 3
sum = a + b
print(f"{a} + {b} = {sum}")

# 乘法演示
times = a * b
print(f"{a} * {b} = {times}")

# 用户输入两个数字并输出它们的和
a_input = int(input("请输入第一个数字: "))
b_input = int(input("请输入第二个数字: "))
sum_input = a_input + b_input
print(f"{a_input} + {b_input} = {sum_input}")

# 循环打印1到5
print(f"循环打印1到5：")
for i in range(1, 6):
    print(i)

# 函数封装

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

# 判断奇偶
def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} 是偶数")
    else:
        print(f"{num} 是奇数")

# 用户输入两个数字并输出它们的乘积
x_input = int(input("请输入要相乘的第一个数字: "))
y_input = int(input("请输入要相乘的第二个数字: "))
product = multiply(x_input, y_input)
print(f"{x_input} * {y_input} = {product}")

# 判断用户输入的数字奇偶
num_check = int(input("请输入一个数字判断奇偶: "))
check_even_odd(num_check) 