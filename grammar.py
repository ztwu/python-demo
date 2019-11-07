#python的基础语法

array1 = {1,2,3,4,5}

for item in array1:
    print(item)

array2 = [1,2,3,4,5]

for item in array2:
    print(item)

flag = ''
if flag == True:
    print("true")
elif flag == False:
    print("false")
else:
    print("no")

count = 0
while(count < 10):
    count += 1
    if count%2 > 0:
        continue
    else:
        print("count: ",count)

count = 0
while(count < 10):
    count += 1
    if count > 5:
        break
    else:
        print("count: ",count)

numbers = [1,2,3,4,5]
a1 = []
a2 = []
while(len(numbers)):
    number = numbers.pop()
    if number%2==0:
        a1.append(number)
    else:
        a2.append(number)

numbers = [1,2,3,4,5]
print(numbers[0])

#python里的列表用“[]”,可重复，类型可不同
list = [1,"ztwu"]
print(list[1])

#元组是只读的，不能修改。元组用“()”表示
tuple = (1,2,3,4,5)
print(tuple[1])

#字典存储键值对数据 ,字典用"{}"表示
dict = {"name":"ztwu5"}
print(dict["name"])


