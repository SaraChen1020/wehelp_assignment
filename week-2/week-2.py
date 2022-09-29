# 要求一
def calculate(min, max, step):
            sum=0
            for i in range(min, max+1, step): 
                sum=sum+i
            print(sum)

calculate(1, 3, 1)
calculate(4, 8, 2)
calculate(-1, 2, 2)

# 要求二
def avg(data):
    people=0
    sum=0
    employees=data["employees"] #取出employees列表
    for i in employees:
        manager=i["manager"] #取出manager的值
        if manager==False:
            people=people+1 #計算出有幾位False
            salary=i["salary"]
            sum=sum+salary #計算薪資總和

    result=sum/people   
    print(result)

avg({"employees":[{"name":"John","salary":30000,"manager":False},
{"name":"Bob","salary":60000,"manager":True},
{"name":"Jenny","salary":50000,"manager":False},
{"name":"Tony","salary":40000,"manager":False}]})

# 要求三
def func(a):
    def addsum(b,c):
        print(a+b*c)
    return addsum

func(2)(3, 4)
func(5)(1, -5)
func(-3)(2, 9)


# 要求四
def maxProduct(nums):
    A=[]
    N=len(nums)
    for s in range(N):
        f=nums[s] #nums[0][1][2][3]
        for i in range(s+1,N): #range(1,4) (2,4) (3,4) (4,4)
            x=f*nums[i]
            A=A+[x] #把相乘後的結果放進陣列裡
    result=max(A) #取陣列最大值
    print(result)

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到  2
maxProduct([-5, -2]) # 得到 10

# 要求五
def twoSum(nums,target):
    N=len(nums) #N為4
    for s in range(N):
        f=nums[s]
        for i in range(s+1,N):
            x=f+nums[i]
            if x==target:
                return [s,i]


result=twoSum([2, 11, 7, 15], 9)
print(result)

# 要求六
def maxZeros(nums):
    N=len(nums) #nums長度
    repeat_time=0 #計算出現0的次數
    not_ans=0 #計算不為0的次數
    B=[] 

    for i in nums:
        if i==0:
            repeat_time += 1 #出現0時就+1
            B=B+[repeat_time] #將有出現0的次數放入[]中
            result=max(B) #取[]中最大值 代表連續出現次數的最大值
        else:
             repeat_time=0 #如果不為0 就將計算歸0
             not_ans+=1  #計算不為0的次數
    
    if not_ans==N: #如果不為0的次數與nums內的長度相同,代表裡面都沒有0
        result=0 #故將result歸0

    print(result)


maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3