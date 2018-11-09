# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class FirstEntity(KBEngine.Entity):
    """
    第一个实体的base部分的实现
    """

    def __init__(self):
        KBEngine.Entity.__init__(self)
        INFO_MSG("Hello ComblockEngine! I'm the first entity. My name is %s, id=%s" % (self.name, self.id))

    #   ===========================================
    #                   def中定义
    #   ===========================================
    def hello(self, content):
        """
        say hello
        :param content:内容
        :return:
        """
        INFO_MSG("Hello ComblockEngine! I'm %s. I got your content=%s" % (self.name, content))

    def createCell(self, sceneCell):
        """
        创建cell部分
        :param sceneCell:场景所在的cellEntityCall
        """
        DEBUG_MSG("FirstEntity:createCell, scene id=%s" % sceneCell.id)
        # API：创建该实体的cell部分
        self.createCellEntity(sceneCell)

    def destroySelf(self):
        """
        删除自己
        """

        if self.cell is not None:
            # 销毁cell部分
            self.destroyCellEntity()
            return

        # 销毁base部分
        if not self.isDestroyed:
            self.destroy()

    #   ===========================================
    #                   系统回调
    #   ===========================================

    def onDestroy(self):
        """
        KBEngine method.
        entity销毁
        """
        DEBUG_MSG("FirstEntity::onDestroy: %i." % self.id)

    def onGetCell(self):
        """
        KBEngine method.
        entity的cell部分实体被创建成功时回调
        """
        DEBUG_MSG("FirstEntity[%i]::onGetCell:%s" % (self.id, self.cell))

    def onLoseCell(self):
        """
        KBEngine method.
        entity的cell部分实体丢失
        """
        DEBUG_MSG("FirstEntity[%i]::onLoseCell: " % self.id)
        self.destroySelf()

    def onRestore(self):
        """
        KBEngine method.
        entity的cell部分实体被恢复成功
        """
        DEBUG_MSG("FirstEntity[%i]::onRestore: %s" % (self.id, self.cell))
