# encoding: utf-8
# module Wms.RemotingObjects calls itself RemotingObjects
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from System.Collections.Generic import *
from ..__init__ import *

# functions

def ResultObject(): # real signature unknown; restored from __doc__
 """
 ResultObject()
 ResultObject(success: bool)
 ResultObject(success: bool,message: str)
 """
 pass
# classes

class AnswerOptionsEnum:
 """ enum (flags) AnswerOptionsEnum,values: Abort (4),Cancel (2),Ignore (16),No (64),NoResponse (0),OK (1),Retry (8),Yes (32) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return AnswerOptionsEnum()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Abort=None
 Cancel=None
 Ignore=None
 No=None
 NoResponse=None
 OK=None
 Retry=None
 value__=None
 Yes=None


class AnswerOptionsEnumHelper(object):
 """ AnswerOptionsEnumHelper() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return AnswerOptionsEnumHelper()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def ConvertFromDialogResult(result):
  """ ConvertFromDialogResult(result: DialogResult) -> AnswerOptionsEnum """
  pass
 @staticmethod
 def ConvertToMessageBoxButtons(PossibleAnswers):
  """ ConvertToMessageBoxButtons(PossibleAnswers: int) -> MessageBoxButtons """
  pass
 @staticmethod
 def IsAnswerAllowed(PossibleAnswers,Answer):
  """ IsAnswerAllowed(PossibleAnswers: int,Answer: AnswerOptionsEnum) -> bool """
  pass

class IFindableList:
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IFindableList()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def ExistsByProperty(self,id):
  """ ExistsByProperty(self: IFindableList,id: str) -> bool """
  pass
 def FindAll(self,searchString,exactMatchesOnly):
  """ FindAll(self: IFindableList,searchString: str,exactMatchesOnly: bool) -> object """
  pass
 def FindIndex(self,id):
  """ FindIndex(self: IFindableList,id: str) -> int """
  pass
 def GetObject(self,*__args):
  """
  GetObject(self: IFindableList,id: str) -> object
  GetObject(self: IFindableList,propertyName: str,searchString: str) -> object
  
   Gets the object by a specific property name and search string
  
   propertyName: The name of the property to check
   searchString: The value to look for
  """
  pass
 def Remove(self,id):
  """ Remove(self: IFindableList,id: str) """
  pass
 def Update(self,id,property,value):
  """
  Update(self: IFindableList,id: object,property: str,value: object) -> bool
  
   Make sure the value parameter has the same type as the actual field to update!
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class Answers(FindableList):
 """ Answers() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Answers()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetAnswerCount(self,countAnswer):
  """ GetAnswerCount(self: Answers,countAnswer: AnswerOptionsEnum) -> int """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Total=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Total(self: Answers) -> int

"""

 TotalAbort=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalAbort(self: Answers) -> int

"""

 TotalCancel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalCancel(self: Answers) -> int

"""

 TotalNo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalNo(self: Answers) -> int

"""

 TotalNoResponse=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalNoResponse(self: Answers) -> int

"""

 TotalRetry=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalRetry(self: Answers) -> int

"""

 TotalYes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TotalYes(self: Answers) -> int

"""



class BatchInfo(object):
 """
 BatchInfo(text: str)
 BatchInfo(text: str,tag: object)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return BatchInfo()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,text,tag=None):
  """
  __new__(cls: type,text: str)
  __new__(cls: type,text: str,tag: object)
  """
  pass
 Children=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Children(self: BatchInfo) -> List[BatchInfo]

Set: Children(self: BatchInfo)=value
"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Tag(self: BatchInfo) -> object

Set: Tag(self: BatchInfo)=value
"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Text(self: BatchInfo) -> str

Set: Text(self: BatchInfo)=value
"""



class ChangeBarcodeArgs(object):
 """
 Arguments used for changing the barcode of an item.
 
 ChangeBarcodeArgs()
 ChangeBarcodeArgs(itemCode: str,barcode: str,creditor: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ChangeBarcodeArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,itemCode=None,barcode=None,creditor=None):
  """
  __new__(cls: type)
  __new__(cls: type,itemCode: str,barcode: str,creditor: str)
  """
  pass
 Barcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The new barcode value.

Get: Barcode(self: ChangeBarcodeArgs) -> str

Set: Barcode(self: ChangeBarcodeArgs)=value
"""

 Creditor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the creditor to which the item belongs.

Get: Creditor(self: ChangeBarcodeArgs) -> str

Set: Creditor(self: ChangeBarcodeArgs)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The itemcode of the item from wich the barcode has to be changed.

Get: ItemCode(self: ChangeBarcodeArgs) -> str

Set: ItemCode(self: ChangeBarcodeArgs)=value
"""


 Default=None


class DataBindingTypes:
 """ enum DataBindingTypes,values: DisplayMember (1),UniqueId (2),ValueMember (0) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DataBindingTypes()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 DisplayMember=None
 UniqueId=None
 ValueMember=None
 value__=None


class DbObject(object):
 """  """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DbObject()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 CreatedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CreatedBy(self: DbObject) -> str

Set: CreatedBy(self: DbObject)=value
"""

 CreatedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CreatedOn(self: DbObject) -> DateTime

Set: CreatedOn(self: DbObject)=value
"""

 ModifiedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ModifiedBy(self: DbObject) -> str

Set: ModifiedBy(self: DbObject)=value
"""

 ModifiedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ModifiedOn(self: DbObject) -> DateTime

Set: ModifiedOn(self: DbObject)=value
"""



class Device(DbObject):
 """ Device() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Device()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Id(self: Device) -> int

Set: Id(self: Device)=value
"""

 MacAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: MacAddress(self: Device) -> str

Set: MacAddress(self: Device)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Name(self: Device) -> str

Set: Name(self: Device)=value
"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Type(self: Device) -> DeviceTypesEnum

Set: Type(self: Device)=value
"""



