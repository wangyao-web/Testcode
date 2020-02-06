a =[31,28,31,31,31,30,31,31,30,31,30,31]
year = int(input ("请输入年份："))
moth = int(input ("请输入月份："))
day = int(input ("请输入日："))
if year % 4 ==0 and year %100 !== 0 or year % 400 == 0 :
    a[1] = 29

for i in range(moth-1):
    days = a[i-1]+day
return  days
print("{}-{}-{}是今年的第{}天.format(year,moth,day,days)")
    
    

