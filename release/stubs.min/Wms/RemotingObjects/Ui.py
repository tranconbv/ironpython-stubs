# encoding: utf-8
# module Wms.RemotingObjects.Ui calls itself Ui
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class UiForm(object):
 """
 data Abstraction of a ui Form element
 
 UiForm()
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return UiForm()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Fields=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Fields that are part of the form

Get: Fields(self: UiForm) -> List[UiFormField]

Set: Fields(self: UiForm)=value
"""



class UiFormField(object):
 """ UiFormField() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return UiFormField()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 AllowBlank=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Wether user is allowed to leave the field blank

Get: AllowBlank(self: UiFormField) -> bool

Set: AllowBlank(self: UiFormField)=value
"""

 DefaultValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Default value shown in form field when nothing is filled in.

Get: DefaultValue(self: UiFormField) -> object

Set: DefaultValue(self: UiFormField)=value
"""

 Label=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Translation key shown next to the input field.

Get: Label(self: UiFormField) -> str

Set: Label(self: UiFormField)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Name of the key in de resulting Options Dictoinary

Get: Name(self: UiFormField) -> str

Set: Name(self: UiFormField)=value
"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Datatype of the form field. think: string,datetime number,UserId,ZoneId. These types must be implemented in javascript formBuilder.

Get: Type(self: UiFormField) -> str

Set: Type(self: UiFormField)=value
"""



