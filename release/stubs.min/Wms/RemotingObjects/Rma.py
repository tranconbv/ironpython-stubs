# encoding: utf-8
# module Wms.RemotingObjects.Rma calls itself Rma
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class DeleteFreeRmaLineArgs(object):
 """ DeleteFreeRmaLineArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DeleteFreeRmaLineArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 CacheKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CacheKey(self: DeleteFreeRmaLineArgs) -> CacheKey

Set: CacheKey(self: DeleteFreeRmaLineArgs)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemCode(self: DeleteFreeRmaLineArgs) -> str

Set: ItemCode(self: DeleteFreeRmaLineArgs)=value
"""

 OrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderNumber(self: DeleteFreeRmaLineArgs) -> str

Set: OrderNumber(self: DeleteFreeRmaLineArgs)=value
"""

 Reason=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Reason(self: DeleteFreeRmaLineArgs) -> str

Set: Reason(self: DeleteFreeRmaLineArgs)=value
"""



class GetHistoryRmaOrderLinesArgs(object):
 """ GetHistoryRmaOrderLinesArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return GetHistoryRmaOrderLinesArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 CustomerNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerNumber(self: GetHistoryRmaOrderLinesArgs) -> str

Set: CustomerNumber(self: GetHistoryRmaOrderLinesArgs)=value
"""

 HistorySalesOrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: HistorySalesOrderNumber(self: GetHistoryRmaOrderLinesArgs) -> str

Set: HistorySalesOrderNumber(self: GetHistoryRmaOrderLinesArgs)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemCode(self: GetHistoryRmaOrderLinesArgs) -> str

Set: ItemCode(self: GetHistoryRmaOrderLinesArgs)=value
"""

 OrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderNumber(self: GetHistoryRmaOrderLinesArgs) -> str

Set: OrderNumber(self: GetHistoryRmaOrderLinesArgs)=value
"""



class GetRmaOrderArgs(object):
 """
 {Delete}
     Arguments wich are used for retrieving RMA orders.
 
 GetRmaOrderArgs()
 GetRmaOrderArgs(rmaOrderId: int,warehouseCode: str,customerNumber: str,filterText: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return GetRmaOrderArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,rmaOrderId=None,warehouseCode=None,customerNumber=None,filterText=None):
  """
  __new__(cls: type)
  __new__(cls: type,rmaOrderId: int,warehouseCode: str,customerNumber: str,filterText: str)
  """
  pass
 CustomerNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerNumber(self: GetRmaOrderArgs) -> str

Set: CustomerNumber(self: GetRmaOrderArgs)=value
"""

 FilterText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: FilterText(self: GetRmaOrderArgs) -> str

Set: FilterText(self: GetRmaOrderArgs)=value
"""

 RmaOrderId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: RmaOrderId(self: GetRmaOrderArgs) -> int

Set: RmaOrderId(self: GetRmaOrderArgs)=value
"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: WarehouseCode(self: GetRmaOrderArgs) -> str

Set: WarehouseCode(self: GetRmaOrderArgs)=value
"""


 Default=None


class GetRmaOrderCustomersArgs(object):
 """
 Arguments wich are used for retrieving customers from RMA orders.
 
 GetRmaOrderCustomersArgs()
 GetRmaOrderCustomersArgs(warehouseCode: str,filterText: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return GetRmaOrderCustomersArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,warehouseCode=None,filterText=None):
  """
  __new__(cls: type)
  __new__(cls: type,warehouseCode: str,filterText: str)
  """
  pass
 FilterText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: FilterText(self: GetRmaOrderCustomersArgs) -> str

Set: FilterText(self: GetRmaOrderCustomersArgs)=value
"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: WarehouseCode(self: GetRmaOrderCustomersArgs) -> str

Set: WarehouseCode(self: GetRmaOrderCustomersArgs)=value
"""


 Default=None


class GetRmaOrderLinesArgs(object):
 """
 GetRmaOrderLinesArgs()
 GetRmaOrderLinesArgs(orderId: int)
 GetRmaOrderLinesArgs(orderNumber: str)
 GetRmaOrderLinesArgs(orderId: int,orderNumber: str)
 GetRmaOrderLinesArgs(orderId: int,orderNumber: str,warehouseCode: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return GetRmaOrderLinesArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,orderId: int)
  __new__(cls: type,orderNumber: str)
  __new__(cls: type,orderId: int,orderNumber: str)
  __new__(cls: type,orderId: int,orderNumber: str,warehouseCode: str)
  """
  pass
 OrderId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderId(self: GetRmaOrderLinesArgs) -> int