class DeviceInformation(object):
 """
 DeviceInformation()
 DeviceInformation(type: DeviceTypesEnum,name: str,serialNumber: str,operatingSystem: str,hardwareInformation: List[str])
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DeviceInformation()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,type=None,name=None,serialNumber=None,operatingSystem=None,hardwareInformation=None):
  """
  __new__(cls: type)
  __new__(cls: type,type: DeviceTypesEnum,name: str,serialNumber: str,operatingSystem: str,hardwareInformation: List[str])
  """
  pass
 HardwareInformation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: HardwareInformation(self: DeviceInformation) -> List[str]

Set: HardwareInformation(self: DeviceInformation)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Name(self: DeviceInformation) -> str

Set: Name(self: DeviceInformation)=value
"""

 OperatingSystem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OperatingSystem(self: DeviceInformation) -> str

Set: OperatingSystem(self: DeviceInformation)=value
"""

 SerialNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: SerialNumber(self: DeviceInformation) -> str

Set: SerialNumber(self: DeviceInformation)=value
"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Type(self: DeviceInformation) -> DeviceTypesEnum

Set: Type(self: DeviceInformation)=value
"""



class Devices(FindableList):
 """ Devices() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Devices()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass

class DeviceTypesEnum:
 """ enum DeviceTypesEnum,values: Handheld (2),Other (0),Portal (3),Terminal (1) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DeviceTypesEnum()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Handheld=None
 Other=None
 Portal=None
 Terminal=None
 value__=None


class Error(object):
 """
 Error(text: str)
 Error(text: str,details: str)
 Error(key: str,text: str,details: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Error()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,text: str)
  __new__(cls: type,text: str,details: str)
  __new__(cls: type,key: str,text: str,details: str)
  """
  pass
 Details=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Details(self: Error) -> str

"""

 Key=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Key(self: Error) -> str

Set: Key(self: Error)=value
"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Text(self: Error) -> str

"""



class Errors(List):
 """ Errors() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Errors()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def ToString(self):
  """
  ToString(self: Errors) -> str
  
   Returns a System.String that represents the current System.Object.
   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 def __str__(self,*args):
  pass

class FindableList(List):
 """
 FindableList[T]()
 FindableList[T](collection: IEnumerable[T])
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return FindableList()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def ExistsByProperty(self,id):
  """ ExistsByProperty(self: FindableList[T],id: str) -> bool """
  pass
 def FindAll(self,*__args):
  """ FindAll(self: FindableList[T],searchString: str,exactMatchesOnly: bool) -> object """
  pass
 def FindIndex(self,*__args):
  """ FindIndex(self: FindableList[T],id: str) -> int """
  pass
 @staticmethod
 def FromIEnumerable(list):
  """ FromIEnumerable(list: IEnumerable[T]) -> FindableList[T] """
  pass
 def GetObject(self,*__args):
  """
  GetObject(self: FindableList[T],id: str) -> object
  GetObject(self: FindableList[T],propertyName: str,searchString: str) -> object
  
   Gets the object by a specific property name and search string
  
   propertyName: The name of the property to check
   searchString: The value to look for
  """
  pass
 def IsLifeExpired(self,lifeTimeConfig):
  """ IsLifeExpired(self: FindableList[T],lifeTimeConfig: Dictionary[CacheLifeTimes,int]) -> bool """
  pass
 def Remove(self,*__args):
  """ Remove(self: FindableList[T],id: str) """
  pass
 def Update(self,id,property,value):
  """
  Update(self: FindableList[T],id: object,property: str,value: object) -> bool
  
   Make sure the value parameter has the same type as the actual field to update!
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,collection=None):
  """
  __new__(cls: type)
  __new__(cls: type,collection: IEnumerable[T])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 CreatedAt=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CreatedAt(self: FindableList[T]) -> DateTime

"""

 Hidden=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Hidden(self: FindableList[T]) -> bool

"""

 IsDisposable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsDisposable(self: FindableList[T]) -> bool

"""

 IsUserRemovable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """By default,all objects are user removable.

Get: IsUserRemovable(self: FindableList[T]) -> bool

"""

 Key=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Key(self: FindableList[T]) -> CacheKey

Set: Key(self: FindableList[T])=value
"""

 Lifetime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Lifetime(self: FindableList[T]) -> CacheLifeTimes

Set: Lifetime(self: FindableList[T])=value
"""

 PreserveState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PreserveState(self: FindableList[T]) -> bool

"""



class GetLogLinesArgs(object):
 """ GetLogLinesArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return GetLogLinesArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Device=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Device(self: GetLogLinesArgs) -> str

Set: Device(self: GetLogLinesArgs)=value
"""

 EndDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: EndDate(self: GetLogLinesArgs) -> str

Set: EndDate(self: GetLogLinesArgs)=value
"""

 OnlyLastTwoDays=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OnlyLastTwoDays(self: GetLogLinesArgs) -> bool

Set: OnlyLastTwoDays(self: GetLogLinesArgs)=value
"""

 Paging=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Paging(self: GetLogLinesArgs) -> PagingParams

Set: Paging(self: GetLogLinesArgs)=value
"""

 SearchText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: SearchText(self: GetLogLinesArgs) -> str

Set: SearchText(self: GetLogLinesArgs)=value
"""

 StartDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: StartDate(self: GetLogLinesArgs) -> str

Set: StartDate(self: GetLogLinesArgs)=value
"""

 Types=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Types(self: GetLogLinesArgs) -> str

Set: Types(self: GetLogLinesArgs)=value
"""

 UserName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: UserName(self: GetLogLinesArgs) -> str

Set: UserName(self: GetLogLinesArgs)=value
"""

 Zone=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Zone(self: GetLogLinesArgs) -> str

