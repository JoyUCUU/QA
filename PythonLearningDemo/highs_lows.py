import  csv
from  matplotlib import pyplot as plt
from datetime import  datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date  = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[2])
        except ValueError:
            print(current_date,'Missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates,highs, c='red')
plt.plot(dates,lows, c='blue')
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.5)
#设置图形的格式
plt.title('Daily high and low temperatures-2014\nDeath valley,CA', fontsize=20)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)',fontsize=16)
plt.tick_params(axis='both', which='both',labelsize=16)

plt.show()