Set: OrderId(self: GetRmaOrderLinesArgs)=value
"""

 OrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderNumber(self: GetRmaOrderLinesArgs) -> str

Set: OrderNumber(self: GetRmaOrderLinesArgs)=value
"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: WarehouseCode(self: GetRmaOrderLinesArgs) -> str

Set: WarehouseCode(self: GetRmaOrderLinesArgs)=value
"""


 Default=None


class RmaOrder:
 """
 Represents a single RMA order. Contains all general information of a purchase order.
    
    It doesn't contain the order lines! Those are gathered by using the Wms.RemotingObjects.Rma.RmaOrderLines and Wms.RemotingObjects.Rma.RmaOrderLine
    objects.
 
 RmaOrder()
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return RmaOrder()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def CreateDummyFromCustomer(orderNumber,warehouseCode,customer):
  """ CreateDummyFromCustomer(orderNumber: str,warehouseCode: str,customer: Customer) -> RmaOrder """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: RmaOrder) -> int """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 CustomerAddressLine1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Address of the customer,containing the street name and number.

Get: CustomerAddressLine1(self: RmaOrder) -> str

Set: CustomerAddressLine1(self: RmaOrder)=value
"""

 CustomerAddressLine2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Second address of the customer,containing the street name and number.

Get: CustomerAddressLine2(self: RmaOrder) -> str

Set: CustomerAddressLine2(self: RmaOrder)=value
"""

 CustomerAddressLine3=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Third address of the customer,containing the street name and number.

Get: CustomerAddressLine3(self: RmaOrder) -> str

Set: CustomerAddressLine3(self: RmaOrder)=value
"""

 CustomerCity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Necessary for Userinterface BOXwise Mobile.

Get: CustomerCity(self: RmaOrder) -> str

Set: CustomerCity(self: RmaOrder)=value
"""

 CustomerContact=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerContact(self: RmaOrder) -> str

Set: CustomerContact(self: RmaOrder)=value
"""

 CustomerContactEmail=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerContactEmail(self: RmaOrder) -> str

Set: CustomerContactEmail(self: RmaOrder)=value
"""

 CustomerCountryCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Necessary for Userinterface BOXwise Mobile.

Get: CustomerCountryCode(self: RmaOrder) -> str

Set: CustomerCountryCode(self: RmaOrder)=value
"""

 CustomerCountryName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerCountryName(self: RmaOrder) -> str

Set: CustomerCountryName(self: RmaOrder)=value
"""

 CustomerName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Necessary for Userinterface BOXwise  Mobile.
   Full name of the customer of the RMA order.

Get: CustomerName(self: RmaOrder) -> str

Set: CustomerName(self: RmaOrder)=value
"""

 CustomerNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Necessary for Userinterface BOXwise  Mobile.

Get: CustomerNumber(self: RmaOrder) -> str

Set: CustomerNumber(self: RmaOrder)=value
"""

 CustomerPhoneNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerPhoneNumber(self: RmaOrder) -> str

Set: CustomerPhoneNumber(self: RmaOrder)=value
"""

 CustomerState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerState(self: RmaOrder) -> str

Set: CustomerState(self: RmaOrder)=value
"""

 CustomerZipCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerZipCode(self: RmaOrder) -> str

Set: CustomerZipCode(self: RmaOrder)=value
"""



class HistoryRmaOrder(RmaOrder):
 """ HistoryRmaOrder() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HistoryRmaOrder()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 GroupGuid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: GroupGuid(self: HistoryRmaOrder) -> Guid

Set: GroupGuid(self: HistoryRmaOrder)=value
"""

 YourReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: YourReference(self: HistoryRmaOrder) -> str

Set: YourReference(self: HistoryRmaOrder)=value
"""



class RmaOrderLine:
 """
 Represents a single order line of a RMA order.
 
 RmaOrderLine()
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return RmaOrderLine()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Clone(self):
  """ Clone(self: RmaOrderLine) -> object """
  pass
 @staticmethod
 def FromHistoryOutboundOrderLine(line,itemDefaultLocation):
  """ FromHistoryOutboundOrderLine(line: HistoryOutboundOrderLine,itemDefaultLocation: str) -> RmaOrderLine """
  pass
 @staticmethod
 def FromItem(item,itemDefaultLocation):
  """ FromItem(item: Item,itemDefaultLocation: str) -> RmaOrderLine """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 HistorySalesOrderId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Id of the salesorder that was used to send the item to the customer.

Get: HistorySalesOrderId(self: RmaOrderLine) -> int

Set: HistorySalesOrderId(self: RmaOrderLine)=value
"""

 HistorySalesOrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Number of the salesorder that was used to send the item to the customer.

