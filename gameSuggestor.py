import gspread
import discord
from oauth2client.service_account import ServiceAccountCredentials
 
def AddGame(member):
# use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
     
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("Game Holder Sheet").sheet1
     
    # Extract and print all of the values
    results = sheet.get_all_records()
    x = 1
    row = 2
    col = 1

    while(not sheet.cell(row,col)):#Looks for the discrim
        if(member.discrimniator == sheet.cell(1,col)):
            break
        row = row + 1;
        print('Reading in {}'.format(sheet.cell(row,col)))
    sheet.update_cell(row,col,member.discriminator)

    while(sheet.cell(row,col)):
        if(sheet.cell(row,col)):
            break
        else:
            print("On {}".format(sheet.cell(row,col)))
            col = col + 1;

    
    print(member.discriminator)
    sheet.update_cell(row,col,member.game)        




    print("Closing Add Game")
