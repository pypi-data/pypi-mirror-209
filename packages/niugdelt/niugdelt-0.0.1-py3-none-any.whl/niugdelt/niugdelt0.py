# Libraries

import boto3
import pandas as pd
import io
from datetime import datetime, timedelta
from simple_colors import *
import time
import sys
import itertools
import threading
from botocore.exceptions import ClientError


# Main Files - Global Variables

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rWorking on your downloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!')

sts_client = boto3.client('sts')
assumed_role_object=sts_client.assume_role(
    RoleArn="arn:aws:iam::278808910769:role/JupyterS3FullAccessRole",
    RoleSessionName="gdelt-session-1"
)

credentials=assumed_role_object['Credentials']

boto3_session = boto3.session.Session(
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'], 
    aws_session_token=credentials['SessionToken']
)

s3 = boto3.resource('s3')
bucket = s3.Bucket('gdelt-all')
s4=boto3_session.client('s3')

# Classes and Functions

class MainFiles:
    # CLASS Documentation:
    # The class MainFiles have the repetitive files that connects the cloud bucket
    # with the functions to execute specific tasks
    # This is the parent class
    # It has two functions: 1) constructor as a self and 2) dates to get the range
    # of dates from the user
    
    def __init__(self):
        classdef = 'class constructor'
        
        
    def date():
        dates = []
        while True:
            start = input("Start date, format mm.dd.yy or 'end': ")
            if start == "end":
                break
            end = input("End date, format mm.dd.yy or 'end': ")
            try:
                start =  datetime.strptime(start,"%m.%d.%y")
                end =  datetime.strptime(end,"%m.%d.%y")
                for i in range((end-start).days+1):
                    dates.append(start)
                    start += timedelta(days=1)
                break
            except ValueError:
                print("Wrong format. Try again write 'end'")
                time.sleep(5)
        return(dates)
        


class Downloading(MainFiles):
    
    def __init__(self):
        
        MainFiles.__init__(self)
        
        
    def vcounts(self):
        # V1-Counts
        dates = MainFiles.date()

        dfa = []
        for i in range(len(dates)):
            j = i-1
            x = date_string = dates[j].strftime('%Y%m%d')
            key = 'v1/dt=' + x + '/' + x + '-cameo-counts.parquet'
            try:
                obj = s4.get_object(Bucket='gdelt-all', Key=key)
                df = pd.read_parquet(io.BytesIO(obj['Body'].read()))
                dfa.append(df)
                
            except ClientError as ex:
                if ex.response['Error']['Code'] == 'NoSuchKey':
                    print("No info for the dates provided")
                    return

        data = pd.concat(dfa, axis=0)

        data.to_csv(r'cameo-counts.csv', index = None, header=True)
  

    def vgkg(self):
        # V1 - gkg
        dates = MainFiles.date()
        
        dfa = []
        for i in range(len(dates)):
            j = i-1
            x = date_string = dates[j].strftime('%Y%m%d')
            key = 'v1/dt=' + x + '/' + x + '-cameo-gkg.parquet'
            try:
                obj = s4.get_object(Bucket='gdelt-all', Key=key)
                df = pd.read_parquet(io.BytesIO(obj['Body'].read()))
                dfa.append(df)
                
            except ClientError as ex:
                if ex.response['Error']['Code'] == 'NoSuchKey':
                    print("No info for the dates provided")
                    return                

        data = pd.concat(dfa, axis=0)

        data.to_csv(r'cameo-gkg.csv', index = None, header=True)

    def engexport(self):
        # V2 English-Export
        dates = MainFiles.date()
        
        dfa = []
        for i in range(len(dates)):
            j = i-1
            x = date_string = dates[j].strftime('%Y%m%d')
            prefix = 'v2/dt=' + x + '/'
            startsw = 'v2/dt=' + x + '/' + x + '-en-export'
            for obj in bucket.objects.filter(Prefix=prefix):
                if obj.key.startswith(startsw):
                    obj = s4.get_object(Bucket='gdelt-all', Key=obj.key)
                    df = pd.read_parquet(io.BytesIO(obj['Body'].read()))
                    dfa.append(df)

        try:
            data = pd.concat(dfa, axis=0)
            data.to_csv(r'en-export.csv', index = None, header=True)
            
        except ValueError:
            print("No data for the dates provided")
            return

    def enggkg(self):
        # v2 English-GKG
        dates = MainFiles.date()
        
        dfa = []
        for i in range(len(dates)):
            j = i-1
            x = date_string = dates[j].strftime('%Y%m%d')
            prefix = 'v2/dt=' + x + '/'
            startsw = 'v2/dt=' + x + '/' + x + '-en-gkg'
            for obj in bucket.objects.filter(Prefix=prefix):
                if obj.key.startswith(startsw):
                    obj = s4.get_object(Bucket='gdelt-all', Key=obj.key)
                    df = pd.read_parquet(io.BytesIO(obj['Body'].read()))
                    dfa.append(df)
                    
        try:
            data = pd.concat(dfa, axis=0)
            data.to_csv(r'en-gkg.csv', index = None, header=True)
            
        except ValueError:
            print("No data for the dates provided")
            return

    def engmen(self):
        # V2 English-Mentions
        dates = MainFiles.date()
        
        dfa = []
        for i in range(len(dates)):
            j = i-1
            x = date_string = dates[j].strftime('%Y%m%d')
            prefix = 'v2/dt=' + x + '/'
            startsw = 'v2/dt=' + x + '/' + x + '-en-mentions'
            for obj in bucket.objects.filter(Prefix=prefix):
                if obj.key.startswith(startsw):
                    obj = s4.get_object(Bucket='gdelt-all', Key=obj.key)
                    df = pd.read_parquet(io.BytesIO(obj['Body'].read()))
                    dfa.append(df)

        try:
            data = pd.concat(dfa, axis=0)
            data.to_csv(r'en-mentions.csv', index = None, header=True)       
        except ValueError:
            print("No data for the dates provided")
            return
            
    def transl(self):
        # V2 Translations
        dates = MainFiles.date()
        
        dfa = []
        for i in range(len(dates)):
            j = i-1
            x = date_string = dates[j].strftime('%Y%m%d')
            prefix = 'v2/dt=' + x + '/'
            startsw = 'v2/dt=' + x + '/' + x + '-tr-export'
            for obj in bucket.objects.filter(Prefix=prefix):
                if obj.key.startswith(startsw):
                    obj = s4.get_object(Bucket='gdelt-all', Key=obj.key)
                    df = pd.read_parquet(io.BytesIO(obj['Body'].read()))
                    dfa.append(df)
                    
        try:
            data = pd.concat(dfa, axis=0)
            data.to_csv(r'tr-translation.csv', index = None, header=True)
            
        except ValueError:
            print("No data for the dates provided")
            return


    def wfile(self):
        message = "file processing"
        return(message)

   
