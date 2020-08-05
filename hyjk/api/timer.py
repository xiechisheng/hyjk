
def timing():


    from api.models import rtsp_info as RTSPDeviceDB
    import binascii
    import re
    import socket
    import json
    import requests
    from datetime import datetime,timedelta
    rtspDeviceObjs=RTSPDeviceDB.objects.all()
    for item in rtspDeviceObjs:
        bin_id=item.bin_id
        # print("开始")
        # print(bin_id)
        registerData = {"accesskeyid": "chinaunicomocean", "accesskeysecret": "C511268A3237BA9C4418BF89F3CF12EB",
                        "cameraIndex": bin_id}

        response = requests.get(url="http://192.168.1.220:11082/api/camera/sensor/realtime", params=registerData)

        resultData = json.loads(response.text)

        new_s = ""

        # print(resultData)
        data_dick = resultData["data"][0]
        strlist = []
        n_time = datetime.now()+timedelta(hours=+8)

        if ("significantwaveheight" or "dominantwavedirection" or "tide") in data_dick.keys():


            # str1 = data_dick["stationName"]
            str1 =item.name
            dick1 = {"str": str1, "value": "01"}
            strlist.append(dick1)
            if "tide" in data_dick.keys():
                befor_time = n_time + timedelta(minutes=-20)
                detester=data_dick["tideacquisitiontime"]
                date = datetime.strptime(detester, '%Y-%m-%d %H:%M:%S')
                # print(befor_time)
                # print(date)
                if date<befor_time:

                    str2 = "潮位：__"
                    dick2 = {"str": str2, "value": "03"}
                    strlist.append(dick2)
                else:

                    try:
                        str2 = "潮位：%.2fcm"%data_dick["tide"]
                        dick2 = {"str": str2, "value": "03"}
                        strlist.append(dick2)
                    except Exception as e:
                        print(e)

            if "significantwaveheight" in data_dick.keys():
                befor_time = n_time + timedelta(hours=-2)
                detester = data_dick["waveacquisitiontime"]
                date = datetime.strptime(detester, '%Y-%m-%d %H:%M:%S')

                if date < befor_time:

                    str3 = "浪高：__"
                    dick3 = {"str": str3, "value": "04"}

                    strlist.append(dick3)
                else:

                    str3 = "浪高：%.2fm"%data_dick["significantwaveheight"]
                    dick3 = {"str": str3, "value": "04"}

                    strlist.append(dick3)

            if "dominantwavedirection" in data_dick.keys():
                befor_time = n_time + timedelta(hours=-2)
                detester = data_dick["waveacquisitiontime"]
                date = datetime.strptime(detester, '%Y-%m-%d %H:%M:%S')

                if date < befor_time:
                    str4 = "浪向：__"
                    dick4 = {"str": str4, "value": "05"}
                    strlist.append(dick4)
                else:
                    str4 = "浪向：%.2f°"%data_dick["dominantwavedirection"]
                    dick4 = {"str": str4, "value": "05"}
                    strlist.append(dick4)
            str5 = "深圳市规划和自然资源局"
            dick5 = {"str": str5, "value": "06"}
            strlist.append(dick5)

            str6 = "深圳市海洋监测预报中心"
            dick6 = {"str": str6, "value": "07"}
            strlist.append(dick6)

            # print(strlist)

            for str in strlist:
                changdu = int(len(binascii.b2a_hex(str["str"].encode("utf8"))) / 2 + 1)

                if changdu < 16:
                    changdu = "0" + hex(changdu)[-1:]
                else:
                    changdu = hex(changdu)[-2:]
                # print(changdu)
                # print(type(changdu))

                s = binascii.b2a_hex(str["str"].encode("utf8")).decode()
                # print(s)

                s = "ff" + changdu + str["value"] + s + "00"
                s = s + hex(sum([int(i, 16) for i in re.findall(r'.{2}', s) if i != '']))[-2:]
                new_s += s
                # print(s)

            new_s = new_s + "ff00ff"
            # print(new_s)

        else:
            # str1 = data_dick["stationName"]
            str1 =item.name
            dick1 = {"str": str1, "value": "01"}
            strlist.append(dick1)

            str5 = "深圳市规划和自然资源局"
            dick5 = {"str": str5, "value": "06"}
            strlist.append(dick5)

            str6 = "深圳市海洋监测预报中心"
            dick6 = {"str": str6, "value": "07"}
            strlist.append(dick6)
            # print(strlist)
            for str in strlist:
                changdu = int(len(binascii.b2a_hex(str["str"].encode("utf8"))) / 2 + 1)

                if changdu < 16:
                    changdu = "0" + hex(changdu)[-1:]
                else:
                    changdu = hex(changdu)[-2:]
                # print(changdu)
                # print(type(changdu))

                s = binascii.b2a_hex(str["str"].encode("utf8")).decode()
                # print(s)

                s = "ff" + changdu + str["value"] + s + "00"
                s = s + hex(sum([int(i, 16) for i in re.findall(r'.{2}', s) if i != '']))[-2:]
                new_s += s
                # print(s)

            new_s = new_s + "ff00ff"
            # print(new_s)

        try:
            udp_soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建套接字

            local_address = ('', 9999)

            udp_soc.bind(local_address)  # 绑定端口

            str = binascii.a2b_hex(new_s)
            # print(item.ip)

            udp_soc.sendto(str, (item.ip, 1026))  # 发送数据，包含对方IP和port

            udp_soc.close()
            # print("结束")
        except Exception as err:
            print(err)



