import requests as r; import json as j

# 在这里填写你的Token
t = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOnsiZ3JhbnRUeXBlIjoiIiwic2NvcGUiOiIifSwiYXVkIjp7Im93bmVyIjp7ImFwcElkIjoieG13ODA2NjUzMjI0MTA1MCIsInVjSWQiOjMzNjk1NTIsImFjY291bnQiOiIxOTE1OTEwODMyOSJ9LCJ2aXNpdG9yIjoiLnhpYW9tYXdhbmcuY29tIn0sImV4cCI6MTcyNDc2MDg4M30.a3IdtbjQzRtG16QY3lLQtrcxyMfQTMgPWAmcUeGr9gY"

def a(u, v=None, w=None, x='GET', y=None):
    try:
        if x == 'OPTIONS':
            z = r.options(u, params=v, headers=w)
        elif x == 'POST':
            z = r.post(u, json=y, headers=w)
        else:  # 默认是 'GET'
            z = r.get(u, params=v, headers=w)
        z.raise_for_status()
        
        return z
    except r.RequestException as B:
        print(f"请求失败: {B}")
        return None

def C():
    D = "https://community-api.xiaomawang.com/api/v1/user/validate-token"
    E = {"token": t}
    F = a(D, v=E)
    if F:
        G = "https://community-api.xiaomawang.com/api/v1/message/get-unread"
        H = a(G)
        if H:
            I = "https://community-api.xiaomawang.com/api/v1/report/get-comment-list"
            J = {"page": 1, "pageSize": 10, "reportStatus": 0}
            K = {"Access-Token": t}
            L = a(I, v=J, w=K)
            if L:
                M = L.json().get("data", {})
                N = M.get("total", 0)
                O = M.get("list", [])
                print(f"总数: {N}")
                for P in O:
                    Q = P.get("userId")
                    R = P.get("targetObject", {}).get("fromUserObject", {}).get("nickname")
                    S = P.get("targetObject", {}).get("content")
                    if Q and R and S:
                        T = f"https://world.xiaomawang.com/w/person/project/all/{Q}"
                        print(f"案件编号: {P['id']}")
                        print(f"\033[34m用户昵称: {R}\033[0m")
                        print(f"\033[31m评论内容: {S}\033[0m")
                        print(f"用户ID: {Q} (超链接: {T})")
                        U = input("是否受理该案件？（输入 '受理' 或 '跳过'）：").strip().lower()
                        if U == '受理':
                            V = P['id']
                            W = f"https://community-api.xiaomawang.com/api/v1/report/get-info?reportId={V}"
                            X = a(W, w={"Access-Token": t}, x='OPTIONS')
                            if X:
                                Y = a(W, w={"Access-Token": t})
                                if Y:
                                    print("\033[32m案件信息请求成功\033[0m")
                                    Z = Y.json().get("data", {})
                                    a1 = Z.get("list", [{}])[0]
                                    a2 = a1.get("id")
                                    a3 = a1.get("reportUserId")
                                    a4 = a1.get("createTimeFormat")
                                    a5 = a1.get("reasonName")
                                    a6 = a1.get("checkerName")
                                    print(f"案件编号: {P['id']}")
                                    print(f"\033[31m被举报用户ID:{Q}\033[0m")
                                    print(f"举报时间: {a4}")
                                    print(f"\033[31m举报内容: {Z.get('list', [{}])[0].get('content', '未提供')}\033[0m")
                                    print(f"\033[31m举报类型: {a5}\033[0m")
                                    if 'com' in S:
                                        print("\033[33m请注意:评论内容可能含有广告链接！\033[0m")
                                    if '该评论违反了社区守则' in S or '[小码王' in S or '''\n''' in S:
                                        print("\033[33m请注意:评论内容可能为刷屏或无意义内容\033[0m")
                                    print(f"审核员: {a6}")
                                    print(f"评论内容: {S}")
                                    a7 = input("请选择处理结果（正常显示：1，替换：2，删除：3）：").strip()
                                    a8 = input("请输入受理备注：").strip()
                                    a9 = input("请输入举报人站内信内容：").strip()
                                    a0 = input("请输入被举报人站内信内容：").strip()
                                    b1 = "https://community-api.xiaomawang.com/api/v1/report/verify-comment"
                                    b2 = {"reportId": P['id'], "reporterIsSend": 1, "userIsSend": 1, "reportDetailIds": [a1['id']], "action": int(a7), "remark": a8, "reporterMessage": f"感谢您对社区内容的正义维护，您的举报已受理。{a9}", "userMessage": f"您的评论存在违规内容，该评论及子回复已被系统管理员删除。{a0}"}
                                    b3 = a(b1, w={"Access-Token": t}, x='POST', y=b2)
                                    if b3:
                                        print("案件处理成功")
                                        print("服务器响应:", b3.json())
                                    else:
                                        print("案件处理失败")
                                else:
                                    print("获取案件信息失败")
                            else:
                                print("OPTIONS 请求失败")
                        else:
                            print(f"案件 {P['id']} 已跳过")
                        print()
            else:
                print("第三个请求失败")
        else:
            print("第二个请求失败")
    else:
        print("第一个请求失败")

if __name__ == "__main__":
    C()
