class Fact:
   def __init__(self, name, knowledge):
       self.name = name
       self.knowledge = knowledge

class Person:
   def __init__(self, name):
       self.name = name
       self.knowledge_limit = 0.5  # 限度的初始值
       self.facts = []

    
   def add_fact(self, fact):
       self.facts.append(fact)
       
   def learn(self, fact):
       # 计算新的知识水平
       new_knowledge = (self.knowledge_limit + fact.knowledge) / 2

       # 如果新的知识水平不超过限度,则更新知识水平
       if new_knowledge <= self.knowledge_limit:
           self.knowledge_limit = new_knowledge
           self.add_fact(fact)
       else:
           # 如果新的知识水平超过限度,则产生矛盾
           print(f"{self.name}对{fact.name}的认知超过了限度,产生了矛盾!")
   
   #人尝试性学习，自己产生矛盾
   def ptry(self, fact):
       if fact.knowledge > self.knowledge_limit:
           self.facts.append(fact)
           self.knowledge_limit = (self.knowledge_limit + fact.knowledge) / 2
           print(f"{self.name}对{fact.name}的认知超过了限度,产生了矛盾!")
       
       
   def dele(self, fact):
       self.facts.remove(fact)

# 创建一个事实对象
fact1 = Fact("社会矛盾", 0.8)
fact2 = Fact("推荐算法", 0.6)
fact3 = Fact("思维定式", 0.4)

# 创建一个用户对象
user1 = Person("张三")
#user1.add_fact(fact1)
#user1.add_fact(fact2)

# 用户学习新的事实
user1.learn(fact3)

#正反馈的推荐算法
n = 2 #正反馈强度
def recommend(user, fact):
    if (fact.knowledge + user.knowledge_limit)/n >= user.knowledge_limit:
        user.knowledge_limit = user.knowledge_limit
    else:
        user.learn(fact)