# encoding: utf-8
# module Wms.RemotingImplementation.MessageQueue.Execution.Marshalling calls itself Marshalling
# from Wms.RemotingImplementation,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class MarshalledMessageHandlerExecutor(MarshalledObject):
 """ MarshalledMessageHandlerExecutor(lifetime: TimeSpan) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MarshalledMessageHandlerExecutor()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Execute(self,handlerDescriptor,message):
  """ Execute(self: MarshalledMessageHandlerExecutor,handlerDescriptor: MessageHandlerDescriptor,message: IMessage) -> HandleResult """
  pass
 @staticmethod
 def __new__(self,lifetime):
  """ __new__(cls: type,lifetime: TimeSpan) """
  pass
 StateServerChannelName=property(lambda self: object(),lambda self,v: None,lambda self: None)



class MarshalledMessagePublisherExecutor(MarshalledObject):
 """ MarshalledMessagePublisherExecutor(lifetime: TimeSpan) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MarshalledMessagePublisherExecutor()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Execute(self,publisherDescriptor):
  """ Execute(self: MarshalledMessagePublisherExecutor,publisherDescriptor: MessagePublisherDescriptor) """
  pass
 @staticmethod
 def __new__(self,lifetime):
  """ __new__(cls: type,lifetime: TimeSpan) """
  pass
 StateServer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: StateServer(self: MarshalledMessagePublisherExecutor) -> MessagePublisherExecutorStateServer

"""

 StateServerChannelName=property(lambda self: object(),lambda self,v: None,lambda self: None)



class MessagePublisherExecutorStateServer(MarshalledLogger):
 """ MessagePublisherExecutorStateServer() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MessagePublisherExecutorStateServer()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject
  
   Creates a shallow copy of the current System.MarshalByRefObject object.
  
   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the object to be assigned a new identity when it is marshaled across a remoting 
    boundary. A value of false is usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone,which will cause remoting client calls 
    to be routed to the remote server object.
  
   Returns: A shallow copy of the current System.MarshalByRefObject object.
  MemberwiseClone(self: object) -> object
  
   Creates a shallow copy of the current System.Object.
   Returns: A shallow copy of the current System.Object.
  """
  pass
 def OnCreateMessage(self,message):
  """ OnCreateMessage(self: MessagePublisherExecutorStateServer,message: IMessage) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

