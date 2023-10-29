class Fact:
    def __init__(self, name, knowledge, time_complexity):
        self.name = name
        self.knowledge = knowledge
        self.time_complexity = time_complexity

def learn(fact, recommendation):
    # 更新 knowledge 和 time_complexity
    fact.knowledge += recommendation
    fact.time_complexity *= fact.knowledge
    
    

def check_limit(fact):
    # 检查是否超过“限度”
    return fact.knowledge > fact.time_complexity 

def recommendation(fact):
    # 计算推荐值
    return 0.5 * fact.knowledge

def main():
    b = 0
    facts = [Fact("学习", 0.5, 1), Fact("阅读", 0.4, b), Fact("运动", 0.8, b), Fact("娱乐", 0.5, b)]
    print("初始状态:")
    user = Person("张三")
    print(user.knowledge_limit)
    count = 0
    for i in facts:
        learn(i, recommendation(i))
        b = i.time_complexity
        if check_limit(i):
            for j in facts:
                if j.knowledge > user.knowledge_limit:
                    user.ptry(j)#进行自主学习
                    break
            print(f"第{count+1}次学习后,产生矛盾:")
            print(i.name, i.knowledge, i.time_complexity)
            break
        else:
            user.learn(i)
            print(f"第{count+1}次学习后:")
            print(i.name, i.knowledge, i.time_complexity, b)
        count += 1

class Person:
   def __init__(self, name):
       self.name = name
       self.knowledge_limit = 0.5  # 限度的初始值
       self.facts = []

    
   def add_fact(self, fact):
       self.facts.append(fact)
       
   def learn(self, fact):
       # 计算新的知识水平
       new_knowledge = (self.knowledge_limit + fact.knowledge - 0.5) / 2
       n = 2 #level
       if ((fact.knowledge - 0.5) + self.knowledge_limit)/n >= self.knowledge_limit:
            self.knowledge_limit = self.knowledge_limit
       else:
            self.knowledge_limit = new_knowledge
            self.add_fact(fact)
       
   
   #人尝试性学习，自己产生矛盾
   def ptry(self, fact):
       self.facts.append(fact)
       self.knowledge_limit = (self.knowledge_limit + fact.knowledge) / 2
       print(f"{self.name}对{fact.name}的认知超过了限度,产生了矛盾!")
       
       
   def dele(self, fact):
       self.facts.remove(fact)




if __name__ == "__main__":
    main()