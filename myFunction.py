"""This file contains MyTools class that will use a object ManageDB to manage Mongo DB installed into computer"""

from dbMongo import *



class MyTools(object):
    count11 = 1
    def __init__(self):
        """This is a constructor"""
        pass

    def insertPointCluster(self,pointClusterGeoJson):
        """This method allows to insert Point like GeoJSON into DB"""
        try:
            id = managedb.insertPointClusterDB(pointClusterGeoJson)
            print("count insertion DB: {}".format(self.count11))
            self.count11 +=1
        except Exception as e:
            print("exception error DB", str(e))

    def groupByClassCluster(self):
        """This method allows to get clusters's point grouped by class from DB"""
        try:
            cursorClassCluster = managedb.groupByClassClusterDB()
            return cursorClassCluster
        except Exception as e:
            print("exception error DB", str(e))

    def insertClassClusterDB(self,classCluster,colorHEX):
        """This method allows to insert a class cluster into DB"""
        try:
            classClusterRecord = {"classCluster":str(classCluster),"color":colorHEX}
            id = managedb.insertClassClusterDB(classClusterRecord)
            print("id: ",id)
        except Exception as e:
            print("exception error DB", str(e))

mytool = MyTools()


