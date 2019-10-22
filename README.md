# CSVtoPoint
This software allows to insert clusters' points with specific location (longitude,latitude) from  csv file into a mongoDB. In this case these points belong to unsupervised analysis. From DB this data will be available to web app Weather Labeling Web App into leaflet map.

Configuration:

1. Install Weather Labeling Web App: https://github.com/rosario-riccio/Weather-Labeling-Web-Application. It's necessary to execute all comands of configuration.
2. git clone https://github.com/rosario-riccio/CSVtoPoint.git
3. cd CSVtoPoint
4. virtualenv venv
5. source venv/bin/activate
6. pip install --upgrade pip
7. pip install -r requirements.txt
8. insert your path where there are csv files into variable src in main.py: src = "<insert your path where are csv files>"
9. python main.py
