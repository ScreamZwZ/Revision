# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Nhập vào danh sách các số nguyên từ người dùng
danh_sach = list(map(int, input("Nhập vào danh sách số nguyên (các số cách nhau bởi dấu cách): ").split()))

# Khởi tạo biến tổng các số nguyên tố
tong_so_nguyen_to = 0

# Duyệt qua từng số trong danh sách và tính tổng các số nguyên tố
for so in danh_sach:
    if is_prime(so):
        tong_so_nguyen_to += so

# In kết quả
print(f"Tổng các số nguyên tố là: {tong_so_nguyen_to}")
