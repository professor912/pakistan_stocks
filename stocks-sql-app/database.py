import pymysql
import pandas as pd




class DataBase:
    def __init__(self):
        try:
            self.con = pymysql.connect(
                host='mysql-356ecd9d-hammadmessi48-b201.d.aivencloud.com',
                user='avnadmin',
                password='AVNS_F8_KmQ_c_2TpP-mfHjt',
                database='defaultdb',
                port=24753,
                ssl={'ca': r'stocks-sql-app/ca.pem'}
            )

            
            self.cursor = self.con.cursor()
            print('Connection Established')
        except:
            print('Connection Failed')
            
    def fetch_all_stocks(self):
        self.cursor.execute('select distinct(symbol) from stock')
        data = self.cursor.fetchall()
        all_stocks = []
        for i in data:
            all_stocks.append(i[0])
            
        return all_stocks
            
    
    def fetch_openprice_yearly(self,symbol):
        self.cursor.execute(
            
            f"""
            select date,open from stock
            where symbol = '{symbol}'
            """
        )
        data = self.cursor.fetchall()
        date = []
        open = []
        for i in data:
            date.append(i[0])
            open.append(i[1])
        return date,open



    def fetch_volume_yearly(self,symbol):
        self.cursor.execute(
            
            f"""
            select date,volume from stock
            where symbol = '{symbol}'
            """
        )
        data = self.cursor.fetchall()
        date = []
        volume = []
        for i in data:
            date.append(i[0])
            volume.append(i[1])
        return date,volume
    
    
    def fetch_rolling_average(self,symbol):
        self.cursor.execute(
            
            f"""
            select date,avg(close) over(order by date rows between 30 preceding and current row ) 
            as 'rolling_avg' from stock where symbol = '{symbol}'

            """
        )
        data = self.cursor.fetchall()
        date = []
        rolling_average = []
        for i in data:
            date.append(i[0])
            rolling_average.append(i[1])
        return date,rolling_average
    
    
    
    def fetch_daily_return(self,symbol):
        self.cursor.execute(
            
            f"""
            select date, ((close-lag(close) over(PARTITION BY symbol ORDER BY date))/lag(close) over(PARTITION BY symbol ORDER BY date))*100 AS 'pct_change'
            from stock where symbol = '{symbol}'

            """
        )
        data = self.cursor.fetchall()
        date = []
        daily_return = []
        for i in data:
            date.append(i[0])
            daily_return.append(i[1])
        return date,daily_return
    
    
    def fetch_risk_vs_return(self,symbol):
        self.cursor.execute(
            
            f"""
            select std(pct_change),avg(pct_change) from (
            select  ((close-lag(close) over(PARTITION BY symbol ORDER BY date))/lag(close) over(PARTITION BY symbol ORDER BY date))*100 AS 'pct_change'
            from stock where symbol = '{symbol}') t
            """
        )
        data = self.cursor.fetchall()
        risk = []
        return_value = []
        for i in data:
            risk.append(i[0])
            return_value.append(i[1])
        return risk,return_value
    
    
    def fetch_corr_data(self,symbol1,symbol2):
        self.cursor.execute(
            
            f"""
            select date,
            sum(case when symbol = '{symbol1}' then open else 0 end ) as '{symbol1}',
            SUM(CASE WHEN symbol = '{symbol2}' THEN open ELSE 0 END) AS '{symbol2}'
            from stock
            group by date
            """
        )
        data = self.cursor.fetchall()
        df = pd.DataFrame(data,columns=['date',symbol1,symbol2])
        df.set_index('date',inplace=True)
        return df
    
    def fetch_corr_data_return(self,symbol1,symbol2):
        self.cursor.execute(
            
            f"""
            with pct as (select  date,symbol,((close-lag(close) over(PARTITION BY symbol ORDER BY date))/lag(close) over(PARTITION BY symbol ORDER BY date))*100 AS 'pct_change'
            from stock ) 
            select date,
            sum(case when symbol = '{symbol1}' then pct_change
                        else 0 end) as '{symbol1}' ,
            sum(case when symbol = '{symbol2}' then pct_change  else 0 end) as '{symbol2}'
            from pct 
            group by date
            """
        )
        data = self.cursor.fetchall() 
        df = pd.DataFrame(data,columns=['date',symbol1,symbol2])
        df.set_index('date',inplace=True)
        return df
    
    
    def fetch_corr_data_return_4(self,symbol1,symbol2,symbol3,symbol4):
        self.cursor.execute(
            
            f"""
            with pct as (select  date,symbol,((close-lag(close) over(PARTITION BY symbol ORDER BY date))/lag(close) over(partition by symbol order by date))*100 AS 'pct_change'
            from stock ) 
            select date,
            sum(case when symbol = '{symbol1}' then pct_change
                        else 0 end) as '{symbol1}' ,
            sum(case when symbol = '{symbol2}' then pct_change  else 0 end) as '{symbol2}',
            sum(case when symbol = '{symbol3}' then pct_change  else 0 end) as '{symbol3}',
            sum(case when symbol = '{symbol4}' then pct_change  else 0 end) as '{symbol4}'
            from pct 
            group by date
            """
        )
        data = self.cursor.fetchall() 
        df = pd.DataFrame(data,columns=['date',symbol1,symbol2,symbol3,symbol4])
        df.set_index('date',inplace=True)
        return df
        
    def fetch_corr_data_4(self,symbol1,symbol2,symbol3,symbol4):
        self.cursor.execute(
            
            f"""
            select date,
            sum(case when symbol = '{symbol1}' then open else 0 end ) as '{symbol1}',
            SUM(CASE WHEN symbol = '{symbol2}' THEN open ELSE 0 END) AS '{symbol2}',
            SUM(CASE WHEN symbol = '{symbol3}' THEN open ELSE 0 END) AS '{symbol3}',
            SUM(CASE WHEN symbol = '{symbol4}' THEN open ELSE 0 END) AS '{symbol4}'
            from stock
            group by date
            """
        )
        data = self.cursor.fetchall()
        df = pd.DataFrame(data,columns=['date',symbol1,symbol2,symbol3,symbol4])
        df.set_index('date',inplace=True)
        return df
d = DataBase()

# print(d.fetch_openprice_yearly('OGDC'))symbol1,symbol2,symbol3,symbol4
