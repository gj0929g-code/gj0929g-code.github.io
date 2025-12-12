# BMI 計算
身高 = float(input("請輸入你的身高 (m): "))
體重 = float(input("請輸入你的體重 (kg): "))
bmi = 體重/(身高 ** 2)
print (f"你的bmi值為：{round (bmi)}")
if bmi < 18.5:
    print (f"你的體重過輕")
elif bmi < 24:
    print (f"你的體重健康")
elif bmi < 27:
    print (f"你的體重過重")
elif bmi < 30:
    print("你的體重輕度肥胖")
elif bmi < 35:
    print("你的體重中度肥胖")
else:
    print("你的體重重度肥胖")