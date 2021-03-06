# encoding: utf-8
# module Wms.RemotingImplementation.Stock calls itself Stock
# from Wms.RemotingImplementation,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class AllocatedStockArgs(object):
 """ AllocatedStockArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return AllocatedStockArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemCode(self: AllocatedStockArgs) -> str

Set: ItemCode(self: AllocatedStockArgs)=value
"""

 ItemDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemDescription(self: AllocatedStockArgs) -> str

Set: ItemDescription(self: AllocatedStockArgs)=value
"""

 ItemIds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemIds(self: AllocatedStockArgs) -> ItemIdentifications

Set: ItemIds(self: AllocatedStockArgs)=value
"""

 LineNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LineNumber(self: AllocatedStockArgs) -> str

Set: LineNumber(self: AllocatedStockArgs)=value
"""

 OrderId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderId(self: AllocatedStockArgs) -> str

Set: OrderId(self: AllocatedStockArgs)=value
"""

 OrderLineId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderLineId(self: AllocatedStockArgs) -> str

Set: OrderLineId(self: AllocatedStockArgs)=value
"""

 OrderNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderNumber(self: AllocatedStockArgs) -> str

Set: OrderNumber(self: AllocatedStockArgs)=value
"""

 Quantity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Quantity(self: AllocatedStockArgs) -> Decimal

Set: Quantity(self: AllocatedStockArgs)=value
"""

 ReferenceId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ReferenceId(self: AllocatedStockArgs) -> AllocatedStockItemReference

Set: ReferenceId(self: AllocatedStockArgs)=value
"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WarehouseCode(self: AllocatedStockArgs) -> str

Set: WarehouseCode(self: AllocatedStockArgs)=value
"""

 WarehouseLocationCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WarehouseLocationCode(self: AllocatedStockArgs) -> str

Set: WarehouseLocationCode(self: AllocatedStockArgs)=value
"""



class AddAllocatedStockArgs(AllocatedStockArgs):
 """ AddAllocatedStockArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return AddAllocatedStockArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 IsItemIdentificationItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsItemIdentificationItem(self: AddAllocatedStockArgs) -> bool

Set: IsItemIdentificationItem(self: AddAllocatedStockArgs)=value
"""

 ItemIdentificationRegistration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemIdentificationRegistration(self: AddAllocatedStockArgs) -> ItemIdentificationRegistration

Set: ItemIdentificationRegistration(self: AddAllocatedStockArgs)=value
"""

 ItemIdentificationToAdd=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemIdentificationToAdd(self: AddAllocatedStockArgs) -> ItemIdentification

Set: ItemIdentificationToAdd(self: AddAllocatedStockArgs)=value
"""



class AllocationSettings(object):
 """ AllocationSettings() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return AllocationSettings()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetLocationsForLine(self,line,locs):
  """ GetLocationsForLine(self: AllocationSettings,line: OutboundOrderLine,locs: IEnumerable[ItemStock]) -> IEnumerable[ItemStock] """
  pass
 DecrementStock=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DecrementStock(self: AllocationSettings) -> bool

Set: DecrementStock(self: AllocationSettings)=value
"""

 ExcludeBlockedItemIdentifications=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExcludeBlockedItemIdentifications(self: AllocationSettings) -> bool

Set: ExcludeBlockedItemIdentifications(self: AllocationSettings)=value
"""

 ForbiddenLocations=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ForbiddenLocations(self: AllocationSettings) -> List[Location]

Set: ForbiddenLocations(self: AllocationSettings)=value
"""

 GetLocationsForLineDelegate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GetLocationsForLineDelegate(self: AllocationSettings) -> OnGetLocationsForLine

Set: GetLocationsForLineDelegate(self: AllocationSettings)=value
"""

 IgnoreAllocations=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IgnoreAllocations(self: AllocationSettings) -> bool

Set: IgnoreAllocations(self: AllocationSettings)=value
"""

 IgnoreBlockedForInboundLocations=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IgnoreBlockedForInboundLocations(self: AllocationSettings) -> bool

Set: IgnoreBlockedForInboundLocations(self: AllocationSettings)=value
"""

 IgnoreBlockedForOutboundLocations=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IgnoreBlockedForOutboundLocations(self: AllocationSettings) -> bool

Set: IgnoreBlockedForOutboundLocations(self: AllocationSettings)=value
"""

 LocationSelectionAlgorithm=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LocationSelectionAlgorithm(self: AllocationSettings) -> LocationSelectionAlgorithmType

Set: LocationSelectionAlgorithm(self: AllocationSettings)=value
"""

 OnDecreaseStockWithAssignedStock=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OnDecreaseStockWithAssignedStock(self: AllocationSettings) -> DecreaseStockWithAssignedStock

