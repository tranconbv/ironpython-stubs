# encoding: utf-8
# module Wms.EdiMessaging.Metadata calls itself Metadata
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from System.Collections.Generic import *
from ..__init__ import *

# functions

def MessageHandlerDescriptor(handlerType,createInstance,IMessageHandler): # real signature unknown; restored from __doc__
 """ MessageHandlerDescriptor(handlerType: Type,createInstance: Func[IMessageHandler]) """
 pass
def MessagePublisherDescriptor(handlerType,createInstance,IMessagePublisher): # real signature unknown; restored from __doc__
 """ MessagePublisherDescriptor(handlerType: Type,createInstance: Func[IMessagePublisher]) """
 pass
# classes

class ObjectDescriptor(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ObjectDescriptor()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def ExtractAttribute(self):
  """ ExtractAttribute(self: ObjectDescriptor) -> DescriptorAttribute """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,handlerType: Type) """
  pass
 ExecuteIsolated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExecuteIsolated(self: ObjectDescriptor) -> bool

"""

 FriendlyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FriendlyName(self: ObjectDescriptor) -> str

"""

 Fullname=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Fullname(self: ObjectDescriptor) -> str

"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: ObjectDescriptor) -> Guid

"""


 HandlerType=None


# variables with complex values

