import time
import  datetime
import math

aa = time.time()
print(aa)

bb = time.localtime()
print(bb)

cc = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(cc)

dd = datetime.datetime.now();
print(dd)

def fun_test(p1,p2):
    return p1+p2

a = fun_test("hello","world")
print(a)

a = fun_test(p2='world',p1='hello')
print(a)

def fun_test_param(p1,*p2):
    print(p1)
    for i in p2:
        print(i)
    return;

fun_test_param("test",1,2,3,4)

#匿名函数
sum = lambda p1,p2:p1+p2
print(sum(5,8))

total = 10;
def test_function(arg):
    b = arg + 10;
    print("局部：",b)
    return;

test_function(total)
print(total)