Set: OnDecreaseStockWithAssignedStock(self: AllocationSettings)=value
"""

 PickTypesToInclude=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PickTypesToInclude(self: AllocationSettings) -> LocationPickTypeEnum

Set: PickTypesToInclude(self: AllocationSettings)=value
"""


 DecreaseStockWithAssignedStock=None
 OnGetLocationsForLine=None


class BatchAllocationSink(object):
 """
 BatchAllocationSink()
 BatchAllocationSink(generatePick2PlaceImage: bool,preferredColumns: int)
 BatchAllocationSink(args: BatchAllocationSinkArgs)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return BatchAllocationSink()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def AddLine(self,*__args):
  """ AddLine(self: BatchAllocationSink,line: OutboundOrderLine,loc: ItemStock)AddLine(self: BatchAllocationSink,orderLine: OutboundOrderLine,location: ItemStock,allocation: AllocatedStockItem) """
  pass
 def CommitMutations(self):
  """ CommitMutations(self: BatchAllocationSink) """
  pass
 def CreateBatch(self,tag):
  """ CreateBatch(self: BatchAllocationSink,tag: object) -> Batch """
  pass
 def GetBatch(self,line,loc):
  """ GetBatch(self: BatchAllocationSink,line: OutboundOrderLine,loc: ItemStock) -> Batch """
  pass
 def GetBatchByTag(self,tag):
  """ GetBatchByTag(self: BatchAllocationSink,tag: object) -> Batch """
  pass
 def GetReferenceId(self,line,loc):
  """ GetReferenceId(self: BatchAllocationSink,line: OutboundOrderLine,loc: ItemStock) -> AllocatedStockItemReference """
  pass
 def RemoveBatchByTag(self,tag):
  """ RemoveBatchByTag(self: BatchAllocationSink,tag: object) """
  pass
 def SyncOrderLineWithAllocation(self,orderLine,allocation):
  """ SyncOrderLineWithAllocation(self: BatchAllocationSink,orderLine: OutboundOrderLine,allocation: AllocatedStockItem) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,generatePick2PlaceImage: bool,preferredColumns: int)
  __new__(cls: type,args: BatchAllocationSinkArgs)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Batches=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Batches(self: BatchAllocationSink) -> Batches

Set: Batches(self: BatchAllocationSink)=value
"""

 DefaultBatch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DefaultBatch(self: BatchAllocationSink) -> Batch

Set: DefaultBatch(self: BatchAllocationSink)=value
"""

 GetBatchDelegate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GetBatchDelegate(self: BatchAllocationSink) -> OnGetBatch

Set: GetBatchDelegate(self: BatchAllocationSink)=value
"""


 OnGetBatch=None


class BatchAllocationSinkArgs(object):
 """ BatchAllocationSinkArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return BatchAllocationSinkArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 GeneratePick2PlaceImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GeneratePick2PlaceImage(self: BatchAllocationSinkArgs) -> bool

Set: GeneratePick2PlaceImage(self: BatchAllocationSinkArgs)=value
"""

 PreferredColumns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreferredColumns(self: BatchAllocationSinkArgs) -> int

Set: PreferredColumns(self: BatchAllocationSinkArgs)=value
"""

 ProcessingMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ProcessingMode(self: BatchAllocationSinkArgs) -> BatchPackProcessingModeEnum

Set: ProcessingMode(self: BatchAllocationSinkArgs)=value
"""



class BatchSink(BatchAllocationSink):
 """
 BatchSink()
 BatchSink(args: BatchAllocationSinkArgs)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return BatchSink()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,args=None):
  """
  __new__(cls: type)
  __new__(cls: type,args: BatchAllocationSinkArgs)
  """
  pass

