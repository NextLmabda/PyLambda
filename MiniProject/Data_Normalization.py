
import numpy as np

class Normalize_Data:
    '''
    This class .........
    '''
    
    def __init__(self, df):
        '''
        df: pandas DataFrame -> Pandas dataframe
        '''
        print('I am running the init method')
        self.df = df
    
    def Change_Columns_Name(self, columns):
        output = {}
        for col in columns:
            if col[0].islower():
                colNew = col.replace(col[0], col[0].upper())
                output[col] = colNew
                
        return output
    
    def Change(self):
        self.df.rename(columns = self.Change_Columns_Name(self.df.columns), inplace=True)
  
    def Normalize(self):
        '''
        
        '''
        self.df['TotalCharges'] = self.df["TotalCharges"].replace(" ",np.nan)

        #Dropping null values from total charges column which contain .15% missing data 
        self.df = self.df[self.df["TotalCharges"].notnull()]
        self.df = self.df.reset_index()[self.df.columns]
        
        self.df["TotalCharges"] = self.df["TotalCharges"].astype(float) # converting the TotalCharges to float datatype
        
        replace_cols = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                'TechSupport','StreamingTV', 'StreamingMovies']
        for i in replace_cols : 
            self.df[i]  = self.df[i].replace({'No internet service' : 'Yes'})
            
        self.df["SeniorCitizen"] = self.df["SeniorCitizen"].replace({1:"Yes",0:"No"})
        
        self.df['Tenure'] = self.df['Tenure'].apply(self.tenure_lab)
        
    def initiate_process(self):
        self.Change_Columns_Name(self.df.columns)
        self.Change()
        self.Normalize()
        return self.df
    
    def tenure_lab(self, x):

            if x <= 12 :
                return "Tenure_0-12"
            elif (x > 12) & (x <= 24 ):
                return "Tenure_12-24"
            elif (x > 24) & (x <= 48) :
                return "Tenure_24-48"
            elif (x > 48) & (x <= 60) :
                return "Tenure_48-60"
            elif x > 60 :
                return "Tenure_gt_60"
        
    
    
class Omolewa:
    
    def Multiply(x):
        
        return x ** 2
    
    
def Divide(x, y):
    return x % y