Set: Zone(self: GetLogLinesArgs)=value
"""



class HistoryFilterBase(object):
 """  """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HistoryFilterBase()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 FromDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: FromDate(self: HistoryFilterBase) -> Nullable[DateTime]

"""

 SearchText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SearchText(self: HistoryFilterBase) -> str

Set: SearchText(self: HistoryFilterBase)=value
"""

 TimeSpan=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TimeSpan(self: HistoryFilterBase) -> TimeFilterHistoryEnum

Set: TimeSpan(self: HistoryFilterBase)=value
"""

 ToDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ToDate(self: HistoryFilterBase) -> DateTime

"""



class IDbObject:
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IDbObject()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 CreatedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CreatedBy(self: IDbObject) -> str

Set: CreatedBy(self: IDbObject)=value
"""

 CreatedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CreatedOn(self: IDbObject) -> DateTime

Set: CreatedOn(self: IDbObject)=value
"""

 ModifiedBy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ModifiedBy(self: IDbObject) -> str

Set: ModifiedBy(self: IDbObject)=value
"""

 ModifiedOn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ModifiedOn(self: IDbObject) -> DateTime

Set: ModifiedOn(self: IDbObject)=value
"""



class ImplementedFunctionalities(object):
 """ ImplementedFunctionalities() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ImplementedFunctionalities()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def ToMobileVariant(self):
  """
  ToMobileVariant(self: ImplementedFunctionalities) -> ImplementedFunctionalities
  
   Used by the Mobile because it doesn't have a reference to the ERP links.
  """
  pass
 CreateReceiptsWithoutPurchaseOrder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to create a receipt without a purchase order?

Get: CreateReceiptsWithoutPurchaseOrder(self: ImplementedFunctionalities) -> bool

"""

 GetItemCodeFromBarcode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to retrieve an item with a given barcode?

Get: GetItemCodeFromBarcode(self: ImplementedFunctionalities) -> bool

"""

 GetItemIdentifictionAvailable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to check if the item identifications are available?

Get: GetItemIdentifictionAvailable(self: ImplementedFunctionalities) -> bool

"""

 GetItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to retrieve items?

Get: GetItems(self: ImplementedFunctionalities) -> bool

"""

 GetItemsOnLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to retrieve the items on a specific warehouselocation?

Get: GetItemsOnLocation(self: ImplementedFunctionalities) -> bool

"""

 GetItemStockInfo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to retrieve the stock info from an item?

Get: GetItemStockInfo(self: ImplementedFunctionalities) -> bool

"""

 GetPurchaseOrderLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to retrieve all order lines from a purchase order?

Get: GetPurchaseOrderLines(self: ImplementedFunctionalities) -> bool

"""

 GetPurchaseOrders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to retrieve the purchase orders of each vendor?

Get: GetPurchaseOrders(self: ImplementedFunctionalities) -> bool

"""

 GetPurchaseOrderVendors=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to retrieve the purchase vendors?

Get: GetPurchaseOrderVendors(self: ImplementedFunctionalities) -> bool

"""

 GetRmaOrderCustomers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to retrieve the customers of RMA orders?

Get: GetRmaOrderCustomers(self: ImplementedFunctionalities) -> bool

"""

 GetRmaOrderLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to retrieve all order lines from a RMA order?

Get: GetRmaOrderLines(self: ImplementedFunctionalities) -> bool

"""

 GetRmaOrders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to retrieve the RMA orders of each customer?

Get: GetRmaOrders(self: ImplementedFunctionalities) -> bool

"""

 GetSalesOrderCustomers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to retrieve customer information from all sales orders?

Get: GetSalesOrderCustomers(self: ImplementedFunctionalities) -> bool

"""

 GetSalesOrderLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to retrieve all sales orderlines?

Get: GetSalesOrderLines(self: ImplementedFunctionalities) -> bool

"""

 GetSalesOrders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to retrieve sales orders?

Get: GetSalesOrders(self: ImplementedFunctionalities) -> bool

"""

 GetSerialNumberExists=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to check if a serial number of an item exists in the ERP system.

Get: GetSerialNumberExists(self: ImplementedFunctionalities) -> bool

"""

 GetWarehouseLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to retrieve a warehouselocation from a product?

Get: GetWarehouseLocation(self: ImplementedFunctionalities) -> bool

"""

 GetWarehouses=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to retrieve information about the warehouses?

Get: GetWarehouses(self: ImplementedFunctionalities) -> bool

"""

 HasSupportForDefaultInboundLocation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Does the link support a default inbound location on a warehouse?

Get: HasSupportForDefaultInboundLocation(self: ImplementedFunctionalities) -> bool

"""

 HasSupportForDefaultItemLocationPerWarehouse=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasSupportForDefaultItemLocationPerWarehouse(self: ImplementedFunctionalities) -> bool

"""

 ImportSalesOrders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to retrieve all sales orders with their order lines and customers?

Get: ImportSalesOrders(self: ImplementedFunctionalities) -> bool

"""

 PrintAdhocRmaInvoice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to print invoices for an adhoc RMA receipt?

Get: PrintAdhocRmaInvoice(self: ImplementedFunctionalities) -> bool

"""

 PrintPackingSlipUsingCustomPrinter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to print packing slips when a custom printer is passed while processing salesorders?

Get: PrintPackingSlipUsingCustomPrinter(self: ImplementedFunctionalities) -> bool

"""

 PrintSalesInvoice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to print invoices of a sales order after fulfillment?

Get: PrintSalesInvoice(self: ImplementedFunctionalities) -> bool

"""

 ProcessAdhocRmaOrders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to create and process an adhoc RMA order?

Get: ProcessAdhocRmaOrders(self: ImplementedFunctionalities) -> bool

"""

 ProcessCounts=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to process counts with the data wich will be provided by BOXwise?

Get: ProcessCounts(self: ImplementedFunctionalities) -> bool

"""

 ProcessPurchaseOrderLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to process a specific purchase order with the data wich will be provided by BOXwise?