class DefaultPrintAllocationSettings(AllocationSettings):
 """ DefaultPrintAllocationSettings() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DefaultPrintAllocationSettings()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""

class EnhancedStockAllocater(object):
 """
 EnhancedStockAllocater(stockManager: IStockManager)
 EnhancedStockAllocater(stockManager: IStockManager,settings: AllocationSettings,allocationSink: IAllocationSink)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return EnhancedStockAllocater()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def AllocateLine(self,line):
  """ AllocateLine(self: EnhancedStockAllocater,line: OutboundOrderLine) -> bool """
  pass
 def AllocateLines(self,lines):
  """ AllocateLines(self: EnhancedStockAllocater,lines: IEnumerable[OutboundOrderLine]) """
  pass
 def DeAllocateStockAllocation(self,allocation):
  """ DeAllocateStockAllocation(self: EnhancedStockAllocater,allocation: ItemStockAllocation) """
  pass
 def Dispose(self):
  """ Dispose(self: EnhancedStockAllocater) """
  pass
 def ReAllocateItems(self,referenceId,itemCode,warehouseCode,outboundOrderLines,overwriteAllocation):
  """ ReAllocateItems(self: EnhancedStockAllocater,referenceId: AllocatedStockItemReference,itemCode: str,warehouseCode: str,outboundOrderLines: OutboundOrderLines,overwriteAllocation: bool) """
  pass
 def UpdateAllocationForLine(self,line,warehouseLocationCode,deltaQuantity,itemIdNumber,useAssignedNumber):
  """ UpdateAllocationForLine(self: EnhancedStockAllocater,line: OutboundOrderLine,warehouseLocationCode: str,deltaQuantity: Decimal,itemIdNumber: str,useAssignedNumber: bool) -> bool """
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
 def __new__(self,stockManager,settings=None,allocationSink=None):
  """
  __new__(cls: type,stockManager: IStockManager)
  __new__(cls: type,stockManager: IStockManager,settings: AllocationSettings,allocationSink: IAllocationSink)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 AllocationSink=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AllocationSink(self: EnhancedStockAllocater) -> IAllocationSink

Set: AllocationSink(self: EnhancedStockAllocater)=value
"""

 Settings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Settings(self: EnhancedStockAllocater) -> AllocationSettings

