"""This file contains the ManageDB Class allows to manage DB"""

from pymongo import MongoClient

class ManageDB(object):

    def __init__(self):
        try:
            client = MongoClient("mongodb://localhost:27017/")
            db = client.MediStormSeekerDB
        except Exception as e:
            print("db non pronto " + str(e))
        self.db = db

    def insertPointClusterDB(self,pointClusterGeoJson):
        """This method allows to insert a cluster point as GeoJson in DB"""
        id = self.db.PointClusterCollection.insert(pointClusterGeoJson)
        return id

    def groupByClassClusterDB(self):
        """This method allows to obtain the clusters' points grouped by class from DB"""
        cursorClassCluster = self.db.PointClusterCollection.aggregate([{"$group": {"_id": "$properties.classCluster", "count": {"$sum":1}}}])
        return cursorClassCluster

    def insertClassClusterDB(self,classClusterRecord):
        """This method allows to insert a specific cluster into DB"""
        id= self.db.ClassClusterCollection.insert(classClusterRecord)
        return id

managedb = ManageDB()