Get: ProcessPurchaseOrderLines(self: ImplementedFunctionalities) -> bool

"""

 ProcessRmaOrderLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to process a specific RMA order with the data wich will be provided by BOXwise?

Get: ProcessRmaOrderLines(self: ImplementedFunctionalities) -> bool

"""

 ProcessSalesOrderLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to process a specific sales order with the data wich will be provided by BOXwise?

Get: ProcessSalesOrderLines(self: ImplementedFunctionalities) -> bool

"""

 UpdateExpiryDateWithCounts=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to register the expiry date of a batchnumber with a count.

Get: UpdateExpiryDateWithCounts(self: ImplementedFunctionalities) -> bool

"""

 ValidateOrders=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Is the link able to validate orders?

Get: ValidateOrders(self: ImplementedFunctionalities) -> bool

"""



class IPagedList:
 """  """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IPagedList()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 TotalRowsMatched=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the total rows that have matched the query. This is not the total rows in the collection.

Get: TotalRowsMatched(self: IPagedList) -> Int64

Set: TotalRowsMatched(self: IPagedList)=value
"""



class Items(FindableList):
 """
 Container for the Wms.RemotingObjects.Inventory.Item objects.
 
 Items()
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Items()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def FromIEnumerable(items):
  """ FromIEnumerable(items: IEnumerable[Item]) -> Items """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 DisplayMember='Description'
 ValueMember='Code'


class IUniqueHashable:
 """  """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IUniqueHashable()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetUniqueHashCode(self):
  """ GetUniqueHashCode(self: IUniqueHashable) -> str """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class License(object):
 """
 License information for a BOXwise license
 
 License()
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return License()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 AddressLine1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """First address line container street and number

Get: AddressLine1(self: License) -> str

Set: AddressLine1(self: License)=value
"""

 AddressLine2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Optional second address line contain extra information,eg: first floor,room 12

Get: AddressLine2(self: License) -> str

Set: AddressLine2(self: License)=value
"""

 AddressLine3=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Optional third line if more info is required than after second line.

Get: AddressLine3(self: License) -> str

Set: AddressLine3(self: License)=value
"""

 BeginDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Datetime from when the license is valid

Get: BeginDate(self: License) -> Nullable[DateTime]

Set: BeginDate(self: License)=value
"""

 Country=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Name of country of the address

Get: Country(self: License) -> str

Set: Country(self: License)=value
"""

 CustomerName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Name of the customer/company

Get: CustomerName(self: License) -> str

Set: CustomerName(self: License)=value
"""

 CustomerNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Customer number in our accounting software (profit)

Get: CustomerNumber(self: License) -> str

Set: CustomerNumber(self: License)=value
"""

 Email=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Email address the customer is reachable on.

Get: Email(self: License) -> str

Set: Email(self: License)=value
"""

 EndDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Datetime upto when the license is valid

Get: EndDate(self: License) -> Nullable[DateTime]

Set: EndDate(self: License)=value
"""

 IsDemoLicense=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Wether the license is a demo/test license.
   Warning will be shown that its a demo license

Get: IsDemoLicense(self: License) -> bool

Set: IsDemoLicense(self: License)=value
"""

 Number=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Unique number for the license eg: 89

Get: Number(self: License) -> str

Set: Number(self: License)=value
"""

 NumberOfBosClients=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Number of BOS(OPH) clients allowed for this license registered at the same time

Get: NumberOfBosClients(self: License) -> int

Set: NumberOfBosClients(self: License)=value
"""

 NumberOfClients=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NumberOfClients(self: License) -> int

Set: NumberOfClients(self: License)=value
"""

 Phone=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Phone number the customer is reachable on.

Get: Phone(self: License) -> str

Set: Phone(self: License)=value
"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """State or province in country

Get: State(self: License) -> str

Set: State(self: License)=value
"""

 Warnings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Warnings about this license that will be shown in portal.

Get: Warnings(self: License) -> List[str]

Set: Warnings(self: License)=value
"""



class LogLine(DbObject):
 """ LogLine() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return LogLine()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 AccessId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: AccessId(self: LogLine) -> str

Set: AccessId(self: LogLine)=value
"""

 AppDomain=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: AppDomain(self: LogLine) -> str

Set: AppDomain(self: LogLine)=value
"""

 Category=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Category(self: LogLine) -> str

Set: Category(self: LogLine)=value
"""

 ClientName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ClientName(self: LogLine) -> str

Set: ClientName(self: LogLine)=value
"""

 EventId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: EventId(self: LogLine) -> int

Set: EventId(self: LogLine)=value
"""

 EventType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: EventType(self: LogLine) -> str

Set: EventType(self: LogLine)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Id(self: LogLine) -> int

Set: Id(self: LogLine)=value
"""

 MachineName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: MachineName(self: LogLine) -> str

Set: MachineName(self: LogLine)=value
"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Message(self: LogLine) -> str

Set: Message(self: LogLine)=value
"""

 Priority=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Priority(self: LogLine) -> int

Set: Priority(self: LogLine)=value
"""

 ProcessId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ProcessId(self: LogLine) -> str

Set: ProcessId(self: LogLine)=value
"""

 ProcessName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ProcessName(self: LogLine) -> str

Set: ProcessName(self: LogLine)=value
"""

 Thread=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Thread(self: LogLine) -> int

Set: Thread(self: LogLine)=value
"""

 TimeStamp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: TimeStamp(self: LogLine) -> DateTime

Set: TimeStamp(self: LogLine)=value
"""

 Title=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Title(self: LogLine) -> str

Set: Title(self: LogLine)=value
"""

 UserName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: UserName(self: LogLine) -> str

Set: UserName(self: LogLine)=value
"""

 WindowsIdentity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: WindowsIdentity(self: LogLine) -> str

Set: WindowsIdentity(self: LogLine)=value
"""

 Zone=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Zone(self: LogLine) -> str

