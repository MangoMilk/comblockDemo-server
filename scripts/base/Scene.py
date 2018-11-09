# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class Scene(KBEngine.Entity):
    """
    Scene的base部分，可以操控CellApp上真正scene的实体
    注意：它是一个实体，并不是真正的space，真正的space存在于cellapp的内存中，通过这个实体与之关联并操控space。
    """

    def __init__(self):
        KBEngine.Entity.__init__(self)
        # 向cellappmgr请求创建一个cell，并关联本实体对象
        # 参数cellappIndex为None，表示由引擎负载均衡进行动态选择
        self.createCellEntityInNewSpace(None)

        # 保存一下当前场景中的所有实体
        # 包含的实体字典，key=id，value=EntityCall
        self.entities = {}

    #   ===========================================
    #                   def中定义
    #   ===========================================

    def loginToScene(self, entityCall):
        """
        某个Entity请求登录到该场景
        :param entityCall: 要进入本场景的实体entityCall
        """
        entityCall.createCell(self.cell)
        self.onEnter(entityCall)

    def logoutScene(self, entityId):
        """
        某个玩家请求登出该场景
        :param entityId: 登出者的id
        """
        self.onLeave(entityId)

    def onEnter(self, entityCall):
        """
        virtual method.
        进入后的通知
        """
        self.entities[entityCall.id] = entityCall

        # 通知scene的cell部分，有人进来了
        if self.cell is not None:
            self.cell.onEnter(entityCall)

    def onLeave(self, entityId):
        """
        virtual method.
        离开后的通知
        """
        if entityId in self.entities:
            del self.entities[entityId]

        # 通知scene的cell部分，有人离开了
        if self.cell is not None:
            self.cell.onLeave(entityId)

    #   ===============================================
    #                       系统回调
    #   ===============================================

    def onGetCell(self):
        """
        entity的cell部分被创建成功
        """
        DEBUG_MSG("Scene[%i]::onGetCell: " % self.id)
        props = {
            "name": "MyFirstEntity",
            "position": (1.7, 0, 0)  # 为了和Account实体在空间中的位置不重叠，这里设置一个差别
        }
        entity = KBEngine.createEntityLocally("FirstEntity", props)
        self.loginToScene(entity)

    def onLoseCell(self):
        """
        entity的cell部分实体丢失
        """

        DEBUG_MSG("Scene[%i]::onLoseCell:" % self.id)
