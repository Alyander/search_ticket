import logic.tracker
import datetime
from datetime import timedelta,datetime 
tracker = logic.tracker.Tracker()
startDate = "DATASTART"
endDate = "DATEEND"
start_object = datetime.strptime(startDate, "%Y-%m-%d")
end_object = datetime.strptime(endDate, "%Y-%m-%d")
currentD = start_object
listDict = []
while currentD <= end_object:
    proizd_ua_and_booking_uz=datetime.strftime(currentD, "%Y-%m-%d")
    tickets_ua = datetime.strftime(currentD, "%d.%m.%Y")
    listDict.append({"url":f"URL", 
    "class":"CLASS",
    "args":"id OR class name"
    })
    currentD += timedelta(days=1)
tracker.tracking(listDict,0,0,0)