import pandas as pd

# Đọc dữ liệu từ file CSV
data = pd.read_csv('Sunspots.csv')

# Kiểm tra giá trị thiếu trong từng cột
print("Số lượng giá trị thiếu trong mỗi cột:")
missing_values = data.isnull().sum()
print(missing_values)

# Kiểm tra tổng số hàng có ít nhất một giá trị thiếu
total_missing_rows = data.isnull().any(axis=1).sum()
print(f"\nTổng số hàng có ít nhất một giá trị thiếu: {total_missing_rows}")

# Xử lý giá trị thiếu
# - Nếu cột 'Date' thiếu, loại bỏ hàng đó vì ngày tháng là cần thiết
# - Nếu cột 'Monthly Mean Total Sunspot Number' thiếu, thay bằng 0
if missing_values['Date'] > 0:
    data = data.dropna(subset=['Date'])
    print(f"Đã loại bỏ {missing_values['Date']} hàng có giá trị thiếu trong cột 'Date'.")

if missing_values['Monthly Mean Total Sunspot Number'] > 0:
    data['Monthly Mean Total Sunspot Number'] = data['Monthly Mean Total Sunspot Number'].fillna(0)
    print(f"Đã thay thế {missing_values['Monthly Mean Total Sunspot Number']} giá trị thiếu trong cột 'Monthly Mean Total Sunspot Number' bằng 0.")

# Kiểm tra lại giá trị thiếu sau khi xử lý
print("\nSố lượng giá trị thiếu sau khi xử lý:")
print(data.isnull().sum())

# Lưu dữ liệu đã xử lý vào file mới
data.to_csv('Sunspots_cleaning.csv', index=False)
print("\nĐã lưu dữ liệu sau khi xử lý vào 'Sunspots_cleaningcleaning'.")