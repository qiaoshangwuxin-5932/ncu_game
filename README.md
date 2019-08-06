<<<<<<< HEAD
# ncu_game
# 推介
# 游戏
#用户提交
## URL : user/
## method : POST
## 接收数据格式 :  json
   +
            {
                "username":"username"
            }
<<<<<<< HEAD
       
## 返回数据 :

   + success:
        
            {
                'success':True,
                'status':1
            }                    
        
   + deft:
        
=======
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
>>>>>>> 49ab43c80a137b1a2c8025017237d427e6f6e082
            {
                "status":0,
                "success":False,
                "message":'用户已重复，请更换注册名字'
             }
        
---
#获取问题
## URL : choise/
##method : POST
## 须接收数据 : json
   +  
            {
                "groups":"产品组"
            }
## 返回数据 :
   +  
            {
                "0": {
                    "status": 1,
                    "question": 1,
                    "data": {
                        "id": 6,
                        "data": {
                            "question": "产品们都有着共同的酸甜苦辣，产品最喜欢说的一句话可能是？",
                            "A": "实现这个不难的",
                            "B": "给个排期吧",
                            "C": "这个功能要不砍了吧？"
                        }
                    }
                },
                "1": {
                    "status": 1,
                    "question": 2,
                    "data": {
                        "id": 7,
                        "data": {
                            "question": "你突然想到了关于新产品的绝妙想法，你该用什么方式清楚地向研发表述你的idea？",
                            "A": "给他你的手绘原型图",
                            "B": "用你的高超口才叙述",
                            "C": "用AXURE出好原型图"
                        }
                    }
                },
                "2": {
                    "status": 1,
                    "question": 3,
                    "data": {
                        "id": 8,
                        "data": {
                            "question": "一个成熟的产品，和研发在新产品上有了矛盾时，很有可能采取什么手段？",
                            "A": "扮演舔狗",
                            "B": "激情辩论",
                            "C": "冷处理"
                        }
                    }
                },
                "3": {
                    "status": 1,
                    "question": 4,
                    "data": {
                        "id": 9,
                        "data": {
                            "question": "以下哪项不是产品需要做的事？",
                            "A": "需求分析",
                            "B": "用户调研、",
                            "C": "UI设计"
                        }
                    }
                },
                "4": {
                    "status": 1,
                    "question": 5,
                    "data": {
                        "id": 10,
                        "data": {
                            "question": "你认为一个起步阶段的产品经理最需要看？",
                            "A": "通识读本",
                            "B": "摄影画册",
                            "C": "专业入门书籍"
                        }
                    }
                }
            }

---

#返回图片
## URL : image/
## method : POST
## 需接收数据 : json
   +    
            {
	            "username":"我最帅" 这真的只是个例子
            }
## 返回数据 :
   + 50 - 65
                
            50-65.png
   + 65 - 70
   
            65-70.png       
   + 70 - 85
   
            70-80.png
   + 85 - 100
   
            85-100.png
---           
# 提交分数
## URL : score/
## method : POST
## 需接受数据 : json
   + 
   
            {
                "username":"我最帅",
                "groups":"研发组",
                "question":"程序员们的头发数量可能截然不同，但说的话却常相似。研发最喜欢说的一句话可能是?",
                "answer":"C"
            }
##  返回数据 :
   +        
   
            {
                "status":1,
                "success":True
            }
---

# 九宫格
## URL : nine/
## method : POST
## 需接收数据  : json
   +        
   
            [1,2,3,4,5,6,7,8,9]
## 返回数据 :
   + success
            
            ?
   + deft 
   
            {
                'status':0,
                'success':False,
                'message':'你的拼图有错误哦'
            },
   
  ----    
   
=======
>>>>>>> c342f4e7a8a56a1171e54a331aa131410abb0f74