Set: Settings(self: EnhancedStockAllocater)=value
"""



class EnhancedStockManager(object):
 """
 EnhancedStockManager(messaging: IMessaging)
 EnhancedStockManager()
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return EnhancedStockManager()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def AllocateOutboundOrderLine(self,item,allocationSettings,allocationSink):
  """ AllocateOutboundOrderLine(self: EnhancedStockManager,item: KeyValuePair[str,List[OutboundOrderLine]],allocationSettings: AllocationSettings,allocationSink: IAllocationSink) """
  pass
 def AllocateOutboundOrderLines(self,orderLines,allocationSettings,allocationSink):
  """ AllocateOutboundOrderLines(self: EnhancedStockManager,orderLines: IEnumerable[OutboundOrderLine],allocationSettings: AllocationSettings,allocationSink: IAllocationSink) -> bool """
  pass
 def ChangeStock(self,itemCode,location,qty,*__args):
  """ ChangeStock(self: EnhancedStockManager,itemCode: str,location: Location,qty: Decimal,swallowErrors: bool)ChangeStock(self: EnhancedStockManager,itemCode: str,location: Location,qty: Decimal,itemIds: ItemIdentifications,swallowErrors: bool) """
  pass
 def ClearAllocatedStock(self):
  """ ClearAllocatedStock(self: EnhancedStockManager) """
  pass
 def ConsolidateAllocations(self,oldReferenceId,newReferenceId,orderLine,itemLocation):
  """ ConsolidateAllocations(self: EnhancedStockManager,oldReferenceId: AllocatedStockItemReference,newReferenceId: AllocatedStockItemReference,orderLine: OutboundOrderLine,itemLocation: BatchItemLocationBase) """
  pass
 def DeAllocateStock(self,*__args):
  """
  DeAllocateStock(self: EnhancedStockManager,referenceId: AllocatedStockItemReference) -> int
  DeAllocateStock(self: EnhancedStockManager,referenceId: AllocatedStockItemReference,orderLine: OutboundOrderLine,itemLocation: BatchItemLocationBase)DeAllocateStock(self: EnhancedStockManager,allocation: ItemStockAllocation)DeAllocateStock(self: EnhancedStockManager,args: AllocatedStockArgs) -> int
  """
  pass
 def FindFreeStock(self,itemCode,selector,excludeBlockedItemIds,type,referenceId,includeAssignedLines):
  """ FindFreeStock(self: EnhancedStockManager,itemCode: str,selector: Func[ItemStock,bool],excludeBlockedItemIds: bool,type: AssignedItemIdsFilterType,referenceId: AllocatedStockItemReference,includeAssignedLines: bool) -> List[ItemStock] """
  pass
 def FindItemStockAllocations(self,itemCode,selector):
  """ FindItemStockAllocations(self: EnhancedStockManager,itemCode: str,selector: Func[AllocatedStockItem,bool]) -> ItemStockAllocationList """
  pass
 def FindStockAndAllocations(self,*__args):
  """
  FindStockAndAllocations(self: EnhancedStockManager,itemCode: str,stockSelector: Func[ItemStock,bool]) -> List[ItemStockWithAllocations]
  FindStockAndAllocations(self: EnhancedStockManager,filterBy: GetStockManagerListArgs) -> IEnumerable[ItemStockWithAllocations]
  """
  pass
 def FulfillDirectOrderLines(self,directOrder):
  """ FulfillDirectOrderLines(self: EnhancedStockManager,directOrder: DirectOrder) """
  pass
 def FulfillOutboundOrderLines(self,lines,deAllocateStock,adjustStock):
  """ FulfillOutboundOrderLines(self: EnhancedStockManager,lines: IEnumerable[OutboundOrderLine],deAllocateStock: bool,adjustStock: bool) """
  pass
 def GetAllItemIdentifications(self,filterBy):
  """ GetAllItemIdentifications(self: EnhancedStockManager,filterBy: GetAllItemIdentificationsArgs) -> ItemIdentifications """
  pass
 def GetAvailableItemIdsOnLocationIncludingAllocated(self,referenceId,args):
  """ GetAvailableItemIdsOnLocationIncludingAllocated(self: EnhancedStockManager,referenceId: AllocatedStockItemReference,args: GetItemIdentificationArgs) -> ItemIdentifications """
  pass
 def GetBatchableOrderLines(self,input,settings,batchable,nonBatchable):
  """ GetBatchableOrderLines(self: EnhancedStockManager,input: IEnumerable[OutboundOrderLine],settings: AllocationSettings) -> (List[OutboundOrderLine],List[OutboundOrderLine]) """
  pass
 def GetStockAllocator(self,settings,allocationSink):
  """ GetStockAllocator(self: EnhancedStockManager,settings: AllocationSettings,allocationSink: IAllocationSink) -> IStockAllocater """
  pass
 def GetStockByFilter(self,filterBy):
  """ GetStockByFilter(self: EnhancedStockManager,filterBy: GetStockManagerListArgs) -> IEnumerable[ItemStock] """
  pass
 def GetStockOnMatchingFilter(self,filterBy):
  """ GetStockOnMatchingFilter(self: EnhancedStockManager,filterBy: GetStockManagerListArgs) -> IEnumerable[ItemStock] """
  pass
 def GetStockTotals(self,itemCode,warehouseCode):
  """ GetStockTotals(self: EnhancedStockManager,itemCode: str,warehouseCode: str) -> ItemStockTotals """
  pass
 def GetValidPickLocations(self,settings,warehouseCode,itemCode):
  """ GetValidPickLocations(self: EnhancedStockManager,settings: AllocationSettings,warehouseCode: str,itemCode: str) -> ItemStockList """
  pass
 def IsAllocated(self,orderId,lineId,itemCode,referenceIds):
  """ IsAllocated(self: EnhancedStockManager,orderId: Nullable[int],lineId: Nullable[int],itemCode: str) -> (bool,List[AllocatedStockItemReference]) """
  pass
 def MergeErpStock(self,list):
  """ MergeErpStock(self: EnhancedStockManager,list: IEnumerable[ItemStock]) """
  pass
 def ReAllocateItems(self,referenceId,itemCode,warehouseCode,outboundOrderLines,overwriteAllocation):
  """ ReAllocateItems(self: EnhancedStockManager,referenceId: AllocatedStockItemReference,itemCode: str,warehouseCode: str,outboundOrderLines: OutboundOrderLines,overwriteAllocation: bool) """
  pass
 def ReAllocateStock(self,args):
  """ ReAllocateStock(self: EnhancedStockManager,args: ReallocateStockArgs) """
  pass
 def SetGeneral(self,general):
  """ SetGeneral(self: EnhancedStockManager,general: IGeneral) """
  pass
 def TransferItems(self,transfer):
  """ TransferItems(self: EnhancedStockManager,transfer: WarehouseTransfer) """
  pass
 def TryAllocateItemOnLocation(self,args,errorMessage):
  """ TryAllocateItemOnLocation(self: EnhancedStockManager,args: AddAllocatedStockArgs) -> (bool,str) """
  pass
 def UpdateAllocationForOutboundOrderLine(self,line,warehouseLocationCode,quantity,itemIdNumber,useAssignedNumber,allocationSink,allocationSettings):
  """ UpdateAllocationForOutboundOrderLine(self: EnhancedStockManager,line: OutboundOrderLine,warehouseLocationCode: str,quantity: Decimal,itemIdNumber: str,useAssignedNumber: bool,allocationSink: IAllocationSink,allocationSettings: AllocationSettings) -> bool """
  pass
 def ValidateLocation(self,referenceId,warehouseCode,warehouseLocationCode,itemCode,itemIdNumber):
  """ ValidateLocation(self: EnhancedStockManager,referenceId: AllocatedStockItemReference,warehouseCode: str,warehouseLocationCode: str,itemCode: str,itemIdNumber: str) -> Decimal """
  pass
 def ValidateProcessQuantity(self,orderLinesPairs,message):
  """ ValidateProcessQuantity(self: EnhancedStockManager,orderLinesPairs: Dictionary[OutboundOrder,OutboundOrderLines]) -> (bool,str) """
  pass
 def ValidateStockForTransferQuantityOnLocationFrom(self,item,referenceId,message):
  """ ValidateStockForTransferQuantityOnLocationFrom(self: EnhancedStockManager,item: WarehouseTransferItem,referenceId: AllocatedStockItemReference) -> (bool,str) """
  pass
 def Where(self,*__args):
  """
  Where(self: EnhancedStockManager,selector: Func[ItemStock,bool]) -> List[ItemStock]
  Where(self: EnhancedStockManager,filterBy: GetStockManagerListArgs) -> List[ItemStock]
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,messaging=None):
  """
  __new__(cls: type,messaging: IMessaging)
  __new__(cls: type)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass

