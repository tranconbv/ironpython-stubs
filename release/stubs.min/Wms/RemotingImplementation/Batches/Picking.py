# encoding: utf-8
# module Wms.RemotingImplementation.Batches.Picking calls itself Picking
# from Wms.RemotingImplementation,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class RegularPicker(object):
 """ RegularPicker(args: PickingArgs,outboundOrderLines: OutboundOrderLines,itemPickLocations: ItemPickLocations) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return RegularPicker()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Dispose(self):
  """ Dispose(self: RegularPicker) """
  pass
 def Pick(self,dfObject):
  """ Pick(self: RegularPicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
  pass
 def Putback(self,dfObject):
  """ Putback(self: RegularPicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
  pass
 def ReoccupyOutboundOrderLines(self,*args):
  """ ReoccupyOutboundOrderLines(self: RegularPicker) """
  pass
 def RollBack(self,*args):
  """ RollBack(self: RegularPicker) """
  pass
 def Validate(self,dfObject):
  """ Validate(self: RegularPicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
  pass
 def ValidatePutback(self,dfObject):
  """ ValidatePutback(self: RegularPicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
  pass
 def ValidateReferences(self,dfObject):
  """ ValidateReferences(self: RegularPicker,dfObject: DataFlowObject[PickArgs]) -> bool """
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
 def __new__(self,args,outboundOrderLines,itemPickLocations):
  """ __new__(cls: type,args: PickingArgs,outboundOrderLines: OutboundOrderLines,itemPickLocations: ItemPickLocations) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 ItemPickLocations=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemPickLocations(self: RegularPicker) -> ItemPickLocations

"""

 OutboundOrderLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OutboundOrderLines(self: RegularPicker) -> OutboundOrderLines

"""


 _itemPickLocations=None
 _outboundOrderLines=None
 _outboundOrderLinesOriginal=None
 _warehouseCode=None
 _warehouseLocationCode=None


class DifferentLocationAndMorePicker(RegularPicker):
 """ DifferentLocationAndMorePicker(args: PickingArgs,outboundOrderLines: OutboundOrderLines,itemPickLocations: ItemPickLocations) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DifferentLocationAndMorePicker()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def BasicValidation(self,*args):
  """ BasicValidation(self: DifferentLocationAndMorePicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
  pass
 def Pick(self,dfObject):
  """ Pick(self: DifferentLocationAndMorePicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
  pass
 def ReoccupyOutboundOrderLines(self,*args):
  """ ReoccupyOutboundOrderLines(self: RegularPicker) """
  pass
 def RollBack(self,*args):
  """ RollBack(self: RegularPicker) """
  pass
 def Validate(self,dfObject):
  """ Validate(self: DifferentLocationAndMorePicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
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
 def __new__(self,args,outboundOrderLines,itemPickLocations):
  """ __new__(cls: type,args: PickingArgs,outboundOrderLines: OutboundOrderLines,itemPickLocations: ItemPickLocations) """
  pass
 _itemPickLocations=None
 _outboundOrderLines=None
 _outboundOrderLinesOriginal=None
 _warehouseCode=None
 _warehouseLocationCode=None


class DifferentLocationPicker(DifferentLocationAndMorePicker):
 """ DifferentLocationPicker(args: PickingArgs,outboundOrderLines: OutboundOrderLines,itemPickLocations: ItemPickLocations) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DifferentLocationPicker()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def BasicValidation(self,*args):
  """ BasicValidation(self: DifferentLocationAndMorePicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
  pass
 def ReoccupyOutboundOrderLines(self,*args):
  """ ReoccupyOutboundOrderLines(self: RegularPicker) """
  pass
 def RollBack(self,*args):
  """ RollBack(self: RegularPicker) """
  pass
 def Validate(self,dfObject):
  """ Validate(self: DifferentLocationPicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
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
 def __new__(self,args,outboundOrderLines,itemPickLocations):
  """ __new__(cls: type,args: PickingArgs,outboundOrderLines: OutboundOrderLines,itemPickLocations: ItemPickLocations) """
  pass
 _itemPickLocations=None
 _outboundOrderLines=None
 _outboundOrderLinesOriginal=None
 _warehouseCode=None
 _warehouseLocationCode=None


class ItemIdRegularPicker(object):
 """ ItemIdRegularPicker(args: PickingArgs,outboundOrderLines: OutboundOrderLines,itemPickLocations: ItemPickLocations) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ItemIdRegularPicker()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def AddAllocationForRollback(self,line,number,quantity):
  """ AddAllocationForRollback(self: ItemIdRegularPicker,line: OutboundOrderLine,number: str,quantity: Decimal) """
  pass
 def ChangeAllocations(self,itemId):
  """ ChangeAllocations(self: ItemIdRegularPicker,itemId: ItemIdentification) -> bool """
  pass
 def CheckIfStockOfItemIdIsSufficient(self,dfObject):
  """ CheckIfStockOfItemIdIsSufficient(self: ItemIdRegularPicker,dfObject: DataFlowObject[PickArgs]) -> bool """
  pass
 def DeAllocateItemIdOnNonAssignedLines(self,*args):
  """ DeAllocateItemIdOnNonAssignedLines(self: ItemIdRegularPicker,itemIdToRemove: str,qtyToRemove: Decimal,pickLocToEdit: ItemPickLocation) -> bool """
  pass
 def DecreaseAllocatedQuantitiesOnFreeItemIds(self,quantityToRemove,numberToIgnore,warehouseLocationToIgnore):
  """ DecreaseAllocatedQuantitiesOnFreeItemIds(self: ItemIdRegularPicker,quantityToRemove: Decimal,numberToIgnore: str,warehouseLocationToIgnore: str) -> bool """
  pass
 def Dispose(self):
  """ Dispose(self: ItemIdRegularPicker) """
  pass
 def Pick(self,dfObject):
  """ Pick(self: ItemIdRegularPicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
  pass
 def Putback(self,dfObject,itemId):
  """ Putback(self: ItemIdRegularPicker,dfObject: DataFlowObject[PickArgs],itemId: ItemIdentification) -> DataFlowObject[PickArgs] """
  pass
 def ReoccupyOutboundOrderLines(self):
  """ ReoccupyOutboundOrderLines(self: ItemIdRegularPicker) """
  pass
 def RollBack(self):
  """ RollBack(self: ItemIdRegularPicker) """
  pass
 def TryValidateSerialNumberItem(self,*args):
  """ TryValidateSerialNumberItem(self: ItemIdRegularPicker,itemIdNumber: str,dfObject: DataFlowObject[PickArgs]) -> bool """
  pass
 def Validate(self,dfObject):
  """ Validate(self: ItemIdRegularPicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
  pass
 def ValidateParameter(self,dfObject):
  """ ValidateParameter(self: ItemIdRegularPicker,dfObject: DataFlowObject[PickArgs]) -> bool """
  pass
 def ValidatePutback(self,dfObject):
  """ ValidatePutback(self: ItemIdRegularPicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
  pass
 def ValidateReferences(self,dfObject):
  """ ValidateReferences(self: ItemIdRegularPicker,dfObject: DataFlowObject[PickArgs]) -> bool """
  pass
 def ValidateWithoutItemIdentifications(self,dfObject):
  """ ValidateWithoutItemIdentifications(self: ItemIdRegularPicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
  pass
 def ValidateWithPickedItemIds(self,dfObject,qtyFreeOfNumber):
  """ ValidateWithPickedItemIds(self: ItemIdRegularPicker,dfObject: DataFlowObject[PickArgs],qtyFreeOfNumber: Decimal) -> bool """
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
 def __new__(self,args,outboundOrderLines,itemPickLocations):
  """ __new__(cls: type,args: PickingArgs,outboundOrderLines: OutboundOrderLines,itemPickLocations: ItemPickLocations) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 ItemPickLocations=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemPickLocations(self: ItemIdRegularPicker) -> ItemPickLocations

"""

 OutboundOrderLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: OutboundOrderLines(self: ItemIdRegularPicker) -> OutboundOrderLines

"""


 _allocateItemIds=None
 _allocationsAdded=None
 _batchId=None
 _getAvailableStockOnLocationForCurrentBatch=None
 _isSerialNumberItem=None
 _itemCode=None
 _itemPickLocations=None
 _itemPickLocationsOriginal=None
 _outboundOrderLines=None
 _outboundOrderLinesOriginal=None
 _updateDelegate=None
 _warehouseCode=None
 _warehouseLocationCode=None


class ItemIdDifferentLocationAndMorePicker:
 """ ItemIdDifferentLocationAndMorePicker(args: PickingArgs,outboundOrderLines: OutboundOrderLines,itemPickLocations: ItemPickLocations) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ItemIdDifferentLocationAndMorePicker()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def DeAllocateItemIdOnNonAssignedLines(self,*args):
  """ DeAllocateItemIdOnNonAssignedLines(self: ItemIdRegularPicker,itemIdToRemove: str,qtyToRemove: Decimal,pickLocToEdit: ItemPickLocation) -> bool """
  pass
 def DecreaseAllocatedQuantitiesOnFreeItemIds(self,quantityToRemove,numberToIgnore,warehouseLocationToIgnore):
  """ DecreaseAllocatedQuantitiesOnFreeItemIds(self: ItemIdDifferentLocationAndMorePicker,quantityToRemove: Decimal,numberToIgnore: str,warehouseLocationToIgnore: str) -> bool """
  pass
 def Pick(self,dfObject):
  """ Pick(self: ItemIdDifferentLocationAndMorePicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
  pass
 def TryValidateSerialNumberItem(self,*args):
  """ TryValidateSerialNumberItem(self: ItemIdRegularPicker,itemIdNumber: str,dfObject: DataFlowObject[PickArgs]) -> bool """
  pass
 def Validate(self,dfObject):
  """ Validate(self: ItemIdDifferentLocationAndMorePicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
  pass
 def ValidateWithoutItemIdentifications(self,dfObject):
  """ ValidateWithoutItemIdentifications(self: ItemIdDifferentLocationAndMorePicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
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
 def __new__(self,args,outboundOrderLines,itemPickLocations):
  """ __new__(cls: type,args: PickingArgs,outboundOrderLines: OutboundOrderLines,itemPickLocations: ItemPickLocations) """
  pass
 _allocateItemIds=None
 _allocationsAdded=None
 _batchId=None
 _getAvailableStockOnLocationForCurrentBatch=None
 _isSerialNumberItem=None
 _itemCode=None
 _itemPickLocations=None
 _itemPickLocationsOriginal=None
 _outboundOrderLines=None
 _outboundOrderLinesOriginal=None
 _updateDelegate=None
 _warehouseCode=None
 _warehouseLocationCode=None


class ItemIdDifferentLocationPicker:
 """ ItemIdDifferentLocationPicker(args: PickingArgs,outboundOrderLines: OutboundOrderLines,itemPickLocations: ItemPickLocations) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ItemIdDifferentLocationPicker()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def DeAllocateItemIdOnNonAssignedLines(self,*args):
  """ DeAllocateItemIdOnNonAssignedLines(self: ItemIdRegularPicker,itemIdToRemove: str,qtyToRemove: Decimal,pickLocToEdit: ItemPickLocation) -> bool """
  pass
 def TryValidateSerialNumberItem(self,*args):
  """ TryValidateSerialNumberItem(self: ItemIdRegularPicker,itemIdNumber: str,dfObject: DataFlowObject[PickArgs]) -> bool """
  pass
 def Validate(self,dfObject):
  """ Validate(self: ItemIdDifferentLocationPicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
  pass
 def ValidateWithoutItemIdentifications(self,dfObject):
  """ ValidateWithoutItemIdentifications(self: ItemIdDifferentLocationPicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
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
 def __new__(self,args,outboundOrderLines,itemPickLocations):
  """ __new__(cls: type,args: PickingArgs,outboundOrderLines: OutboundOrderLines,itemPickLocations: ItemPickLocations) """
  pass
 _allocateItemIds=None
 _allocationsAdded=None
 _batchId=None
 _getAvailableStockOnLocationForCurrentBatch=None
 _isSerialNumberItem=None
 _itemCode=None
 _itemPickLocations=None
 _itemPickLocationsOriginal=None
 _outboundOrderLines=None
 _outboundOrderLinesOriginal=None
 _updateDelegate=None
 _warehouseCode=None
 _warehouseLocationCode=None


class ItemIdMorePicker:
 """ ItemIdMorePicker(args: PickingArgs,outboundOrderLines: OutboundOrderLines,itemPickLocations: ItemPickLocations) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ItemIdMorePicker()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def DeAllocateItemIdOnNonAssignedLines(self,*args):
  """ DeAllocateItemIdOnNonAssignedLines(self: ItemIdRegularPicker,itemIdToRemove: str,qtyToRemove: Decimal,pickLocToEdit: ItemPickLocation) -> bool """
  pass
 def Pick(self,dfObject):
  """ Pick(self: ItemIdMorePicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
  pass
 def Putback(self,dfObject,itemId):
  """ Putback(self: ItemIdMorePicker,dfObject: DataFlowObject[PickArgs],itemId: ItemIdentification) -> DataFlowObject[PickArgs] """
  pass
 def TryValidateSerialNumberItem(self,*args):
  """ TryValidateSerialNumberItem(self: ItemIdRegularPicker,itemIdNumber: str,dfObject: DataFlowObject[PickArgs]) -> bool """
  pass
 def Validate(self,dfObject):
  """ Validate(self: ItemIdMorePicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
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
 def __new__(self,args,outboundOrderLines,itemPickLocations):
  """ __new__(cls: type,args: PickingArgs,outboundOrderLines: OutboundOrderLines,itemPickLocations: ItemPickLocations) """
  pass
 _allocateItemIds=None
 _allocationsAdded=None
 _batchId=None
 _getAvailableStockOnLocationForCurrentBatch=None
 _isSerialNumberItem=None
 _itemCode=None
 _itemPickLocations=None
 _itemPickLocationsOriginal=None
 _outboundOrderLines=None
 _outboundOrderLinesOriginal=None
 _updateDelegate=None
 _warehouseCode=None
 _warehouseLocationCode=None


class MorePicker(RegularPicker):
 """ MorePicker(args: PickingArgs,outboundOrderLines: OutboundOrderLines,itemPickLocations: ItemPickLocations) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return MorePicker()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Pick(self,dfObject):
  """ Pick(self: MorePicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
  pass
 def Putback(self,dfObject):
  """ Putback(self: MorePicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
  pass
 def ReoccupyOutboundOrderLines(self,*args):
  """ ReoccupyOutboundOrderLines(self: RegularPicker) """
  pass
 def RollBack(self,*args):
  """ RollBack(self: RegularPicker) """
  pass
 def Validate(self,dfObject):
  """ Validate(self: MorePicker,dfObject: DataFlowObject[PickArgs]) -> DataFlowObject[PickArgs] """
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
 def __new__(self,args,outboundOrderLines,itemPickLocations):
  """ __new__(cls: type,args: PickingArgs,outboundOrderLines: OutboundOrderLines,itemPickLocations: ItemPickLocations) """
  pass
 _itemPickLocations=None
 _outboundOrderLines=None
 _outboundOrderLinesOriginal=None
 _warehouseCode=None
 _warehouseLocationCode=None


class PickerFactory(object):
 """ PickerFactory(args: PickingArgs) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PickerFactory()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def CreateItemIdPicker(self):
  """ CreateItemIdPicker(self: PickerFactory) -> ItemIdRegularPicker """
  pass
 def CreatePicker(self):
  """ CreatePicker(self: PickerFactory) -> RegularPicker """
  pass
 def Dispose(self):
  """ Dispose(self: PickerFactory) """
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
 def __new__(self,args):
  """ __new__(cls: type,args: PickingArgs) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass

class PickFlavour:
 """ enum PickFlavour,values: ChangeRoute (2),DeliverMore (1),DeliverMoreAndChangeRoute (3),Regular (0) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PickFlavour()
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
 ChangeRoute=None
 DeliverMore=None
 DeliverMoreAndChangeRoute=None
 Regular=None
 value__=None


class PickingArgs(object):
 """ PickingArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PickingArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Batch=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Batch(self: PickingArgs) -> Batch

Set: Batch(self: PickingArgs)=value
"""

 IsPicking=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsPicking(self: PickingArgs) -> bool

Set: IsPicking(self: PickingArgs)=value
"""

 ItemCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemCode(self: PickingArgs) -> str

Set: ItemCode(self: PickingArgs)=value
"""

 ItemId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ItemId(self: PickingArgs) -> ItemIdentification

Set: ItemId(self: PickingArgs)=value
"""

 Quantity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Quantity(self: PickingArgs) -> Decimal

Set: Quantity(self: PickingArgs)=value
"""

 WarehouseCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WarehouseCode(self: PickingArgs) -> str

Set: WarehouseCode(self: PickingArgs)=value
"""

 WarehouseLocationCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: WarehouseLocationCode(self: PickingArgs) -> str

Set: WarehouseLocationCode(self: PickingArgs)=value
"""


 GetAvailableStockOnLocationForCurrentBatch=None
 GetAvailableStockOnLocationForCurrentBatchDelegate=None
 UpdateAllocation=None
 UpdateAllocationDelegate=None


