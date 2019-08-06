# ncu_game
## 推介
## 游戏
#用户提交
## URL : user/
###  接收数据格式 :  json
        '''
            {
                "username":"username"
            }
        '''
### 返回数据
#### success:
'''
            {
                'success':True,
                'status':1
            }                     
'''
#### deft:
        '''
            {
                "status":0,
                "success":False,
                "message":'用户已重复，请更换注册名字'
             }
        ’‘'