Set: Zone(self: LogLine)=value
"""



class Mapping(object):
 """
 Mapping[TKey,TValue,TInfo](key: TKey,value: TValue)
 Mapping[TKey,TValue,TInfo](key: TKey,value: TValue,info: TInfo)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Mapping()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,key,value,info=None):
  """
  __new__(cls: type,key: TKey,value: TValue)
  __new__(cls: type,key: TKey,value: TValue,info: TInfo)
  """
  pass
 Info=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Info(self: Mapping[TKey,TValue,TInfo]) -> TInfo

Set: Info(self: Mapping[TKey,TValue,TInfo])=value
"""

 Key=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Key(self: Mapping[TKey,TValue,TInfo]) -> TKey

"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Value(self: Mapping[TKey,TValue,TInfo]) -> TValue

Set: Value(self: Mapping[TKey,TValue,TInfo])=value
"""



class Mappings(object):
 """
 Mappings[TKey,TValue,TInfo](capacity: int)
 Mappings[TKey,TValue,TInfo]()
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Mappings()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Add(self,key,value,info=None):
  """ Add(self: Mappings[TKey,TValue,TInfo],key: TKey,value: TValue)Add(self: Mappings[TKey,TValue,TInfo],key: TKey,value: TValue,info: TInfo) """
  pass
 def ContainsKey(self,key):
  """ ContainsKey(self: Mappings[TKey,TValue,TInfo],key: TKey) -> bool """
  pass
 def ContainsValue(self,value):
  """ ContainsValue(self: Mappings[TKey,TValue,TInfo],value: TValue) -> bool """
  pass
 def GetEnumerator(self):
  """ GetEnumerator(self: Mappings[TKey,TValue,TInfo]) -> Enumerator """
  pass
 def GetInfo(self,key):
  """ GetInfo(self: Mappings[TKey,TValue,TInfo],key: TKey) -> TInfo """
  pass
 def Remove(self,key):
  """ Remove(self: Mappings[TKey,TValue,TInfo],key: TKey) -> bool """
  pass
 def SetInfo(self,key,info):
  """ SetInfo(self: Mappings[TKey,TValue,TInfo],key: TKey,info: TInfo) """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 @staticmethod
 def __new__(self,capacity=None):
  """
  __new__(cls: type,capacity: int)
  __new__(cls: type)
  """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass

class OrderTypeEnum:
 """ enum OrderTypeEnum,values: Purchase (0),Replenishment (3),Rma (1),Rtv (4),Sales (2) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return OrderTypeEnum()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Purchase=None
 Replenishment=None
 Rma=None
 Rtv=None
 Sales=None
 value__=None


class PagedList(List):
 """
 PagedList[T]()
 PagedList[T](capacity: int)
 PagedList[T](collection: IEnumerable[T])
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PagedList()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,capacity: int)
  __new__(cls: type,collection: IEnumerable[T])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 TotalRowsMatched=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the total rows that have matched the query. This is not the total rows in the collection.

Get: TotalRowsMatched(self: PagedList[T]) -> Int64

Set: TotalRowsMatched(self: PagedList[T])=value
"""



class PagingParams(object):
 """
 Default model for paging and sorting results.
 
 PagingParams()
 PagingParams(start: int,limit: int,sortColumn: str,sortDirection: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PagingParams()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetHashCode(self):
  """
  GetHashCode(self: PagingParams) -> int
  
   Unique hash depending on contents.
     Identical contents leads to identical hash.
  """
  pass
 def GetSortAsString(self):
  """
  GetSortAsString(self: PagingParams) -> str
  
   Sql sort string. usable for easy objects.
  """
  pass
 @staticmethod
 def __new__(self,start=None,limit=None,sortColumn=None,sortDirection=None):
  """
  __new__(cls: type)
  __new__(cls: type,start: int,limit: int,sortColumn: str,sortDirection: str)
  """
  pass
 IsSortingApplied=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If sort order is defined

Get: IsSortingApplied(self: PagingParams) -> bool

"""

 Limit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """How many records to return (after Wms.RemotingObjects.PagingParams.Start).

Get: Limit(self: PagingParams) -> int

Set: Limit(self: PagingParams)=value
"""

 SortAscending=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If sort order is ascending,default false.
   Descending is more handy,think of id and created_at means latest first.

Get: SortAscending(self: PagingParams) -> bool

"""

 Start=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """index of first record to be returned (1=first record).

Get: Start(self: PagingParams) -> int

Set: Start(self: PagingParams)=value
"""


 SortColumn=None
 SortDirection=None


class ProfilingLogEntries(FindableList):
 """ ProfilingLogEntries() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ProfilingLogEntries()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass

class ProfilingUserNode(object):
 """
 ProfilingUserNode()
 ProfilingUserNode(userKey: int,userName: str,machineName: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ProfilingUserNode()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def ToString(self):
  """ ToString(self: ProfilingUserNode) -> str """
  pass
 @staticmethod
 def __new__(self,userKey=None,userName=None,machineName=None):
  """
  __new__(cls: type)
  __new__(cls: type,userKey: int,userName: str,machineName: str)
  """
  pass
 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: ProfilingUserNode) -> int

Set: Id(self: ProfilingUserNode)=value
"""

 MachineName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MachineName(self: ProfilingUserNode) -> str

Set: MachineName(self: ProfilingUserNode)=value
"""

 UserKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UserKey(self: ProfilingUserNode) -> int

Set: UserKey(self: ProfilingUserNode)=value
"""

 UserName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UserName(self: ProfilingUserNode) -> str

Set: UserName(self: ProfilingUserNode)=value
"""



class ProfilingLogEntry(ProfilingUserNode):
 """ ProfilingLogEntry() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ProfilingLogEntry()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 AccessId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AccessId(self: ProfilingLogEntry) -> str

