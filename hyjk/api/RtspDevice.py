from api.ErrorCode import getErrMsgByCode
from api.models import rtsp_info as RTSPDeviceDB
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from api.public import reqbody_verify
from django.db import transaction


@csrf_exempt
@api_view(["post"])
def rtspDeviceInfoAdd(request):
    """
    Rtsp设备信息--新增
    :return:
    """
    try:
        reqBody = json.loads(request.body)
    except Exception as err:
        return Response({"result": 11001001, "msg": getErrMsgByCode(11001001, err)}, content_type="application/json")

    if reqbody_verify(reqBody, err_code=17001001) is None:
        pass
    else:
        return reqbody_verify(reqBody, err_code=17001001)

    if "ip" not in reqBody:
        return Response({"result": 11001006, "msg": getErrMsgByCode(11001006, None)}, content_type="application/json")
    else:
        deviceIp = reqBody["ip"]

    if "name" not in reqBody:
        return Response({"result": 11001007, "msg": getErrMsgByCode(11001007, None)}, content_type="application/json")
    else:
        deviceName = reqBody["name"]

    # if "longitude" not in reqBody:
    #     return Response({"result": 11001008, "msg": getErrMsgByCode(11001008, None)}, content_type="application/json")
    # else:
    #     longitude = reqBody["longitude"]


    # if "latitude" not in reqBody:
    #     return Response({"result": 11001009, "msg": getErrMsgByCode(11001009, None)}, content_type="application/json")
    # else:
    #     latitude = reqBody["latitude"]

    if "address" not in reqBody:
        return Response({"result": 11001010, "msg": getErrMsgByCode(11001010, None)}, content_type="application/json")
    else:
        address = reqBody["address"]

    if "observation_area" not in reqBody:
        return Response({"result": 11001011, "msg": getErrMsgByCode(11001011, None)}, content_type="application/json")
    else:
        observation_area = reqBody["observation_area"]

    if "observation_target" not in reqBody:
        return Response({"result": 11001012, "msg": getErrMsgByCode(11001012, None)}, content_type="application/json")
    else:
        observation_target = reqBody["observation_target"]

    # if "enable" not in reqBody:
    #     return Response({"result": 11001013, "msg": getErrMsgByCode(11001013, None)}, content_type="application/json")
    # else:
    #     enable = reqBody["enable"]
    #
    # if "bin_id" not in reqBody:
    #     return Response({"result": 11001014, "msg": getErrMsgByCode(11001014, None)}, content_type="application/json")
    # else:
    #     bin_id = reqBody["bin_id"]
    longitude=None
    latitude=None
    bin_id=None
    tide_level_name=None
    tide_level_code =None
    wave_heigh_name=None
    wave_heigh_code=None
    wave_direction_name=None
    wave_direction_code=None
    port=None

    if "tide_level_name" in reqBody:
        tide_level_name = reqBody["tide_level_name"]

    if "tide_level_code" in reqBody:
        tide_level_code = reqBody["tide_level_code"]

    if "wave_heigh_name" in reqBody:
        wave_heigh_name = reqBody["wave_heigh_name"]

    if "wave_heigh_code" in reqBody:
        wave_heigh_code = reqBody["wave_heigh_code"]

    if "wave_direction_name" in reqBody:
        wave_direction_name = reqBody["wave_direction_name"]

    if "wave_direction_code" in reqBody:
        wave_direction_code = reqBody["wave_direction_code"]

    if "port" in reqBody:
        port = reqBody["port"]

    if "longitude" in reqBody:
        longitude = reqBody["longitude"]

    if "latitude" in reqBody:
        latitude = reqBody["latitude"]

    if "bin_id" in reqBody:
        bin_id = reqBody["bin_id"]

    deviceObj = RTSPDeviceDB()
    deviceObj.ip=deviceIp
    deviceObj.name=deviceName
    deviceObj.address=address
    deviceObj.observation_area=observation_area
    deviceObj.observation_target=observation_target

    if longitude:
        deviceObj.longitude = longitude
    if latitude:
        deviceObj.latitude = latitude
    if bin_id:
        deviceObj.bin_id=bin_id
    if tide_level_name:
        deviceObj.tide_level_name=tide_level_name
    if tide_level_code:
        deviceObj.tide_level_code=tide_level_code
    if wave_heigh_name:
        deviceObj.wave_heigh_name=wave_heigh_name
    if wave_heigh_code:
        deviceObj.wave_heigh_code=wave_heigh_code
    if wave_direction_name:
        deviceObj.wave_direction_name=wave_direction_name
    if wave_direction_code:
        deviceObj.wave_direction_code=wave_direction_code
    if port:
        deviceObj.port=port

    try:
        deviceObj.save()

    except Exception as err:
        Response({"result": 11001015, "msg": getErrMsgByCode(11001015, err)}, content_type="application/json")

    return Response({"result": 0, "msg": "OK"}, content_type="application/json")


