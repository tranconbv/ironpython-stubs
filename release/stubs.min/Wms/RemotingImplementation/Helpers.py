# encoding: utf-8
# module Wms.RemotingImplementation.Helpers calls itself Helpers
# from Wms.RemotingImplementation,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class DataFlowObjectHelper(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DataFlowObjectHelper()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def AreAllQuestionAnsweredPositive(dfObject):
  """ AreAllQuestionAnsweredPositive[T](dfObject: DataFlowObject[T]) -> DataFlowObject[T] """
  pass
 @staticmethod
 def IsQuestionAnswered(dfObject,key,answer):
  """ IsQuestionAnswered[T](dfObject: DataFlowObject[T],key: str) -> (bool,AnswerOptionsEnum) """
  pass
 @staticmethod
 def IsQuestionAnsweredPositive(dfObject,key,answer):
  """ IsQuestionAnsweredPositive[T](dfObject: DataFlowObject[T],key: str) -> (bool,AnswerOptionsEnum) """
  pass
 @staticmethod
 def LogDataFlowResult(dfObject):
  """ LogDataFlowResult[T](dfObject: DataFlowObject[T]) """
  pass
 __all__=[
  'AreAllQuestionAnsweredPositive',
  'IsQuestionAnswered',
  'IsQuestionAnsweredPositive',
  'LogDataFlowResult',
 ]


class DecimalExtensions(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DecimalExtensions()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def FormatDecimal(value):
  """ FormatDecimal(value: Decimal) -> str """
  pass
 __all__=[
  'FormatDecimal',
 ]


class GlobalizationHelper(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return GlobalizationHelper()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def ClearResourceCache():
  """ ClearResourceCache() """
  pass
 @staticmethod
 def GetCultureName(culture):
  """ GetCultureName(culture: str) -> str """
  pass
 @staticmethod
 def GetResources(resourceSet,culture):
  """ GetResources(resourceSet: str,culture: str) -> Translation """
  pass
 @staticmethod
 def SetGlobalizationSettings():
  """ SetGlobalizationSettings() """
  pass
 __all__=[
  'ClearResourceCache',
  'GetCultureName',
  'GetResources',
  'SetGlobalizationSettings',
 ]


class LabelHelper(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return LabelHelper()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def GetPlaceholders(label,systemFieldsRegEx):
  """ GetPlaceholders(label: PrintLabel,systemFieldsRegEx: str) -> List[str] """
  pass
 @staticmethod
 def RenderLabel(label,*__args):
  """
  RenderLabel(label: PrintLabel,data: DataRow,systemFieldsRegEx: str) -> str
  RenderLabel(label: PrintLabel,headerData: DataRow,itemData: DataTable,systemFieldsRegEx: str) -> List[str]
  """
  pass
 __all__=[
  'GetPlaceholders',
  'RenderLabel',
 ]


class OrderMatchesCustomerValidator(object):
 """ OrderMatchesCustomerValidator() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return OrderMatchesCustomerValidator()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def OrderMatchesCustomer(self,order,customer):
  """ OrderMatchesCustomer(self: OrderMatchesCustomerValidator,order: OutboundOrder,customer: Customer) -> bool """
  pass
 CheckCustomerContact=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CheckCustomerContact(self: OrderMatchesCustomerValidator) -> bool

Set: CheckCustomerContact(self: OrderMatchesCustomerValidator)=value
"""

 OrderMatchesCustomerDelegate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderMatchesCustomerDelegate(self: OrderMatchesCustomerValidator) -> OnOrderMatchesCustomerDelegate

Set: OrderMatchesCustomerDelegate(self: OrderMatchesCustomerValidator)=value
"""


 OnOrderMatchesCustomerDelegate=None


class SettingsHelper(object):
 """ SettingsHelper(settingsObject: object) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return SettingsHelper()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Dispose(self):
  """ Dispose(self: SettingsHelper) """
  pass
 def Load(self,onlyUserAndMachineSettings=None):
  """ Load(self: SettingsHelper)Load(self: SettingsHelper,onlyUserAndMachineSettings: bool) """
  pass
 def LoadMemberValue(self,*__args):
  """ LoadMemberValue(self: SettingsHelper,member: MemberInfo)LoadMemberValue(self: SettingsHelper,memberName: str) """
  pass
 def SaveAll(self,onlyUserAndMachineSettings=None):
  """ SaveAll(self: SettingsHelper)SaveAll(self: SettingsHelper,onlyUserAndMachineSettings: bool) """
  pass
 def SaveMemberValue(self,*__args):
  """ SaveMemberValue(self: SettingsHelper,member: MemberInfo)SaveMemberValue(self: SettingsHelper,memberName: str,value: object) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,settingsObject):
  """ __new__(cls: type,settingsObject: object) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass

class StringHelpers(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return StringHelpers()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def CreateMessageFromCollection(message,collection):
  """ CreateMessageFromCollection(message: str,collection: IEnumerable[str]) -> str """
  pass
 @staticmethod
 def EncodeAsCode128SetA(input):
  """ EncodeAsCode128SetA(input: str) -> str """
  pass
 @staticmethod
 def NormalizeForAscii(input):
  """ NormalizeForAscii(input: str) -> str """
  pass
 @staticmethod
 def RemoveNonAsciiCharacters(input,replaceWith=None):
  """
  RemoveNonAsciiCharacters(input: str,replaceWith: str) -> str
  RemoveNonAsciiCharacters(input: str) -> str
  """
  pass
 __all__=[
  'CreateMessageFromCollection',
  'EncodeAsCode128SetA',
  'NormalizeForAscii',
  'RemoveNonAsciiCharacters',
 ]


