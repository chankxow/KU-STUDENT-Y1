m = int(input("M: "))
n = int(input("N: "))

m_woodplate,n_woodplate = m*2,n*1

m_logs , n_logs = m*6,n*4

result_plate = m_woodplate + n_woodplate
result_logs = m_logs + n_logs

print(result_plate,result_logs)