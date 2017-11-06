import gspread
import discord
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
 
def checkPing(member):
# use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
     
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("Ping Users Sheet").sheet1

    today = date.today()
    print("{}".format(today))
    print("{}".format(sheet.cell(2,5).value))
    today = str(today)
    row = 1
    col = 1
  
    while(sheet.cell(row,1).value != "~"):#This is not efficent or very easy to read, make it more orginized
        
        if(member.discriminator == sheet.cell(row,1).value):#If user has already pinged before
           
            if(sheet.cell(2,5).value == today):#If the sheet is already updated for today add 1 to used pings
              
                temp = sheet.cell(row,3).value
                temp = int(temp)
                temp  = temp + 1;
                sheet.update_cell(row,3,temp)
                break
            else:#Otherwise reset the sheet and clears
                
         
                
                tempRow = 2
                
                while(sheet.cell(tempRow,1).value != "~"):
                    sheet.update_cell(tempRow,3,"0")
                    tempRow = tempRow + 1

                sheet.update_cell(2,5,today)#Update date last checked value
                
                temp = sheet.cell(row,3).value
                temp = int(temp)
                temp  = temp + 1;
                sheet.update_cell(row,3,temp)
                break
                
            break
        
        elif(sheet.cell(row,1).value == '~'):#If end is reached
         
            sheet.update_cell(row,1,member.discriminator)
            sheet.update_cell(row,2,"3")
            sheet.update_cell(row,3,"1")
            sheet.update_cell(row+1,1,"~")#This shows the end of the list
            break
        
        else:#If not at end of list and user not found move down a row
            row = row + 1;
       
        
    allowed = sheet.cell(row,2).value#Holds the allowed amount of pings
    used = sheet.cell(row,3).value#Holds how many times the user has pinged

    
 
    if(used > allowed):#If user goes over the limit it sends true, sending a message to the owner
        return 1
    else:#Else it sends false doing nothing
        return 0
        
    sheet.update(2,5,date.today())
    
    print(member.discriminator)
   




    print("Closing ping abuse")