class IAllocationSink:
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IAllocationSink()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def AddLine(self,*__args):
  """ AddLine(self: IAllocationSink,line: OutboundOrderLine,loc: ItemStock)AddLine(self: IAllocationSink,orderLine: OutboundOrderLine,location: ItemStock,allocation: AllocatedStockItem) """
  pass
 def CommitMutations(self):
  """ CommitMutations(self: IAllocationSink) """
  pass
 def GetReferenceId(self,line,loc):
  """ GetReferenceId(self: IAllocationSink,line: OutboundOrderLine,loc: ItemStock) -> AllocatedStockItemReference """
  pass
 def SyncOrderLineWithAllocation(self,orderLine,allocation):
  """ SyncOrderLineWithAllocation(self: IAllocationSink,orderLine: OutboundOrderLine,allocation: AllocatedStockItem) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class IStockAllocater:
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IStockAllocater()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def AllocateLines(self,lines):
  """ AllocateLines(self: IStockAllocater,lines: IEnumerable[OutboundOrderLine]) """
  pass
 def DeAllocateStockAllocation(self,allocation):
  """ DeAllocateStockAllocation(self: IStockAllocater,allocation: ItemStockAllocation) """
  pass
 def ReAllocateItems(self,referenceId,itemCode,warehouseCode,outboundOrderLines,overwriteAllocation):
  """ ReAllocateItems(self: IStockAllocater,referenceId: AllocatedStockItemReference,itemCode: str,warehouseCode: str,outboundOrderLines: OutboundOrderLines,overwriteAllocation: bool) """
  pass
 def UpdateAllocationForLine(self,line,warehouseLocationCode,deltaQuantity,itemIdNumber,useAssignedNumber):
  """ UpdateAllocationForLine(self: IStockAllocater,line: OutboundOrderLine,warehouseLocationCode: str,deltaQuantity: Decimal,itemIdNumber: str,useAssignedNumber: bool) -> bool """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 AllocationSink=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AllocationSink(self: IStockAllocater) -> IAllocationSink

Set: AllocationSink(self: IStockAllocater)=value
"""

 Settings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Settings(self: IStockAllocater) -> AllocationSettings

