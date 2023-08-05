继承TaskBase，可以实现子类方法的自动埋点和错误统计等功能.本次更新如下：
- 方法出现异常后，会自动记录错误，而不是使整个程序崩溃.
- 本次增加了将日志输出到本地文件。

### *使用示例：*
``` python
from taskbase import TaskBase
import time

class testSubClass(TaskBase):
    def my_method(self, arg1, arg2, arg3):
        time.sleep(0.5)
        print("猜猜看，父类做了些什么？")

    def error_test(self):
        time.sleep(1.2)
        try:
            print(1/0)            
        except Exception as e:
            print(e)
        print(1/0)
        print("hello")

a=testSubClass()
a.my_method(10086,time,"第三个参数")
a.error_test()
```

### *输出显示：*
``` powershell
猜猜看，父类做了些什么？
2023-05-17 16:27:50     0.500s  TaskBase.testSubClass.my_method(10086, <module 'time' (, 第三个参数)
division by zero
2023-05-17 16:27:52     testSubClass.error_test()出现异常:       division by zero
2023-05-17 16:27:51     1.200s  TaskBase.testSubClass.error_test()
```

---
### 友情链接
| 名称 | 链接 |
| ---- | ---- |
| markdown语法 | https://daringfireball.net/projects/markdown/ |
| PowerShell 7 | https://github.com/PowerShell/PowerShell/releases |
| P语义化版本 | https://semver.org/lang/zh-CN/
