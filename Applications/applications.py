import pandas as pd
import os
import difflib
system_apps=pd.read_csv('Data\Extensions_CSV.csv')

installed_apps_path=(os.popen("where *.exe").read().split("\n"))
installed_apps=[]

for i in range(0,len(installed_apps_path)):
    installed_apps_path[i]=installed_apps_path[i].split("\\")
    installed_apps.append(installed_apps_path[i][-1])


installed_apps_names=[]
installed_apps_extensions=[]
for i in range(0,len(installed_apps)):
    installed_apps_names.append(installed_apps[i].split('.')[0])
    installed_apps_extensions.append(str(installed_apps[i]))

installed_apps_dataframe=pd.DataFrame()
installed_apps_dataframe['Application']=installed_apps_names
installed_apps_dataframe['Actual Extension']=installed_apps_extensions
installed_apps_dataframe.to_csv('Data\Installed_Apps.csv')

all_applications=pd.concat([system_apps,installed_apps_dataframe])
#all_applications.to_excel("Data\applications.xlsx")

def launch_application(application):
    path="Data"
    all_applications=pd.read_excel(path+'\Applications.xlsx')
    print(all_applications.shape)
    application=application.lower()
    if application in all_applications['Application'].values:     
        app=(all_applications[all_applications['Application']==application]['Actual Extension'])
        app_final=str(app.iloc[:1].values)
        app_final=app_final.replace("[u'",'')
        app_final=app_final.replace("['",'')
        app_final=app_final.replace("']",'')

        print (app_final)
        os.popen("start "+ app_final)
    else:
        predictions=[]
        
        for i in range(0,len(all_applications['Application'])):
            a=application
            b=all_applications['Application'][i]
            seq = difflib.SequenceMatcher(None,a,b)
            d = seq.ratio()*100            
            predictions.append(d)
            
        #print(max(predictions))
        index_value=predictions.index(max(predictions))
        app_final=all_applications['Actual Extension'][index_value]
        print("Do You mean "+ all_applications['Application'][index_value]+"?")
        answer=raw_input("Response:")
        answer=answer.lower()
        if  'yes'or'yeah'or'correct' in answer:
            os.popen("start "+ app_final)
        else:
            print("Sorry Then Couldn't find anything with the name")
    
        

#launch_application('Hotspot')

