# encoding: utf-8
# module Wms.EdiMessaging.Processor calls itself Processor
# from Wms.EdiMessaging,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class IMessageHandler:
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IMessageHandler()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Handle(self,message):
  """ Handle(self: IMessageHandler,message: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class JsonMessage(MessageBase):
 """
 JsonMessage()
 JsonMessage(messageType: Type,jsonString: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return JsonMessage()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,messageType=None,jsonString=None):
  """
  __new__(cls: type)
  __new__(cls: type,messageType: Type,jsonString: str)
  """
  pass

class MessageHandlerBase(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MessageHandlerBase()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Handle(self,message):
  """ Handle(self: MessageHandlerBase[TMessage],message: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass

class MessageProcessor(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MessageProcessor()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def AddHandler(self):
  """ AddHandler[(TMessage,THandler)](self: MessageProcessor) -> MessageProcessor """
  pass
 def CreateHandlerOfType(self,*args):
  """ CreateHandlerOfType(self: MessageProcessor,handlerType: Type) -> IMessageHandler """
  pass
 def ExtractMessage(self,*args):
  """ ExtractMessage(self: MessageProcessor,message: IMessage) -> object """
  pass
 def HandleMessage(self,*args):
  """ HandleMessage(self: MessageProcessor,obj: IMessage) """
  pass
 def Start(self,token):
  """ Start(self: MessageProcessor,token: CancellationToken) -> Task """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,queueProvider: IQueueProvider) """
  pass
 _queueProvider=None