Set: Settings(self: IStockAllocater)=value
"""



class IStockManager:
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IStockManager()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def AllocateOutboundOrderLines(self,orderLines,allocationSettings,allocationSink):
  """ AllocateOutboundOrderLines(self: IStockManager,orderLines: IEnumerable[OutboundOrderLine],allocationSettings: AllocationSettings,allocationSink: IAllocationSink) -> bool """
  pass
 def ChangeStock(self,itemCode,location,qty,*__args):
  """ ChangeStock(self: IStockManager,itemCode: str,location: Location,qty: Decimal,swallowErrors: bool)ChangeStock(self: IStockManager,itemCode: str,location: Location,qty: Decimal,itemIds: ItemIdentifications,swallowErrors: bool) """
  pass
 def ClearAllocatedStock(self):
  """ ClearAllocatedStock(self: IStockManager) """
  pass
 def ConsolidateAllocations(self,oldReferenceId,newReferenceId,orderLine,itemLocation):
  """ ConsolidateAllocations(self: IStockManager,oldReferenceId: AllocatedStockItemReference,newReferenceId: AllocatedStockItemReference,orderLine: OutboundOrderLine,itemLocation: BatchItemLocationBase) """
  pass
 def DeAllocateStock(self,*__args):
  """
  DeAllocateStock(self: IStockManager,referenceId: AllocatedStockItemReference) -> int
  DeAllocateStock(self: IStockManager,referenceId: AllocatedStockItemReference,orderLine: OutboundOrderLine,itemLocation: BatchItemLocationBase)DeAllocateStock(self: IStockManager,allocation: ItemStockAllocation)DeAllocateStock(self: IStockManager,args: AllocatedStockArgs) -> int
  """
  pass
 def FindFreeStock(self,itemCode,selector,excludeBlockedItemIds,type,referenceId,includeAssignedLines):
  """ FindFreeStock(self: IStockManager,itemCode: str,selector: Func[ItemStock,bool],excludeBlockedItemIds: bool,type: AssignedItemIdsFilterType,referenceId: AllocatedStockItemReference,includeAssignedLines: bool) -> List[ItemStock] """
  pass
 def FindItemStockAllocations(self,itemCode,selector):
  """ FindItemStockAllocations(self: IStockManager,itemCode: str,selector: Func[AllocatedStockItem,bool]) -> ItemStockAllocationList """
  pass
 def FindStockAndAllocations(self,*__args):
  """
  FindStockAndAllocations(self: IStockManager,filterBy: GetStockManagerListArgs) -> IEnumerable[ItemStockWithAllocations]
  FindStockAndAllocations(self: IStockManager,itemCode: str,stockSelector: Func[ItemStock,bool]) -> List[ItemStockWithAllocations]
  """
  pass
 def FulfillDirectOrderLines(self,directOrder):
  """ FulfillDirectOrderLines(self: IStockManager,directOrder: DirectOrder) """
  pass
 def FulfillOutboundOrderLines(self,lines,deAllocateStock,adjustStock):
  """ FulfillOutboundOrderLines(self: IStockManager,lines: IEnumerable[OutboundOrderLine],deAllocateStock: bool,adjustStock: bool) """
  pass
 def GetAllItemIdentifications(self,filterBy):
  """ GetAllItemIdentifications(self: IStockManager,filterBy: GetAllItemIdentificationsArgs) -> ItemIdentifications """
  pass
 def GetAvailableItemIdsOnLocationIncludingAllocated(self,referenceId,args):
  """ GetAvailableItemIdsOnLocationIncludingAllocated(self: IStockManager,referenceId: AllocatedStockItemReference,args: GetItemIdentificationArgs) -> ItemIdentifications """
  pass
 def GetBatchableOrderLines(self,input,settings,batchable,nonBatchable):
  """ GetBatchableOrderLines(self: IStockManager,input: IEnumerable[OutboundOrderLine],settings: AllocationSettings) -> (List[OutboundOrderLine],List[OutboundOrderLine]) """
  pass
 def GetStockAllocator(self,settings,allocationSink):
  """ GetStockAllocator(self: IStockManager,settings: AllocationSettings,allocationSink: IAllocationSink) -> IStockAllocater """
  pass
 def GetStockByFilter(self,filterBy):
  """ GetStockByFilter(self: IStockManager,filterBy: GetStockManagerListArgs) -> IEnumerable[ItemStock] """
  pass
 def GetStockOnMatchingFilter(self,args):
  """ GetStockOnMatchingFilter(self: IStockManager,args: GetStockManagerListArgs) -> IEnumerable[ItemStock] """
  pass
 def GetStockTotals(self,itemCode,warehouseCode):
  """ GetStockTotals(self: IStockManager,itemCode: str,warehouseCode: str) -> ItemStockTotals """
  pass
 def GetValidPickLocations(self,settings,warehouseCode,itemCode):
  """ GetValidPickLocations(self: IStockManager,settings: AllocationSettings,warehouseCode: str,itemCode: str) -> ItemStockList """
  pass
 def IsAllocated(self,orderId,lineId,itemCode,referenceIds):
  """ IsAllocated(self: IStockManager,orderId: Nullable[int],lineId: Nullable[int],itemCode: str) -> (bool,List[AllocatedStockItemReference]) """
  pass
 def MergeErpStock(self,list):
  """ MergeErpStock(self: IStockManager,list: IEnumerable[ItemStock]) """
  pass
 def ReAllocateItems(self,referenceId,itemCode,warehouseCode,outboundOrderLines,overwriteAllocation):
  """ ReAllocateItems(self: IStockManager,referenceId: AllocatedStockItemReference,itemCode: str,warehouseCode: str,outboundOrderLines: OutboundOrderLines,overwriteAllocation: bool) """
  pass
 def ReAllocateStock(self,args):
  """ ReAllocateStock(self: IStockManager,args: ReallocateStockArgs) """
  pass
 def SetGeneral(self,general):
  """ SetGeneral(self: IStockManager,general: IGeneral) """
  pass
 def TransferItems(self,transfer):
  """ TransferItems(self: IStockManager,transfer: WarehouseTransfer) """
  pass
 def TryAllocateItemOnLocation(self,args,errorMessage):
  """ TryAllocateItemOnLocation(self: IStockManager,args: AddAllocatedStockArgs) -> (bool,str) """
  pass
 def UpdateAllocationForOutboundOrderLine(self,line,warehouseLocationCode,deltaQuantity,itemIdNumber,useAssignedNumber,allocationSink,allocationSettings):
  """ UpdateAllocationForOutboundOrderLine(self: IStockManager,line: OutboundOrderLine,warehouseLocationCode: str,deltaQuantity: Decimal,itemIdNumber: str,useAssignedNumber: bool,allocationSink: IAllocationSink,allocationSettings: AllocationSettings) -> bool """
  pass
 def ValidateLocation(self,referenceId,warehouseCode,warehouseLocationCode,itemCode,itemIdNumber):
  """ ValidateLocation(self: IStockManager,referenceId: AllocatedStockItemReference,warehouseCode: str,warehouseLocationCode: str,itemCode: str,itemIdNumber: str) -> Decimal """
  pass
 def ValidateProcessQuantity(self,orderLinesPairs,message):
  """ ValidateProcessQuantity(self: IStockManager,orderLinesPairs: Dictionary[OutboundOrder,OutboundOrderLines]) -> (bool,str) """
  pass
 def ValidateStockForTransferQuantityOnLocationFrom(self,item,referenceId,message):
  """ ValidateStockForTransferQuantityOnLocationFrom(self: IStockManager,item: WarehouseTransferItem,referenceId: AllocatedStockItemReference) -> (bool,str) """
  pass
 def Where(self,selector):
  """ Where(self: IStockManager,selector: Func[ItemStock,bool]) -> List[ItemStock] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class ItemStockAllocationExtensions(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ItemStockAllocationExtensions()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def EnrichWithBatchData(this,batchNames,orderNumbers,lineNumbers,barcodes):
  """ EnrichWithBatchData(this: ItemStockAllocationList,batchNames: Dictionary[str,str],orderNumbers: Dictionary[str,str],lineNumbers: Dictionary[str,str],barcodes: Dictionary[str,str]) """
  pass
 @staticmethod
 def EnrichWithDirectOrderData(this):
  """ EnrichWithDirectOrderData(this: ItemStockAllocationList) """
  pass
 @staticmethod
 def EnrichWithMessageQueueData(this):
  """ EnrichWithMessageQueueData(this: ItemStockAllocationList) """
  pass
 __all__=[
  'EnrichWithBatchData',
  'EnrichWithDirectOrderData',
  'EnrichWithMessageQueueData',
 ]


class LocationSelectionAlgorithmType:
 """ enum LocationSelectionAlgorithmType,values: AlphabeticSort (1),AlphabeticSortBulkFirst (2),LeastLocations (0),LeastLocationsBulkFirst (3) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return LocationSelectionAlgorithmType()
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
 AlphabeticSort=None
 AlphabeticSortBulkFirst=None
 LeastLocations=None
 LeastLocationsBulkFirst=None
 value__=None


class LockException(Exception):
 """ LockException(message: str) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return LockException()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message):
  """ __new__(cls: type,message: str) """
  pass
 def __str__(self,*args):
  pass
 SerializeObjectState=None


