import pandas as pd
import urllib.request as req
import bs4
import time
import os
import datetime


def print_intro():
    stock_nums = [3008, 2330, 2891, 2317, 2454]
    stock_name = ['大立光', '台積電', '中信金', '鴻海  ', '聯發科']
    for i in range(len(stock_nums)):
        print(stock_name[i], end='\t')
        print(stock_nums[i])
    print('下載每個月的資料要花5秒（太頻繁會被證交所封鎖IP），建議可從2018開始分析，分析時間越久下載檔案會越久！')


def get_stock_prices(Stock_No: str, year: str, month: str):
    """ To get trading infos about target stock from TW證交所 
    through get method and parse to dataframe.

    Args:
        Stock_No (str): stock number
        year (str): christian era
        month (str): month

    Returns:
        _type_: pandas.DataFrame
    """
    # 證交所查詢股票網站
    url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date=' + \
        str(year)+str(month).rjust(2, '0')+'01&stockNo='+str(Stock_No)
    with req.urlopen(url) as response:
        data = response.read().decode('utf-8')
    soup = bs4.BeautifulSoup(data, 'html.parser')
    results = soup.find_all('td')  # td tag includes date and trading info.
    dates = []
    vol = []
    turnover = []
    op = []
    high = []
    low = []
    close = []
    count = 0

    # split different info
    for line in results[9:]:
        if count % 9 == 0:
            dates.append(line.string)
        elif count % 9 == 1:
            vol.append(line.string)
        elif count % 9 == 2:
            turnover.append(line.string)
        elif count % 9 == 3:
            op.append(line.string)
        elif count % 9 == 4:
            high.append(line.string)
        elif count % 9 == 5:
            low.append(line.string)
        elif count % 9 == 6:
            close.append(line.string)
        count += 1

    df = pd.DataFrame({
        'Date': dates,
        'Volume': vol,
        'Turnover': turnover,
        'Open': op,
        'High': high,
        'Low': low,
        'Close': close
    })
    return df


def download_stock(Stock_No: str, from_: str):
    """ To download 

    Args:
        Stock_No (str): stock number
        from_ (str): christian era
    """

    t1 = time.time()
    df_total = pd.DataFrame({})
    print('start downloading...., 抓一個月的資料要花五秒, 你抓越久以前的資料要等越久....')
    time_now = datetime.datetime.now()
    year_now = time_now.year
    month_now = time_now.month
    dir = str(Stock_No) + '_' + str(from_)

    # save as csv file from get_stock_prices function
    if not os.path.exists(os.getcwd() + '/' + dir + '/' + str(Stock_No) + '_from_' + str(from_) + '.csv'):
        for year in range(from_, year_now):
            for month in range(1, 13):
                df = get_stock_prices(Stock_No, year, month)
                df_total = df_total.append(df)
                time.sleep(5)
        for month in range(1, month_now+1):
            df = get_stock_prices(Stock_No, year_now, month)
            df_total = df_total.append(df)
        if not os.path.exists(dir):
            os.mkdir(dir)
            df_total.to_csv(os.getcwd() + '/' + dir + '/' +
                            str(Stock_No) + '_from_' + str(from_) + '.csv')
        elif os.path.exists(dir):
            df_total.to_csv(os.getcwd() + '/' + dir + '/' +
                            str(Stock_No) + '_from_' + str(from_) + '.csv')
        else:
            pass
    t2 = time.time()
    print('downloaded')
    print('Time cost :', str(round(t2-t1, 4)), 'seconds')


if __name__ == '__main__':
    print_intro()
    Stock_No = int(input('請輸入想下載的股票代碼：'))
    from_ = int(input('想從西元第幾年後開始下載？'))
    download_stock(Stock_No, from_)
