# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 14:43:10 2023

@author: Adith
"""

import pandas as pd
import streamlit as st
import pickle

import matplotlib.pyplot as plt
import seaborn as sn 
from PIL import Image



filename = "final_model.sav"
loaded_model = pickle.load(open(filename,'rb'))

df = pd.read_csv("clustering_final.csv")
st.set_option('deprecation.showPyplotGlobalUse', False)

df_cust5 = pd.read_csv("plot_dataframe.csv")
df_cust = pd.read_excel("marketing_campaign1.xlsx")

df_cust7 = pd.read_csv("evaluation_dataframe.csv")

st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)

st.header('Customer Segmentation App')




st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Homepage", "Data Analysis" ,"Form"))
backgroundColor="#FFFFFF"



        
if page =="Homepage":
    
    
    image = Image.open(r'C:/Users/INDIA/customer_segmentation_public_app/customer segmentation.jpg')

    st.image(image)
    
    st.write("Customer Personality Analysis is a detailed analysis of a company’s ideal customers. It helps a business to better understand its customers and makes it easier for them to modify products according to the specific needs, behaviors and concerns of different types of customers. Customer personality analysis helps a business to modify its product based on its target customers from different types of customer segments")
    
    
if page =="Data Analysis":
    
    graphs = st.sidebar.button("Univariate Plots")
    plots = st.sidebar.button("Bivariate plots")
    
    clusters = st.sidebar.button("Evaluation Plots")
    solutions = st.sidebar.button("Conclusion")
    about = st.sidebar.button("About")
    
    st.markdown('<hr>', unsafe_allow_html=True)
    
    if graphs:
        
        # checking with the count of education 
        sn.set_style('whitegrid') 
        sn.countplot(x ='Education',data=df_cust)  
        plt.show()
        st.write("We observe that most of the customers come from a good background of education ,most of them are having post graduation and graduation degrees ")
        st.pyplot()
        
        st.markdown('<hr>', unsafe_allow_html=True)
        
        
        
     
        
        
        #checking count with customers accepted campaigns 
        fig,ax = plt.subplots(1,5,figsize = (20,8))
        colors =['#9EF8EE','#348888']
        fig.suptitle('Campaign Acceptance',fontsize = 40)
        sn.countplot(ax = ax[0],x = 'AcceptedCmp1',data=df_cust)
        sn.countplot(ax = ax[1],x = 'AcceptedCmp2',data=df_cust)
        sn.countplot(ax = ax[2],x = 'AcceptedCmp3',data=df_cust)
        sn.countplot(ax = ax[3],x = 'AcceptedCmp4',data=df_cust)
        sn.countplot(ax = ax[4],x = 'AcceptedCmp5',data=df_cust)
        plt.tight_layout()
        st.write("We observe that most of the people have not participated in any of the campaigns and accepted offers")
        st.pyplot()
        
        st.markdown('<hr>', unsafe_allow_html=True)
        
        
        fig,ax = plt.subplots(nrows = 3,ncols = 2,figsize = (15,7))
        fig.suptitle('Amount Spent on products',fontsize = 20)
        sn.histplot(ax = ax[0,0],x = 'MntFishProducts',data=df_cust)
        sn.histplot(ax = ax[0,1],x = 'MntFruits',data=df_cust)
        sn.histplot(ax = ax[1,0],x = 'MntGoldProds',data=df_cust)
        sn.histplot(ax = ax[1,1],x = 'MntMeatProducts',data=df_cust)
        sn.histplot(ax = ax[2,0],x = 'MntSweetProducts',data=df_cust)
        sn.histplot(ax = ax[2,1],x = 'MntWines',data=df_cust)
        plt.tight_layout()
        st.write("We observe that most of the customer have highest expenditure over wines and meatproducts and least engaged with fruits ")
        st.pyplot()
        
        st.markdown('<hr>', unsafe_allow_html=True)
        
        #plotting with purchases at different locations 
        fig,ax = plt.subplots(nrows = 2,ncols = 2,figsize = (15,7))
        fig.suptitle('Purchases at Locations',fontsize = 20)
        sn.histplot(ax = ax[0,0],x = 'NumDealsPurchases',data=df_cust)
        sn.histplot(ax = ax[0,1],x = 'NumCatalogPurchases',data=df_cust)
        sn.histplot(ax = ax[1,0],x = 'NumStorePurchases',data=df_cust)
        sn.histplot(ax = ax[1,1],x = 'NumWebPurchases',data=df_cust)
        
        plt.tight_layout()
        st.write("* We observe most of the customers have reached to catalogs and purchased items and have selected particular item ")
        st.write(" * we can also see most of the customers have prefeered online shopping and have purchased from website ")
        st.write("* most of customers have reach out to store and we can infer that customers purchase rate through store is less compared to other locations ")
        st.pyplot()
        
        st.markdown('<hr>', unsafe_allow_html=True)
    
    

    if plots:
        
    
    
        #plotting with Family Distribution and their expenses 
        fig,ax = plt.subplots(1,2,figsize = (12,8))
        fig.suptitle("Family Expenses Distribution",fontsize = 30)
        ax[0].set_title('Family Expenses Distribution',fontsize = 15)
        ax[1].set_title('Family Distribution',fontsize = 15)
        plt.pie(df_cust5.Family.value_counts(),
          labels=['1','2','3','4','5'], autopct= '%.2f%%',shadow=True,
          colors = ['#9EF8EE','#348888'],explode= [0.1,0.0,0.0,0.0,0.0],
          textprops={'size':'large',
                     'fontweight':'bold'})
        sn.barplot(ax=ax[0],data = df_cust5,x='Family',y = 'Expenses',palette="mako",)
        
        st.write(" We observe that Family with an average of 3 have higher expenses compared to family having memebers more than 3 ")
       
       
        st.pyplot()
        
        st.markdown('<hr>', unsafe_allow_html=True)
        
        
        #plotting Education with Expenses 
        fig,ax = plt.subplots(1,2,figsize =(12,8))
        fig.suptitle("Education Expenses Distribution",fontsize = 30)
        ax[0].set_title('Stripplot Distribution',fontsize = 15)
        ax[1].set_title('Bar Distribution',fontsize = 15)
        sn.stripplot(ax=ax[0],data= df_cust5,x = 'Education',y = 'Expenses',palette='cividis',jitter=True)
        sn.barplot(ax = ax [1],data = df_cust5,x = 'Education',y = 'Expenses',palette='winter')
        st.pyplot()
        
        st.write("We observe that with higher education the expenses our higher")
        
        st.markdown('<hr>', unsafe_allow_html=True)

    
    #plotting with Expenses and purchases 
        fig,ax = plt.subplots(nrows=2,ncols=2,figsize = (15,10))
        fig.suptitle("Expenses-Purchases Plot",fontsize = 30)
        sn.regplot(ax=ax[0,0],x='Expenses',y = 'Purchases',data=df_cust5)
        sn.scatterplot(ax=ax[0,1],x='Expenses',y = 'Purchases',data=df_cust5,hue = 'Income_Category')
        sn.histplot(ax=ax[1,0],x='Purchases',hue ='Education',multiple="stack",palette="RdBu",
                edgecolor = ".3",data=df_cust5)
        sn.lineplot(ax =ax[1,1],x='Purchases',y ='Expenses',data = df_cust5,hue = 'Family'
                ,palette = "Set2")
        ax[0,0].set_title("Regression plot")
        ax[0,1].set_title("Purchases - Expenses scatter plot with Income")
        ax[1,0].set_title("Purchases - Education Histogram plot")
        ax[1,1].set_title("Purchases - Expenses Lineplot with Family Size")
        st.pyplot()
        st.write("We observe that most families with higher education have higher expenses and purchases and these segment belong to Middle and Upper Middle Class compared to other families from other segments")
        
        st.markdown('<hr>', unsafe_allow_html=True)

    
    #plotting with Age Distribution With Expenses and purchases 
        fig,ax = plt.subplots(1,2,figsize = (15,10))
        fig.suptitle("Customer Type Purchases - Expenses Distribution",fontsize = 20)
        ax[0].set_title('Customer Age Expenses - Purchases Distribution',fontsize = 15)
        ax[1].set_title('Customer Distribution',fontsize = 15)
        sn.scatterplot(ax=ax[0],data = df_cust5,x='Expenses',y = 'Purchases', hue ='Customer_Segment',markers = True,
                   palette="bright")
        plt.pie(df_cust5.Customer_Segment.value_counts(),
                labels=['Gen X','Boomer','Millennial','Silent'], autopct= '%.2f%%',shadow=True,
                colors = ['#FFCB9A','#D2E8E3'],explode= [0.1,0.0,0.0,0.0],
                textprops={'size':'large',
                     'fontweight':'bold'})
        st.pyplot()
        
        st.write("We observe that the age groups ranging from Genx and Boomers have the highest purchases compared to other Age groups")
        
        st.markdown('<hr>', unsafe_allow_html=True)

    #plotting with Income category and Customer Segment With Family 
        fig,ax = plt.subplots(nrows = 2,ncols = 3,figsize = (15,10))
        fig.suptitle(" Income Class - Customer Segment- Family Distribution",fontsize = 20)
        ax[0,0].set_title('Income Class-Family',fontsize = 15)
        ax[0,1].set_title('Customer Segment-Family',fontsize = 15)
        ax[1,0].set_title('Income Class-Purchases-Family',fontsize = 15)
        ax[1,1].set_title('Customer Segment-Purchases-Family',fontsize = 15)
        ax[0,2].set_title('Income Segment-Family Division',fontsize = 15)
        ax[1,2].set_title('Customer Age Segment-Family Division',fontsize = 15)
        sn.histplot(ax=ax[0,0],data = df_cust5,x ='Income_Category', hue ='Family',
                   palette="Paired",multiple = 'dodge')
        sn.histplot(ax=ax[0,1],data = df_cust5,x ='Customer_Segment', hue ='Family',
                   palette="Paired",multiple = 'dodge')
        sn.stripplot(ax=ax[1,0],data = df_cust5,x ='Family',y = 'Purchases', hue ='Income_Category',
                   palette="Paired")
        sn.stripplot(ax=ax[1,1],data = df_cust5,x ='Family',y = 'Purchases', hue ='Customer_Segment',
                   palette="Paired",)
        colors =['#93BFB7', '#13678A', '#45C4B0', 
              '#9AEBA3']
        explode = (0.1, 0.00, 0.00, 0.00,)
    
        labels = 'Middle','Upper-Middle','lower','upper' #adding labels 
    
        grp_family = df_cust5.groupby('Income_Category')['Family'].sum().sort_values(ascending = False) #grouping by income category and family 
        ax[0,2].pie(grp_family,colors = colors,explode = explode,
                autopct='%1.1f%%', textprops={'size':'large',
                     'fontweight':'bold'},shadow = True,labels = labels,startangle = 180,
                pctdistance = 0.80)
        labels2 = 'GenX','Boomer','Millennial','Silent'
        grp_segment = df_cust5.groupby('Customer_Segment')['Family'].sum().sort_values(ascending = False) #grouping by customer Age segment and family
        ax[1,2].pie(grp_segment,colors = colors,explode = explode,
                autopct='%1.1f%%', textprops={'size':'large',
                     'fontweight':'bold'},shadow = True,labels = labels2,startangle = 180,
                pctdistance = 0.80) # plotting a pie chart 
        plt.tight_layout()
        
        st.write(" We observe that 80 percent of our customers are from Lower , Middle and upper Middle class with age ranging from Millennials to baby Boomers, customers from upper class and silent age groups have least purchase rate and come in the 20 percent.")
    
        st.pyplot()
    
   
    if clusters:
        
            
        #checking with the distribution of clusters 
        fig,ax = plt.subplots(1,2,figsize = (15,10))
        sn.countplot(ax = ax [0],x = df_cust7['clusters'],palette = 'bright') 
        colors =['#9EF8EE','#348888']
        fig.suptitle('Cluster Analytics',fontsize = 40)
        df_cust7.clusters.value_counts().plot(ax = ax [1],kind ='pie', autopct= '%.2f%%',shadow=True,explode = [0.1,0.0,0.0],colors=colors)
        plt.tight_layout()
        st.pyplot()
        st.markdown('<hr>', unsafe_allow_html=True)
        
        #plotting with clusters with customers accepted the offers 
        sn.countplot(data = df_cust7,x = 'Acceptance',hue = 'clusters',palette = 'bright')
        st.pyplot()
        st.markdown('<hr>', unsafe_allow_html=True)
        
   
            
            #evaluating purchases according to income categories 
        fig,ax = plt.subplots(nrows = 2,ncols = 2,figsize = (15,10))
        sn.scatterplot(ax = ax [0,0],data = df_cust7,x =  'Income_Category_lower',y = 'Purchases',hue = 'clusters',palette = 'bright')
        sn.scatterplot(ax = ax [0,1],data = df_cust7,x =   'Income_Category_middle',y = 'Purchases',hue = 'clusters',palette = 'bright')
        sn.scatterplot(ax = ax [1,0],data = df_cust7,x =  'Income_Category_upper_middle',y = 'Purchases',hue = 'clusters',palette = 'bright')
        sn.scatterplot(ax = ax [1,1],data = df_cust7,x =   'Income_Category_upper',y = 'Purchases',hue = 'clusters',palette = 'bright')
        st.pyplot()
        
        st.markdown('<hr>', unsafe_allow_html=True)
    
            
            #evaluating purchases according to age categories 
        fig,ax = plt.subplots(nrows = 2,ncols = 2,figsize = (15,10))
        sn.scatterplot(ax = ax [0,0],data = df_cust7,x =  'Customer_Segment_Millennial',y = 'Purchases',hue = 'clusters',palette = 'bright')
        sn.scatterplot(ax = ax [0,1],data = df_cust7,x =    'Customer_Segment_Gen X',y = 'Purchases',hue = 'clusters',palette = 'bright')
        sn.scatterplot(ax = ax [1,0],data = df_cust7,x =   'Customer_Segment_Boomer',y = 'Purchases',hue = 'clusters',palette = 'bright')
        sn.scatterplot(ax = ax [1,1],data = df_cust7,x =   'Customer_Segment_Silent',y = 'Purchases',hue = 'clusters',palette = 'bright')
        st.pyplot()
       
    if solutions:
        
        
            
        
        st.title("Solutions")
        st.write(" * When it comes to Purchases and expenses we have observed that most of the people come from middle and upper-middle class backgrounds and have the highest purchases and expenses, they almost comprise 80% of the total segmentation.")
        st.write(" * We can attract this segment with more offers and campaigns with the products and bring the prices to affordable rates with association to another items, so every middle and upper middle class family engage with the company ")
        st.write(" * we can run an advertise campaign for these segments that would improve sales of the products and could attract the consumer with discounts and coupons with two or more products.") 
        st.write(" * We could also look at the age segmentation and we observed that most of our consumers are from GenX to boomers so for these groups we could create awareness by catalogs and run a creative campaigns and keeps offers for consumers who fall in this age group.") 
        st.write(" * When it  comes to families for families we can keep products like hampers and call it as family pack and we have observed that consumers with a family are more in ratio when compared to bachelors or couples ")           
        st.write(" * To end with a conclusion the company has to create more awareness of their products, discounts , offers, campaigns, advertisements and digital media marketing  for the income groups that fall in middle class and upper middle class and between age groups that fall in GenX and Boomers that are within a family.This would increase the range of consumers and sales of products.")
        
    if about:
        
        st.write("In this project we have worked over Customer Segmentation for a company and perform a personality analysis of the customers purchases over products")
        st.write("In this project we have understood that the customer segmentation can be divided into many types of segmentation and also we have observed that which classes have the highest purchases and expenses based on income and age categories ")
        st.write("A Project By Team 6")
        st.write("Thankyou")
        
    
            
        
        
        
        
        
        
        
        
        
elif page == "Form":
    



    
    st.sidebar.header('Customer Details')
    with st.form("Customer Details"):
        
     
        
        Purchases = st.sidebar.number_input(label ='Total Purchases',step=(10))
        day_engaged = st.sidebar.number_input(label ='Number of Days with Company',step=(100))
        Acceptance = st.sidebar.selectbox('Number Of Campaign offers Accepted',('1','2','3','4','5'))
        Family = st.sidebar.selectbox('Members In a Family',('1','2','3','4','5'))
        Income_Category_lower = st.sidebar.selectbox('Lower Class (1K - 30K)', ('0','1'))
        Income_Category_middle =  st.sidebar.selectbox('Middle Class (30K - 60K)', ('0','1'))
        Income_Category_upper_middle =  st.sidebar.selectbox('Upper Middle Class (60K - 90K)', ('0','1'))
        Income_Category_upper =  st.sidebar.selectbox('Upper Class (90K - 100K Above)', ('0','1'))
        Customer_Segment_Millennial =  st.sidebar.selectbox('Millennial (27 - 42 years old)', ('0','1'))
        Customer_Segment_Gen_X	 =  st.sidebar.selectbox('GenX (43 - 56 years old)	', ('0','1'))
        Customer_Segment_Boomer =  st.sidebar.selectbox('Boomer (59 - 70 years old)' , ('0','1'))
        Customer_Segment_Silent =  st.sidebar.selectbox('Silent (78 - 84 years old)', ('0','1'))
        Education_Grad =  st.sidebar.selectbox('Graduate', ('0','1'))
        Education_PostGrad =  st.sidebar.selectbox('PostGraduate', ('0','1'))
        Education_Undergrad =  st.sidebar.selectbox('Undergraduate', ('0','1'))
        
        
        data=[[Purchases,day_engaged,Acceptance,Family,Income_Category_lower,Income_Category_middle,Income_Category_upper_middle,Income_Category_upper,Customer_Segment_Millennial,Customer_Segment_Gen_X,Customer_Segment_Boomer,Customer_Segment_Silent,Education_Grad,Education_PostGrad,Education_Undergrad]]
        
        
        submitted = st.sidebar.button("Submit")
       
        
    if submitted:
        
        
        
       st.markdown("Cluster Information") 
       clust = loaded_model.predict(data)[0]
       st.write('cluster 0 -  the purchases are moderate with lowest enrollment with the company and has highest acceeptance to campaign offers')
       st.write('cluster 1 -  the purchases are lowest with moderate enrollment with the company and has lowest acceptance to campaign offers' )
       st.write('cluster 2 -  the purchases are highest with highest enrollment with the company and has moderate acceptance to campaign offers ')
       
    
        
        
       cluster_df1=df[df['clusters']==clust]
       plt.rcParams["figure.figsize"] = (5,5)
        
       for c in cluster_df1:
            grid = sn.FacetGrid(cluster_df1,col = 'clusters')
            grid = grid.map(plt.hist,c )
            plt.show()
            st.pyplot()

        
        
        
        
 
    

    
    
    
    
    
    