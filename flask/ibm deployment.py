# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:51:41 2022

@author: user
"""
import requests
import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "_uQJaQRra2V-2lHNbQY1-q314HMfQ3Rkw1ZhkFeVDtWN"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["pH","Temprature","Taste","Odor","Fat","Turbidity","Colour"]], "values": [[6.7,45,1,1,1,0,245]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/f7293f6f-67be-4c43-9eb5-917a520bac11/predictions?version=2022-06-07', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())