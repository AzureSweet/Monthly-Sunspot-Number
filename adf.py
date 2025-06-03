import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

# Đọc dữ liệu từ file CSV (đã xử lý giá trị thiếu)
# Thay đổi đường dẫn nếu file không nằm trong cùng thư mục
data = pd.read_csv('Sunspots_cleaning.csv')

# Chuyển cột Date thành định dạng datetime và đặt làm index
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)
sunspots = data['Monthly Mean Total Sunspot Number']

# Hàm kiểm tra tính dừng bằng ADF test
def adf_test(series, title=''):
    result = adfuller(series, autolag='AIC')
    print(f'\nADF Test on {title}')
    print(f'ADF Statistic: {result[0]}')
    print(f'p-value: {result[1]}')
    print(f'Critical Values: {result[4]}')
    if result[1] < 0.05:
        print('Kết luận: Chuỗi dừng (Stationary) - Bác bỏ giả thuyết không.')
    else:
        print('Kết luận: Chuỗi không dừng (Non-stationary) - Không bác bỏ giả thuyết không.')
    print('')

# Kiểm tra tính dừng của chuỗi gốc
print("Kiểm tra tính dừng của chuỗi gốc:")
adf_test(sunspots, title="Original Sunspot Series")

# Vẽ biểu đồ chuỗi thời gian gốc
plt.figure(figsize=(12, 6))
plt.plot(sunspots, label='Original Sunspot Series', color='blue')
plt.title('Monthly Sunspot Number (1749-2021)')
plt.xlabel('Date')
plt.ylabel('Sunspot Number')
plt.legend()
plt.grid(True)
plt.show()

