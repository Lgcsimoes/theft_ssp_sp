# Visualization of vehicle robbery and theft in part of São Paulo state, Brazil

This project aims at visualizing the spatial distribution of vehicle robbery and theft in the Vale do Paraiba region of São Paulo state, Brazil. Only events occured between January and June 2016 will be considered, however the methodology can be easily extended to any other date range or location in São Paulo state. Public government data is used in this project, data parsing is done by Python and visualization is made through Google MyMaps. The event location address is converted to latitude/longitude information (geotagging) using the Google Maps API.

## Data extraction

The public data information can be found [here](http://www.ssp.sp.gov.br/transparenciassp/Consulta.aspx), at the Data Transparency website of São Paulo state Public Security Office. The data used in this study can be reproduced by exporting "furto de veículo" (vehicle theft) and "roubo de veículo" (vehicle robbery). The department considered was "DEINTER 1 - SAO JOSE DOS CAMPOS".

Data could be scrapped automatically using a scrapper tool such as Selenium (working directly with a tool such as BeautifulSoup would not work because the website is written in JavaScript), however it was decided to manually download the data for each month, due to the short time span considered.

The data can be downloaded by choosing each year/month and felony type (robbery or theft) and clicking on "Exportar" at the lower right. A .xls file will be downloaded but **beware**, it is in fact a .csv file! For ease of analysis, the original .csv files were converted to .xls files and are available in this repository as DadosBO*.csv files. Of course, the current analysis could be performed by directly parsing the .csv files.

## Data parsing and geotagging

Parsing

## Data visualization

Visualization