Get: HistorySalesOrderNumber(self: RmaOrderLine) -> str

Set: HistorySalesOrderNumber(self: RmaOrderLine)=value
"""

 ItemRmaPrice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ItemRmaPrice(self: RmaOrderLine) -> Decimal

Set: ItemRmaPrice(self: RmaOrderLine)=value
"""

 ReasonCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ReasonCode(self: RmaOrderLine) -> str

Set: ReasonCode(self: RmaOrderLine)=value
"""

 ReasonDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ReasonDescription(self: RmaOrderLine) -> str

Set: ReasonDescription(self: RmaOrderLine)=value
"""



class HistoryRmaOrderLine(RmaOrderLine):
 """ HistoryRmaOrderLine() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HistoryRmaOrderLine()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 DateReceived=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DateReceived(self: HistoryRmaOrderLine) -> DateTime

Set: DateReceived(self: HistoryRmaOrderLine)=value
"""



class HistoryRmaOrderLines(FindableList):
 """ HistoryRmaOrderLines() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HistoryRmaOrderLines()
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
 TotalRowsMatched=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: TotalRowsMatched(self: HistoryRmaOrderLines) -> Int64

Set: TotalRowsMatched(self: HistoryRmaOrderLines)=value
"""



class HistoryRmaOrders(FindableList):
 """ HistoryRmaOrders() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return HistoryRmaOrders()
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
 TotalRowsMatched=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """when paging is used this property holds the total number of rows 
   which are returned by the query

Get: TotalRowsMatched(self: HistoryRmaOrders) -> Int64

Set: TotalRowsMatched(self: HistoryRmaOrders)=value
"""



class ProcessAdhocRmaArgs(object):
 """ ProcessAdhocRmaArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ProcessAdhocRmaArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 CustomerNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CustomerNumber(self: ProcessAdhocRmaArgs) -> str

Set: CustomerNumber(self: ProcessAdhocRmaArgs)=value
"""

 InvoiceLayoutRma=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: InvoiceLayoutRma(self: ProcessAdhocRmaArgs) -> str

Set: InvoiceLayoutRma(self: ProcessAdhocRmaArgs)=value
"""

 PrintRmaInvoices=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: PrintRmaInvoices(self: ProcessAdhocRmaArgs) -> bool

Set: PrintRmaInvoices(self: ProcessAdhocRmaArgs)=value
"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: WarehouseCode(self: ProcessAdhocRmaArgs) -> str

Set: WarehouseCode(self: ProcessAdhocRmaArgs)=value
"""

 YourReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: YourReference(self: ProcessAdhocRmaArgs) -> str

Set: YourReference(self: ProcessAdhocRmaArgs)=value
"""



class ReceiveRmaArgs(ReceiveArgs):
 """ ReceiveRmaArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReceiveRmaArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetIdString(self):
  """ GetIdString(self: ReceiveRmaArgs) -> str """
  pass
 HistoryOrderId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: HistoryOrderId(self: ReceiveRmaArgs) -> int

Set: HistoryOrderId(self: ReceiveRmaArgs)=value
"""

 HistoryOrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: HistoryOrderNumber(self: ReceiveRmaArgs) -> str

Set: HistoryOrderNumber(self: ReceiveRmaArgs)=value
"""

 QuantityDeliveredOnOrder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: QuantityDeliveredOnOrder(self: ReceiveRmaArgs) -> Decimal

Set: QuantityDeliveredOnOrder(self: ReceiveRmaArgs)=value
"""

 RmaReason=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: RmaReason(self: ReceiveRmaArgs) -> RmaReason

Set: RmaReason(self: ReceiveRmaArgs)=value
"""



class ReceiveAdhocRmaArgs(ReceiveRmaArgs):
 """ ReceiveAdhocRmaArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReceiveAdhocRmaArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 ModifiedReceiveLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Contains the modified Wms.RemotingObjects.Rma.RmaReceiveLines of the orginal Wms.RemotingObjects.Rma.RmaReceiveLines
   which were created for an adhoc Touch RMA.

Get: ModifiedReceiveLines(self: ReceiveAdhocRmaArgs) -> RmaReceiveLines

