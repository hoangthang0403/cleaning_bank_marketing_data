import pandas as pd
import numpy as np


client = pd.read_csv("bank_marketing.csv",usecols=['client_id','age','job','marital','education','credit_default','mortgage'])
client['job'] = client['job'].str.replace('.', '')
client['education'] = client['education'].str.replace('.','')
client['education'] = client['education'].replace('unknown',np.nan)

m = {'no':False,'unknown':False,'yes':True}

client['credit_default'] = client['credit_default'].map(m)
client['credit_default'] = client['credit_default'].astype(bool)
client['mortgage'] = client['credit_default'].map(m)
client['mortgage'] = client['credit_default'].astype(bool)

client.to_csv('client.csv',index = False)

campaign = pd.read_csv("bank_marketing.csv",usecols=['client_id','number_contacts','contact_duration',
                                                     'previous_campaign_contacts','previous_outcome','campaign_outcome','day','month'])

po = {'success':True,'failure': False, 'nonexistent': False}
campaign['previous_outcome'] = campaign['previous_outcome'].map(po)
campaign['previous_outcome'] = campaign['previous_outcome'].astype(bool)

co = {'yes':True,'no':False}
campaign['campaign_outcome'] = campaign['campaign_outcome'].map(co)
campaign['campaign_outcome'] = campaign['campaign_outcome'].astype(bool)

campaign['month'] = campaign['month'].str.capitalize()
campaign['day'] = campaign['day'].astype(str)
campaign['year'] = '2022'
campaign['last_contact_date'] = campaign['day'] + '-' + campaign['month'] + '-'+ campaign['year']
campaign['last_contact_date'] = pd.to_datetime(campaign['last_contact_date'],format = '%d-%b-%Y') # switch format to match with input values

campaign.drop(['month','day'],axis = 1,inplace = True)

campaign.to_csv('campaign.csv',index = False)


economics = pd.read_csv('bank_marketing.csv',usecols = ['client_id','cons_price_idx','euribor_three_months'])

economics.to_csv('economics.csv',index = False) # index = False to avoid an unnamed additional column

