import json
class IDS:
    __ids__ = json.loads(open("id.json").read())
    def __init__(self):
        pass
    def getID(self,string:str) -> int:
        for idCity in self.__ids__:
            name = idCity.get("name")
            id = idCity.get("id")
            if name == string:
                return id
    def getCoupleID(self,fromCity:str,toCity:str) -> list:
        listCity = []
        for idCity in self.__ids__:
            name = idCity.get("name")
            id = idCity.get("id")
            if name == fromCity:
                listCity.append("from")
                listCity.append(id)
            elif name == toCity:
                listCity.append("to")
                listCity.append(id)
        return listCity