class MessageQueueAllocationSink(object):
 """ MessageQueueAllocationSink(messageReferenceId: Nullable[Guid]) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MessageQueueAllocationSink()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def AddLine(self,*__args):
  """ AddLine(self: MessageQueueAllocationSink,line: OutboundOrderLine,loc: ItemStock)AddLine(self: MessageQueueAllocationSink,orderLine: OutboundOrderLine,location: ItemStock,allocation: AllocatedStockItem) """
  pass
 def CommitMutations(self):
  """ CommitMutations(self: MessageQueueAllocationSink) """
  pass
 def GetReferenceId(self,line,loc):
  """ GetReferenceId(self: MessageQueueAllocationSink,line: OutboundOrderLine,loc: ItemStock) -> AllocatedStockItemReference """
  pass
 def SyncOrderLineWithAllocation(self,orderLine,allocation):
  """ SyncOrderLineWithAllocation(self: MessageQueueAllocationSink,orderLine: OutboundOrderLine,allocation: AllocatedStockItem) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,messageReferenceId):
  """ __new__(cls: type,messageReferenceId: Nullable[Guid]) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass

class MessageQueueStockAllocater(object):
 """ MessageQueueStockAllocater(stockManager: IStockManager,settings: AllocationSettings,allocationSink: IAllocationSink) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MessageQueueStockAllocater()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def AllocateLine(self,line):
  """ AllocateLine(self: MessageQueueStockAllocater,line: OutboundOrderLine) -> bool """
  pass
 def AllocateLines(self,lines):
  """ AllocateLines(self: MessageQueueStockAllocater,lines: IEnumerable[OutboundOrderLine]) """
  pass
 def DeAllocateStockAllocation(self,allocation):
  """ DeAllocateStockAllocation(self: MessageQueueStockAllocater,allocation: ItemStockAllocation) """
  pass
 def Dispose(self):
  """ Dispose(self: MessageQueueStockAllocater) """
  pass
 def ReAllocateItems(self,referenceId,itemCode,warehouseCode,outboundOrderLines,overwriteAllocation):
  """ ReAllocateItems(self: MessageQueueStockAllocater,referenceId: AllocatedStockItemReference,itemCode: str,warehouseCode: str,outboundOrderLines: OutboundOrderLines,overwriteAllocation: bool) """
  pass
 def UpdateAllocationForLine(self,line,warehouseLocationCode,deltaQuantity,itemIdNumber,useAssignedNumber):
  """ UpdateAllocationForLine(self: MessageQueueStockAllocater,line: OutboundOrderLine,warehouseLocationCode: str,deltaQuantity: Decimal,itemIdNumber: str,useAssignedNumber: bool) -> bool """
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
 def __new__(self,stockManager,settings,allocationSink):
  """ __new__(cls: type,stockManager: IStockManager,settings: AllocationSettings,allocationSink: IAllocationSink) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 AllocationSink=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AllocationSink(self: MessageQueueStockAllocater) -> IAllocationSink

Set: AllocationSink(self: MessageQueueStockAllocater)=value
"""

 Settings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Settings(self: MessageQueueStockAllocater) -> AllocationSettings

