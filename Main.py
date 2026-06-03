from datetime import datetime

# data-1 (copy from your image)
data1 = {
    "deviceID": "dh28dslkja",
    "deviceType": "LaserCutter",
    "timestamp": 1624445837783,
    "location": "japan/tokyo/keiyō-industrial-zone/daikibo-factory-meiyo/section-1",
    "operationStatus": "healthy",
    "temp": 22
}

# data-2 (copy from your image)
data2 = {
    "device": {
        "id": "dh28dslkja",
        "type": "LaserCutter"
    },
    "timestamp": "2021-06-23T10:57:17.783Z",
    "country": "japan",
    "city": "tokyo",
    "area": "keiyō-industrial-zone",
    "factory": "daikibo-factory-meiyo",
    "section": "section-1",
    "data": {
        "status": "healthy",
        "temperature": 22
    }
}


def convertFromFormat1(jsonObject):
    return jsonObject


def convertFromFormat2(jsonObject):
    result = {}

    result["deviceID"] = jsonObject["device"]["id"]
    result["deviceType"] = jsonObject["device"]["type"]

    iso_time = jsonObject["timestamp"]
    dt = datetime.fromisoformat(iso_time.replace("Z", "+00:00"))
    result["timestamp"] = int(dt.timestamp() * 1000)

    location = [
        jsonObject["country"],
        jsonObject["city"],
        jsonObject["area"],
        jsonObject["factory"],
        jsonObject["section"]
    ]
    result["location"] = "/".join(location)

    result["operationStatus"] = jsonObject["data"]["status"]
    result["temp"] = jsonObject["data"]["temperature"]

    return result


# test run
print(convertFromFormat1(data1))
print(convertFromFormat2(data2))