@csrf_exempt
@api_view(["post"])
def rtspDeviceInfoModify(request):
    """
    Rtsp设备信息--修改
    :return:
    """
    try:
        reqBody = json.loads(request.body)
    except Exception as err:
        return Response({"result": 11002001, "msg": getErrMsgByCode(11002001, err)}, content_type="application/json")

    if reqbody_verify(reqBody, err_code=17002001) is None:
        pass
    else:
        return reqbody_verify(reqBody, err_code=17002001)

    if "id" not in reqBody:
        return Response({"result": 11002006, "msg": getErrMsgByCode(11002006, None)}, content_type="application/json")
    else:
        deviceID = reqBody["id"]

    deviceName = None
    deviceIP = None
    longitude=None
    latitude=None
    address=None
    observation_area=None
    observation_target=None
    # enable=None
    bin_id=None
    tide_level_name=None
    tide_level_code=None
    wave_heigh_name=None
    wave_heigh_code=None
    wave_direction_name=None
    wave_direction_code=None
    Port=None


    if "name" in reqBody:
        deviceName = reqBody["name"]

    if "ip" in reqBody:
        deviceIP = reqBody["ip"]

    if "longitude" in reqBody:
        longitude = reqBody["longitude"]

    if "latitude" in reqBody:
        latitude = reqBody["latitude"]

    if "address" in reqBody:
        address = reqBody["address"]

    if "observation_area" in reqBody:
        observation_area = reqBody["observation_area"]

    if "observation_target" in reqBody:
        observation_target = reqBody["observation_target"]

    # if "enable" in reqBody:
    #     enable = reqBody["enable"]

    if "bin_id" in reqBody:
        bin_id = reqBody["bin_id"]

    if "tide_level_name" in reqBody:
        tide_level_name = reqBody["tide_level_name"]

    if "tide_level_code" in reqBody:
        tide_level_code = reqBody["tide_level_code"]

    if "wave_heigh_name" in reqBody:
        wave_heigh_name = reqBody["wave_heigh_name"]

    if "wave_heigh_code" in reqBody:
        wave_heigh_code = reqBody["wave_heigh_code"]

    if "wave_direction_name" in reqBody:
        wave_direction_name = reqBody["wave_direction_name"]

    if "wave_direction_code" in reqBody:
        wave_direction_code = reqBody["wave_direction_code"]

    if "port" in reqBody:
        Port = reqBody["port"]

    try:
        deviceObj = RTSPDeviceDB.objects.get(id=deviceID)
    except Exception as err:
        return Response({"result": 11002007, "msg": getErrMsgByCode(11002007, err)}, content_type="application/json")

    if deviceName is not None:
        deviceObj.name = deviceName

    if deviceIP is not None:
        deviceObj.ip = deviceIP


    if longitude is not None:
        deviceObj.longitude = longitude

    if latitude is not None:
        deviceObj.latitude = latitude

    if address is not None:
        deviceObj.address = address

    if observation_area is not None:
        deviceObj.observation_area = observation_area

    if observation_target is not None:
        deviceObj.observation_target = observation_target

    # if enable is not None:
    #     deviceObj.enable = enable

    if bin_id is not None:
        deviceObj.bin_id = bin_id

    if tide_level_name is not None:
        deviceObj.tide_level_name = tide_level_name

    if tide_level_code is not None:
        deviceObj.tide_level_code = tide_level_code

    if wave_heigh_name is not None:
        deviceObj.wave_heigh_name = wave_heigh_name

    if wave_heigh_code is not None:
        deviceObj.wave_heigh_code = wave_heigh_code

    if wave_direction_name is not None:
        deviceObj.wave_direction_name = wave_direction_name

    if wave_direction_code is not None:
        deviceObj.wave_direction_code = wave_direction_code

    if Port is not None:
        deviceObj.port = Port


    try:
        deviceObj.save()
    except Exception as err:
        return Response({"result": 11002008, "msg": getErrMsgByCode(11002008, err)}, content_type="application/json")

    return Response({"result": 0, "msg": "OK"}, content_type="application/json")

