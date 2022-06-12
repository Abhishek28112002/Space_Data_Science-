
# from sklearn.linear_model import SGDClassifier
import sys
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import RobustScaler
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import seaborn as sb
import os
from csv import writer
from csv import reader
import requests
def accu(pipe1 ,pipe3,df,dfr):
    X_test_accu=df.iloc[14000:15000,:].values
    y_test_accu=dfr.iloc[14000:15000,-1].values
    for i in range(len(y_test_accu)):
        if y_test_accu[i]=='AFP':
            y_test_accu[i]=0
        if y_test_accu[i]=='PC':
            y_test_accu[i]=1
        if y_test_accu[i]=='NTP': 
            y_test_accu[i]=2
        if y_test_accu[i]=='UNK':
            y_test_accu[i]=3
    y_test_accu=y_test_accu.astype('int')

    pred_kn=pipe1.predict_proba(X_test_accu)
    pred_rf=pipe3.predict_proba(X_test_accu)
    y_pred_accu=[]
    a=1
    c=8
    for i in range(len(X_test_accu)):
        pro_score_0=a*proba_SVC[i][0]+c*proba_RF[i][0]
        pro_score_1=a*proba_SVC[i][1]+c*proba_RF[i][1]
        pro_score_2=a*proba_SVC[i][2]+c*proba_RF[i][2]
        pro_score_3=a*proba_SVC[i][3]+c*proba_RF[i][3]

                        
        if(pro_score_0>=pro_score_1 and pro_score_0>=pro_score_2 and pro_score_0>=pro_score_3):
            y_pred_accu.append(0)
        elif(pro_score_1>=pro_score_0 and pro_score_1>=pro_score_2 and pro_score_1>=pro_score_3):
            y_pred_accu.append(1)
        elif(pro_score_2>=pro_score_0 and pro_score_2>=pro_score_1 and pro_score_2>=pro_score_3):
            y_pred_accu.append(2)
        elif(pro_score_3>=pro_score_0 and pro_score_3>=pro_score_1 and pro_score_3>=pro_score_2):
            y_pred_accu.append(3)
    print(accuracy_score(y_test_accu,y_pred_accu)) 
    cf=confusion_matrix(y_test_accu,y_pred_accu)
    sb.heatmap(cf,annot=True,xticklabels=['AFP','PC','NTP','UNK'],yticklabels=['AFP','PC','NTP','UNK'])

#paths
training_path=r"full_data.csv" 
testing=r"./uploads/python.csv"
output_path=r"./uploads/python.csv"
cols=['tce_period', 'tce_time0bk_err', 'tce_impact_err', 'tce_depth', 'tce_depth_err', 'tce_prad_err', 'tce_steff_err', 'tce_slogg_err']


df=pd.read_csv(training_path,usecols=cols)
dfr=pd.read_csv(training_path,usecols=['av_training_set'])
X_train=df.iloc[:14000,:].values
y_train=dfr.iloc[:14000,-1].values
for i in range(len(y_train)):
    if y_train[i]=='AFP':
        y_train[i]=0
    if y_train[i]=='PC':
        y_train[i]=1
    if y_train[i]=='NTP': 
        y_train[i]=2
    if y_train[i]=='UNK':
        y_train[i]=3
y_train=y_train.astype('int')

dfT=pd.read_csv(testing,usecols=cols)
X_test=dfT.iloc[:,:].values
no_rows=len(dfT)
os.remove(testing)

pipe1 = Pipeline([("Standard Scaling",RobustScaler()),("SGD Regression",KNeighborsClassifier())])
pipe1.fit(X_train, y_train)  # apply scaling on training data
# print("K Nearest Neighbors Trained")
# print("Mean absolute error",mean_absolute_error(Y_pred,y_test))
proba_SVC=pipe1.predict_proba(X_test)


pipe3 = Pipeline([("Standard Scaling",RobustScaler()),("SGD Regression",RandomForestClassifier(random_state=12,n_estimators=100))])
pipe3.fit(X_train, y_train) # apply scaling on training data
# print("Random Forest Trained")
# print("Mean absolute error",mean_absolute_error(Y_pred,y_test))
proba_RF=pipe3.predict_proba(X_test)
# print("Random Forest Tested")
y_pred=[]
value=10
a=1
b=2
c=8
for i in range(len(X_test)):
    pro_score_0=a*proba_SVC[i][0]+c*proba_RF[i][0]
    pro_score_1=a*proba_SVC[i][1]+c*proba_RF[i][1]
    pro_score_2=a*proba_SVC[i][2]+c*proba_RF[i][2]
    pro_score_3=a*proba_SVC[i][3]+c*proba_RF[i][3]

                    
    if(pro_score_0>=pro_score_1 and pro_score_0>=pro_score_2 and pro_score_0>=pro_score_3):
        y_pred.append(0)
    elif(pro_score_1>=pro_score_0 and pro_score_1>=pro_score_2 and pro_score_1>=pro_score_3):
        y_pred.append(1)
    elif(pro_score_2>=pro_score_0 and pro_score_2>=pro_score_1 and pro_score_2>=pro_score_3):
        y_pred.append(2)
    elif(pro_score_3>=pro_score_0 and pro_score_3>=pro_score_1 and pro_score_3>=pro_score_2):
        y_pred.append(3)
                
actual_Class=[]
for i in range(len(X_test)):
    if y_pred[i]==0:
        actual_Class.append('AFP')
    if y_pred[i]==1:
        actual_Class.append('PC')
    if y_pred[i]==2:
        actual_Class.append('NTP')
    if y_pred[i]==3:
        actual_Class.append('UNK')

# print("Count of AFP",actual_Class.count("AFP"))
# print("Count of PC",actual_Class.count("PC"))
# print("Count of NTP",actual_Class.count("NTP"))
# print("Count of UNK",actual_Class.count("UNK"))

# print(actual_Class.__len__())
# Open the input_file in read mode and output_file in write mode
with open(output_path, 'w', newline='') as write_obj:
    # Create a csv.reader object from the input file object
    # Create a csv.writer object from the output file object
    csv_writer = writer(write_obj)
    # Read each row of the input csv file as list
    i=0
    j=0
    for row in range(no_rows):
        if j==0:
            j=1
            csv_writer.writerow(["class"])
        else:
            csv_writer.writerow([actual_Class[i]])
            i+=1
print("succesfully written")
r=requests.get("http://./uploads/python.csv")
with open("output.csv", 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024): 
        if chunk:
            f.write(chunk)
# accu(pipe1=pipe1,pipe3=pipe3,df=df,dfr=dfr)
