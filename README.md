# 这个系统叫做faRe，这个系统具体讲述的是一个社会认知系统，是关于人对某个事物或者是事件的认知。

1.社会实际整体是一个矛盾体，而任何一个人对某个事物的认知是不矛盾的，这种情况相当于人对一件事物的了解程度是有限的，这里设置一个量来对量这个“有限的了解程度”，这个量叫做“限度”，只要人对这个事物的认知不超过这个“限度”，人对这个事物的认知就不会产生矛盾，反之，如果人对这个事物的认知超过了一定的“限度”，那么人就会在这个事物的认知上产生矛盾。

2.而使得人对事物的认知保持在一个动态平衡的“限度”里面的主要因素之一就是正反馈的推荐算法，原因是现在人了解事物多数都是在通过互联网来获得对一个事物的认知，而现在的推荐算法又相当发达，具备很强的正反馈特性，人们一旦通过正反馈的推荐算法去提高对一个事物的认知，人们只会提高对这个事物其中部分方面的认知，而这种认知使得人脑形成一般的思维定式，即达到一种相对的无矛盾状态。

3.而一旦人对这个事物的认知超过了“限度”，人对这个事物认知就会产生很大的矛盾，也就触碰到了这个社会的实际整体，也就是点1说到的矛盾体。

#注意V1.0主要用作参考，具体运行是V2.0

# V1.0

Society_R是1.0版本，只是对上面的3点进行了概括，具体的参数是：

knowledge_limit = 0.5  # 限度的初始值

knowledge:知识的值

learn()：学习新知识，更新数据

recommend()：正反馈推荐算法，主要是控制人吸收的知识为小于knowledge_limit，而大于knowledge_limit就不会推荐，使得矛盾不会产生

# V2.0

Society_T增加了时间复杂度，为的是为人增加了一个自我尝试学习的功能，当在默认的正反馈推荐算法下学习某件事物的人经历一段时间后即会触发该功能，也就是强制的学习一个大于当前knowledge_limit的值的知识，从而触发矛盾。

参数：
上面有重复的不再介绍

1.time_complexity：时间复杂度

2.ptry():自我尝试学习功能，突破正反馈的推荐算法，学习大于knowledge_limit的知识，可以通俗理解为了解到事物的另外一面

# 算法启发

当今社会一件事物的信息面太多，我们每个人对同一事物的认知都有不同，每个人很难全面的认知到一件事物，而往往越全面，人的对该事物的认知矛盾就会加深。
本算法简单描述了一下这种现象
