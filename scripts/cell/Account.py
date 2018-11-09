# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class Account(KBEngine.Entity):
    """
    Account实体的cell部分
    """

    def __init__(self):
        KBEngine.Entity.__init__(self)

    # --------------------------------------------------------------------------------------------
    #                              def中定义的方法
    # --------------------------------------------------------------------------------------------

    # --------------------------------------------------------------------------------------------
    #                              System Callbacks
    # --------------------------------------------------------------------------------------------
    def onTimer(self, id, userArg):
        """
        KBEngine method.
        使用addTimer后， 当时间到达则该接口被调用
        @param id		: addTimer 的返回值ID
        @param userArg	: addTimer 最后一个参数所给入的数据
        """
        DEBUG_MSG(id, userArg)

    def onDestroy(self):
        """
        KBEngine method.
        entity销毁
        """
        DEBUG_MSG("Account::onDestroy: %i." % self.id)
