import csv
from datetime import datetime

path = 'Google Stock Market Data - google_stock_data.csv'
file = open(path, newline='')

reader = csv.reader(file)

# first line is header
header = next(reader)

# read the remaining data
data= []
for row in reader:
    # row = [Date, OPen, High, Low, Close, Adj. close]
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1]) 
    high = float(row[2]) 
    low = float(row[3]) 
    close = float(row[4]) 
    volume = int(row[5])
    adj_close = float(row[6]) 

    data.append([date, open_price, high, low, close, volume, adj_close])

"""In finance a stock return is just a percentage change in price. A daily return is a percentage change from 
one day to the next. There are also Daily, weekly, MOnthly, quartely and yearly returns. For now we only consider daily returns """

returns_path = 'google_returns.csv'
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(['Date','Return'])

# To compute the daily change in price as a percent, we need the adjusted price for two consecutive days. 
# NB: The first day does not have a previous day, that is why we are using len(data)-1
for i in range(len(data)-1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]

    # since the data is sorted in a chronoligical manner
    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]

    # Compute the daily return
    daily_return = (todays_price - yesterdays_price)/yesterdays_price
   
    # Format date in a use friendly way
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, daily_return])


    