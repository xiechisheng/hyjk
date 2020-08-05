import logging as log_obj
logger = log_obj.getLogger("hyjk")


ErrorCodeMsg = {
                # 用户登录
                "10000001": "Post信息解析失败",
                "10000002": "缺少参数: login",
                "10000003": "缺少参数: password",
                "10000004": "账号未注册",
                "10000005": "账号和密码不一致",
                "10000006": "账号被禁用",
                "10000007": "无法生成Token信息",
                # 用户登出
                "10001001": "Post信息解析失败",
                "10001002": "缺少参数: login",
                "10001003": "缺少参数: token",
                "10001004": "Token信息解析失败",
                "10001005": "账号未登录或登录超时",
                "10001006": "Token信息删除失败",
                # 新增用户信息
                "10002006": "缺少参数: login",
                "10002007": "账号已被注册",
                "10002008": "缺少参数: password",
                "10002009": "缺少参数: nickname",
                "10002010": "缺少参数: enable",
                "10002011": "用户信息存储失败",
                # 修改用户信息
                "10003005": "缺少参数: id",
                "10003006": "账号不存在",
                "10003007": "用户信息更新失败",
                # 查询用户信息
                "10004006":"用户信息查询失败",
                # 删除用户信息
                "10005005": "缺少参数: id",
                "10005006": "用户信息不存在",
                "10005007": "不允许删除Admin账号",
                "10005008": "用户信息删除失败",

                #新增rtsp设备信息
                "11001006": "缺少参数: ip",
                "11001007": "缺少参数: name",
                "11001008": "缺少参数: longitude",
                "11001009": "缺少参数: latitude",
                "11001010": "缺少参数: address",
                "11001011": "缺少参数: observation_area",
                "11001012": "缺少参数: observation_target",
                "11001013": "缺少参数: enable",
                "11001014": "缺少参数: bin_id",
                "11001015": "rtsp设备新增失败",
                # 修改Rtsp设备信息
                "11002006": "缺少参数: id",
                "11002007": "Rtsp设备信息不存在",
                "11002008": "Rtsp设备信息更新失败",
                # 查询Rtsp设备信息
                "11003006": "Rtsp设备信息查询失败",
                # 删除Rtsp设备信息
                "11004006": "缺少参数: id",
                "11004007": "Rtsp设备信息不存在",
                "11004008": "Rtsp设备信息删除失败",
}


def getErrMsgByCode(err_code, err_obj):
    """
    错误码--获取
    :return:
    """
    str_err_code = str(err_code)

    if err_obj is None:
        err_msg = ErrorCodeMsg[str_err_code]
    else:
        if int(str_err_code[7]) == 1:
            err_msg = "Post信息解析失败" + "<" + format(err_obj) + ">"
        else:
            err_msg = ErrorCodeMsg[str_err_code] + "<" + format(err_obj) + ">"

    logger.error(err_msg)

    return err_msg

