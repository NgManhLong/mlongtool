# máy tính 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Không thể chia cho 0!"
    return x / y

def main():
    print("Máy tính đơn giản")
    print("Chọn phép tính:")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")

    choice = input("Nhập lựa chọn (1/2/3/4): ")

    if choice not in ('1', '2', '3', '4'):
        print("Lựa chọn không hợp lệ!")
        return

    try:
        a = float(input("Nhập số thứ nhất: "))
        b = float(input("Nhập số thứ hai: "))
    except ValueError:
        print("Vui lòng nhập số hợp lệ!")
        return

    if choice == '1':
        print(f"Kết quả: {add(a, b)}")
    elif choice == '2':
        print(f"Kết quả: {subtract(a, b)}")
    elif choice == '3':
        print(f"Kết quả: {multiply(a, b)}")
    elif choice == '4':
        print(f"Kết quả: {divide(a, b)}")

if __name__ == "__main__":
    main()