@csrf_exempt
@api_view(["post"])
def rtspDeviceInfoQueryAll(request):
    """
    Rtsp设备信息--全部
    :return:
    """
    print(format(request.body))
    try:
        reqBody = json.loads(request.body)
    except Exception as err:
        return Response({"result": 11003001, "msg": getErrMsgByCode(11003001, err)}, content_type="application/json")

    if reqbody_verify(reqBody, err_code=11003001) is None:
        pass
    else:
        return reqbody_verify(reqBody, err_code=17003001)


    indexPage = None
    countInfo = None
    Type=None
    if "page" in reqBody:
        indexPage = reqBody["page"]

    if "count" in reqBody:
        countInfo = reqBody["count"]

    if "type" in reqBody:
        Type=reqBody["type"]


    resData = {}

    try:
        if Type:
            if Type==0:
                rtspDeviceObjs = RTSPDeviceDB.objects.filter(bin_id_isnull=True)
            else:
                rtspDeviceObjs = RTSPDeviceDB.objects.filter(bin_id_isnull=False)
        else:
            rtspDeviceObjs = RTSPDeviceDB.objects.all()

        resultObjList = rtspDeviceObjs
        resultInfoList = []

        for item in resultObjList:
            deviceObj = {}

            deviceObj["id"] = item.id
            deviceObj["ip"] = item.ip
            deviceObj["name"] = item.name
            deviceObj["longitude"] = item.longitude
            deviceObj["latitude"] = item.latitude
            deviceObj["address"] = item.address
            deviceObj["observation_area"] = item.observation_area
            deviceObj["observation_target"] = item.observation_target
            deviceObj["bin_id"] = item.bin_id
            deviceObj["tide_level_name"] = item.tide_level_name
            deviceObj["tide_level_code"]=item.tide_level_code
            deviceObj["wave_heigh_name"]=item.wave_heigh_name
            deviceObj["wave_heigh_code"]=item.wave_heigh_code
            deviceObj["wave_direction_name"]=item.wave_direction_name
            deviceObj["wave_direction_code"]=item.wave_direction_code
            deviceObj["port"]=item.port

            resultInfoList.append(deviceObj)

        if indexPage and countInfo:
            indexStart = (indexPage - 1) * countInfo

            if indexStart < 0:
                indexStart = 0

            indexEnd = indexStart + countInfo

            if indexEnd >= rtspDeviceObjs.count():
                indexEnd = rtspDeviceObjs.count()

            resultInfoList = resultInfoList[indexStart:indexEnd]
        else:
            resultInfoList = resultInfoList

        resData["info"] = resultInfoList
    except Exception as err:
        return Response({"result": 11003006, "msg": getErrMsgByCode(11003006, err)}, content_type="application/json")

    resData["total"] = resultObjList.count()

    return Response({"result": 0, "msg": "OK", "data": resData}, content_type="application/json")


@csrf_exempt
@api_view(["post"])
def rtspDeviceInfoDelete(request):
    """
    Rtsp信息--删除
    :return:
    """
    try:
        reqBody = json.loads(request.body)
    except Exception as err:
        return Response({"result": 11004001, "msg": getErrMsgByCode(11004001, err)}, content_type="application/json")

    if reqbody_verify(reqBody, err_code=17005001) is None:
        pass
    else:
        return reqbody_verify(reqBody, err_code=17005001)

    if "id" not in reqBody:
        return Response({"result": 11004006, "msg": getErrMsgByCode(11004006, None)}, content_type="application/json")
    else:
        deviceID = reqBody["id"]

    try:
        deviceObj = RTSPDeviceDB.objects.get(id=deviceID)
    except Exception as err:
        return Response({"result": 11004007, "msg": getErrMsgByCode(11004007, err)}, content_type="application/json")

    try:
        deviceObj.delete()
    except Exception as err:
        return Response({"result": 11004008, "msg": getErrMsgByCode(11004008, err)}, content_type="application/json")

    return Response({"result": 0, "msg": "OK"}, content_type="application/json")