# INTERFACE DOWNLOADING      
        
def submenu1():

    again = 'y'
    
    # Loop for more GDELT User interaction

    while again.upper() == 'Y':
        
        global done

        print(red('Enter 1 for GDELT 1.0 - GKG', ['bold']))
        print(red('Enter 2 for GDELT 1.0 - COUNTS', ['bold']))
        print(blue('Enter 3 for GDELT 2.0 - ENGLISH - EXPORT', ['bold']))
        print(blue('Enter 4 for GDELT 2.0 - ENGLISH - MENTIONS', ['bold']))
        print(blue('Enter 5 for GDELT 2.0 - ENGLISH - GKG', ['bold']))
        print(green('Enter 6 for GDELT 2.0 - TRANSLATIONS - EXPORT', ['bold']))
        
        option = int(input('Which option [1, 2, 3, 4, 5, 6]: '))
        
        if option == 1:
            done = False
            t = threading.Thread(target=animate)
            t.start()
            r = Downloading()
            message = r.wfile()
            print(message)
            r.vcounts()
            time.sleep(10)
            done = True           

            
        elif option == 2:
            done = False
            t = threading.Thread(target=animate)
            t.start()
            r = Downloading()
            message = r.wfile()
            print(message)
            r.vgkg()
            time.sleep(10)
            done = True           
            
        elif option == 3:
            done = False
            t = threading.Thread(target=animate)
            t.start()
            r = Downloading()
            message = r.wfile()
            print(message)
            r.engexport()
            time.sleep(10)
            done = True           
            
        elif option == 4:
            done = False
            t = threading.Thread(target=animate)
            t.start()
            r = Downloading()
            message = r.wfile()
            print(message)
            r.enggkg()
            time.sleep(10)
            done = True           

        elif option == 5:
            done = False
            t = threading.Thread(target=animate)
            t.start()
            r = Downloading()
            message = r.wfile()
            print(message)
            r.engmen()
            time.sleep(10)
            done = True           
            
        elif option == 6:
            done = False
            t = threading.Thread(target=animate)
            t.start()
            r = Downloading()
            message = r.wfile()
            print(message)
            r.transl()
            time.sleep(10)
            done = True           
 
        else:
            print('follow the instructions')
            
        again = input('Another file to download (y = YES, n = NO): ')



