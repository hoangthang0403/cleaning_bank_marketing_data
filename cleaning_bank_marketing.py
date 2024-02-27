# Importing libraries
import pandas as pd
import numpy as np

# Reading data into DataFrame
client = pd.read_csv("bank_marketing.csv",usecols=['client_id','age','job','marital','education','credit_default','mortgage'])

# Removing '.' from string
client['job'] = client['job'].str.replace('.', '')
client['education'] = client['education'].str.replace('.','')

# Replacing 'unknown' string by np.NaN value
client['education'] = client['education'].replace('unknown',np.nan)

# Creating mapping dictionary to unify values
m = {'no':False,'unknown':False,'yes':True}

# Unifying data by using .map method
client['credit_default'] = client['credit_default'].map(m)

# Converting to boolean type
client['credit_default'] = client['credit_default'].astype(bool)

# Unifying data by using .map method
client['mortgage'] = client['credit_default'].map(m)

# Converting to boolean type
client['mortgage'] = client['credit_default'].astype(bool)

# Saving result to csv file.
# index=False to avoid an unnamed additional column.
client.to_csv('client.csv',index = False)


# Reading data into DataFrame
campaign = pd.read_csv("bank_marketing.csv",usecols=['client_id','number_contacts','contact_duration',
                                                     'previous_campaign_contacts','previous_outcome','campaign_outcome','day','month'])

# Creating mapping dictionary to unify values
po = {'success':True,'failure': False, 'nonexistent': False}

# Unifying data by using .map method
campaign['previous_outcome'] = campaign['previous_outcome'].map(po)

# Converting to boolean type
campaign['previous_outcome'] = campaign['previous_outcome'].astype(bool)

# Creating mapping dictionary to treat 'yes' as True and 'no' as False
co = {'yes':True,'no':False}
campaign['campaign_outcome'] = campaign['campaign_outcome'].map(co)
# Converting to boolean type
campaign['campaign_outcome'] = campaign['campaign_outcome'].astype(bool)

# Capitalizing all values in 'month' column
campaign['month'] = campaign['month'].str.capitalize()

# Converting to str type
campaign['day'] = campaign['day'].astype(str)

# Creating new column with all values equal to '2022'
campaign['year'] = '2022'

# Creating new column called 'last_contact_date' to concat day, month, year into format "%d-%b-%Y"
campaign['last_contact_date'] = campaign['day'] + '-' + campaign['month'] + '-'+ campaign['year']

# Converting to datetime type, take "%d-%b-%Y" as input format
campaign['last_contact_date'] = pd.to_datetime(campaign['last_contact_date'],format = '%d-%b-%Y') # switch format to match with input values

# Dropping 'month', 'day' columns after finished
# axis = 1 to drop columns
campaign.drop(['month','day'],axis = 1,inplace = True)

# Saving result to csv file
campaign.to_csv('campaign.csv',index = False)

# Reading data into DataFrame
economics = pd.read_csv('bank_marketing.csv',usecols = ['client_id','cons_price_idx','euribor_three_months'])

# Saving result to csv file
economics.to_csv('economics.csv',index = False)