@csrf_exempt
@api_view(["post"])
def rtspDeviceInfoBatchAdd(request):
    """
    Rtsp设备信息--批量新增
    :return:
    """
    try:
        reqBodys = json.loads(request.body)
    except Exception as err:
        return Response({"result": 11001001, "msg": getErrMsgByCode(11001001, err)}, content_type="application/json")

    if reqbody_verify(reqBodys, err_code=17001001) is None:
        pass
    else:
        return reqbody_verify(reqBodys, err_code=17001001)

    if "infoList" not in reqBodys:
        return Response({"result": 11001016, "msg": getErrMsgByCode(11001016, None)}, content_type="application/json")
    else:
        infoList = reqBodys["infoList"]

    for reqBody in infoList:

        if "ip" not in reqBody:
            return Response({"result": 11001006, "msg": getErrMsgByCode(11001006, None)}, content_type="application/json")
        else:
            deviceIp = reqBody["ip"]

        if "name" not in reqBody:
            return Response({"result": 11001007, "msg": getErrMsgByCode(11001007, None)}, content_type="application/json")
        else:
            deviceName = reqBody["name"]

        if "address" not in reqBody:
            return Response({"result": 11001010, "msg": getErrMsgByCode(11001010, None)}, content_type="application/json")
        else:
            address = reqBody["address"]

        if "observation_area" not in reqBody:
            return Response({"result": 11001011, "msg": getErrMsgByCode(11001011, None)}, content_type="application/json")
        else:
            observation_area = reqBody["observation_area"]

        if "observation_target" not in reqBody:
            return Response({"result": 11001012, "msg": getErrMsgByCode(11001012, None)}, content_type="application/json")
        else:
            observation_target = reqBody["observation_target"]

        longitude=None
        latitude=None
        bin_id=None
        tide_level_name=None
        tide_level_code =None
        wave_heigh_name=None
        wave_heigh_code=None
        wave_direction_name=None
        wave_direction_code=None
        port=None

        if "tide_level_name" in reqBody:
            tide_level_name = reqBody["tide_level_name"]

        if "tide_level_code" in reqBody:
            tide_level_code = reqBody["tide_level_code"]

        if "wave_heigh_name" in reqBody:
            wave_heigh_name = reqBody["wave_heigh_name"]

        if "wave_heigh_code" in reqBody:
            wave_heigh_code = reqBody["wave_heigh_code"]

        if "wave_direction_name" in reqBody:
            wave_direction_name = reqBody["wave_direction_name"]

        if "wave_direction_code" in reqBody:
            wave_direction_code = reqBody["wave_direction_code"]

        if "port" in reqBody:
            port = reqBody["port"]

        if "longitude" in reqBody:
            longitude = reqBody["longitude"]

        if "latitude" in reqBody:
            latitude = reqBody["latitude"]

        if "bin_id" in reqBody:
            bin_id = reqBody["bin_id"]
        savePoint = transaction.savepoint()
        try:
            deviceObj = RTSPDeviceDB()
            deviceObj.ip=deviceIp
            deviceObj.name=deviceName
            deviceObj.address=address
            deviceObj.observation_area=observation_area
            deviceObj.observation_target=observation_target

            if longitude:
                deviceObj.longitude = longitude
            if latitude:
                deviceObj.latitude = latitude
            if bin_id:
                deviceObj.bin_id=bin_id
            if tide_level_name:
                deviceObj.tide_level_name=tide_level_name
            if tide_level_code:
                deviceObj.tide_level_code=tide_level_code
            if wave_heigh_name:
                deviceObj.wave_heigh_name=wave_heigh_name
            if wave_heigh_code:
                deviceObj.wave_heigh_code=wave_heigh_code
            if wave_direction_name:
                deviceObj.wave_direction_name=wave_direction_name
            if wave_direction_code:
                deviceObj.wave_direction_code=wave_direction_code
            if port:
                deviceObj.port=port
            deviceObj.save()

        except Exception as err:
            transaction.savepoint_rollback(savePoint)
            Response({"result": 11001015, "msg": getErrMsgByCode(11001015, err)}, content_type="application/json")

        transaction.savepoint_commit(savePoint)

    return Response({"result": 0, "msg": "OK"}, content_type="application/json")
