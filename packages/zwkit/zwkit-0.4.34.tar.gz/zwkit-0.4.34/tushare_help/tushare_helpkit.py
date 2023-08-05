import tushare as ts
import pandas as pd
import kit.date_kit as date_kit
def get_daily_stock(pro,ts_code,start_date,end_date,limit,offset,num:int = 0):
    start_date = date_kit.to_yyyymmdd(start_date)
    end_date = date_kit.to_yyyymmdd(end_date)
    temp = pro.daily(ts_code=ts_code, limit=limit, offset=offset * limit, start_date=start_date, end_date=end_date)
    if temp.empty:
        if num > 5:
            print("已经重试了5次，还是没有数据",ts_code)
            return pd.DataFrame()
        return get_daily_stock(pro,ts_code, start_date,end_date ,limit, offset, num + 1)
    else:
        return temp

def get_daily(pro,symbol,start,end,limit,offset):
    temp = get_daily_stock(pro,symbol,start,end,limit,offset,0)
    return temp



def get_daily_adj_factor(pro,ts_code,start_date,end_date,limit,offset,num:int = 0):
    start_date = date_kit.to_yyyymmdd(start_date)
    end_date = date_kit.to_yyyymmdd(end_date)

    temp = pro.adj_factor(ts_code=ts_code, limit=limit, offset=offset * limit, start_date=start_date, end_date=end_date)
    if temp.empty:
        if num > 5:
            print("已经重试了5次，还是没有数据",ts_code)
            return pd.DataFrame()
        return get_daily_adj_factor(pro,ts_code, start_date,end_date ,limit, offset, num + 1)
    else:
        return temp

def daily_adj_factor(symbol,start,end,limit,offset):
    temp = get_daily_adj_factor(symbol,start,end,limit,offset,0)
    return temp