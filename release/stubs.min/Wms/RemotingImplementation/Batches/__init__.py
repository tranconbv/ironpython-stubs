# encoding: utf-8
# module Wms.RemotingImplementation.Batches calls itself Batches
# from Wms.RemotingImplementation,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from System.Collections.Generic import *
from ..__init__ import *

# no functions
# classes

class BatchesExtensions(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return BatchesExtensions()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def ExtractFastLookupDictionaries(this,batchNames,orderNumbers,lineNumbers,barcodes):
  """ ExtractFastLookupDictionaries(this: Batches) -> (Dictionary[str,str],Dictionary[str,str],Dictionary[str,str],Dictionary[str,str]) """
  pass
 @staticmethod
 def GetUnpackedItemsOfCustomer(batches,customer):
  """ GetUnpackedItemsOfCustomer(batches: IEnumerable[Batch],customer: PackCustomer) -> IEnumerable[ValueTuple[ItemPackLocation,OutboundOrderLine]] """
  pass
 __all__=[
  'ExtractFastLookupDictionaries',
  'GetUnpackedItemsOfCustomer',
 ]


class BatchManager(object):
 """ BatchManager() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return BatchManager()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def CalculateAge(createdAt):
  """ CalculateAge(createdAt: DateTime) -> str """
  pass
 @staticmethod
 def CreateBatchBarcode():
  """ CreateBatchBarcode() -> str """
  pass
 @staticmethod
 def CreateCustomerNumbers(batch):
  """ CreateCustomerNumbers(batch: Batch) """
  pass
 @staticmethod
 def DeleteBatchById(id):
  """ DeleteBatchById(id: str) """
  pass
 @staticmethod
 def DeleteBatchIfNothingChanged(batchCacheKey):
  """ DeleteBatchIfNothingChanged(batchCacheKey: CacheKey) """
  pass
 @staticmethod
 def GetAllBatches():
  """ GetAllBatches() -> Batches """
  pass
 @staticmethod
 def GetApprovedBatches():
  """ GetApprovedBatches() -> Batches """
  pass
 @staticmethod
 def GetBatchByCacheKey(cacheKey):
  """ GetBatchByCacheKey(cacheKey: CacheKey) -> Batch """
  pass
 @staticmethod
 def GetBatchById(id,cacheKey):
  """ GetBatchById(id: str) -> (Batch,CacheKey) """
  pass
 @staticmethod
 def GetBatchesByIds(batchIds):
  """ GetBatchesByIds(batchIds: List[str]) -> Batches """
  pass
 @staticmethod
 def GetBatchesIncomplete():
  """ GetBatchesIncomplete() -> Batches """
  pass
 @staticmethod
 def GetBatchesIncompleteSimple():
  """ GetBatchesIncompleteSimple() -> BatchBaseList """
  pass
 @staticmethod
 def GetBatchNames(allocatedStockItemReferences,batchNames):
  """ GetBatchNames(allocatedStockItemReferences: List[AllocatedStockItemReference]) -> List[str] """
  pass
 @staticmethod
 def GetCompletedBatches():
  """ GetCompletedBatches() -> Batches """
  pass
 @staticmethod
 def SaveBatch(batch):
  """ SaveBatch(batch: Batch) -> Batch """
  pass
 SyncLock=None


class BatchPackManager(object):
 """ BatchPackManager(stockManager: IStockManager,transportPackages: TransportPackages) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return BatchPackManager()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def AddCodAmountToFirstPackage(self,result):
  """ AddCodAmountToFirstPackage(self: BatchPackManager,result: ErpProcessSalesOrderLinesResult) """
  pass
 def AddHistoryIdsToPackage(self,lines):
  """ AddHistoryIdsToPackage(self: BatchPackManager,lines: OutboundOrderLines) """
  pass
 def CheckQuantityToMoveWithProcessedItems(self,dfObject):
  """ CheckQuantityToMoveWithProcessedItems(self: BatchPackManager,dfObject: DataFlowObject[MoveTransportItemsBetweenTransportPackagesArgs]) -> DataFlowObject[MoveTransportItemsBetweenTransportPackagesArgs] """
  pass
 @staticmethod
 def CleanUpPackages(batch):
  """ CleanUpPackages(batch: Batch) """
  pass
 @staticmethod
 def CleanUpTransportPackages():
  """ CleanUpTransportPackages() """
  pass
 def ClearProcessedQuantities(self):
  """ ClearProcessedQuantities(self: BatchPackManager) """
  pass
 @staticmethod
 def CreateTransportPackages(dfObject,packagesKey):
  """ CreateTransportPackages(dfObject: DataFlowObject[GetItemsToPackArgs]) -> (DataFlowObject[GetItemsToPackArgs],CacheKey) """
  pass
 def Dispose(self):
  """ Dispose(self: BatchPackManager) """
  pass
 def GetBatchesByOrderNumber(self,orderNumber):
  """ GetBatchesByOrderNumber(self: BatchPackManager,orderNumber: str) -> IEnumerable[Batch] """
  pass
 @staticmethod
 def GetCustomersPending(args,customers):
  """ GetCustomersPending(args: GetCustomersWithPendingPackagesArgs) -> (int,PackCustomers) """
  pass
 @staticmethod
 def GetDeliveryDateTime():
  """ GetDeliveryDateTime() -> DateTime """
  pass
 def GetGroupedFulfillableOrderLines(self,mergeSoLines,mergePackLocations,subtractFulfilledQuantities):
  """ GetGroupedFulfillableOrderLines(self: BatchPackManager,mergeSoLines: bool,mergePackLocations: bool,subtractFulfilledQuantities: bool) -> Dictionary[OutboundOrder,OutboundOrderLines] """
  pass
 def GetOutboundOrderLinesForFulFillment(self,outboundOrderLines):
  """ GetOutboundOrderLinesForFulFillment(self: BatchPackManager,outboundOrderLines: IEnumerable[OutboundOrderLine]) -> OutboundOrderLines """
  pass
 def GetOutboundOrderLinesForFulFillmentGrouped(self,outboundOrderLines,mergePackLocations):
  """ GetOutboundOrderLinesForFulFillmentGrouped(self: BatchPackManager,outboundOrderLines: IEnumerable[OutboundOrderLine],mergePackLocations: bool) -> OutboundOrderLines """
  pass
 @staticmethod
 def GetPickupDateTime():
  """ GetPickupDateTime() -> DateTime """
  pass
 def IsContainerBox(self,boxGuid):
  """ IsContainerBox(self: BatchPackManager,boxGuid: Guid) -> bool """
  pass
 def IsEverythingPacked(self):
  """ IsEverythingPacked(self: BatchPackManager) -> bool """
  pass
 def IsSomethingPacked(self):
  """ IsSomethingPacked(self: BatchPackManager) -> bool """
  pass
 def MoveItems(self,fromBoxGuid,toBoxGuid,items,orderNumber,warning):
  """ MoveItems(self: BatchPackManager,fromBoxGuid: Guid,toBoxGuid: Guid,items: TransportItems,orderNumber: str) -> (bool,str) """
  pass
 def RemoveOrdersComplete(self):
  """ RemoveOrdersComplete(self: BatchPackManager) """
  pass
 def RemoveOrdersIncomplete(self):
  """ RemoveOrdersIncomplete(self: BatchPackManager) """
  pass
 def RemoveProcessedOutboundOrderLines(self,order,adjustStock):
  """ RemoveProcessedOutboundOrderLines(self: BatchPackManager,order: OutboundOrder,adjustStock: bool) """
  pass
 def SetPackedUserAndTime(self,orderNumbers):
  """ SetPackedUserAndTime(self: BatchPackManager,orderNumbers: IEnumerable[str]) """
  pass
 def SetQuantityProcessedOnTransportItems(self,lines):
  """ SetQuantityProcessedOnTransportItems(self: BatchPackManager,lines: OutboundOrderLines) """
  pass
 def ValidateStockBeforeProcessPacking(self,dfObject):
  """ ValidateStockBeforeProcessPacking(self: BatchPackManager,dfObject: DataFlowObject[ProcessBatchPackingArgs]) -> bool """
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
 def __new__(self,stockManager,transportPackages):
  """ __new__(cls: type,stockManager: IStockManager,transportPackages: TransportPackages) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass

class BatchPickManager(object):
 """ BatchPickManager(batch: Batch,stock: IStockManager,settings: AllocationSettings) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return BatchPickManager()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def CheckBatchScanForItem(self,args):
  """ CheckBatchScanForItem(self: BatchPickManager,args: BatchScanArgs) -> BatchScanResult """
  pass
 def CheckBatchScanForLocation(self,barcode,warehouseCode,expectedLocationCode):
  """ CheckBatchScanForLocation(self: BatchPickManager,barcode: str,warehouseCode: str,expectedLocationCode: str) -> BatchScanResult """
  pass
 @staticmethod
 def CreateImagesForColliLetters(customers):
  """ CreateImagesForColliLetters(customers: PackCustomers) """
  pass
 def DetermineRoute(self,locations=None):
  """ DetermineRoute(self: BatchPickManager)DetermineRoute(locations: BatchPickLocations) -> BatchPickLocations """
  pass
 def Dispose(self):
  """ Dispose(self: BatchPickManager) """
  pass
 def GetItemIdsAvailable(self,args):
  """ GetItemIdsAvailable(self: BatchPickManager,args: GetItemIdentificationArgs) -> ItemIdentifications """
  pass
 def GetItemsToPickOnLocation(self,warehouseCode,warehouseLocationCode):
  """ GetItemsToPickOnLocation(self: BatchPickManager,warehouseCode: str,warehouseLocationCode: str) -> BatchPickLocations """
  pass
 def GetLocationsPerOrder(self,args,putback):
  """ GetLocationsPerOrder(self: BatchPickManager,args: PickArgs,putback: bool) -> List[ValueTuple[str,ItemPickLocation]] """
  pass
 def MarkPickLocationAsPicked(self,idOfBatchPickLocation):
  """ MarkPickLocationAsPicked(self: BatchPickManager,idOfBatchPickLocation: str) -> BatchPickLocation """
  pass
 def Pick(self,dfObject):
  """ Pick(self: BatchPickManager,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
  pass
 def PickItemId(self,dfObject):
  """ PickItemId(self: BatchPickManager,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
  pass
 def PickItemIdRange(self,item,dfObject):
  """ PickItemIdRange(self: BatchPickManager,item: Item,dfObject: DataFlowObject[PickItemIdRangeArgs]) -> DataFlowObject[PickItemIdRangeArgs] """
  pass
 def PickMultipleItemIds(self,item,itemIds,dfObject):
  """ PickMultipleItemIds(self: BatchPickManager,item: Item,itemIds: List[str],dfObject: DataFlowObject[PickItemIdsArgs]) -> DataFlowObject[PickItemIdsArgs] """
  pass
 def PrepareWarehouseTransferForOrderLines(self,transferDescription,orderLines,recordId,getDestinationLocationForLineDelegate):
  """ PrepareWarehouseTransferForOrderLines(self: BatchPickManager,transferDescription: str,orderLines: IEnumerable[OutboundOrderLine],recordId: int,getDestinationLocationForLineDelegate: OnGetDestinationLocationForLine) -> WarehouseTransfer """
  pass
 def PutBack(self,dfObject):
  """ PutBack(self: BatchPickManager,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
  pass
 def ReallocatePickedOutboundOrderLine(self,containerBoxGuid,orderLine,pickLoc,warehouseCodeTo,warehouseLocationCodeTo,outerReference,innerReference):
  """ ReallocatePickedOutboundOrderLine(self: BatchPickManager,containerBoxGuid: Guid,orderLine: OutboundOrderLine,pickLoc: ItemPickLocation,warehouseCodeTo: str,warehouseLocationCodeTo: str,outerReference: str,innerReference: str) """
  pass
 def ReallocatePickedSalesOrderLines(self,batch,warehouseLocationCodeTo):
  """ ReallocatePickedSalesOrderLines(self: BatchPickManager,batch: Batch,warehouseLocationCodeTo: str) """
  pass
 @staticmethod
 def RecreateBatchPickLocations(batch=None):
  """
  RecreateBatchPickLocations(batch: Batch) -> BatchPickLocations
  RecreateBatchPickLocations(self: BatchPickManager)
  """
  pass
 def RemovePickedLocations(self):
  """ RemovePickedLocations(self: BatchPickManager) """
  pass
 def SetPickProcessed(self):
  """ SetPickProcessed(self: BatchPickManager) """
  pass
 def UpdateColliReference(self,*__args):
  """ UpdateColliReference(self: BatchPickManager,typeToUpdate: ReferenceType,args: PickArgs,orderNumber: str,quantity: Decimal,putBack: bool)UpdateColliReference(self: BatchPickManager,args: PickArgs,putBack: bool) """
  pass
 def UpdateColloReferences(self,args,putBack):
  """ UpdateColloReferences(self: BatchPickManager,args: PickArgs,putBack: bool) """
  pass
 def ValidateBatchedItem(self,selectedBatchPickLocation,itemCode):
  """ ValidateBatchedItem(self: BatchPickManager,selectedBatchPickLocation: BatchPickLocation,itemCode: str) -> DataFlowObject[CacheKey] """
  pass
 def ValidateBatchPickLocation(self,selectedBatchPickLocation,warehouseLocationCode):
  """ ValidateBatchPickLocation(self: BatchPickManager,selectedBatchPickLocation: BatchPickLocation,warehouseLocationCode: str) -> DataFlowObject[CacheKey] """
  pass
 def ValidateIfAllPicked(self):
  """ ValidateIfAllPicked(self: BatchPickManager) -> bool """
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
 def __new__(self,batch,stock,settings):
  """ __new__(cls: type,batch: Batch,stock: IStockManager,settings: AllocationSettings) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 BoxColors=None


class ColliRegistrationResult(object):
 """ ColliRegistrationResult() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ColliRegistrationResult()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def AddCount(self,count):
  """ AddCount(self: ColliRegistrationResult,count: Count) """
  pass
 def AddOrderLineId(self,batchId,lineId):
  """ AddOrderLineId(self: ColliRegistrationResult,batchId: Guid,lineId: int) """
  pass
 AreColliHandled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AreColliHandled(self: ColliRegistrationResult) -> bool

Set: AreColliHandled(self: ColliRegistrationResult)=value
"""

 Counts=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Counts(self: ColliRegistrationResult) -> Dictionary[int,CountForColliRegistration]

"""

 OrderLineIds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderLineIds(self: ColliRegistrationResult) -> Dictionary[Guid,List[int]]

"""



class ColliRegistrator(object):
 """ ColliRegistrator(transportPackages: TransportPackages) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ColliRegistrator()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Dispose(self):
  """ Dispose(self: ColliRegistrator) """
  pass
 def HandleColliForStockRegistration(self):
  """ HandleColliForStockRegistration(self: ColliRegistrator) -> ColliRegistrationResult """
  pass
 @staticmethod
 def UndoColliForStockRegistration(transportPackages,result):
  """ UndoColliForStockRegistration(transportPackages: TransportPackages,result: ColliRegistrationResult) """
  pass
 def ValidateTransportPackage(self,package):
  """ ValidateTransportPackage(self: ColliRegistrator,package: TransportPackage) """
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
 def __new__(self,transportPackages):
  """ __new__(cls: type,transportPackages: TransportPackages) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass

class CountForColliRegistration(object):
 """ CountForColliRegistration() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return CountForColliRegistration()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemCode(self: CountForColliRegistration) -> str

Set: ItemCode(self: CountForColliRegistration)=value
"""

 ItemId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemId(self: CountForColliRegistration) -> ItemIdentification

Set: ItemId(self: CountForColliRegistration)=value
"""

 Quantity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Quantity(self: CountForColliRegistration) -> Decimal

Set: Quantity(self: CountForColliRegistration)=value
"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WarehouseCode(self: CountForColliRegistration) -> str

Set: WarehouseCode(self: CountForColliRegistration)=value
"""

 WarehouseLocationCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WarehouseLocationCode(self: CountForColliRegistration) -> str

Set: WarehouseLocationCode(self: CountForColliRegistration)=value
"""



class PickingList(object):
 """ PickingList() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PickingList()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Create(self,batch):
  """ Create(self: PickingList,batch: Batch) -> BatchPickLocations """
  pass
 def Dispose(self):
  """ Dispose(self: PickingList) """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass

# variables with complex values

