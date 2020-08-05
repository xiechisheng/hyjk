from api.ErrorCode import getErrMsgByCode
from api.models import user_info as userDB
import json
import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from api.public import reqbody_verify



from api.public import tokenQuery
from django.db import transaction
from api.public import tokenEncode
from api.public import tokenDecode
from api.public import tokenDelete
from api.public import mysql_password




@csrf_exempt
@api_view(["post"])
def userLogin(request):
    """
    用户信息--登录
    :return:
    """
    try:
        reqBody = json.loads(request.body)
    except Exception as err:
        return Response({"result": 10000001, "msg": getErrMsgByCode(10000001, err)}, content_type="application/json")

    if "login" not in reqBody:
        return Response({"result": 10000002, "msg": getErrMsgByCode(10000002, None)}, content_type="application/json")
    else:
        loginName = reqBody["login"]

    if "password" not in reqBody:
        return Response({"result": 10000003, "msg":getErrMsgByCode(10000003, None)}, content_type="application/json")
    else:
        loginPwd = reqBody["password"]

    try:
        userObj = userDB.objects.get(login=loginName)
    except userDB.DoesNotExist:
        return Response({"result": 10000004, "msg": getErrMsgByCode(10000004, None)}, content_type="application/json")

    if userObj.password != mysql_password(loginPwd):
        return Response({"result": 10000005, "msg": getErrMsgByCode(10000005, None)}, content_type="application/json")

    if userObj.enable == 0:
        return Response({"result": 10000006, "msg": getErrMsgByCode(10000007, None)}, content_type="application/json")

    strTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tokenValue = tokenEncode({"id": userObj.id, "login": userObj.login,"time": strTime})
    print(tokenValue)
    if tokenValue is None:
        return Response({"result": 10000007, "msg": getErrMsgByCode(10000007, None)}, content_type="application/json")

    resData = {}

    resData["id"] = userObj.id
    resData["login"] = userObj.login
    resData["nickname"] = userObj.nickname
    resData["enable"] = userObj.enable
    resData["token"] = tokenValue

    return Response({"result": 0, "msg": "OK", "data": resData}, content_type="application/json")

@csrf_exempt
@api_view(["post"])
def userLogout(request):
    """
    用户信息--登出
    :return:
    """
    try:
        reqBody = json.loads(request.body)
    except Exception as err:
        return Response({"result": 10001001, "msg": getErrMsgByCode(10001001, err)}, content_type="application/json")

    if "login" not in reqBody:
        return Response({"result": 10001002, "msg": getErrMsgByCode(10001002, None)}, content_type="application/json")
    else:
        loginName = reqBody["login"]

    if "token" not in reqBody:
        return Response({"result": 10001003, "msg": getErrMsgByCode(10002002, None)}, content_type="application/json")
    else:
        loginToken = reqBody["token"]

    tokenInfo = tokenDecode(loginToken)

    if tokenInfo is None:
        return Response({"result": 10001004, "msg": getErrMsgByCode(10001004, None)}, content_type="application/json")

    tokenCache = tokenQuery(loginName)

    if tokenCache != loginToken:
        return Response({"result": 10001005, "msg": getErrMsgByCode(10001005, None)}, content_type="application/json")

    if tokenDelete(loginName) is False:
        return Response({"result": 10001006, "msg": getErrMsgByCode(10001006, None)}, content_type="application/json")

    return Response({"result": 0, "msg": "OK"}, content_type="application/json")


# @csrf_exempt
@api_view(["post"])
def userInfoAdd(request):
    """
    用户信息--新增
    :return:
    """
    try:
        reqBody = json.loads(request.body)
    except Exception as err:
        return Response({"result": 10002001, "msg": getErrMsgByCode(10002001, err)}, content_type="application/json")

    if reqbody_verify(reqBody, err_code=10002001) is None:
        pass
    else:
        return reqbody_verify(reqBody, err_code=10002001)

    if "login" not in reqBody:
        return Response({"result": 10002006, "msg": getErrMsgByCode(10002006, None)}, content_type="application/json")
    else:
        userLogin = reqBody["login"]

    if userDB.objects.filter(login=userLogin):
        return Response({"result": 10002007, "msg": getErrMsgByCode(10002007, None)}, content_type="application/json")

    if "password" not in reqBody:
        return Response({"result": 10002008, "msg": getErrMsgByCode(10002008, None)}, content_type="application/json")
    else:
        userPwd = reqBody["password"]

    if "nickname" not in reqBody:
        return Response({"result": 10002009, "msg": getErrMsgByCode(10002009, None)}, content_type="application/json")
    else:
        userName = reqBody["nickname"]

    if "enable" not in reqBody:
        return Response({"result": 10002010, "msg": getErrMsgByCode(10002010, None)}, content_type="application/json")
    else:
        userEnable = reqBody["enable"]

    userObj = userDB()

    userObj.login = userLogin
    userObj.password = mysql_password(userPwd)
    userObj.nickname = userName
    userObj.enable = userEnable

    savePoint = transaction.savepoint()

    try:
        userObj.save()
    except Exception as err:
        transaction.savepoint_rollback(savePoint)
        Response({"result": 10002011, "msg":getErrMsgByCode(10002011, None)}, content_type="application/json")

    transaction.savepoint_commit(savePoint)

    return Response({"result": 0, "msg": "OK"}, content_type="application/json")



