saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát")

    choice = input("Chọn chức năng: ").strip()

    match choice:

        # ===== 1. XEM DANH SÁCH =====
        case "1":
            if not saving_accounts:
                print("Danh sách sổ tiết kiệm hiện đang trống")
            else:
                index = 1
                for acc in saving_accounts:
                    print(
                        f"{index}. Mã sổ: {acc['account_id']} | "
                        f"Khách hàng: {acc['customer_name']} | "
                        f"Số tiền: {acc['balance']} | "
                        f"Kỳ hạn: {acc['term_months']} tháng | "
                        f"Lãi suất: {acc['interest_rate']}%/năm | "
                        f"Trạng thái: {acc['status']}"
                    )
                    index += 1

        # ===== 2. MỞ SỔ MỚI =====
        case "2":
            account_id = input("Nhập mã sổ: ").strip().upper()
            customer_name = input("Nhập tên khách hàng: ").strip()

            if customer_name == "":
                print("Tên khách hàng không được để trống")
                continue

            try:
                balance = int(input("Nhập số tiền gửi: "))
                term_months = int(input("Nhập kỳ hạn (tháng): "))
                interest_rate = float(input("Nhập lãi suất năm: "))
            except:
                print("Dữ liệu không hợp lệ")
                continue

            if balance <= 0 or term_months <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue

            if interest_rate <= 0:
                print("Lãi suất không hợp lệ!")
                continue

            found = False
            for acc in saving_accounts:
                if acc["account_id"] == account_id:
                    found = True
                    break

            if found:
                print("Mã sổ tiết kiệm đã tồn tại!")
            else:
                saving_accounts.append({
                    "account_id": account_id,
                    "customer_name": customer_name,
                    "balance": balance,
                    "term_months": term_months,
                    "interest_rate": interest_rate,
                    "status": "active"
                })
                print("Mở sổ tiết kiệm thành công!")

        # ===== 3. CẬP NHẬT =====
        case "3":
            account_id = input("Nhập mã sổ cần cập nhật: ").strip().upper()
            found = False

            for acc in saving_accounts:
                if acc["account_id"] == account_id:
                    found = True

                    if acc["status"] == "closed":
                        print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
                        break

                    name = input("Nhập tên mới: ").strip()
                    if name == "":
                        print("Tên khách hàng không được để trống")
                        break

                    try:
                        balance = int(input("Nhập số tiền mới: "))
                        term = int(input("Nhập kỳ hạn mới: "))
                        rate = float(input("Nhập lãi suất mới: "))
                    except:
                        print("Dữ liệu không hợp lệ")
                        break

                    if balance <= 0 or term <= 0 or rate <= 0:
                        print("Thông tin cập nhật không hợp lệ")
                        break

                    acc["customer_name"] = name
                    acc["balance"] = balance
                    acc["term_months"] = term
                    acc["interest_rate"] = rate
                    print("Cập nhật sổ tiết kiệm thành công!")
                    break

            if not found:
                print("Không tìm thấy mã sổ tiết kiệm!")

        # ===== 4. TẤT TOÁN =====
        case "4":
            account_id = input("Nhập mã sổ cần tất toán: ").strip().upper()
            found = False

            for acc in saving_accounts:
                if acc["account_id"] == account_id:
                    found = True
                    acc["status"] = "closed"
                    print("Tất toán sổ tiết kiệm thành công!")
                    break

            if not found:
                print("Không tìm thấy mã sổ tiết kiệm")

        # ===== 5. TÍNH LÃI ĐẾN HẠN =====
        case "5":
            account_id = input("Nhập mã sổ cần tính lãi: ").strip().upper()
            found = False

            for acc in saving_accounts:
                if acc["account_id"] == account_id:
                    found = True

                    if acc["status"] == "closed":
                        print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                        break

                    interest = acc["balance"] * acc["interest_rate"] / 100 * acc["term_months"] / 12
                    total = acc["balance"] + interest
                    print(f"Tiền lãi dự kiến: {interest}")
                    print(f"Tổng tiền nhận: {total}")
                    break

            if not found:
                print("Không tìm thấy mã sổ tiết kiệm")

        # ===== 6. RÚT TRƯỚC HẠN =====
        case "6":
            account_id = input("Nhập mã sổ: ").strip().upper()

            try:
                actual_months = int(input("Nhập số tháng thực gửi: "))
            except:
                print("Số tháng thực gửi không hợp lệ!")
                continue

            if actual_months <= 0:
                print("Số tháng thực gửi không hợp lệ!")
                continue

            found = False
            for acc in saving_accounts:
                if acc["account_id"] == account_id:
                    found = True

                    if acc["status"] == "closed":
                        print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                        break

                    if actual_months < acc["term_months"]:
                        rate = 0.5
                    else:
                        rate = acc["interest_rate"]

                    interest = acc["balance"] * rate / 100 * actual_months / 12
                    total = acc["balance"] + interest

                    print(f"Lãi suất áp dụng: {rate}%")
                    print(f"Tiền lãi thực nhận: {interest}")
                    print(f"Tổng tiền thực nhận: {total}")
                    break

            if not found:
                print("Không tìm thấy mã sổ tiết kiệm")

        # ===== 7. THOÁT =====
        case "7":
            print("Thoát chương trình.")
            break

        # ===== MENU SAI =====
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại")