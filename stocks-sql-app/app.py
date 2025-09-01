from database import DataBase
import streamlit as st
import pandas as pd 
import plotly.express as px 
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import seaborn as sns
st.set_page_config(layout='wide')
db = DataBase()

# st.title('Pakistan Stock Exchange Analysis')

st.sidebar.title('Analysis')

option = st.sidebar.selectbox('Select Type Of Analysis',['Individual','Comparitive'])

if option == 'Individual':
    
    symbol = st.sidebar.selectbox('Select Company',db.fetch_all_stocks())
    st.title(f'{symbol} Analysis')
    
    st.header('Return VS Risk Analysis')
    risk,return_value = db.fetch_risk_vs_return(symbol)
    fig = px.scatter(x=risk,y=return_value,labels={'x':'Risk Value','y':'Return Value'})
    st.plotly_chart(fig) 
    
    
    col1,col2 = st.columns(2)
    
    with col1:
        st.header('Day by Day stock open price Analysis')
        date,open = db.fetch_openprice_yearly(symbol)
        fig = px.line(x=date,y=open,labels={'x':'Date','y':'Open Price'})
        st.plotly_chart(fig)
        
    with col2:
        st.header('Day by Day stock traded Volume Analysis')
        date,volume = db.fetch_volume_yearly(symbol)
        fig = px.line(x=date,y=volume,labels={'x':'Date','y':'Volume'})
        st.plotly_chart(fig)

    col3,col4 = st.columns(2)
    
    with col3:
        st.header('Monthly stock rolling average Volume Analysis')
        date,rolling_average = db.fetch_rolling_average(symbol)
        fig = px.line(x=date,y=rolling_average,labels={'x':'Date','y':'Rolling Average'})
        st.plotly_chart(fig) 
    
    with col4:
        st.header('Weekly stock Daily Return Analysis')
        date,daily_return = db.fetch_daily_return(symbol)
        fig = px.line(x=date,y=daily_return,labels={'x':'Date','y':'Daily Return'})
        st.plotly_chart(fig) 
        
        
        
        
        
        
        
        
        
