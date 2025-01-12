# Nhập vào chuỗi ký tự từ người dùng
chuoi = input("Nhập vào một chuỗi: ")

# Khởi tạo biến đếm số từ
so_tu = 0

# Duyệt qua từng ký tự trong chuỗi
for i in range(len(chuoi)):
    # Nếu gặp dấu cách và không phải là khoảng trắng đầu tiên thì đếm là một từ
    if chuoi[i] != ' ' and (i == 0 or chuoi[i-1] == ' '):
        so_tu += 1

# In ra kết quả
print(f"Số từ trong chuỗi là: {so_tu}")
