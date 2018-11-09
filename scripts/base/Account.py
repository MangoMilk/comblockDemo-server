# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class Account(KBEngine.Proxy):
    """
    账号实体
    客户端登陆到服务端后，服务端将自动创建这个实体，通过这个实体与客户端进行账户相关交互
    """

    def __init__(self):
        KBEngine.Proxy.__init__(self)

    # --------------------------------------------------------------------------------------------
    #                              def中定义的方法
    # --------------------------------------------------------------------------------------------
    def createCell(self, sceneCell):
        """
        创建cell部分
        :param sceneCell:场景所在的cellEntityCall
        """
        DEBUG_MSG("Account:createCell, scene id=%s" % sceneCell.id)
        # API：创建该实体的cell部分
        self.createCellEntity(sceneCell)

    def enterGame(self):
        """
        客户端点击进入游戏按钮后发来的请求
        :return:
        """
        DEBUG_MSG("Account[%i].enterGame:" % self.id)

        self.client.onEnterGameSuccess()
        # 把自己传送到指定的scene
        KBEngine.globalData["scene"].loginToScene(self)

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

    def onClientEnabled(self):
        """
        KBEngine method.
        该entity被正式激活为可使用， 此时entity已经建立了client对应实体。
        """
        INFO_MSG("account[%i] entities enable. entityCall:%s" % (self.id, self.client))

    def onClientDeath(self):
        """
        KBEngine method.
        客户端对应实体已经销毁
        """
        DEBUG_MSG("Account[%i].onClientDeath:" % self.id)

        if self.cell is not None:
            # 销毁cell实体
            self.destroyCellEntity()
            return

        self.destroy()

    def onDestroy(self):
        """
        KBEngine method.
        entity销毁
        """
        DEBUG_MSG("Account::onDestroy: %i." % self.id)

    def onLogOnAttempt(self, ip, port, password):
        """
        KBEngine method.
        客户端登陆失败时会回调到这里
        """
        INFO_MSG("Account[%i]::onLogOnAttempt: ip=%s, port=%s, selfclient=%s" % (self.id, ip, port, self.client))
        return KBEngine.LOG_ON_ACCEPT
