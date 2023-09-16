
folderPath = r'C:\Users\User\Desktop\김지호입니\linear_program' # 폴더 경로
attributeTable = 'ncsorft_data.csv' # 파일 이름
os.chdir(folderPath)
df = pd.read_csv(attributeTable,encoding='cp949',thousands = ',')
df = df[['hours', 'temperature']]
df['temperature'].astype(float)
df.sort_values(by='hours',ascending=False)
plt.figure(figsize=(15, 8))
plt.rcParams.update({'font.size': 22})
ax = df.set_index('hours')['temperature'].plot(kind='line', marker='d')
ax.set_ylabel("Ear temperature (°C)")
ax.set_xlabel("Hours since Moderna second dose")
plt.show()