Set: ModifiedReceiveLines(self: ReceiveAdhocRmaArgs)=value
"""

 OrderKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderKey(self: ReceiveAdhocRmaArgs) -> int

Set: OrderKey(self: ReceiveAdhocRmaArgs)=value
"""

 ReceivedReceiveLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ReceivedReceiveLines(self: ReceiveAdhocRmaArgs) -> RmaReceiveLines

Set: ReceivedReceiveLines(self: ReceiveAdhocRmaArgs)=value
"""



class ReceiveRmaMultiArgs(ReceiveItemIdMultiArgs):
 """ ReceiveRmaMultiArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReceiveRmaMultiArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetIdString(self):
  """ GetIdString(self: ReceiveRmaMultiArgs) -> str """
  pass
 HistoryOrderId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: HistoryOrderId(self: ReceiveRmaMultiArgs) -> int

Set: HistoryOrderId(self: ReceiveRmaMultiArgs)=value
"""

 HistoryOrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: HistoryOrderNumber(self: ReceiveRmaMultiArgs) -> str

Set: HistoryOrderNumber(self: ReceiveRmaMultiArgs)=value
"""

 QuantityDeliveredOnOrder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: QuantityDeliveredOnOrder(self: ReceiveRmaMultiArgs) -> Decimal

Set: QuantityDeliveredOnOrder(self: ReceiveRmaMultiArgs)=value
"""

 ReceiveArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ReceiveArgs(self: ReceiveRmaMultiArgs) -> ReceiveRmaArgs

"""

 RmaReason=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: RmaReason(self: ReceiveRmaMultiArgs) -> RmaReason

Set: RmaReason(self: ReceiveRmaMultiArgs)=value
"""

 UnitCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: UnitCode(self: ReceiveRmaMultiArgs) -> str

Set: UnitCode(self: ReceiveRmaMultiArgs)=value
"""



class RmaOrderArgs(object):
 """
 Provides a filter for the RMA orders.
 
 RmaOrderArgs()
 RmaOrderArgs(id: int)
 RmaOrderArgs(id: int,orderNumber: str)
 RmaOrderArgs(warehouseCode: str)
 RmaOrderArgs(warehouseCode: str,customerNumber: str)
 RmaOrderArgs(warehouseCode: str,customerNumber: str,searchText: str)
 RmaOrderArgs(warehouseCode: str,customerNumber: str,searchText: str,groupkey: int)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return RmaOrderArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,id: int)
  __new__(cls: type,id: int,orderNumber: str)
  __new__(cls: type,warehouseCode: str)
  __new__(cls: type,warehouseCode: str,customerNumber: str)
  __new__(cls: type,warehouseCode: str,customerNumber: str,searchText: str)
  __new__(cls: type,warehouseCode: str,customerNumber: str,searchText: str,groupkey: int)
  """
  pass
 CustomerNumber=None
 Default=None
 GroupKey=None
 Id=None
 OrderNumber=None
 SearchText=None
 WarehouseCode=None


class RmaOrderLines:
 """
 Container for the Wms.RemotingObjects.Rma.RmaOrderLine objects.
 
 RmaOrderLines()
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return RmaOrderLines()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def FromIEnumerable(inboundOrderLines):
  """ FromIEnumerable(inboundOrderLines: IEnumerable[InboundOrderLine]) -> RmaOrderLines """
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
 DisplayMember='ItemCode'
 ValueMember='Id'


class RmaOrders:
 """ RmaOrders() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return RmaOrders()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetCacheKey(self):
  """ GetCacheKey(self: RmaOrders) -> int """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: RmaOrders) -> int """
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
 DisplayMember='Number'
 ValueMember='Id'


class RmaReason(object):
 """ RmaReason() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return RmaReason()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Equals(self,obj):
  """ Equals(self: RmaReason,obj: object) -> bool """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: RmaReason) -> int """
  pass
 def ToString(self):
  """ ToString(self: RmaReason) -> str """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __ne__(self,*args):
  pass
 Code=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Code(self: RmaReason) -> str

Set: Code(self: RmaReason)=value
"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Description(self: RmaReason) -> str

Set: Description(self: RmaReason)=value
"""



