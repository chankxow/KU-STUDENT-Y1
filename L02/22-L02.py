days = int(input('How many day : ')) #สร้างตัวแปร
distcount_days = 0.95 # ลดราคา5%
total = 0 #ตัวแปรเก็บราคารวม
for i in range(days):       
    price = float(input(f'Input price in day {i+1} : '))
    total += price * distcount_days #ตัวแปร ราคาที่ลดราคาแล็ว มารวมกับจำรวนราคาที่ถูกลดไปแล้วเมื่อวันก่อน
    distcount_days -=0.01 #เพิ่ม%การลดราคาต่อวัน เป็นรอบตามloop days
print(f'Summary price = {total:.2f}')