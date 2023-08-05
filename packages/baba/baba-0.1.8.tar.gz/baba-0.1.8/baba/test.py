from taskbase import TaskBase
import time

class testSubClass(TaskBase):
    def my_method(self, arg1, arg2, arg3):
        time.sleep(0.5)
        print(f"{arg1}给{arg2}同学打了{arg3}分")

    def error_test(self):
        print(1/0)      
        print("hello")  # 这行代码不会被执行

a=testSubClass()
a.my_method('老师','有容',59)
a.error_test()   # 如果不继承父类，运行到这里异常退出
a.my_method('老师','lilei',88)  