class RmaReasons(FindableList):
 """ RmaReasons() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return RmaReasons()
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
 DisplayMember='Description'
 ValueMember='Code'


class RmaReceiveLine:
 """ RmaReceiveLine() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return RmaReceiveLine()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Clone(self):
  """ Clone(self: RmaReceiveLine) -> object """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: RmaReceiveLine) -> int """
  pass
 @staticmethod
 def GetIdString(itemCode,unitCode,salesOrderId,rmaReason):
  """ GetIdString(itemCode: str,unitCode: str,salesOrderId: int,rmaReason: RmaReason) -> str """
  pass
 def ValidateOrderIdWithOrderLine(self,*args):
  """ ValidateOrderIdWithOrderLine(self: RmaReceiveLine,orderLine: InboundOrderLine,orderId: int) -> bool """
  pass
 def ValidateOrderNumberWithOrderLine(self,*args):
  """ ValidateOrderNumberWithOrderLine(self: RmaReceiveLine,orderLine: InboundOrderLine,orderNumber: str) -> bool """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 CompareHistoryOutboundOrderNumbers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CompareHistoryOutboundOrderNumbers(self: RmaReceiveLine) -> bool

Set: CompareHistoryOutboundOrderNumbers(self: RmaReceiveLine)=value
"""

 HistorySalesOrderId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: HistorySalesOrderId(self: RmaReceiveLine) -> int

Set: HistorySalesOrderId(self: RmaReceiveLine)=value
"""

 HistorySalesOrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: HistorySalesOrderNumber(self: RmaReceiveLine) -> str

Set: HistorySalesOrderNumber(self: RmaReceiveLine)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Id(self: RmaReceiveLine) -> str

"""

 Reason=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Reason(self: RmaReceiveLine) -> RmaReason

Set: Reason(self: RmaReceiveLine)=value
"""

 ReasonAsString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ReasonAsString(self: RmaReceiveLine) -> str

"""

 SalesOrderAsDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: SalesOrderAsDescription(self: RmaReceiveLine) -> str

"""


 DisplayMember=None
 ValueMember=None


class RmaReceiveLines:
 """
 RmaReceiveLines()
 RmaReceiveLines(compareHistoryOrderNumbers: bool)
 RmaReceiveLines(collection: IEnumerable[InboundReceiveLine])
 RmaReceiveLines(collection: IEnumerable[InboundReceiveLine],compareHistoryOrderNumbers: bool)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return RmaReceiveLines()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Add(self,*__args):
  """ Add(self: RmaReceiveLines,receiveLine: InboundReceiveLine) """
  pass
 def AddLinesFrom(self,orderLines,reason=None):
  """ AddLinesFrom(self: RmaReceiveLines,orderLines: RmaOrderLines,reason: RmaReason) """
  pass
 @staticmethod
 def FromIEnumerable(lines):
  """ FromIEnumerable(lines: IEnumerable[InboundReceiveLine]) -> RmaReceiveLines """
  pass
 def GetIdsOfReceivedOrders(self):
  """ GetIdsOfReceivedOrders(self: RmaReceiveLines) -> List[int] """
  pass
 def GetQuantityReceived(self,predicate):
  """ GetQuantityReceived(self: RmaReceiveLines,predicate: Predicate[InboundReceiveLine]) -> Decimal """
  pass
 def GetQuantityReceivedOfItem(self,*__args):
  """ GetQuantityReceivedOfItem(self: RmaReceiveLines,receiveLineId: str) -> Decimal """
  pass
 def GetReceivedOrderLinesByOrderId(self,orderId):
  """ GetReceivedOrderLinesByOrderId(self: RmaReceiveLines,orderId: int) -> InboundOrderLines """
  pass
 def IndexOf(self,item,index=None,count=None):
  """ IndexOf(self: RmaReceiveLines,lineId: str) -> int """
  pass
 def Sort(self,*__args):
  """ Sort(self: RmaReceiveLines,comparer: Func[InboundReceiveLine,str]) -> InboundReceiveLines """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
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
  __new__(cls: type,compareHistoryOrderNumbers: bool)
  __new__(cls: type,collection: IEnumerable[InboundReceiveLine])
  __new__(cls: type,collection: IEnumerable[InboundReceiveLine],compareHistoryOrderNumbers: bool)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 CompareHistoryOutboundOrderNumbers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: CompareHistoryOutboundOrderNumbers(self: RmaReceiveLines) -> bool

Set: CompareHistoryOutboundOrderNumbers(self: RmaReceiveLines)=value
"""

 OrderIds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderIds(self: RmaReceiveLines) -> Dictionary[int,str]

"""

 OrderNumberList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: OrderNumberList(self: RmaReceiveLines) -> str

"""