Set: AccessId(self: ProfilingLogEntry)=value
"""

 AppDomain=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AppDomain(self: ProfilingLogEntry) -> str

Set: AppDomain(self: ProfilingLogEntry)=value
"""

 Categories=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Categories(self: ProfilingLogEntry) -> str

Set: Categories(self: ProfilingLogEntry)=value
"""

 ClientName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ClientName(self: ProfilingLogEntry) -> str

Set: ClientName(self: ProfilingLogEntry)=value
"""

 ElapsedSeconds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ElapsedSeconds(self: ProfilingLogEntry) -> Decimal

Set: ElapsedSeconds(self: ProfilingLogEntry)=value
"""

 EventId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: EventId(self: ProfilingLogEntry) -> int

Set: EventId(self: ProfilingLogEntry)=value
"""

 EventType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: EventType(self: ProfilingLogEntry) -> str

Set: EventType(self: ProfilingLogEntry)=value
"""

 HasChildren=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasChildren(self: ProfilingLogEntry) -> bool

Set: HasChildren(self: ProfilingLogEntry)=value
"""

 Message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Message(self: ProfilingLogEntry) -> str

Set: Message(self: ProfilingLogEntry)=value
"""

 PrimaryKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PrimaryKey(self: ProfilingLogEntry) -> int

Set: PrimaryKey(self: ProfilingLogEntry)=value
"""

 Priority=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Priority(self: ProfilingLogEntry) -> int

Set: Priority(self: ProfilingLogEntry)=value
"""

 ProcessId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ProcessId(self: ProfilingLogEntry) -> str

Set: ProcessId(self: ProfilingLogEntry)=value
"""

 ProcessName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ProcessName(self: ProfilingLogEntry) -> str

Set: ProcessName(self: ProfilingLogEntry)=value
"""

 Thread=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Thread(self: ProfilingLogEntry) -> int

Set: Thread(self: ProfilingLogEntry)=value
"""

 TimeStamp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TimeStamp(self: ProfilingLogEntry) -> DateTime

Set: TimeStamp(self: ProfilingLogEntry)=value
"""

 Title=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Title(self: ProfilingLogEntry) -> str

Set: Title(self: ProfilingLogEntry)=value
"""

 WindowsIdentity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WindowsIdentity(self: ProfilingLogEntry) -> str

Set: WindowsIdentity(self: ProfilingLogEntry)=value
"""



class ProfilingUserNodes(FindableList):
 """ ProfilingUserNodes() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ProfilingUserNodes()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass

class Question(object):
 """
 Question()
 Question(key: str,text: str,possibleAnswers: int)
 Question(key: str,text: str,details: str,possibleAnswers: int)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Question()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,key=None,text=None,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,key: str,text: str,possibleAnswers: int)
  __new__(cls: type,key: str,text: str,details: str,possibleAnswers: int)
  """
  pass
 Answer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Answer(self: Question) -> AnswerOptionsEnum

Set: Answer(self: Question)=value
"""

 Details=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Details(self: Question) -> str

Set: Details(self: Question)=value
"""

 IsAnswered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsAnswered(self: Question) -> bool

"""

 Key=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Key(self: Question) -> str

Set: Key(self: Question)=value
"""

 PossibleAnswers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PossibleAnswers(self: Question) -> int

Set: PossibleAnswers(self: Question)=value
"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Text(self: Question) -> str

Set: Text(self: Question)=value
"""



class QuestionConstants(object):
 """ QuestionConstants() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return QuestionConstants()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 PreReceiptsArchive='PreReceiptsArchive'
 PreReceiptsDelete='PreReceiptsDelete'
 PreReceiptsSave='PreReceiptsSave'
 PrintRmaInvoice='PrintRmaInvoice'


class Questions(List):
 """ Questions() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Questions()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def ContainsKey(self,key):
  """ ContainsKey(self: Questions,key: str) -> bool """
  pass
 def IndexOf(self,*__args):
  """ IndexOf(self: Questions,Key: str) -> int """
  pass
 def IsQuestionAnswered(self,key):
  """ IsQuestionAnswered(self: Questions,key: str) -> bool """
  pass
 def ToString(self):
  """
  ToString(self: Questions) -> str
  
   Returns a System.String that represents the current System.Object.
   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 def __str__(self,*args):
  pass
 CountNotAnswered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CountNotAnswered(self: Questions) -> int

