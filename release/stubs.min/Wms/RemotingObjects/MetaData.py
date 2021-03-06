# encoding: utf-8
# module Wms.RemotingObjects.MetaData calls itself MetaData
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class EnumHelper(object):
 """ EnumHelper() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return EnumHelper()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def ParseOrDefault(input,defaultValue,ignoreCase):
  """ ParseOrDefault[T](input: str,defaultValue: T,ignoreCase: bool) -> T """
  pass
 @staticmethod
 def TryParse(input,defaultValue,result,ignoreCase):
  """ TryParse[T](input: str,defaultValue: T,ignoreCase: bool) -> (bool,T) """
  pass

class EnumStringHelper(object):
 """ EnumStringHelper(enumType: Type) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return EnumStringHelper()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetListValues(self):
  """
  GetListValues(self: EnumStringHelper) -> IList
  
   Gets the values as a 'bindable' list datasource.
   Returns: IList for data binding
  """
  pass
 def GetStringValue(self,*__args):
  """
  GetStringValue(self: EnumStringHelper,valueName: str) -> str
  
   Gets the string value associated with the given enum value.
  
   valueName: Name of the enum value.
   Returns: String Value
  GetStringValue(value: Enum) -> str
  
   Gets a string value for a particular enum value.
  
   value: Value.
   Returns: String Value associated via a Wms.RemotingObjects.MetaData.EnumStringValueAttribute attribute,or null if not found.
  """
  pass
 def GetStringValues(self):
  """
  GetStringValues(self: EnumStringHelper) -> List[str]
  
   Gets the string values associated with the enum.
   Returns: String value array
  """
  pass
 def IsStringDefined(self,*__args):
  """
  IsStringDefined(self: EnumStringHelper,stringValue: str) -> bool
  
   Return the existence of the given string value within the enum.
  
   stringValue: String value.
   Returns: Existence of the string value
  IsStringDefined(self: EnumStringHelper,stringValue: str,ignoreCase: bool) -> bool
  
   Return the existence of the given string value within the enum.
  
   stringValue: String value.
   ignoreCase: Denotes whether to conduct a case-insensitive match on the supplied string value
   Returns: Existence of the string value
  IsStringDefined(enumType: Type,stringValue: str) -> bool
  
   Return the existence of the given string value within the enum.
  
   enumType: Type of enum
   stringValue: String value.
   Returns: Existence of the string value
  IsStringDefined(enumType: Type,stringValue: str,ignoreCase: bool) -> bool
  
   Return the existence of the given string value within the enum.
  
   enumType: Type of enum
   stringValue: String value.
   ignoreCase: Denotes whether to conduct a case-insensitive match on the supplied string value
   Returns: Existence of the string value
  """
  pass
 @staticmethod
 def Parse(type,stringValue,ignoreCase=None):
  """
  Parse(type: Type,stringValue: str) -> object
  
   Parses the supplied enum and string value to find an associated enum value (case sensitive).
  
   type: Type.
   stringValue: String value.
   Returns: Enum value associated with the string value,or null if not found.
  Parse(type: Type,stringValue: str,ignoreCase: bool) -> object
  
   Parses the supplied enum and string value to find an associated enum value.
  
   type: Type.
   stringValue: String value.
   ignoreCase: Denotes whether to conduct a case-insensitive match on the supplied string value
   Returns: Enum value associated with the string value,or null if not found.
  """
  pass
 @staticmethod
 def __new__(self,enumType):
  """ __new__(cls: type,enumType: Type) """
  pass
 EnumType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the underlying enum type for this instance.

Get: EnumType(self: EnumStringHelper) -> Type

"""



class EnumStringValueAttribute:
 """ EnumStringValueAttribute(value: str) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return EnumStringValueAttribute()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,value):
  """ __new__(cls: type,value: str) """
  pass
 def __reduce_ex__(self,*args):
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Value(self: EnumStringValueAttribute) -> str

"""



