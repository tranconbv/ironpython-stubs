# encoding: utf-8
# module Wms.RemotingObjects.ShippingLayers.Exceptions calls itself Exceptions
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class ShipperFatalException(Exception):
 """
 ShipperFatalException(message: str)
 ShipperFatalException(message: str,innerException: Exception)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ShipperFatalException()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message,innerException=None):
  """
  __new__(cls: type,message: str)
  __new__(cls: type,message: str,innerException: Exception)
  """
  pass
 def __str__(self,*args):
  pass
 SerializeObjectState=None


class ShipperCommunicationException(ShipperFatalException):
 """
 ShipperCommunicationException(message: str,shouldRetry: bool)
 ShipperCommunicationException(message: str,innerException: Exception,shouldRetry: bool)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ShipperCommunicationException()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message,*__args):
  """
  __new__(cls: type,message: str,shouldRetry: bool)
  __new__(cls: type,message: str,innerException: Exception,shouldRetry: bool)
  """
  pass
 def __str__(self,*args):
  pass
 ShouldRetry=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ShouldRetry(self: ShipperCommunicationException) -> bool

"""


 SerializeObjectState=None


