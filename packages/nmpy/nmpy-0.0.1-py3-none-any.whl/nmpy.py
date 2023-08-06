
class input(Exception):
    def __init__(self, message):
        self.message = message
        input

    def __str__(self):
        return self.message

try:
    raise input("\033[31m" + """

    ##级数求和
    m=int(input())
    S=0
    for i in range(11,m+1):
        S=S+i
    print("sum = {}".format(S))

    ##乘积项求和
    m = int(input())
    result = 0
    for i in range(1, m):
        result += i * (i+1)
    print(f'sum = {result}')

    ##BC类和对象
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def move(self, x1, y1):
            new_x = self.x + x1
            new_y = self.y + y1
            return Point(new_x, new_y)

        def __str__(self):
            return f"({self.x},{self.y})"

    if __name__ == '__main__':
        while True:
            try:
                x, y, n = map(int, input().split())
                point = Point(x, y)
                for i in range(n):
                    xi, yi = map(int, input().split())
                    point = point.move(xi, yi)
                print(point)
            except EOFError:
                break

    ##BC字符替换
    s = input()
    trans = {chr(i+65): chr(90-i) for i in range(26)}
    result = ""
    for c in s:
        if c in trans:
            result += trans[c]
        else:
            result += c
    print(result)

    ##HS余弦函数近似值
    def factorial(n):
        prod = 1
        for i in range(1, n + 1):
            prod *= i
        return prod

    def funcos(eps, x):
        i = 0
        sum = 0
        while pow(x, 2 * i) / factorial(2 * i) >= eps:
            sum += pow(-1, i) * pow(x, 2 * i) / factorial(2 * i)
            i += 1
        return sum

    ##HS三边长求面积
    try:
        p = (a + b + c) * 0.5
        c = (p * (p - a) * (p - b) * (p - c))
        ans = pow(c, 0.5)
        ans = str(ans)
        ans = float(ans)

    ##HS找钱
    def giveChange(num):
        x=int(num/10)
        m=num%10
        y=int(m/5)
        m=m%5
        z=int(m/1)
        print("{} = {}*10 + {}*5 + {}*1".format(num,x,y,z))

    ##HS多项式值
    def polyvalue(lst, x):
        n = len(lst)
        result = 0
        for i in range(n):
            result += lst[i] * (x ** i)
        return result

    ##HS切片
    def func(list1):
        if len(list1) > 2:
            return list1[:2]
        else:
            return list1

    ##HS计算薪资
    def bonus(sales):
        s = float(sales)
        n = 5000
        if s <= 10000:
            return n
        elif s > 10000 and s <= 20000:
            return s*0.1 + n
        elif s > 20000 and s <= 50000:
            return s*0.15 + n
        elif s > 50000 and s <= 100000:
            return s*0.2 +n
        else:
            return s*0.25 + n

    ##统计数字个数
    def CountDigit(number, digit):
        count = 0
        number = str(abs(number))
        for ch in number:
            if int(ch) == digit:
                count += 1
        return count
    """ + "\033[0m")
except input as e:
    print(e)

