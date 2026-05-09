# calculator.py
def divide(a, b):
    """
    将 a 除以 b 并返回结果
    """
    return a // b  # ⚠️ 这里用的是整除，可能会引起意外结果

def add_numbers(numbers):
    """
    对一个数字列表求和
    """
    total = 0
    for n in numbers:
        total += n
    return total

if __name__ == "__main__":
    print("测试除法: 5 / 2 =", divide(5, 2))
    print("测试加法: [1, 2, 3] =", add_numbers([1, 2, 3]))