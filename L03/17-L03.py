def simple_interest(p, r, t) :
    i = p*(r/100)*t
    return i+p

"""เพื่อคืนค่าเงินรวมของการคิดดอกเบี้ยเชิงเดียว จากสูตร
ดอกเบี้ย = เงินต้น x อัตราดอกเบี้ย x ระยะเวลากู้ยืม
"""


def compound_interest(p, r, t)  :
    total = p *(1+(r/100))**t 
    return total
"""เพื่อคืนค่าเงินรวมของการคิดดอกเบี้ยทบต้น จากสูตร
เงินรวม = เงินต้น x (1 +อัตราดอกเบี้ย) ระยะเวลากู้ยืม"""

p = float(input('Enter principle: '))
r = float(input('Enter interest rate: '))
t = float(input('Enter time: '))

#print('Return money for simple interest calculation is %.2f Baht.' % (simple_interest(p, r, t)))
#print('Return money for compound interest calculation is %.2f Baht.' % (compound_interest(p, r, t)))
print(f'Return money for simple interest calculation is {simple_interest(p, r, t):.2f} Baht.')
print(f'Return money for compound interest calculation is {compound_interest(p, r, t):.2f} Baht.')
