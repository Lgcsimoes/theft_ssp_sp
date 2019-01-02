#
from xlrd import open_workbook
import json
import requests
import csv

google_key = 'INSERT_YOUR_KEY_HERE'

outputFile = open('output_2016_01-06.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['Latitude', 'Longitude', 'Comentários'])

errorFile = open('error_file.txt','w')
errorFile.write('List of failed fetches of Lat/Long coordinates:' + '\n')


workBooks = [ 'DadosBO_DEINTER1_Furtos_2016_01.xls', 'DadosBO_DEINTER1_Roubos_2016_01.xls', 'DadosBO_DEINTER1_Furtos_2016_02.xls', 'DadosBO_DEINTER1_Roubos_2016_02.xls', 'DadosBO_DEINTER1_Furtos_2016_03.xls', 'DadosBO_DEINTER1_Roubos_2016_03.xls', 'DadosBO_DEINTER1_Furtos_2016_04.xls', 'DadosBO_DEINTER1_Roubos_2016_04.xls', 'DadosBO_DEINTER1_Furtos_2016_05.xls', 'DadosBO_DEINTER1_Roubos_2016_05.xls', 'DadosBO_DEINTER1_Furtos_2016_06.xls', 'DadosBO_DEINTER1_Roubos_2016_06.xls']

for wbName in workBooks:

    wb = open_workbook(wbName)

    sheet = wb.sheet_by_index(0)
    for i in range(1,sheet.nrows):
        street = sheet.cell_value(i,12)
        number = sheet.cell_value(i,13)
        city = sheet.cell_value(i,16)
        addrStr = street+" "+str(number.__round__())+" "+city

        timeOfCrime = sheet.cell_value(i,6)
        dateOfCrime = sheet.cell_value(i,7)
        remark = dateOfCrime + ' ' + timeOfCrime.lower()

        print(addrStr)
        newUrl = "https://maps.googleapis.com/maps/api/geocode/json?address="+addrStr.replace(" ","+")+"&key="+google_key

        response = requests.get(newUrl).content.decode('utf-8')
        responseJson = json.loads(response)
        if responseJson.get('status') == 'OK':
            latitude = responseJson.get("results")[0].get("geometry").get("location").get("lat")
            longitude = responseJson.get("results")[0].get("geometry").get("location").get("lng")
            outputWriter.writerow([latitude, longitude, remark])
        else:
            print("Failed data catch: ", addrStr)
            errorFile.write(addrStr+': '+remark + '\n')

outputFile.close()
errorFile.close()
