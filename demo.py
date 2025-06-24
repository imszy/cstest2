print("Hello, World!")

a = 5
b = 3
sum = a + b
print(f"{a} + {b} = {sum}")

# 乘法演示
times = a * b
print(f"{a} * {b} = {times}")

# 用户输入两个数字并输出它们的和
try:
    a_input = int(input("请输入第一个数字: "))
    b_input = int(input("请输入第二个数字: "))
    sum_input = a_input + b_input
    print(f"{a_input} + {b_input} = {sum_input}")
except ValueError:
    print("输入无效，请输入整数！")

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
try:
    x_input = int(input("请输入要相乘的第一个数字: "))
    y_input = int(input("请输入要相乘的第二个数字: "))
    product = multiply(x_input, y_input)
    print(f"{x_input} * {y_input} = {product}")
except ValueError:
    print("输入无效，请输入整数！")

# 判断用户输入的数字奇偶
try:
    num_check = int(input("请输入一个数字判断奇偶: "))
    check_even_odd(num_check)
except ValueError:
    print("输入无效，请输入整数！")

import random

def guess_number_game():
    print("\n欢迎来到猜数字游戏！我已经选好了1到100之间的一个数字。来试试你能几次猜中吧！")
    answer = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("请输入你的猜测（1-100）："))
            attempts += 1
            if guess < answer:
                print("太小了！")
            elif guess > answer:
                print("太大了！")
            else:
                print(f"恭喜你，猜对了！答案就是 {answer}，你一共猜了 {attempts} 次。\n")
                break
        except ValueError:
            print("输入无效，请输入整数！")

guess_number_game()

def file_write_read():
    print("\n文件读写演示：")
    text = input("请输入一段文本，将写入文件output.txt：")
    try:
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("内容已写入output.txt。")
        with open("output.txt", "r", encoding="utf-8") as f:
            content = f.read()
        print("文件内容如下：")
        print(content)
    except Exception as e:
        print(f"文件操作出错：{e}")

file_write_read() 