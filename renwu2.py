admin={"方开":"123","刘晨":"12345"}
user={"张旭":"123321","沈章":"123456","尤赛赛":"123456"}
while True:
    name_=input("请输入用户名(不能以数字开头！)：")
    pass_=input("请输入密码：") 
    if name_  in admin.keys():
        if pass_==admin[name_]:
            print("欢迎您，",name_,"!您的用户组为：管理员")
            break
        else:
            print("密码错误，请重新输入！")
    else : 
        if name_ in user.keys():
            if pass_==user[name_]:
                print("欢迎您，",name_,"!您的用户组为：用户")
                break
            else:
                print("密码错误，请重新输入！")
        else:
            if name_[0] not in ["1","2","3","4","5","6","7","8","9","0"]:
                if pass_=="guest":
                    print("欢迎您，",name_,"!您的用户组为：游客")
                    break
                else:
                    print("密码错误，请重新输入！")
            else:
                print("请输入正确的用户名！")
                    