"""



class RemotingException(Exception):
 """
 RemotingException()
 RemotingException(message: str)
 RemotingException(message: str,innerEx: Exception)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return RemotingException()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message=None,innerEx=None):
  """
  __new__(cls: type)
  __new__(cls: type,message: str)
  __new__(cls: type,message: str,innerEx: Exception)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 SerializeObjectState=None


class RemotingArgumentException(RemotingException):
 """
 RemotingArgumentException()
 RemotingArgumentException(message: str)
 RemotingArgumentException(message: str,inner: Exception)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return RemotingArgumentException()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message=None,inner=None):
  """
  __new__(cls: type)
  __new__(cls: type,message: str)
  __new__(cls: type,message: str,inner: Exception)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 SerializeObjectState=None


class RemotingDbException(RemotingException):
 """
 RemotingDbException()
 RemotingDbException(Message: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return RemotingDbException()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,Message=None):
  """
  __new__(cls: type)
  __new__(cls: type,Message: str)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 SerializeObjectState=None


class RemotingInsufficientRightsException(RemotingException):
 """
 RemotingInsufficientRightsException()
 RemotingInsufficientRightsException(message: str)
 RemotingInsufficientRightsException(message: str,innerEx: Exception)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return RemotingInsufficientRightsException()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message=None,innerEx=None):
  """
  __new__(cls: type)
  __new__(cls: type,message: str)
  __new__(cls: type,message: str,innerEx: Exception)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 SerializeObjectState=None


class RemotingLostErpHostException(RemotingException):
 """
 RemotingLostErpHostException()
 RemotingLostErpHostException(message: str)
 RemotingLostErpHostException(message: str,innerEx: Exception)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return RemotingLostErpHostException()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message=None,innerEx=None):
  """
  __new__(cls: type)
  __new__(cls: type,message: str)
  __new__(cls: type,message: str,innerEx: Exception)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 SerializeObjectState=None


class RemotingMessageException(RemotingException):
 """
 RemotingMessageException()
 RemotingMessageException(message: str)
 RemotingMessageException(message: str,innerEx: Exception)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return RemotingMessageException()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message=None,innerEx=None):
  """
  __new__(cls: type)
  __new__(cls: type,message: str)
  __new__(cls: type,message: str,innerEx: Exception)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 SerializeObjectState=None


class RemotingSecurityViolationException(RemotingException):
 """
 RemotingSecurityViolationException()
 RemotingSecurityViolationException(Message: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return RemotingSecurityViolationException()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,Message=None):
  """
  __new__(cls: type)
  __new__(cls: type,Message: str)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 SerializeObjectState=None


class Schedule(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Schedule()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def IsWithinSchedule(self,value):
  """
  IsWithinSchedule(self: Schedule,value: DateTime) -> bool
  
   Determines if the value falls within the schedule
  """
  pass
 @staticmethod
 def Parse(schedule):
  """
  Parse(schedule: str) -> Schedule
  
   schedule: Example: Mon,Tue(0800:1700),Thu,Fri
  """
  pass

class SerializableDictionary(Dictionary):
 """
 SerializableDictionary[TKey,TValue]()
 SerializableDictionary[TKey,TValue](dictionary: IDictionary[TKey,TValue])
 SerializableDictionary[TKey,TValue](info: SerializationInfo,context: StreamingContext)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return SerializableDictionary()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetSchema(self):
  """ GetSchema(self: SerializableDictionary[TKey,TValue]) -> XmlSchema """
  pass
 def ReadXml(self,reader):
  """ ReadXml(self: SerializableDictionary[TKey,TValue],reader: XmlReader) """
  pass
 def WriteXml(self,writer):
  """ WriteXml(self: SerializableDictionary[TKey,TValue],writer: XmlWriter) """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,dictionary: IDictionary[TKey,TValue])
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass

class ServerHealthEnum:
 """ enum ServerHealthEnum,values: DatabaseUpdateNeeded (4),DifferentHookVersions (5),InvalidConnection (2),InvalidLicense (1),NoDatabase (3),NotReady (6),NotRunning (7),Ok (0) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ServerHealthEnum()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 DatabaseUpdateNeeded=None
 DifferentHookVersions=None
 InvalidConnection=None
 InvalidLicense=None
 NoDatabase=None
 NotReady=None
 NotRunning=None
 Ok=None
 value__=None


class Session(object):
 """ Session() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Session()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 AccessId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: AccessId(self: Session) -> str

Set: AccessId(self: Session)=value
"""

 DeviceType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DeviceType(self: Session) -> DeviceTypesEnum

Set: DeviceType(self: Session)=value
"""

 EndPoint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: EndPoint(self: Session) -> str

Set: EndPoint(self: Session)=value
"""

 MachineName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: MachineName(self: Session) -> str

Set: MachineName(self: Session)=value
"""

 RandomNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: RandomNumber(self: Session) -> str

"""

 UserName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: UserName(self: Session) -> str

Set: UserName(self: Session)=value
"""



class Sessions(FindableList):
 """ Sessions() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Sessions()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 DisplayMember='Name'
 ValueMember='Number'


class StateTransition(object):
 """ StateTransition[T](currentStatus: T,newStatus: T) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return StateTransition()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Equals(self,obj):
  """ Equals(self: StateTransition[T],obj: object) -> bool """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: StateTransition[T]) -> int """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,currentStatus,newStatus):
  """ __new__(cls: type,currentStatus: T,newStatus: T) """
  pass
 def __ne__(self,*args):
  pass
 CurrentStatus=None
 NewStatus=None


class Tag(DbObject):
 """
 Tag()
 Tag(description: str,color: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Tag()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Equals(self,obj):
  """ Equals(self: Tag,obj: object) -> bool """
  pass
 @staticmethod
 def FromString(tagAsString):
  """ FromString(tagAsString: str) -> Tag """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: Tag) -> int """
  pass
 @staticmethod
 def New(description,color):
  """ New(description: str,color: str) -> Tag """
  pass
 def ToString(self):
  """ ToString(self: Tag) -> str """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,description=None,color=None):
  """
  __new__(cls: type)
  __new__(cls: type,description: str,color: str)
  """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Color=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Color(self: Tag) -> str

Set: Color(self: Tag)=value
"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Description(self: Tag) -> str

Set: Description(self: Tag)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Id(self: Tag) -> int

Set: Id(self: Tag)=value
"""

 Target=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Target(self: Tag) -> TagTarget

Set: Target(self: Tag)=value
"""

 TargetAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: TargetAsString(self: Tag) -> str

"""



class Tags(List):
 """
 Tags(collection: IEnumerable[Tag])
 Tags()
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Tags()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def ToString(self):
  """ ToString(self: Tags) -> str """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 @staticmethod
 def __new__(self,collection=None):
  """
  __new__(cls: type,collection: IEnumerable[Tag])
  __new__(cls: type)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 def __str__(self,*args):
  pass
 TagsDelimiter=None