Set: Settings(self: MessageQueueStockAllocater)=value
"""



class ReallocateStockArgs(object):
 """ ReallocateStockArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReallocateStockArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 AllocationSettings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AllocationSettings(self: ReallocateStockArgs) -> AllocationSettings

Set: AllocationSettings(self: ReallocateStockArgs)=value
"""

 OrderLine=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OrderLine(self: ReallocateStockArgs) -> OutboundOrderLine

Set: OrderLine(self: ReallocateStockArgs)=value
"""

 PickLoc=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PickLoc(self: ReallocateStockArgs) -> ItemPickLocation

Set: PickLoc(self: ReallocateStockArgs)=value
"""

 ReferenceId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ReferenceId(self: ReallocateStockArgs) -> str

Set: ReferenceId(self: ReallocateStockArgs)=value
"""

 WarehouseCodeTo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WarehouseCodeTo(self: ReallocateStockArgs) -> str

Set: WarehouseCodeTo(self: ReallocateStockArgs)=value
"""

 WarehouseLocationCodeTo=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WarehouseLocationCodeTo(self: ReallocateStockArgs) -> str

Set: WarehouseLocationCodeTo(self: ReallocateStockArgs)=value
"""



class StockLock(object):
 """
 StockLock()
 StockLock(exclusive: bool)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return StockLock()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Dispose(self):
  """ Dispose(self: StockLock) """
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
 def __new__(self,exclusive=None):
  """
  __new__(cls: type)
  __new__(cls: type,exclusive: bool)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass

class StockStreamTask(TaskBase):
 """ StockStreamTask(settings: SystemSettings) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return StockStreamTask()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Run(self):
  """ Run(self: StockStreamTask) """
  pass
 @staticmethod
 def __new__(self,settings):
  """ __new__(cls: type,settings: SystemSettings) """
  pass
 Settings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Settings(self: StockStreamTask) -> SystemSettings

Set: Settings(self: StockStreamTask)=value
"""



