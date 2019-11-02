"""This software allows to insert clusters' points with specific location (longitude,latitude) from  csv file
into a DB. In this case these points belong to unsupervised analysis.
From DB this data will be available to web app MediStormSeeker into leaflet map"""

from myFunction import *
import pandas as pd
import glob
import os
import datetime
import numpy as np
from webcolors import rgb_to_hex
import sys

#insert your path where there are your csv files
src = "<insert your path>"

def main():
    try:
        os.chdir(src)
    except Exception as e:
        print("Error: there is no local folder", str(e))
        sys.exit(1)
    count = 0
    #value --> on/off step 1
    #value1 --> on/off step2
    value =  True
    value1 = True
    """STEP 1: Each csv file will be analyzed: every point (lon,lat) will be transformed in geojson and the it will be added
    to the DB"""
    if value:
        for filename in glob.glob('*.csv'):
            print(filename)
            try:
                df = pd.read_csv(filename, header=None)
            except Exception as e:
                print("Error: there is no a csv file", str(e))
                sys.exit(1)
            for index, row in df.iterrows():
                check1 = int(row[2])
                if check1 != 0:
                    #inserisce i geojson nel DB

                    filename1 = filename[15:]
                    pre, ext = os.path.splitext(filename1)
                    #print(pre,ext)
                    date1 = datetime.datetime(int(pre[0:4]), int(pre[4:6]), int(pre[6:8]), int(pre[9:11]))
                    #print(date1)
                    pointClusterGeoJson = {
                        "type": "Feature",
                        "properties": {
                            "classCluster": int(row[2]),
                            "dateStr": date1,
                        },
                        "geometry": {
                            "type": "Point",
                            "coordinates": [row[1], row[0]]
                        }
                    }

                    mytool.insertPointCluster(pointClusterGeoJson)
                    count += 1
                    print("{} ) lat:{} | lgn: {} | class: {}".format(count, row[0], row[1], row[2]))
                    print("---------------------------------------")

    #STEP 2
    if value1:
        """STEP 2: it will be created a tuple that assign to each cluster a specific color"""
        print("")
        cursorClassCluster = mytool.groupByClassCluster()
        for record in cursorClassCluster:

            print(record["_id"])
            classCluster = record["_id"]
            colorRGB = list(np.random.choice(range(256), size=3))
            print(colorRGB)
            colorHEX = str(rgb_to_hex((colorRGB[0], colorRGB[1], colorRGB[2])))
            print(colorHEX)
            mytool.insertClassClusterDB(classCluster,colorHEX)
            print("---------------------------")

if __name__ == "__main__":
    main()

