import pandas as pd
df=pd.read_csv(r'C:\Users\Harsh\Desktop\Webscrape\Data.csv')
df.to_json(r'C:\Users\Harsh\Desktop\Webscrape\Data.json')

import csv,json
csvFilePath='Case.csv'
jsonFilePath='Case.json'

data={}
with open(csvFilePath) as csvFile:
	csvReader=csv.DictReader(csvFile)
	for csvRow in csvReader:
		Court_System=csvRow['Court_System']
		Case_Number=csvRow['Case_Number']
                Status_Date=csvRow['Status Date']
                Complaint_No=csvRow['Complaint_No']
                Tracking_Number=csvRow['Tracking_Number']
                District_Case_No=csvRow['District_Case_No']
                Incident_Date=csvRow['Incident_Date']
                Defendant_Name=csvRow['Defendant_Name']
                Filing_Date=csvRow['Filing Date']
                Race=csvRow['Race']
                DOB=csvRow['DOB']
                Sex=csvRow['Sex']
                Address=csvRow['Address']
                city=csvRow['city']
                State=csvRow['State']
                Zip_Code=csvRow['Zip_Code']      
                Court Date=csvRow['Court_Date']
                Court_Time=csvRow['Court_Time']
                Court_Location=csvRow['Court_Location']
                Reason=csvRow['Reason']
                Charge_No=csvRow['Charge_No']
                CJIS/Traffic Code=csvRow['CJIS/Traffic Code']
                Description=csvRow['Description']
                Plea=csvRow['Plea']
                Plea_Date=csvRow['Plea_Date']
                Disposition=csvRow['Disposition']
                Disposition_Date=csvRow['Disposition_Date']
                Verdict=csvRow['Verdict']
                Verdict_Date=csvRow['Verdict_Date']
                Sentence_Starts=csvRow['Sentence_Starts']
                Sentence_Time=csvRow['Sentence_Time']
                Yrs1=csvRow['Yrs1']
                Mos1=csvRow['Mos1']
                Days1=csvRow['Days1']
                Confinement=csvRow['Confinement']
                Yrs2=csvRow['Yrs2']
                Mos2=csvRow['Mos2']
                Days2=csvRow['Days2']
                Yrs3=csvRow['Yrs3']
                Mos3=csvRow['Mos3']
                Days3=csvRow['Days3']
                Charger_no_2=csvRow['Charge_no_2']
                CJIS/Traffic_Code2=csvRow['CJIS/Traffic_Code2']
                Description2=csvRow['Description2']
                Name3=csvRow['Name3']
                Connection=csvRow['Connection']
                Address1=csvRow['Address1']
                Connection2=csvRow['Connection2']
                city2=csvRow['City2']
                
		data[city][Name][Court_System][Case_Number][Status_Date][Tracking Number][District_Case_No][Incident_Date][Defendant_Name][Filing_Date][Filing_Date][Race][DOB][Sex][Address][City][State][zip_code][court_date][court_time][court_location][reason][charge_no][CJIS/Traffic Code][Description][Plea][Plea_date][Disposition][Disposition_date][Verdict][Verdict_date][sentence_starts][Sentence_Time][Yrs1][Mos1][Days1][Confinement][Yrs2][Mos2][Days2][Yrs3][Mos3][Days3][Charge_No2][CJIS/Traffic Code][Description2][Name3][Connection][Address1][Connection2][city2]=csvRow

with open(jsonFilePath,"w") as jsonFile:
	jsonFile.write(json.dumps(data, indent=4))
