import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] ='Malgun Gothic'

matplotlib.rcParams['axes.unicode_minus'] =False
# 직접 파일 이름 지정
file1 = "2023-01-01.xlsx"
file2 = "2023-02-01.xlsx"
file3 = "2023-03-01.xlsx"
file4 = "2023-04-01.xlsx"
file5 = "2023-05-01.xlsx"
file6 = "2023-06-01.xlsx"
files = [file1, file2, file3, file4, file5, file6]

all_data = []

for file in files:
    month_data = pd.read_excel(file)
    month_data['month'] = file.split('-')[1]
    all_data.append(month_data)

combined_data = pd.concat(all_data, ignore_index=True)

# ... (그래프 및 차트 생성 부분은 이전 코드와 동일)


# 월별 전체 사이클 수 그래프
monthly_total_cycles = combined_data.groupby('month')['totalCycle'].sum()
plt.figure(figsize=(10, 6))
monthly_total_cycles.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('월별 전체 사이클 수 (2023년 1월~6월)')
plt.xlabel('월')
plt.ylabel('사이클 수')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("figure1.png")
plt.show()

# 월별 평균 사이클 수 그래프
average_cycles_per_store = combined_data.groupby('month')['totalCycle'].mean()
plt.figure(figsize=(10, 6))
average_cycles_per_store.plot(kind='bar', color='lightcoral', edgecolor='black')
plt.title('월별 평균 사이클 수 (2023년 1월~6월)')
plt.xlabel('월')
plt.ylabel('사이클 수')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("figure2.png")
plt.show()

# 상위 5개 매장의 전체 사이클 수 그래프
top_5_stores = combined_data.groupby('storeId')['totalCycle'].sum().sort_values(ascending=False).head(5)
plt.figure(figsize=(12, 7))
top_5_stores.plot(kind='barh', color='mediumseagreen', edgecolor='black')
plt.title('상위 5개 매장의 전체 사이클 수 (2023년 1월~6월)')
plt.xlabel('사이클 수')
plt.ylabel('매장 ID')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("figure3.png")
plt.show()

# 하위 5개 매장의 전체 사이클 수 그래프
top_5_stores = combined_data.groupby('storeId')['totalCycle'].sum().sort_values(ascending=False).tail(5)
plt.figure(figsize=(12, 7))
top_5_stores.plot(kind='barh', color='mediumseagreen', edgecolor='black')
plt.title('상위 5개 매장의 전체 사이클 수 (2023년 1월~6월)')
plt.xlabel('사이클 수')
plt.ylabel('매장 ID')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("figure6.png")
plt.show()

# 워셔와 드라이어의 분포 히스토그램
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
combined_data['washerCnt'].hist(color='dodgerblue', edgecolor='black', bins=10)
plt.title('워셔 분포')
plt.xlabel('워셔 수')
plt.ylabel('매장 수')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.subplot(1, 2, 2)
combined_data['dryerCnt'].hist(color='salmon', edgecolor='black', bins=10)
plt.title('드라이어 분포')
plt.xlabel('드라이어 수')
plt.ylabel('매장 수')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("figure4.png")
plt.show()

# 월별 총 결제 금액 그래프
monthly_payment_totals = combined_data.groupby('month')['paymentTotal'].sum()
plt.figure(figsize=(10, 6))
monthly_payment_totals.plot(kind='bar', color='goldenrod', edgecolor='black')
plt.title('월별 총 결제 금액 (2023년 1월~6월)')
plt.xlabel('월')
plt.ylabel('결제 금액')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("figure5.png")
plt.show()