@csrf_exempt
@api_view(["post"])
def userInfoModify(request):
    """
    用户信息--修改
    :return:
    """
    try:
        reqBody = json.loads(request.body)
    except Exception as err:
        return Response({"result": 10003001, "msg": getErrMsgByCode(10003001, err)}, content_type="application/json")

    if reqbody_verify(reqBody, err_code=10003001) is None:
        pass
    else:
        return reqbody_verify(reqBody, err_code=10003001)

    tokenInfo = tokenDecode(reqBody["token"])

    if "id" not in reqBody:
        return Response({"result": 10003005, "msg": getErrMsgByCode(10003005, None)}, content_type="application/json")
    else:
        userID = reqBody["id"]

    if userDB.objects.filter(id=userID).count() == 0:
        return Response({"result": 10003006, "msg": getErrMsgByCode(10003006, None)}, content_type="application/json")

    userPwd = None
    userName = None
    userEnable = None


    if "password" not in reqBody:
        pass
    else:
        userPwd = reqBody["password"]

    if "nickname" not in reqBody:
        pass
    else:
        userName = reqBody["nickname"]

    if "enable" not in reqBody:
        pass
    else:
        userEnable = reqBody["enable"]


    userObj = userDB.objects.get(id=userID)

    if userPwd is not None:
        userObj.password = mysql_password(userPwd)

    if userName is not None:
        userObj.nickname = userName

    if userEnable is not None:
        userObj.enable = userEnable

    savePoint = transaction.savepoint()

    try:
        userObj.save()
    except Exception as err:
        transaction.savepoint_rollback(savePoint)
        return Response({"result": 10003007, "msg": getErrMsgByCode(10003007, err)}, content_type="application/json")

    transaction.savepoint_commit(savePoint)

    return Response({"result": 0, "msg": "OK"}, content_type="application/json")

@csrf_exempt
@api_view(["post"])
def userInfoQuery(request):
    """
    用户信息--查询
    :return:
    """
    try:
        reqBody = json.loads(request.body)
    except Exception as err:
        return Response({"result": 10004001, "msg": getErrMsgByCode(10004001, err)}, content_type="application/json")

    if reqbody_verify(reqBody, err_code=10004001) is None:
        pass
    else:
        return reqbody_verify(reqBody, err_code=10004001)


    try:
        userObj = userDB.objects.all()
    except Exception as err:
        return Response({"result": 10004006, "msg": getErrMsgByCode(10004006, err)}, content_type="application/json")
    resDataList=[]
    for item in userObj:
        resData = {}
        resData["id"] = item.id
        resData["login"] = item.login
        resData["nickname"] = item.nickname
        resData["enable"] = item.enable
        resDataList.append(resData)

    return Response({"result": 0, "msg": "OK", "data": resDataList}, content_type="application/json")


@csrf_exempt
@api_view(["post"])
def userInfoDelete(request):
    """
    用户信息--删除
    :return:
    """
    try:
        reqBody = json.loads(request.body)
    except Exception as err:
        return Response({"result": 10005001, "msg": getErrMsgByCode(10005001, err)}, content_type="application/json")

    if reqbody_verify(reqBody, err_code=10005001) is None:
        pass
    else:
        return reqbody_verify(reqBody, err_code=10005001)

    if "id" not in reqBody:
        return Response({"result": 10005005, "msg": getErrMsgByCode(10005005, None)}, content_type="application/json")
    else:
        userID = reqBody["id"]

    try:
        userObj = userDB.objects.get(id=userID)
    except Exception as err:
        return Response({"result": 10005006, "msg": getErrMsgByCode(10005007, err)}, content_type="application/json")

    if userObj.login == "admin":
        return Response({"result": 10005007, "msg": getErrMsgByCode(10005008, None)}, content_type="application/json")

    savePoint = transaction.savepoint()

    try:
        userObj.delete()
    except Exception as err:
        transaction.savepoint_rollback(savePoint)
        return Response({"result": 10005008, "msg": getErrMsgByCode(10005009, err)}, content_type="application/json")

    transaction.savepoint_commit(savePoint)
    return Response({"result": 0, "msg": "OK"}, content_type="application/json")
