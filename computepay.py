def computepay(totalH,PerHMoney):
    pay = totalH *PerHMoney
    return pay

tH = float(input())
tM = int(input())


payable = computepay(tH,tM)
print(payable)

'''"D:\python project\startPython\venv\Scripts\python.exe" "D:/python project/startPython/computepay.py"
450

Process finished with exit code 0
'''