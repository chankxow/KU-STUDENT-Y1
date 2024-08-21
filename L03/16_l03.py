'''นวนเต็ม num ที่กำหนดให้มีค่าตั้งแต่ 0 และน้อยกว่า 10,000 สร้างฟังก์ชันเพื่อส่งกลับตัวเลข ของแต่ละหลักดังนี้

2.1. digit(num) เพื่อคืนค่าตัวเลขในหลักหน่วยของจำนวนเต็ม num
2.2. tens(num) เพื่อคืนค่าตัวเลขในหลักสิบของจำนวนเต็ม num
2.3. hundreds(num) เพื่อคืนค่าตัวเลขในหลักร้อยของจำนวนเต็ม num
2.4. thousands(num) เพื่อคืนค่าตัวเลขในหลักพันของจำนวนเต็ม num

นอกจากนี้ให้สร้างฟังก์ชัน sum_digits(num) เพิ่มเติมเพื่อคืนค่าผลบวกของตัวเลขในแต่ละหลักของ num'''

def thousands(num):
    return num // 1000

def hundreds(num):
    return (num // 100) % 10

def tens(num):
    return ((num % 1000)//10)%10

def digit(num):
    return ((num % 1000)%100)%10

def sum_digits(num):
    return thousands(num) + hundreds(num) + tens(num) +digit(num)


n   = int(input('Enter a number (0 to 9999): '))
print('Digit place is %d.' % (digit(n)))
print('Tens place is %d.' % (tens(n)))
print('Hundreds place is %d.' % (hundreds(n)))
print('Thousands place is %d.' % (thousands(n)))
print('Sum of all digits is %d.' % sum_digits(n))