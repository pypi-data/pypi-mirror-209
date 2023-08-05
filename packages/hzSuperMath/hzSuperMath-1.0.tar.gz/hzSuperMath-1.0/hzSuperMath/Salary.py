"""
用于计算公司员工的薪资
"""
print("被加载...")
company="HYN"
def yearSalary(monthSalary):
    '''
    根据付入的月薪 的值，计算出年薪: monthSalary * 12
    '''
    return monthSalary*12

def daySalary(monthSalary):
    '''
    根据付入的月薪的值，计算出1天的薪资。
     一个月按昭22.5天计算（国家规定的工作日）：monthSalary/22.5
     '''
    return monthSalary/22.5

#测试代码
if __name__ == "__main__":
    print(yearSalary(3000))
    print(daySalary(3000))