elif option == 'Comparitive':
    st.title('Comparitive Analysis')
    
    number_comparision = st.selectbox('Choose number of stocks for Comparision',[2,4])
    
    if number_comparision == 2:
        col1,col2 = st.columns(2)
        with col1:
            stock1 = st.selectbox('Select first Company',db.fetch_all_stocks())
        
        with col2:
            stock2 = st.selectbox('Select second Company',db.fetch_all_stocks()) 
        
        
        if stock1 and stock2:
        
            st.markdown("<h2 style='text-align: center;'>Return VS Risk Value</h2>", unsafe_allow_html=True)
            risk,return_value = db.fetch_risk_vs_return(stock1)
            fig = px.scatter(x=risk,y=return_value,labels={'x':'Risk Value','y':'Return Value'},hover_name = [f'{stock1}'])
            
            risk1,return_value1 = db.fetch_risk_vs_return(stock2)
            fig1 = px.scatter(x=risk1,y=return_value1,labels={'x':'Risk Value','y':'Return Value'},hover_name = [f'{stock2}'])
            
            final_fig = go.Figure(data = fig.data + fig1.data )
            final_fig.update_layout(
                xaxis_title = 'Risk Value',
                yaxis_title = 'Return Value',
            )
            st.plotly_chart(final_fig,use_container_width=True)

            
            plt.style.use('seaborn-v0_8')

            st.markdown("<h2 style='text-align: center;'>Day by Day stock open price Analysis</h2>", unsafe_allow_html=True)
            col3,col4 = st.columns(2)
            
            with col3:
                date,open = db.fetch_openprice_yearly(stock1)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),open)
                ax.set_title(f'{stock1}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Open Price')
                st.pyplot(fig)
                
                
                
            with col4:
                date,open = db.fetch_openprice_yearly(stock2)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),open)
                ax.set_title(f'{stock2}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Open Price')
                st.pyplot(fig)
            
            
            
            st.markdown("<h2 style='text-align: center;'>Day by Day stock Volume Analysis</h2>", unsafe_allow_html=True)

            col5,col6 = st.columns(2)
            
            with col5:
                date,volume = db.fetch_volume_yearly(stock1)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),volume)
                ax.set_title(f'{stock1}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Volume')
                st.pyplot(fig)
            
            
            with col6:
                
                date,volume = db.fetch_volume_yearly(stock2)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),volume)
                ax.set_title(f'{stock2}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Volume')
                st.pyplot(fig)
            
            plt.style.use('seaborn-v0_8')
            # plt.style.use('seaborn-v0_8-darkgrid')
            st.markdown("<h2 style='text-align: center;'>Monthly stock rolling average Volume Analysis</h2>", unsafe_allow_html=True)

            col7,col8 = st.columns(2)
            
            with col7:
                date,rolling_average = db.fetch_rolling_average(stock1)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),rolling_average)
                ax.set_title(f'{stock1}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Rolling Average')
                st.pyplot(fig)
                
            with col8:
                date,rolling_average = db.fetch_rolling_average(stock2)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),rolling_average)
                ax.set_title(f'{stock2}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Rolling Average')
                st.pyplot(fig)
                

            st.markdown("<h2 style='text-align: center;'>Weekly stock Daily Return Analysis</h2>", unsafe_allow_html=True)

            col9,col10 = st.columns(2)
            

            with col9:
                date,daily_return = db.fetch_daily_return(stock1)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),daily_return)
                ax.set_title(f'{stock1}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Daily Return')
                st.pyplot(fig)
                
                
            with col10:
                date,daily_return = db.fetch_daily_return(stock2)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),daily_return)
                ax.set_title(f'{stock2}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Daily Return')
                st.pyplot(fig)

            st.markdown("<h2 style='text-align: center;'>Correlation Map </h2>", unsafe_allow_html=True)

            col11,col12 = st.columns(2)
            
            with col11:
                df1 = db.fetch_corr_data(stock1,stock2)
                fig1,ax = plt.subplots()
                sns.heatmap(df1.corr(),ax=ax)
                ax.set_title('Heat map of of daily open Price')
                st.pyplot(fig1)
        
            with col12:
                df1 = db.fetch_corr_data_return(stock1,stock2)
                fig1,ax = plt.subplots()
                sns.heatmap(df1.corr(),ax=ax)
                ax.set_title('Heat map of of daily return')
                st.pyplot(fig1)
        
        
        
        
        
    plt.style.use('seaborn-v0_8')

    if number_comparision == 4:
        col1,col2,col3,col4 = st.columns(4)
        with col1:
            stock1 = st.selectbox('Select first Company',db.fetch_all_stocks())
        
        with col2:
            stock2 = st.selectbox('Select second Company',db.fetch_all_stocks()) 
        
        with col3:
            stock3 = st.selectbox('Select third Company',db.fetch_all_stocks())
        
        with col4:
            stock4 = st.selectbox('Select fourth Company',db.fetch_all_stocks()) 
            
            
        
        if stock1 and stock2 and stock3 and stock4:
            st.markdown("<h2 style='text-align: center;'>Return VS Risk Value</h2>", unsafe_allow_html=True)
            
            risk,return_value = db.fetch_risk_vs_return(stock1)
            fig = px.scatter(x=risk,y=return_value,labels={'x':'Risk Value','y':'Return Value'},hover_name = [f'{stock1}'])
            
            risk1,return_value1 = db.fetch_risk_vs_return(stock2)
            fig1 = px.scatter(x=risk1,y=return_value1,labels={'x':'Risk Value','y':'Return Value'},hover_name = [f'{stock2}'])
            
            risk2,return_value2 = db.fetch_risk_vs_return(stock3)
            fig2 = px.scatter(x=risk2,y=return_value2,labels={'x':'Risk Value','y':'Return Value'},hover_name = [f'{stock3}'])
            
            risk3,return_value3 = db.fetch_risk_vs_return(stock4)
            fig3 = px.scatter(x=risk3,y=return_value3,labels={'x':'Risk Value','y':'Return Value'},hover_name = [f'{stock4}'])
            
            final_fig = go.Figure(data = fig.data + fig1.data + fig2.data + fig3.data)
            final_fig.update_layout(
                xaxis_title = 'Risk Value',
                yaxis_title = 'Return Value',
            )
            st.plotly_chart(final_fig,use_container_width=True)
            
            
            
            
            st.markdown("<h2 style='text-align: center;'>Day by Day stock open price Analysis</h2>", unsafe_allow_html=True)
            col5,col6,col7,col8 = st.columns(4)
            
            with col5:
                date,open = db.fetch_openprice_yearly(stock1)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),open)
                ax.set_title(f'{stock1}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Open Price')
                st.pyplot(fig)
                
            with col6:
                date,open = db.fetch_openprice_yearly(stock2)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),open)
                ax.set_title(f'{stock2}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Open Price')
                st.pyplot(fig)
                
            with col7:
                date,open = db.fetch_openprice_yearly(stock3)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),open)
                ax.set_title(f'{stock3}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Open Price')
                st.pyplot(fig)
                
            with col8:
                date,open = db.fetch_openprice_yearly(stock4)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),open)
                ax.set_title(f'{stock4}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Open Price')
                st.pyplot(fig)
            
            
            
            plt.style.use('fivethirtyeight')

            st.markdown("<h2 style='text-align: center;'>Day by Day stock Volume Analysis</h2>", unsafe_allow_html=True)

            col9,col10,col11,col12 = st.columns(4)
            
            with col9:
                date,volume = db.fetch_volume_yearly(stock1)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),volume)
                ax.set_title(f'{stock1}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Volume')
                st.pyplot(fig)
            
            
            with col10:
                
                date,volume = db.fetch_volume_yearly(stock2)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),volume)
                ax.set_title(f'{stock2}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Volume')
                st.pyplot(fig)
               
            with col11:
                date,volume = db.fetch_volume_yearly(stock3)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),volume)
                ax.set_title(f'{stock3}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Volume')
                st.pyplot(fig)
            
            
            with col12:
                
                date,volume = db.fetch_volume_yearly(stock4)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),volume)
                ax.set_title(f'{stock4}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Volume')
                st.pyplot(fig)
                
                
                
            plt.style.use('seaborn-v0_8-pastel')
    
            st.markdown("<h2 style='text-align: center;'>Monthly stock rolling average  Analysis</h2>", unsafe_allow_html=True)

            col13,col14,col15,col16 = st.columns(4)
            
            with col13:
                date,rolling_average = db.fetch_rolling_average(stock1)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),rolling_average)
                ax.set_title(f'{stock1}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Rolling Average')
                st.pyplot(fig)
                
            with col14:
                date,rolling_average = db.fetch_rolling_average(stock2)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),rolling_average)
                ax.set_title(f'{stock2}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Rolling Average')
                st.pyplot(fig)
                
                
            with col15:
                date,rolling_average = db.fetch_rolling_average(stock3)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),rolling_average)
                ax.set_title(f'{stock3}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Rolling Average')
                st.pyplot(fig)
                
            with col16:
                date,rolling_average = db.fetch_rolling_average(stock4)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),rolling_average)
                ax.set_title(f'{stock4}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Rolling Average')
                st.pyplot(fig)
                
            
            
            
            plt.style.use('seaborn-v0_8-bright')

            st.markdown("<h2 style='text-align: center;'>Weekly stock Daily Return Analysis</h2>", unsafe_allow_html=True)

            col17,col18,col19,col20 = st.columns(4)
            

            with col17:
                date,daily_return = db.fetch_daily_return(stock1)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),daily_return)
                ax.set_title(f'{stock1}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Daily Return')
                st.pyplot(fig)
                
            with col18:
                date,daily_return = db.fetch_daily_return(stock2)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),daily_return)
                ax.set_title(f'{stock2}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Daily Return')
                st.pyplot(fig)
                
                
                
            with col19:
                date,daily_return = db.fetch_daily_return(stock3)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),daily_return)
                ax.set_title(f'{stock3}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Daily Return')
                st.pyplot(fig)
                
            with col20:
                date,daily_return = db.fetch_daily_return(stock4)
                fig,ax = plt.subplots()
                ax.plot(pd.to_datetime(date),daily_return)
                ax.set_title(f'{stock4}')
                ax.set_xlabel('Date')
                ax.set_ylabel('Daily Return')
                st.pyplot(fig)
                
            st.markdown("<h2 style='text-align: center;'>Correlation Map </h2>", unsafe_allow_html=True)

            col11,col12 = st.columns(2)
            
            with col11:
                df1 = db.fetch_corr_data_4(stock1,stock2,stock3,stock4)
                fig1,ax = plt.subplots()
                sns.heatmap(df1.corr(),ax=ax)
                ax.set_title('Heat map of of daily open Price')
                st.pyplot(fig1)
        
            with col12:
                df1 = db.fetch_corr_data_return_4(stock1,stock2,stock3,stock4)
                fig1,ax = plt.subplots()
                sns.heatmap(df1.corr(),ax=ax)
                ax.set_title('Heat map of of daily return')
                st.pyplot(fig1)