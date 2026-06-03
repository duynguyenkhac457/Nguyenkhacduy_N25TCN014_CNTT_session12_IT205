cart_items = [
    {
        "id": "P001",
        "name": "Dien thoai iPhone 15",
        "number": 1,
        "price": 25000000
    },
    {
        "id": "P002",
        "name": "Op lung Silicon",
        "number": 2,
        "price": 150000
    }
]

while True:
    print("\n=== SHOPEE CART MANAGEMENT CLI ===")
    print("1. Xem giỏ hàng và tổng tiền")
    print("2. Thêm sản phẩm / Tăng số lượng")
    print("3. Cập nhật số lượng sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát")

    choice = input("Chọn chức năng: ").strip()

    match choice:

        # ===== CHỨC NĂNG 1 =====
        case "1":
            if not cart_items:
                print("Giỏ hàng trống.")
            else:
                total_quantity = 0
                total_price = 0

                print("-" * 70)
                for item in cart_items:
                    item_total = item["number"] * item["price"]
                    total_quantity += item["number"]
                    total_price += item_total

                    print(
                        f"{item['id']:<5} | {item['name']:<25} | "
                        f"SL: {item['number']:<3} | "
                        f"Giá: {item['price']:<10} | "
                        f"Tạm tính: {item_total}"
                    )

                print("-" * 70)
                print(f"Tổng số lượng: {total_quantity}")
                print(f"Tổng tiền: {total_price}")

        # ===== CHỨC NĂNG 2 =====
        case "2":
            product_id = input("Nhập mã sản phẩm: ").strip().upper()
            product_name = input("Nhập tên sản phẩm: ").strip()

            try:
                number = int(input("Nhập số lượng: "))
                price = int(input("Nhập đơn giá: "))
            except:
                print("Số lượng và đơn giá phải là số!")
                continue

            if number <= 0 or price < 0:
                print("Số lượng hoặc đơn giá không hợp lệ!")
            else:
                found = False
                for item in cart_items:
                    if item["id"] == product_id:
                        item["number"] += number
                        found = True
                        print("Đã cộng dồn số lượng.")
                        break

                if not found:
                    cart_items.append({
                        "id": product_id,
                        "name": product_name,
                        "number": number,
                        "price": price
                    })
                    print("Đã thêm sản phẩm mới.")

        # ===== CHỨC NĂNG 3 =====
        case "3":
            product_id = input("Nhập mã sản phẩm: ").strip().upper()

            try:
                new_number = int(input("Nhập số lượng mới: "))
            except:
                print("Số lượng phải là số!")
                continue

            if new_number <= 0:
                print("Số lượng không hợp lệ!")
            else:
                found = False
                for item in cart_items:
                    if item["id"] == product_id:
                        item["number"] = new_number
                        found = True
                        print("Cập nhật thành công.")
                        break

                if not found:
                    print("Mã sản phẩm không tồn tại trong giỏ hàng.")

        # ===== CHỨC NĂNG 4 =====
        case "4":
            product_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()
            found = False

            for item in cart_items:
                if item["id"] == product_id:
                    cart_items.remove(item)
                    found = True
                    print("Đã xóa sản phẩm.")
                    break

            if not found:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")

        # ===== CHỨC NĂNG 5 =====
        case "5":
            print("Thoát chương trình.")
            break

        # ===== MENU SAI =====
        case _:
            print("Lựa chọn không hợp lệ! Chỉ nhập từ 1 đến 5.")