class TagTarget:
 """ enum TagTarget,values: Batch (2),NotSet (0),Order (1) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return TagTarget()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Batch=None
 NotSet=None
 Order=None
 value__=None


class ThreadSafeList(object):
 """ ThreadSafeList[T]() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ThreadSafeList()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Clear(self):
  """ Clear(self: ThreadSafeList[T]) """
  pass
 def ContainsKey(self,key):
  """ ContainsKey(self: ThreadSafeList[T],key: str) -> bool """
  pass
 def First(self,comparer):
  pass
 def FirstOrDefault(self,comparer):
  pass
 def GetSchema(self):
  """ GetSchema(self: ThreadSafeList[T]) -> XmlSchema """
  pass
 def ReadXml(self,reader):
  """ ReadXml(self: ThreadSafeList[T],reader: XmlReader) """
  pass
 def Remove(self,*__args):
  """
  Remove(self: ThreadSafeList[T],value: T) -> bool
  Remove(self: ThreadSafeList[T],key: str) -> bool
  """
  pass
 def TryAdd(self,value):
  """ TryAdd(self: ThreadSafeList[T],value: T) -> bool """
  pass
 def TryGet(self,key,value):
  pass
 def TryGetFirst(self,value):
  pass
 def Where(self,comparer):
  """ Where(self: ThreadSafeList[T],comparer: Func[T,bool]) -> List[T] """
  pass
 def WriteXml(self,writer):
  """ WriteXml(self: ThreadSafeList[T],writer: XmlWriter) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Count(self: ThreadSafeList[T]) -> int

"""



class TimeFilterEnum:
 """ enum TimeFilterEnum,values: All (3),Today (0),Tomorrow (1),UpcomingWeek (2) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return TimeFilterEnum()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 All=None
 Today=None
 Tomorrow=None
 UpcomingWeek=None
 value__=None


class TimeFilterHistoryEnum:
 """ enum TimeFilterHistoryEnum,values: All (3),LastWeek (2),Today (0),Yesterday (1) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return TimeFilterHistoryEnum()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 All=None
 LastWeek=None
 Today=None
 value__=None
 Yesterday=None


class UiDataBindingTypeAttribute:
 """ UiDataBindingTypeAttribute(type: DataBindingTypes) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return UiDataBindingTypeAttribute()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def GetDisplayMember(type):
  """
  GetDisplayMember(type: Type) -> str
   Returns: The name of the field that is marked as DisplayMember for Type type
  """
  pass
 @staticmethod
 def GetUniqueIdMember(type):
  """ GetUniqueIdMember(type: Type) -> str """
  pass
 @staticmethod
 def GetValueMember(type):
  """
  GetValueMember(type: Type) -> str
   Returns: The name of the field that is marked as ValueMember for Type type
  """
  pass
 @staticmethod
 def IsDefined(member,type):
  """ IsDefined(member: MemberInfo,type: DataBindingTypes) -> bool """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,type):
  """ __new__(cls: type,type: DataBindingTypes) """
  pass
 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Type(self: UiDataBindingTypeAttribute) -> DataBindingTypes

"""



class UnitTypeEnum:
 """ enum UnitTypeEnum,values: Length (2),Other (1),Time (3),Unspecified (0),Weight (4) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return UnitTypeEnum()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Length=None
 Other=None
 Time=None
 Unspecified=None
 value__=None
 Weight=None


class User(DbObject):
 """ User() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return User()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Equals(self,obj):
  """ Equals(self: User,obj: object) -> bool """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: User) -> int """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 Active=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Active(self: User) -> bool

Set: Active(self: User)=value
"""

 CustomField=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CustomField(self: User) -> str

Set: CustomField(self: User)=value
"""

 EmailAddress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: EmailAddress(self: User) -> str

Set: EmailAddress(self: User)=value
"""

 FullName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: FullName(self: User) -> str

Set: FullName(self: User)=value
"""

 Password=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Password(self: User) -> str

Set: Password(self: User)=value
"""

 PreferredLanguage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Save the preferred language

Get: PreferredLanguage(self: User) -> str

Set: PreferredLanguage(self: User)=value
"""

 UserId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: UserId(self: User) -> int

Set: UserId(self: User)=value
"""

 Username=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Username(self: User) -> str

Set: Username(self: User)=value
"""



class Users(List):
 """ Users() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Users()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 DisplayMember='FullName'
 ValueMember='UserId'


class UserWithSecrets(User):
 """ UserWithSecrets() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return UserWithSecrets()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Hash=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Hash(self: UserWithSecrets) -> str

Set: Hash(self: UserWithSecrets)=value
"""

 Salt=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Salt(self: UserWithSecrets) -> str

Set: Salt(self: UserWithSecrets)=value
"""



class Warning(object):
 """
 Warning()
 Warning(key: str,text: str)
 Warning(key: str,text: str,allowsRetry: bool)
 Warning(key: str,text: str,details: str,allowsRetry: bool)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Warning()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,key=None,text=None,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,key: str,text: str)
  __new__(cls: type,key: str,text: str,allowsRetry: bool)
  __new__(cls: type,key: str,text: str,details: str,allowsRetry: bool)
  """
  pass
 AllowsRetry=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: AllowsRetry(self: Warning) -> bool

Set: AllowsRetry(self: Warning)=value
"""

 Details=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Details(self: Warning) -> str

Set: Details(self: Warning)=value
"""

 Ignore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Ignore(self: Warning) -> bool

Set: Ignore(self: Warning)=value
"""

 Key=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Key(self: Warning) -> str

"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Text(self: Warning) -> str

"""



class Warnings(List):
 """ Warnings() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Warnings()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def ContainsKey(self,key):
  """ ContainsKey(self: Warnings,key: str) -> bool """
  pass
 def IndexOf(self,*__args):
  """ IndexOf(self: Warnings,Key: str) -> int """
  pass
 def ToString(self):
  """
  ToString(self: Warnings) -> str
  
   Returns a System.String that represents the current System.Object.
   Returns: A System.String that represents the current System.Object.
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 def __str__(self,*args):
  pass
 CountNotIgnored=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CountNotIgnored(self: Warnings) -> int

"""



# variables with complex values

