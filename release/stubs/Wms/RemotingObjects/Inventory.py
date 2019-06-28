# encoding: utf-8
# module Wms.RemotingObjects.Inventory calls itself Inventory
# from Wms.RemotingObjects, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AddWarehouseTransferItemIdentitificationArgs:
    """
    AddWarehouseTransferItemIdentitificationArgs()
    AddWarehouseTransferItemIdentitificationArgs(itemId: str, quantity: Decimal)
    """
    @staticmethod # known case of __new__
    def __new__(self, itemId=None, quantity=None):
        """
        __new__(cls: type)
        __new__(cls: type, itemId: str, quantity: Decimal)
        """
        pass

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: AddWarehouseTransferItemIdentitificationArgs) -> str

Set: ItemCode(self: AddWarehouseTransferItemIdentitificationArgs) = value
"""

    ItemIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIds(self: AddWarehouseTransferItemIdentitificationArgs) -> List[ItemIdentification]

Set: ItemIds(self: AddWarehouseTransferItemIdentitificationArgs) = value
"""

    ItemType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemType(self: AddWarehouseTransferItemIdentitificationArgs) -> ItemTypeEnum

Set: ItemType(self: AddWarehouseTransferItemIdentitificationArgs) = value
"""

    OverwriteIfExists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OverwriteIfExists(self: AddWarehouseTransferItemIdentitificationArgs) -> bool

Set: OverwriteIfExists(self: AddWarehouseTransferItemIdentitificationArgs) = value
"""



class AddWarehouseTransferQuantityArgs:
    """ AddWarehouseTransferQuantityArgs() """
    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: AddWarehouseTransferQuantityArgs) -> str

Set: ItemCode(self: AddWarehouseTransferQuantityArgs) = value
"""

    ItemType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemType(self: AddWarehouseTransferQuantityArgs) -> ItemTypeEnum

Set: ItemType(self: AddWarehouseTransferQuantityArgs) = value
"""

    OverwriteIfExists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OverwriteIfExists(self: AddWarehouseTransferQuantityArgs) -> bool

Set: OverwriteIfExists(self: AddWarehouseTransferQuantityArgs) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: AddWarehouseTransferQuantityArgs) -> Decimal

Set: Quantity(self: AddWarehouseTransferQuantityArgs) = value
"""



class AllocatedStockItem:
    """ AllocatedStockItem() """
    def Clone(self):
        """ Clone(self: AllocatedStockItem) -> object """
        pass

    def GetUniqueHashCode(self, referenceId=None, itemCode=None, warehouseCode=None, warehouseLocationCode=None, orderId=None, orderLineId=None, isStockAssigned=None):
        """
        GetUniqueHashCode(self: AllocatedStockItem) -> str
        GetUniqueHashCode(referenceId: AllocatedStockItemReference, itemCode: str, warehouseCode: str, warehouseLocationCode: str, orderId: str, orderLineId: str, isStockAssigned: bool) -> str
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Barcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Barcode(self: AllocatedStockItem) -> str

Set: Barcode(self: AllocatedStockItem) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: AllocatedStockItem) -> str

Set: ItemCode(self: AllocatedStockItem) = value
"""

    ItemIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIds(self: AllocatedStockItem) -> ItemIdentifications

Set: ItemIds(self: AllocatedStockItem) = value
"""

    OrderId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderId(self: AllocatedStockItem) -> str

Set: OrderId(self: AllocatedStockItem) = value
"""

    OrderLineId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderLineId(self: AllocatedStockItem) -> str

Set: OrderLineId(self: AllocatedStockItem) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: AllocatedStockItem) -> Decimal

Set: Quantity(self: AllocatedStockItem) = value
"""

    ReferenceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceId(self: AllocatedStockItem) -> AllocatedStockItemReference

Set: ReferenceId(self: AllocatedStockItem) = value
"""

    StockAssigned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StockAssigned(self: AllocatedStockItem) -> bool

Set: StockAssigned(self: AllocatedStockItem) = value
"""

    StockDecrementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StockDecrementType(self: AllocatedStockItem) -> bool

Set: StockDecrementType(self: AllocatedStockItem) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: AllocatedStockItem) -> AllocatedStockItemTypesEnum

"""

    TypeAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeAsString(self: AllocatedStockItem) -> str

"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: AllocatedStockItem) -> str

Set: WarehouseCode(self: AllocatedStockItem) = value
"""

    WarehouseLocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseLocationCode(self: AllocatedStockItem) -> str

Set: WarehouseLocationCode(self: AllocatedStockItem) = value
"""



class AllocatedStockItemReference:
    """
    AllocatedStockItemReference()
    AllocatedStockItemReference(type: AllocatedStockItemTypesEnum, id: str)
    """
    def Clone(self):
        """ Clone(self: AllocatedStockItemReference) -> AllocatedStockItemReference """
        pass

    def Equals(self, *__args):
        """
        Equals(self: AllocatedStockItemReference, other: AllocatedStockItemReference) -> bool
        Equals(self: AllocatedStockItemReference, obj: object) -> bool
        """
        pass

    @staticmethod
    def Get(expandedReference):
        """ Get(expandedReference: str) -> AllocatedStockItemReference """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: AllocatedStockItemReference) -> int """
        pass

    def ToString(self):
        """ ToString(self: AllocatedStockItemReference) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, type=None, id=None):
        """
        __new__(cls: type)
        __new__(cls: type, type: AllocatedStockItemTypesEnum, id: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: AllocatedStockItemReference) -> str

Set: Id(self: AllocatedStockItemReference) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: AllocatedStockItemReference) -> AllocatedStockItemTypesEnum

Set: Type(self: AllocatedStockItemReference) = value
"""



class AllocatedStockItemTypesEnum:
    """ enum AllocatedStockItemTypesEnum, values: Batch (0), DirectOrder (2), MessageQueue (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Batch = None
    DirectOrder = None
    MessageQueue = None
    value__ = None


class AssignedItemIdsFilterType:
    """ enum AssignedItemIdsFilterType, values: AssignedOnly (2), Exclude (1), Include (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AssignedOnly = None
    Exclude = None
    Include = None
    value__ = None


class AssignType:
    """ enum AssignType, values: All (5), ItemId (2), None (0), Production (4), Purchase (3), Stock (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    All = None
    ItemId = None
    None_ =None
    Production = None
    Purchase = None
    Stock = None
    value__ = None


class BatchItemLocationBase:
    """
    BatchItemLocationBase()
    BatchItemLocationBase(itemId: ItemIdentification)
    BatchItemLocationBase(quantity: Decimal)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, itemId: ItemIdentification)
        __new__(cls: type, quantity: Decimal)
        """
        pass

    ItemIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIds(self: BatchItemLocationBase) -> ItemIdentifications

Set: ItemIds(self: BatchItemLocationBase) = value
"""

    LocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationCode(self: BatchItemLocationBase) -> str

Set: LocationCode(self: BatchItemLocationBase) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: BatchItemLocationBase) -> Decimal

Set: Quantity(self: BatchItemLocationBase) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: BatchItemLocationBase) -> str

Set: WarehouseCode(self: BatchItemLocationBase) = value
"""


    _itemIds = None


class ChangeLicensePlateStatusArgs:
    """ ChangeLicensePlateStatusArgs() """
    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ChangeLicensePlateStatusArgs) -> str

Set: Description(self: ChangeLicensePlateStatusArgs) = value
"""

    LicensePlateId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicensePlateId(self: ChangeLicensePlateStatusArgs) -> int

Set: LicensePlateId(self: ChangeLicensePlateStatusArgs) = value
"""

    NewStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewStatus(self: ChangeLicensePlateStatusArgs) -> LicensePlateStatusEnum

Set: NewStatus(self: ChangeLicensePlateStatusArgs) = value
"""



class CheckLicensePlateIntegrityArgs:
    """ CheckLicensePlateIntegrityArgs() """
    AutoChangeStateToActiveIfNotBroken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoChangeStateToActiveIfNotBroken(self: CheckLicensePlateIntegrityArgs) -> bool

Set: AutoChangeStateToActiveIfNotBroken(self: CheckLicensePlateIntegrityArgs) = value
"""

    AutoChangeStateToBrokenIfNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoChangeStateToBrokenIfNot(self: CheckLicensePlateIntegrityArgs) -> bool

Set: AutoChangeStateToBrokenIfNot(self: CheckLicensePlateIntegrityArgs) = value
"""

    LicensePlateId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicensePlateId(self: CheckLicensePlateIntegrityArgs) -> int

Set: LicensePlateId(self: CheckLicensePlateIntegrityArgs) = value
"""



class CheckLicensePlateIntegrityResult:
    """ CheckLicensePlateIntegrityResult() """
    ErrorMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorMessage(self: CheckLicensePlateIntegrityResult) -> str

Set: ErrorMessage(self: CheckLicensePlateIntegrityResult) = value
"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: CheckLicensePlateIntegrityResult) -> bool

Set: IsValid(self: CheckLicensePlateIntegrityResult) = value
"""



class CreateLicensePlateFromReceiptArgs:
    """ CreateLicensePlateFromReceiptArgs() """
    Lp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lp(self: CreateLicensePlateFromReceiptArgs) -> LicensePlate

Set: Lp(self: CreateLicensePlateFromReceiptArgs) = value
"""

    Reference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reference(self: CreateLicensePlateFromReceiptArgs) -> str

Set: Reference(self: CreateLicensePlateFromReceiptArgs) = value
"""



class EnhancedStockAllocations:
    """ EnhancedStockAllocations() """
    def GetSchema(self):
        """ GetSchema(self: EnhancedStockAllocations) -> XmlSchema """
        pass

    def ReadXml(self, reader):
        """ ReadXml(self: EnhancedStockAllocations, reader: XmlReader) """
        pass

    def WriteXml(self, writer):
        """ WriteXml(self: EnhancedStockAllocations, writer: XmlWriter) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    IsDisposable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDisposable(self: EnhancedStockAllocations) -> bool

"""

    IsUserRemovable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUserRemovable(self: EnhancedStockAllocations) -> bool

"""

    Lifetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lifetime(self: EnhancedStockAllocations) -> CacheLifeTimes

"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreserveState(self: EnhancedStockAllocations) -> bool

"""



class FilterOptions:
    """ enum FilterOptions, values: EmptyLocations (2), None (0), StockLocations (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    EmptyLocations = None
    None_ =None
    StockLocations = None
    value__ = None


class GenerateReplenishmentOrdersArgs:
    """
    GenerateReplenishmentOrdersArgs()
    GenerateReplenishmentOrdersArgs(warehouseCodes: List[str])
    """
    @staticmethod # known case of __new__
    def __new__(self, warehouseCodes=None):
        """
        __new__(cls: type)
        __new__(cls: type, warehouseCodes: List[str])
        """
        pass

    WarehouseCodes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCodes(self: GenerateReplenishmentOrdersArgs) -> List[str]

Set: WarehouseCodes(self: GenerateReplenishmentOrdersArgs) = value
"""



class GetAllItemIdentificationsArgs:
    """ GetAllItemIdentificationsArgs() """
    FilterDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilterDate(self: GetAllItemIdentificationsArgs) -> DateTime

Set: FilterDate(self: GetAllItemIdentificationsArgs) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: GetAllItemIdentificationsArgs) -> str

Set: ItemCode(self: GetAllItemIdentificationsArgs) = value
"""

    PagingAmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PagingAmount(self: GetAllItemIdentificationsArgs) -> int

"""

    SearchText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SearchText(self: GetAllItemIdentificationsArgs) -> str

Set: SearchText(self: GetAllItemIdentificationsArgs) = value
"""


    Default = None


class GetAllocationsArgs:
    """ GetAllocationsArgs() """
    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: GetAllocationsArgs) -> str

Set: ItemCode(self: GetAllocationsArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: GetAllocationsArgs) -> str

Set: WarehouseCode(self: GetAllocationsArgs) = value
"""

    WarehouseLocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseLocationCode(self: GetAllocationsArgs) -> str

Set: WarehouseLocationCode(self: GetAllocationsArgs) = value
"""



class GetItemArgs:
    """
    GetItemArgs()
    GetItemArgs(itemCode: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, itemCode=None):
        """
        __new__(cls: type)
        __new__(cls: type, itemCode: str)
        """
        pass

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: GetItemArgs) -> str

Set: ItemCode(self: GetItemArgs) = value
"""


    Default = None


class GetItemIdentificationArgs:
    """
    GetItemIdentificationArgs()
    GetItemIdentificationArgs(item: Item, warehouseCode: str, warehouseLocationCode: str)
    GetItemIdentificationArgs(item: Item, warehouseCode: str, warehouseLocationCode: str, onlyActive: bool)
    GetItemIdentificationArgs(item: Item, warehouseCode: str, warehouseLocationCode: str, itemId: str, onlyActive: bool)
    GetItemIdentificationArgs(item: Item, warehouseCode: str, warehouseLocationCode: str, itemId: str)
    """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, item=None, warehouseCode=None, warehouseLocationCode=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, item: Item, warehouseCode: str, warehouseLocationCode: str)
        __new__(cls: type, item: Item, warehouseCode: str, warehouseLocationCode: str, onlyActive: bool)
        __new__(cls: type, item: Item, warehouseCode: str, warehouseLocationCode: str, itemId: str, onlyActive: bool)
        __new__(cls: type, item: Item, warehouseCode: str, warehouseLocationCode: str, itemId: str)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Item(self: GetItemIdentificationArgs) -> Item

Set: Item(self: GetItemIdentificationArgs) = value
"""

    ItemId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemId(self: GetItemIdentificationArgs) -> str

Set: ItemId(self: GetItemIdentificationArgs) = value
"""

    OnlyActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnlyActive(self: GetItemIdentificationArgs) -> bool

Set: OnlyActive(self: GetItemIdentificationArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: GetItemIdentificationArgs) -> str

Set: WarehouseCode(self: GetItemIdentificationArgs) = value
"""

    WarehouseLocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseLocationCode(self: GetItemIdentificationArgs) -> str

Set: WarehouseLocationCode(self: GetItemIdentificationArgs) = value
"""


    Default = None


class GetItemLocationsArgs:
    """
    GetItemLocationsArgs()
    GetItemLocationsArgs(paging: PagingParams, itemCode: str, warehouseCode: str, onlyDefaultLocation: bool)
    GetItemLocationsArgs(itemCode: str, warehouseCode: str, onlyDefaultLocation: bool)
    GetItemLocationsArgs(itemCode: str, warehouseCode: str, warehouseLocationCode: str, filter: str, onlyDefaultLocation: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, paging: PagingParams, itemCode: str, warehouseCode: str, onlyDefaultLocation: bool)
        __new__(cls: type, itemCode: str, warehouseCode: str, onlyDefaultLocation: bool)
        __new__(cls: type, itemCode: str, warehouseCode: str, warehouseLocationCode: str, filter: str, onlyDefaultLocation: bool)
        """
        pass

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filter(self: GetItemLocationsArgs) -> str

Set: Filter(self: GetItemLocationsArgs) = value
"""

    ForceRefreshOfCachedLocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForceRefreshOfCachedLocations(self: GetItemLocationsArgs) -> bool

Set: ForceRefreshOfCachedLocations(self: GetItemLocationsArgs) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: GetItemLocationsArgs) -> str

Set: ItemCode(self: GetItemLocationsArgs) = value
"""

    OnlyDefaultLocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnlyDefaultLocations(self: GetItemLocationsArgs) -> bool

Set: OnlyDefaultLocations(self: GetItemLocationsArgs) = value
"""

    Paging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Paging(self: GetItemLocationsArgs) -> PagingParams

Set: Paging(self: GetItemLocationsArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: GetItemLocationsArgs) -> str

Set: WarehouseCode(self: GetItemLocationsArgs) = value
"""

    WarehouseLocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseLocationCode(self: GetItemLocationsArgs) -> str

Set: WarehouseLocationCode(self: GetItemLocationsArgs) = value
"""


    Default = None


class GetItemsArgs:
    """ GetItemsArgs() """
    IncludeBlockedItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeBlockedItems(self: GetItemsArgs) -> bool

Set: IncludeBlockedItems(self: GetItemsArgs) = value
"""

    IncludeCostItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeCostItems(self: GetItemsArgs) -> bool

Set: IncludeCostItems(self: GetItemsArgs) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: GetItemsArgs) -> str

Set: ItemCode(self: GetItemsArgs) = value
"""

    SearchText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SearchText(self: GetItemsArgs) -> str

Set: SearchText(self: GetItemsArgs) = value
"""



class GetItemsOnLocationArgs:
    """
    GetItemsOnLocationArgs()
    GetItemsOnLocationArgs(warehouseCode: str, warehouseLocationCode: str)
    GetItemsOnLocationArgs(warehouseCode: str, warehouseLocationCode: str, itemCode: str)
    GetItemsOnLocationArgs(paging: PagingParams, warehouseCode: str, warehouseLocationCode: str)
    GetItemsOnLocationArgs(paging: PagingParams, warehouseCode: str, warehouseLocationCode: str, itemCode: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, warehouseCode: str, warehouseLocationCode: str)
        __new__(cls: type, warehouseCode: str, warehouseLocationCode: str, itemCode: str)
        __new__(cls: type, paging: PagingParams, warehouseCode: str, warehouseLocationCode: str)
        __new__(cls: type, paging: PagingParams, warehouseCode: str, warehouseLocationCode: str, itemCode: str)
        """
        pass

    IncludeItemsWithoutStock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeItemsWithoutStock(self: GetItemsOnLocationArgs) -> bool

Set: IncludeItemsWithoutStock(self: GetItemsOnLocationArgs) = value
"""

    IncludeLicensePlates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeLicensePlates(self: GetItemsOnLocationArgs) -> bool

Set: IncludeLicensePlates(self: GetItemsOnLocationArgs) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: GetItemsOnLocationArgs) -> str

Set: ItemCode(self: GetItemsOnLocationArgs) = value
"""

    Paging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Paging(self: GetItemsOnLocationArgs) -> PagingParams

Set: Paging(self: GetItemsOnLocationArgs) = value
"""

    SearchText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SearchText(self: GetItemsOnLocationArgs) -> str

Set: SearchText(self: GetItemsOnLocationArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: GetItemsOnLocationArgs) -> str

Set: WarehouseCode(self: GetItemsOnLocationArgs) = value
"""

    WarehouseLocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseLocationCode(self: GetItemsOnLocationArgs) -> str

Set: WarehouseLocationCode(self: GetItemsOnLocationArgs) = value
"""


    Default = None


class GetItemsOnLocationLeftToAddToLpArgs:
    """ GetItemsOnLocationLeftToAddToLpArgs() """
    LocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationCode(self: GetItemsOnLocationLeftToAddToLpArgs) -> str

Set: LocationCode(self: GetItemsOnLocationLeftToAddToLpArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: GetItemsOnLocationLeftToAddToLpArgs) -> str

Set: WarehouseCode(self: GetItemsOnLocationLeftToAddToLpArgs) = value
"""



class GetItemStockListArgs:
    """
    GetItemStockListArgs()
    GetItemStockListArgs(itemCode: str, warehouseCode: str, warehouseLocationCode: str)
    GetItemStockListArgs(itemCode: str, warehouseCode: str, warehouseLocationCode: str, filter: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, itemCode=None, warehouseCode=None, warehouseLocationCode=None, filter=None):
        """
        __new__(cls: type)
        __new__(cls: type, itemCode: str, warehouseCode: str, warehouseLocationCode: str)
        __new__(cls: type, itemCode: str, warehouseCode: str, warehouseLocationCode: str, filter: str)
        """
        pass

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filter(self: GetItemStockListArgs) -> str

Set: Filter(self: GetItemStockListArgs) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: GetItemStockListArgs) -> str

Set: ItemCode(self: GetItemStockListArgs) = value
"""

    OnlyDefaultLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnlyDefaultLocation(self: GetItemStockListArgs) -> bool

Set: OnlyDefaultLocation(self: GetItemStockListArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: GetItemStockListArgs) -> str

Set: WarehouseCode(self: GetItemStockListArgs) = value
"""

    WarehouseLocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseLocationCode(self: GetItemStockListArgs) -> str

Set: WarehouseLocationCode(self: GetItemStockListArgs) = value
"""


    Default = None


class GetItemStockTotalsArgs:
    """ GetItemStockTotalsArgs() """
    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: GetItemStockTotalsArgs) -> str

Set: ItemCode(self: GetItemStockTotalsArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: GetItemStockTotalsArgs) -> str

Set: WarehouseCode(self: GetItemStockTotalsArgs) = value
"""



class GetLicensePlateByCodeArgs:
    """ GetLicensePlateByCodeArgs() """
    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: GetLicensePlateByCodeArgs) -> str

Set: Code(self: GetLicensePlateByCodeArgs) = value
"""

    Statusses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Statusses(self: GetLicensePlateByCodeArgs) -> LicensePlateStatusEnum

Set: Statusses(self: GetLicensePlateByCodeArgs) = value
"""



class GetLicensePlateItemAuditLogEntriesArgs:
    """ GetLicensePlateItemAuditLogEntriesArgs() """
    LicensePlateId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicensePlateId(self: GetLicensePlateItemAuditLogEntriesArgs) -> int

Set: LicensePlateId(self: GetLicensePlateItemAuditLogEntriesArgs) = value
"""



class GetLicensePlateItemsArgs:
    """ GetLicensePlateItemsArgs() """
    FilterText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilterText(self: GetLicensePlateItemsArgs) -> str

Set: FilterText(self: GetLicensePlateItemsArgs) = value
"""

    LicensePlateId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicensePlateId(self: GetLicensePlateItemsArgs) -> int

Set: LicensePlateId(self: GetLicensePlateItemsArgs) = value
"""



class GetLicensePlatesArgs:
    """ GetLicensePlatesArgs() """
    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: GetLicensePlatesArgs) -> str

Set: Code(self: GetLicensePlatesArgs) = value
"""

    FilterText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilterText(self: GetLicensePlatesArgs) -> str

Set: FilterText(self: GetLicensePlatesArgs) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: GetLicensePlatesArgs) -> int

Set: Id(self: GetLicensePlatesArgs) = value
"""

    LocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationCode(self: GetLicensePlatesArgs) -> str

Set: LocationCode(self: GetLicensePlatesArgs) = value
"""

    Statusses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Statusses(self: GetLicensePlatesArgs) -> LicensePlateStatusEnum

Set: Statusses(self: GetLicensePlatesArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: GetLicensePlatesArgs) -> str

Set: WarehouseCode(self: GetLicensePlatesArgs) = value
"""



class GetStockListArgs:
    """ GetStockListArgs() """
    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Items(self: GetStockListArgs) -> Items

Set: Items(self: GetStockListArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: GetStockListArgs) -> str

Set: WarehouseCode(self: GetStockListArgs) = value
"""



class GetStockManagerListArgs:
    """ GetStockManagerListArgs() """
    AssignType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssignType(self: GetStockManagerListArgs) -> AssignType

Set: AssignType(self: GetStockManagerListArgs) = value
"""

    ExcludeAssignedStock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExcludeAssignedStock(self: GetStockManagerListArgs) -> bool

Set: ExcludeAssignedStock(self: GetStockManagerListArgs) = value
"""

    FilterDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilterDate(self: GetStockManagerListArgs) -> DateTime

Set: FilterDate(self: GetStockManagerListArgs) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: GetStockManagerListArgs) -> str

Set: ItemCode(self: GetStockManagerListArgs) = value
"""

    ItemIdentification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIdentification(self: GetStockManagerListArgs) -> str

Set: ItemIdentification(self: GetStockManagerListArgs) = value
"""

    LocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationCode(self: GetStockManagerListArgs) -> str

Set: LocationCode(self: GetStockManagerListArgs) = value
"""

    PagingAmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PagingAmount(self: GetStockManagerListArgs) -> int

"""

    ReferenceDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceDescription(self: GetStockManagerListArgs) -> str

Set: ReferenceDescription(self: GetStockManagerListArgs) = value
"""

    SearchText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SearchText(self: GetStockManagerListArgs) -> str

Set: SearchText(self: GetStockManagerListArgs) = value
"""

    ShowAllocationsExceedingStock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowAllocationsExceedingStock(self: GetStockManagerListArgs) -> bool

Set: ShowAllocationsExceedingStock(self: GetStockManagerListArgs) = value
"""

    ShowAllocationsOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowAllocationsOnly(self: GetStockManagerListArgs) -> bool

Set: ShowAllocationsOnly(self: GetStockManagerListArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: GetStockManagerListArgs) -> str

Set: WarehouseCode(self: GetStockManagerListArgs) = value
"""


    Default = None


class GetWarehouseLocationsArgs:
    """
    GetWarehouseLocationsArgs()
    GetWarehouseLocationsArgs(warehouseCode: str)
    GetWarehouseLocationsArgs(paging: PagingParams, warehouseCode: str)
    GetWarehouseLocationsArgs(paging: PagingParams, warehouseCode: str, warehouseLocationCode: str, filter: str)
    GetWarehouseLocationsArgs(warehouseLocationCodeFrom: str, warehouseLocationCodeTo: str, warehouseCode: str, paging: PagingParams)
    """
    def GetHashCode(self):
        """ GetHashCode(self: GetWarehouseLocationsArgs) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, warehouseCode: str)
        __new__(cls: type, paging: PagingParams, warehouseCode: str)
        __new__(cls: type, paging: PagingParams, warehouseCode: str, warehouseLocationCode: str, filter: str)
        __new__(cls: type, warehouseLocationCodeFrom: str, warehouseLocationCodeTo: str, warehouseCode: str, paging: PagingParams)
        """
        pass

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filter(self: GetWarehouseLocationsArgs) -> str

Set: Filter(self: GetWarehouseLocationsArgs) = value
"""

    Paging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Paging(self: GetWarehouseLocationsArgs) -> PagingParams

Set: Paging(self: GetWarehouseLocationsArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: GetWarehouseLocationsArgs) -> str

Set: WarehouseCode(self: GetWarehouseLocationsArgs) = value
"""

    WarehouseLocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseLocationCode(self: GetWarehouseLocationsArgs) -> str

Set: WarehouseLocationCode(self: GetWarehouseLocationsArgs) = value
"""

    WarehouseLocationCodeFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseLocationCodeFrom(self: GetWarehouseLocationsArgs) -> str

Set: WarehouseLocationCodeFrom(self: GetWarehouseLocationsArgs) = value
"""

    WarehouseLocationCodeTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseLocationCodeTo(self: GetWarehouseLocationsArgs) -> str

Set: WarehouseLocationCodeTo(self: GetWarehouseLocationsArgs) = value
"""


    Default = None


class GetWarehousesArgs:
    """
    GetWarehousesArgs()
    GetWarehousesArgs(warehouseCode: str)
    GetWarehousesArgs(active: bool)
    GetWarehousesArgs(active: bool, hasDefaultInboundLocation: bool)
    GetWarehousesArgs(warehouseLocationCode: str, active: bool)
    GetWarehousesArgs(warehouseCode: str, warehouseLocationCode: str, active: bool, defaultInboundLocation: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, warehouseCode: str)
        __new__(cls: type, active: bool)
        __new__(cls: type, active: bool, hasDefaultInboundLocation: bool)
        __new__(cls: type, warehouseLocationCode: str, active: bool)
        __new__(cls: type, warehouseCode: str, warehouseLocationCode: str, active: bool, defaultInboundLocation: str)
        """
        pass

    Active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Active(self: GetWarehousesArgs) -> Nullable[bool]

Set: Active(self: GetWarehousesArgs) = value
"""

    DefaultInboundLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultInboundLocation(self: GetWarehousesArgs) -> str

Set: DefaultInboundLocation(self: GetWarehousesArgs) = value
"""

    HasDefaultInboundLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasDefaultInboundLocation(self: GetWarehousesArgs) -> Nullable[bool]

Set: HasDefaultInboundLocation(self: GetWarehousesArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: GetWarehousesArgs) -> str

Set: WarehouseCode(self: GetWarehousesArgs) = value
"""

    WarehouseLocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseLocationCode(self: GetWarehousesArgs) -> str

Set: WarehouseLocationCode(self: GetWarehousesArgs) = value
"""


    Default = None


class HistoryReplenishmentOrder:
    """ HistoryReplenishmentOrder() """
    def Clone(self):
        """ Clone(self: HistoryReplenishmentOrder) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Number(self: HistoryReplenishmentOrder) -> str

Set: Number(self: HistoryReplenishmentOrder) = value
"""

    ReplenishToLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReplenishToLocation(self: HistoryReplenishmentOrder) -> Location

Set: ReplenishToLocation(self: HistoryReplenishmentOrder) = value
"""

    ReplenishToLocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReplenishToLocationCode(self: HistoryReplenishmentOrder) -> str

"""

    ReplenishToWarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReplenishToWarehouseCode(self: HistoryReplenishmentOrder) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: HistoryReplenishmentOrder) -> OutboundOrderTypeEnum

"""



class HistoryReplenishmentOrders:
    """ HistoryReplenishmentOrders() """
    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[HistoryOutboundOrder]) -> HistoryReplenishmentOrders """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass


class IAllocatedStockItem:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Barcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Barcode(self: IAllocatedStockItem) -> str

Set: Barcode(self: IAllocatedStockItem) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: IAllocatedStockItem) -> str

Set: ItemCode(self: IAllocatedStockItem) = value
"""

    ItemIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIds(self: IAllocatedStockItem) -> ItemIdentifications

Set: ItemIds(self: IAllocatedStockItem) = value
"""

    OrderId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderId(self: IAllocatedStockItem) -> str

Set: OrderId(self: IAllocatedStockItem) = value
"""

    OrderLineId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderLineId(self: IAllocatedStockItem) -> str

Set: OrderLineId(self: IAllocatedStockItem) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: IAllocatedStockItem) -> Decimal

Set: Quantity(self: IAllocatedStockItem) = value
"""

    ReferenceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceId(self: IAllocatedStockItem) -> AllocatedStockItemReference

Set: ReferenceId(self: IAllocatedStockItem) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: IAllocatedStockItem) -> AllocatedStockItemTypesEnum

"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: IAllocatedStockItem) -> str

Set: WarehouseCode(self: IAllocatedStockItem) = value
"""

    WarehouseLocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseLocationCode(self: IAllocatedStockItem) -> str

Set: WarehouseLocationCode(self: IAllocatedStockItem) = value
"""



class Item:
    """ Item() """
    def ExpectedScanType(self, checkRegistration):
        """ ExpectedScanType(self: Item, checkRegistration: bool) -> ExpectScanOfEnum """
        pass

    def IsBatchNumberItemCheck(self, checkRegistration):
        """ IsBatchNumberItemCheck(self: Item, checkRegistration: bool) -> bool """
        pass

    def IsSerialNumberItemCheck(self, checkRegistration):
        """ IsSerialNumberItemCheck(self: Item, checkRegistration: bool) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Active(self: Item) -> bool

Set: Active(self: Item) = value
"""

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: Item) -> str

Set: Code(self: Item) = value
"""

    CodeSupplier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CodeSupplier(self: Item) -> str

Set: CodeSupplier(self: Item) = value
"""

    DefaultCostPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultCostPrice(self: Item) -> Decimal

Set: DefaultCostPrice(self: Item) = value
"""

    DefaultSalesPrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultSalesPrice(self: Item) -> Decimal

Set: DefaultSalesPrice(self: Item) = value
"""

    DefaultVendorBarcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultVendorBarcode(self: Item) -> str

Set: DefaultVendorBarcode(self: Item) = value
"""

    DefaultVendorName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultVendorName(self: Item) -> str

Set: DefaultVendorName(self: Item) = value
"""

    DefaultVendorNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultVendorNumber(self: Item) -> str

Set: DefaultVendorNumber(self: Item) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: Item) -> str

Set: Description(self: Item) = value
"""

    ExpirationDateRequired = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpirationDateRequired(self: Item) -> bool

Set: ExpirationDateRequired(self: Item) = value
"""

    GTINCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GTINCode(self: Item) -> str

Set: GTINCode(self: Item) = value
"""

    IsBatchNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: IsBatchNumberItem(self: Item) = value
"""

    IsCostItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCostItem(self: Item) -> bool

Set: IsCostItem(self: Item) = value
"""

    IsFractionAllowed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFractionAllowed(self: Item) -> bool

Set: IsFractionAllowed(self: Item) = value
"""

    IsSerialNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: IsSerialNumberItem(self: Item) = value
"""

    ItemGroupCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemGroupCode(self: Item) -> str

Set: ItemGroupCode(self: Item) = value
"""

    ItemGroupDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemGroupDescription(self: Item) -> str

Set: ItemGroupDescription(self: Item) = value
"""

    ItemIdRegistration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIdRegistration(self: Item) -> ItemIdentificationRegistration

Set: ItemIdRegistration(self: Item) = value
"""

    ItemType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemType(self: Item) -> ItemTypeEnum

Set: ItemType(self: Item) = value
"""

    ItemWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemWeight(self: Item) -> Decimal

Set: ItemWeight(self: Item) = value
"""

    Lifetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lifetime(self: Item) -> CacheLifeTimes

"""

    TextDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextDescription(self: Item) -> str

Set: TextDescription(self: Item) = value
"""

    UnitCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitCode(self: Item) -> str

Set: UnitCode(self: Item) = value
"""

    UnitType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitType(self: Item) -> UnitTypeEnum

Set: UnitType(self: Item) = value
"""



class ItemBelongsToLicensePlateArgs:
    """ ItemBelongsToLicensePlateArgs() """
    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: ItemBelongsToLicensePlateArgs) -> str

Set: ItemCode(self: ItemBelongsToLicensePlateArgs) = value
"""

    ItemIdentifications = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIdentifications(self: ItemBelongsToLicensePlateArgs) -> ItemIdentifications

Set: ItemIdentifications(self: ItemBelongsToLicensePlateArgs) = value
"""

    LocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationCode(self: ItemBelongsToLicensePlateArgs) -> str

Set: LocationCode(self: ItemBelongsToLicensePlateArgs) = value
"""

    LpStatussesToCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LpStatussesToCheck(self: ItemBelongsToLicensePlateArgs) -> LicensePlateStatusEnum

Set: LpStatussesToCheck(self: ItemBelongsToLicensePlateArgs) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: ItemBelongsToLicensePlateArgs) -> Decimal

Set: Quantity(self: ItemBelongsToLicensePlateArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: ItemBelongsToLicensePlateArgs) -> str

Set: WarehouseCode(self: ItemBelongsToLicensePlateArgs) = value
"""



class ItemIdentificationBase:
    """ ItemIdentificationBase() """
    BeginDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BeginDate(self: ItemIdentificationBase) -> Nullable[DateTime]

Set: BeginDate(self: ItemIdentificationBase) = value
"""

    EndDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndDate(self: ItemIdentificationBase) -> Nullable[DateTime]

Set: EndDate(self: ItemIdentificationBase) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Number(self: ItemIdentificationBase) -> str

Set: Number(self: ItemIdentificationBase) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: ItemIdentificationBase) -> Decimal

Set: Quantity(self: ItemIdentificationBase) = value
"""



class ItemIdentification:
    """
    ItemIdentification()
    ItemIdentification(number: str, quantity: Decimal, endDate: Nullable[DateTime])
    ItemIdentification(number: str, quantityReceived: Decimal, quantityUsed: Decimal, quantityAvailable: Decimal, quantityAssigned: Decimal, beginDate: Nullable[DateTime], endDate: Nullable[DateTime], blocked: bool, quantity: Decimal)
    ItemIdentification(number: str, itemCode: str, quantityReceived: Decimal, quantityUsed: Decimal, quantityAvailable: Decimal, quantityAssigned: Decimal, quantityAllocated: Decimal, quantityAllocatedOriginal: Decimal, quantityOriginal: Decimal, beginDate: Nullable[DateTime], endDate: Nullable[DateTime], blocked: bool, quantity: Decimal, warehouseCode: str, warehouseLocationCode: str)
    """
    def Clone(self):
        """ Clone(self: ItemIdentification) -> object """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ItemIdentification) -> int """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, number=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, number: str, quantity: Decimal, endDate: Nullable[DateTime])
        __new__(cls: type, number: str, quantityReceived: Decimal, quantityUsed: Decimal, quantityAvailable: Decimal, quantityAssigned: Decimal, beginDate: Nullable[DateTime], endDate: Nullable[DateTime], blocked: bool, quantity: Decimal)
        __new__(cls: type, number: str, itemCode: str, quantityReceived: Decimal, quantityUsed: Decimal, quantityAvailable: Decimal, quantityAssigned: Decimal, quantityAllocated: Decimal, quantityAllocatedOriginal: Decimal, quantityOriginal: Decimal, beginDate: Nullable[DateTime], endDate: Nullable[DateTime], blocked: bool, quantity: Decimal, warehouseCode: str, warehouseLocationCode: str)
        """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(c1: ItemIdentification, c2: ItemIdentification) -> ItemIdentification """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(c1: ItemIdentification, c2: ItemIdentification) -> ItemIdentification """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    AllocationAndStockQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllocationAndStockQuantity(self: ItemIdentification) -> str

"""

    Blocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Blocked(self: ItemIdentification) -> bool

Set: Blocked(self: ItemIdentification) = value
"""

    BoxNumbers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoxNumbers(self: ItemIdentification) -> List[int]

Set: BoxNumbers(self: ItemIdentification) = value
"""

    DatesAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DatesAsString(self: ItemIdentification) -> str

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ItemIdentification) -> str

"""

    IsMarkedAsPicked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMarkedAsPicked(self: ItemIdentification) -> bool

Set: IsMarkedAsPicked(self: ItemIdentification) = value
"""

    IsPicked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPicked(self: ItemIdentification) -> bool

"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: ItemIdentification) -> str

Set: ItemCode(self: ItemIdentification) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Number(self: ItemIdentification) -> str

Set: Number(self: ItemIdentification) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: ItemIdentification) -> Decimal

Set: Quantity(self: ItemIdentification) = value
"""

    QuantityAllocated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityAllocated(self: ItemIdentification) -> Decimal

Set: QuantityAllocated(self: ItemIdentification) = value
"""

    QuantityAllocatedOriginal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityAllocatedOriginal(self: ItemIdentification) -> Decimal

Set: QuantityAllocatedOriginal(self: ItemIdentification) = value
"""

    QuantityAssigned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityAssigned(self: ItemIdentification) -> Decimal

Set: QuantityAssigned(self: ItemIdentification) = value
"""

    QuantityAssignedString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityAssignedString(self: ItemIdentification) -> str

"""

    QuantityAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityAvailable(self: ItemIdentification) -> Decimal

Set: QuantityAvailable(self: ItemIdentification) = value
"""

    QuantityOriginal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityOriginal(self: ItemIdentification) -> Decimal

Set: QuantityOriginal(self: ItemIdentification) = value
"""

    QuantityProcessed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityProcessed(self: ItemIdentification) -> Decimal

Set: QuantityProcessed(self: ItemIdentification) = value
"""

    QuantityReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityReceived(self: ItemIdentification) -> Decimal

Set: QuantityReceived(self: ItemIdentification) = value
"""

    QuantityUsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityUsed(self: ItemIdentification) -> Decimal

Set: QuantityUsed(self: ItemIdentification) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: ItemIdentification) -> str

Set: WarehouseCode(self: ItemIdentification) = value
"""

    WarehouseLocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseLocationCode(self: ItemIdentification) -> str

Set: WarehouseLocationCode(self: ItemIdentification) = value
"""



class ItemIdentificationMetaData:
    """
    ItemIdentificationMetaData()
    ItemIdentificationMetaData(itemCode: str, itemId: str, isBlocked: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, itemCode=None, itemId=None, isBlocked=None):
        """
        __new__(cls: type)
        __new__(cls: type, itemCode: str, itemId: str, isBlocked: bool)
        """
        pass

    IsBlocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBlocked(self: ItemIdentificationMetaData) -> bool

Set: IsBlocked(self: ItemIdentificationMetaData) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: ItemIdentificationMetaData) -> str

Set: ItemCode(self: ItemIdentificationMetaData) = value
"""

    ItemId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemId(self: ItemIdentificationMetaData) -> str

Set: ItemId(self: ItemIdentificationMetaData) = value
"""



class ItemIdentificationRegistration:
    """ enum (flags) ItemIdentificationRegistration, values: Complete (1), OnlyOutbound (2), Unknown (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Complete = None
    OnlyOutbound = None
    Unknown = None
    value__ = None


class ItemIdentifications:
    """
    ItemIdentifications()
    ItemIdentifications(itemId: ItemIdentification)
    ItemIdentifications(collection: IEnumerable[ItemIdentification])
    ItemIdentifications(collection: List[ItemIdentification])
    """
    def AddRange(self, collection):
        """ AddRange(self: ItemIdentifications, collection: IEnumerable[ItemIdentification]) -> List[ItemIdentification] """
        pass

    def Clear(self):
        """ Clear(self: ItemIdentifications) """
        pass

    def Clone(self):
        """ Clone(self: ItemIdentifications) -> object """
        pass

    def ContainsAll(self, itemIds):
        """ ContainsAll(self: ItemIdentifications, itemIds: ItemIdentifications) -> bool """
        pass

    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[ItemIdentification]) -> ItemIdentifications """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ItemIdentifications) -> int """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, itemId: ItemIdentification)
        __new__(cls: type, collection: IEnumerable[ItemIdentification])
        __new__(cls: type, collection: List[ItemIdentification])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(c1: ItemIdentifications, c2: ItemIdentifications) -> ItemIdentifications """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    IsDisposable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDisposable(self: ItemIdentifications) -> bool

"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreserveState(self: ItemIdentifications) -> bool

"""


    DisplayMember = 'Number'
    ValueMember = 'Quantity'


class ItemIdGenerateArgs:
    """ ItemIdGenerateArgs() """
    def AddGeneratedNumber(self, itemId):
        """ AddGeneratedNumber(self: ItemIdGenerateArgs, itemId: ItemIdentification) """
        pass

    def UpdateNumberInfo(self, prefix, suffix, hasLeadingZeroes, staticSerialNumberLength, serialNumberFromAsNumber, serialNumberToAsNumber, numbersToGenerate):
        """ UpdateNumberInfo(self: ItemIdGenerateArgs, prefix: str, suffix: str, hasLeadingZeroes: bool, staticSerialNumberLength: int, serialNumberFromAsNumber: Decimal, serialNumberToAsNumber: Decimal, numbersToGenerate: int) """
        pass

    BatchPickLocationUpdated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BatchPickLocationUpdated(self: ItemIdGenerateArgs) -> BatchPickLocation

Set: BatchPickLocationUpdated(self: ItemIdGenerateArgs) = value
"""

    GeneratedItemIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeneratedItemIds(self: ItemIdGenerateArgs) -> ItemIdentifications

"""

    HasLeadingZeroes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasLeadingZeroes(self: ItemIdGenerateArgs) -> bool

"""

    InboundReceiveLineUpdatet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InboundReceiveLineUpdatet(self: ItemIdGenerateArgs) -> InboundReceiveLine

Set: InboundReceiveLineUpdatet(self: ItemIdGenerateArgs) = value
"""

    NumbersToGenerate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumbersToGenerate(self: ItemIdGenerateArgs) -> int

"""

    Prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Prefix(self: ItemIdGenerateArgs) -> str

"""

    SerialNumberFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SerialNumberFrom(self: ItemIdGenerateArgs) -> str

Set: SerialNumberFrom(self: ItemIdGenerateArgs) = value
"""

    SerialNumberFromAsNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SerialNumberFromAsNumber(self: ItemIdGenerateArgs) -> Decimal

"""

    SerialNumberTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SerialNumberTo(self: ItemIdGenerateArgs) -> str

Set: SerialNumberTo(self: ItemIdGenerateArgs) = value
"""

    SerialNumberToAsNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SerialNumberToAsNumber(self: ItemIdGenerateArgs) -> Decimal

"""

    StaticSerialNumberLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaticSerialNumberLength(self: ItemIdGenerateArgs) -> int

"""

    Suffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Suffix(self: ItemIdGenerateArgs) -> str

"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: ItemIdGenerateArgs) -> str

Set: WarehouseCode(self: ItemIdGenerateArgs) = value
"""

    WarehouseLocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseLocationCode(self: ItemIdGenerateArgs) -> str

Set: WarehouseLocationCode(self: ItemIdGenerateArgs) = value
"""



class ItemInfo:
    """ ItemInfo() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Barcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Barcode(self: ItemInfo) -> str

Set: Barcode(self: ItemInfo) = value
"""

    BaseQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseQuantity(self: ItemInfo) -> Decimal

Set: BaseQuantity(self: ItemInfo) = value
"""

    Factor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Factor(self: ItemInfo) -> Decimal

Set: Factor(self: ItemInfo) = value
"""

    IsBatchNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBatchNumberItem(self: ItemInfo) -> bool

Set: IsBatchNumberItem(self: ItemInfo) = value
"""

    IsSerialNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSerialNumberItem(self: ItemInfo) -> bool

Set: IsSerialNumberItem(self: ItemInfo) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: ItemInfo) -> str

Set: ItemCode(self: ItemInfo) = value
"""

    Lifetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lifetime(self: ItemInfo) -> CacheLifeTimes

"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: ItemInfo) -> Decimal

"""

    UnitCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitCode(self: ItemInfo) -> str

Set: UnitCode(self: ItemInfo) = value
"""



class LocationBase:
    # no doc
    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: LocationBase) -> str

Set: Code(self: LocationBase) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: LocationBase) -> str

"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: LocationBase) -> str

Set: WarehouseCode(self: LocationBase) = value
"""



class Location:
    """ Location() """
    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: Location) -> str

Set: Description(self: Location) = value
"""

    FixedItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FixedItemCode(self: Location) -> str

Set: FixedItemCode(self: Location) = value
"""

    IsBlockedInbound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBlockedInbound(self: Location) -> bool

Set: IsBlockedInbound(self: Location) = value
"""

    IsBlockedOutbound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBlockedOutbound(self: Location) -> bool

Set: IsBlockedOutbound(self: Location) = value
"""

    MaximumStock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumStock(self: Location) -> Decimal

Set: MaximumStock(self: Location) = value
"""

    MinimumStock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumStock(self: Location) -> Decimal

Set: MinimumStock(self: Location) = value
"""

    PickType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickType(self: Location) -> LocationPickTypeEnum

Set: PickType(self: Location) = value
"""

    PickTypeAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickTypeAsString(self: Location) -> str

"""

    PickTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickTypeName(self: Location) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: Location) -> LocationTypeEnum

Set: Type(self: Location) = value
"""

    TypeAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeAsString(self: Location) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: Location) -> str

"""



class ItemLocation:
    """ ItemLocation() """
    def Clone(self):
        """ Clone(self: ItemLocation) -> object """
        pass

    def Equals(self, obj):
        """ Equals(self: ItemLocation, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ItemLocation) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    IsDefaultLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDefaultLocation(self: ItemLocation) -> bool

Set: IsDefaultLocation(self: ItemLocation) = value
"""

    Stock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Stock(self: ItemLocation) -> Decimal

Set: Stock(self: ItemLocation) = value
"""



class ItemLocationComparer:
    """ ItemLocationComparer() """
    def Compare(self, x, y):
        """ Compare(self: ItemLocationComparer, x: ItemLocation, y: ItemLocation) -> int """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class ItemLocations:
    """ ItemLocations() """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalRowsMatched(self: ItemLocations) -> Int64

Set: TotalRowsMatched(self: ItemLocations) = value
"""


    DisplayMember = 'Description'
    UniqueIdMember = 'Id'
    ValueMember = 'Code'


class ItemPackLocation:
    """
    ItemPackLocation()
    ItemPackLocation(boxGuid: Guid, quantity: Decimal, isContainer: bool)
    """
    def Clone(self):
        """ Clone(self: ItemPackLocation) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, boxGuid=None, quantity=None, isContainer=None):
        """
        __new__(cls: type)
        __new__(cls: type, boxGuid: Guid, quantity: Decimal, isContainer: bool)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    BoxGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoxGuid(self: ItemPackLocation) -> Guid

Set: BoxGuid(self: ItemPackLocation) = value
"""

    InnerReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerReference(self: ItemPackLocation) -> str

Set: InnerReference(self: ItemPackLocation) = value
"""

    IsContainer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsContainer(self: ItemPackLocation) -> bool

Set: IsContainer(self: ItemPackLocation) = value
"""

    OuterReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OuterReference(self: ItemPackLocation) -> str

Set: OuterReference(self: ItemPackLocation) = value
"""

    QuantityProcessed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityProcessed(self: ItemPackLocation) -> Decimal

Set: QuantityProcessed(self: ItemPackLocation) = value
"""


    _itemIds = None


class ItemPackLocations:
    """ ItemPackLocations() """
    def ClearExceptForContainer(self):
        """ ClearExceptForContainer(self: ItemPackLocations) """
        pass

    def Clone(self):
        """ Clone(self: ItemPackLocations) -> object """
        pass

    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[ItemPackLocation]) -> ItemPackLocations """
        pass

    def Merge(self, packLocations, compareBoxGuid):
        """ Merge(self: ItemPackLocations, packLocations: IEnumerable[ItemPackLocation], compareBoxGuid: bool) -> ItemPackLocations """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    QuantityPacked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityPacked(self: ItemPackLocations) -> Decimal

"""


    DisplayMember = None
    ValueMember = None


class ItemPickLocation:
    """ ItemPickLocation() """
    def Clone(self):
        """ Clone(self: ItemPickLocation) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(source: ItemPickLocation, toSubtract: ItemPickLocation) -> ItemPickLocation """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    IsMarkedAsPicked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMarkedAsPicked(self: ItemPickLocation) -> bool

Set: IsMarkedAsPicked(self: ItemPickLocation) = value
"""

    IsPicked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPicked(self: ItemPickLocation) -> bool

"""

    ItemIdRegistration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIdRegistration(self: ItemPickLocation) -> ItemIdentificationRegistration

Set: ItemIdRegistration(self: ItemPickLocation) = value
"""

    ItemScanned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemScanned(self: ItemPickLocation) -> bool

Set: ItemScanned(self: ItemPickLocation) = value
"""

    LocationScanned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationScanned(self: ItemPickLocation) -> bool

Set: LocationScanned(self: ItemPickLocation) = value
"""

    ProcessState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProcessState(self: ItemPickLocation) -> ProcessPickState

Set: ProcessState(self: ItemPickLocation) = value
"""

    QuantityAllocated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityAllocated(self: ItemPickLocation) -> Decimal

Set: QuantityAllocated(self: ItemPickLocation) = value
"""

    QuantityAllocatedOriginal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityAllocatedOriginal(self: ItemPickLocation) -> Decimal

Set: QuantityAllocatedOriginal(self: ItemPickLocation) = value
"""


    _itemIds = None


class ItemPickLocations:
    """ ItemPickLocations() """
    def Add(self, *__args):
        """ Add(self: ItemPickLocations, itemPickLocation: ItemPickLocation) """
        pass

    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[ItemPickLocation]) -> ItemPickLocations """
        pass

    def GetLocationCodeIndex(self, locationCode):
        """ GetLocationCodeIndex(self: ItemPickLocations, locationCode: str) -> int """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    DisplayMember = None
    ValueMember = None


class ItemStock:
    """ ItemStock() """
    def Clone(self):
        """ Clone(self: ItemStock) -> object """
        pass

    @staticmethod
    def CreateUniqueHashCode(itemCode, warehouseCode, warehouseLocationCode, orderId, orderLineId, itemId):
        """ CreateUniqueHashCode(itemCode: str, warehouseCode: str, warehouseLocationCode: str, orderId: str, orderLineId: str, itemId: str) -> str """
        pass

    def GetUniqueHashCode(self):
        """ GetUniqueHashCode(self: ItemStock) -> str """
        pass

    def IsSerialBatchItemCheck(self, checkRegistration):
        """ IsSerialBatchItemCheck(self: ItemStock, checkRegistration: bool) -> bool """
        pass

    def Subtract(self, items):
        """ Subtract(self: ItemStock, items: IEnumerable[AllocatedStockItem]) -> ItemStock """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    AssignedSalesOrderId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssignedSalesOrderId(self: ItemStock) -> str

Set: AssignedSalesOrderId(self: ItemStock) = value
"""

    AssignedSalesOrderLineId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssignedSalesOrderLineId(self: ItemStock) -> str

Set: AssignedSalesOrderLineId(self: ItemStock) = value
"""

    AssignedSalesOrderNo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssignedSalesOrderNo(self: ItemStock) -> str

Set: AssignedSalesOrderNo(self: ItemStock) = value
"""

    AssignType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssignType(self: ItemStock) -> AssignType

Set: AssignType(self: ItemStock) = value
"""

    AssignTypeAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssignTypeAsString(self: ItemStock) -> str

"""

    IsBlockedInbound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBlockedInbound(self: ItemStock) -> bool

Set: IsBlockedInbound(self: ItemStock) = value
"""

    IsBlockedOutbound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBlockedOutbound(self: ItemStock) -> bool

Set: IsBlockedOutbound(self: ItemStock) = value
"""

    IsSerialBatchItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSerialBatchItem(self: ItemStock) -> bool

Set: IsSerialBatchItem(self: ItemStock) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: ItemStock) -> str

Set: ItemCode(self: ItemStock) = value
"""

    ItemDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemDescription(self: ItemStock) -> str

Set: ItemDescription(self: ItemStock) = value
"""

    ItemId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemId(self: ItemStock) -> str

Set: ItemId(self: ItemStock) = value
"""

    ItemIdRegistration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIdRegistration(self: ItemStock) -> ItemIdentificationRegistration

Set: ItemIdRegistration(self: ItemStock) = value
"""

    ItemIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIds(self: ItemStock) -> ItemIdentifications

Set: ItemIds(self: ItemStock) = value
"""

    LocationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationType(self: ItemStock) -> LocationTypeEnum

Set: LocationType(self: ItemStock) = value
"""

    PickType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickType(self: ItemStock) -> LocationPickTypeEnum

Set: PickType(self: ItemStock) = value
"""

    Stock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Stock(self: ItemStock) -> Decimal

Set: Stock(self: ItemStock) = value
"""

    StockOnShelve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StockOnShelve(self: ItemStock) -> Decimal

Set: StockOnShelve(self: ItemStock) = value
"""

    UnitCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitCode(self: ItemStock) -> str

Set: UnitCode(self: ItemStock) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: ItemStock) -> str

Set: WarehouseCode(self: ItemStock) = value
"""

    WarehouseLocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseLocationCode(self: ItemStock) -> str

Set: WarehouseLocationCode(self: ItemStock) = value
"""



class ItemStockAllocation:
    """
    ItemStockAllocation()
    ItemStockAllocation(allocatedStockItem: AllocatedStockItem)
    """
    def Clone(self):
        """ Clone(self: ItemStockAllocation) -> ItemStockAllocation """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, allocatedStockItem=None):
        """
        __new__(cls: type)
        __new__(cls: type, allocatedStockItem: AllocatedStockItem)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    BatchName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BatchName(self: ItemStockAllocation) -> str

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ItemStockAllocation) -> str

Set: Description(self: ItemStockAllocation) = value
"""

    ItemId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemId(self: ItemStockAllocation) -> str

Set: ItemId(self: ItemStockAllocation) = value
"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: ItemStockAllocation) -> str

Set: Key(self: ItemStockAllocation) = value
"""

    OrderLineNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderLineNumber(self: ItemStockAllocation) -> str

Set: OrderLineNumber(self: ItemStockAllocation) = value
"""

    OrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderNumber(self: ItemStockAllocation) -> str

Set: OrderNumber(self: ItemStockAllocation) = value
"""



class ItemStockAllocationList:
    """ ItemStockAllocationList() """
    @staticmethod
    def FromIEnumerable(allocations):
        """ FromIEnumerable(allocations: IEnumerable[ItemStockAllocation]) -> ItemStockAllocationList """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    HasAllocationsWithoutBatches = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasAllocationsWithoutBatches(self: ItemStockAllocationList) -> bool

Set: HasAllocationsWithoutBatches(self: ItemStockAllocationList) = value
"""

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalRowsMatched(self: ItemStockAllocationList) -> Int64

Set: TotalRowsMatched(self: ItemStockAllocationList) = value
"""



class ItemStockEqualityComparer:
    """ ItemStockEqualityComparer() """
    def Equals(self, *__args):
        """ Equals(self: ItemStockEqualityComparer, x: ItemStock, y: ItemStock) -> bool """
        pass

    def GetHashCode(self, obj=None):
        """ GetHashCode(self: ItemStockEqualityComparer, obj: ItemStock) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ItemStockList:
    """ ItemStockList() """
    def FindFirstItemStock(self, itemCode, itemId):
        """ FindFirstItemStock(self: ItemStockList, itemCode: str, itemId: str) -> ItemStock """
        pass

    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[ItemStock]) -> ItemStockList """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalRowsMatched(self: ItemStockList) -> Int64

Set: TotalRowsMatched(self: ItemStockList) = value
"""



class ItemStockLocation:
    """ ItemStockLocation() """
    IsDefaultLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDefaultLocation(self: ItemStockLocation) -> bool

Set: IsDefaultLocation(self: ItemStockLocation) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: ItemStockLocation) -> str

Set: ItemCode(self: ItemStockLocation) = value
"""

    OriginalStock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginalStock(self: ItemStockLocation) -> Decimal

Set: OriginalStock(self: ItemStockLocation) = value
"""

    Stock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Stock(self: ItemStockLocation) -> Decimal

Set: Stock(self: ItemStockLocation) = value
"""

    WarehouseLocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseLocationCode(self: ItemStockLocation) -> str

Set: WarehouseLocationCode(self: ItemStockLocation) = value
"""



class ItemStockLocationList:
    """ ItemStockLocationList() """
    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[ItemStockLocation]) -> ItemStockLocationList """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    UniqueIdMember = 'Id'


class ItemStockTotals:
    """ ItemStockTotals() """
    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: ItemStockTotals) -> str

Set: ItemCode(self: ItemStockTotals) = value
"""

    StockAssignedToBatches = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StockAssignedToBatches(self: ItemStockTotals) -> Decimal

Set: StockAssignedToBatches(self: ItemStockTotals) = value
"""

    StockFreeInErp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StockFreeInErp(self: ItemStockTotals) -> Decimal

Set: StockFreeInErp(self: ItemStockTotals) = value
"""

    StockOnShelf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StockOnShelf(self: ItemStockTotals) -> Decimal

Set: StockOnShelf(self: ItemStockTotals) = value
"""



class ItemStockWithAllocations:
    """
    ItemStockWithAllocations()
    ItemStockWithAllocations(stock: ItemStock)
    """
    def AddAllocations(self, allocations):
        """ AddAllocations(self: ItemStockWithAllocations, allocations: List[ItemStockAllocation]) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, stock=None):
        """
        __new__(cls: type)
        __new__(cls: type, stock: ItemStock)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    AllocationAndStockQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllocationAndStockQuantity(self: ItemStockWithAllocations) -> str

"""

    Allocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Allocations(self: ItemStockWithAllocations) -> ItemStockAllocationList

Set: Allocations(self: ItemStockWithAllocations) = value
"""

    HasAllocationsWithoutBatches = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasAllocationsWithoutBatches(self: ItemStockWithAllocations) -> bool

Set: HasAllocationsWithoutBatches(self: ItemStockWithAllocations) = value
"""

    QuantityAllocated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityAllocated(self: ItemStockWithAllocations) -> Decimal

Set: QuantityAllocated(self: ItemStockWithAllocations) = value
"""



class ItemStockWithAllocationsList:
    """ ItemStockWithAllocationsList() """
    @staticmethod
    def FromIEnumerable(allocations):
        """ FromIEnumerable(allocations: IEnumerable[ItemStockWithAllocations]) -> ItemStockWithAllocationsList """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalRowsMatched(self: ItemStockWithAllocationsList) -> Int64

Set: TotalRowsMatched(self: ItemStockWithAllocationsList) = value
"""



class ItemStockWithLocations:
    """ ItemStockWithLocations() """
    BeginDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BeginDate(self: ItemStockWithLocations) -> DateTime

Set: BeginDate(self: ItemStockWithLocations) = value
"""

    EndDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndDate(self: ItemStockWithLocations) -> DateTime

Set: EndDate(self: ItemStockWithLocations) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: ItemStockWithLocations) -> str

Set: ItemCode(self: ItemStockWithLocations) = value
"""

    LocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationCode(self: ItemStockWithLocations) -> str

Set: LocationCode(self: ItemStockWithLocations) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Number(self: ItemStockWithLocations) -> str

Set: Number(self: ItemStockWithLocations) = value
"""

    QuantityAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityAvailable(self: ItemStockWithLocations) -> Decimal

Set: QuantityAvailable(self: ItemStockWithLocations) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: ItemStockWithLocations) -> str

Set: WarehouseCode(self: ItemStockWithLocations) = value
"""



class ItemTypeEnum:
    """ enum ItemTypeEnum, values: LicensePlate (1), Regular (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    LicensePlate = None
    Regular = None
    value__ = None


class LicensePlate:
    """ LicensePlate() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    BestBeforeDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BestBeforeDate(self: LicensePlate) -> Nullable[DateTime]

Set: BestBeforeDate(self: LicensePlate) = value
"""

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: LicensePlate) -> str

Set: Code(self: LicensePlate) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: LicensePlate) -> str

Set: Description(self: LicensePlate) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: LicensePlate) -> int

Set: Id(self: LicensePlate) = value
"""

    LocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationCode(self: LicensePlate) -> str

Set: LocationCode(self: LicensePlate) = value
"""

    NoOfItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NoOfItems(self: LicensePlate) -> int

Set: NoOfItems(self: LicensePlate) = value
"""

    Reference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reference(self: LicensePlate) -> str

Set: Reference(self: LicensePlate) = value
"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: LicensePlate) -> LicensePlateStatusEnum

Set: Status(self: LicensePlate) = value
"""

    StatusAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StatusAsString(self: LicensePlate) -> str

"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: LicensePlate) -> str

Set: WarehouseCode(self: LicensePlate) = value
"""



class LicensePlateAuditLog:
    """ LicensePlateAuditLog() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: LicensePlateAuditLog) -> str

Set: Description(self: LicensePlateAuditLog) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: LicensePlateAuditLog) -> int

Set: Id(self: LicensePlateAuditLog) = value
"""

    LicensePlateId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicensePlateId(self: LicensePlateAuditLog) -> int

Set: LicensePlateId(self: LicensePlateAuditLog) = value
"""

    NewStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewStatus(self: LicensePlateAuditLog) -> LicensePlateStatusEnum

Set: NewStatus(self: LicensePlateAuditLog) = value
"""

    NewStatusAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewStatusAsString(self: LicensePlateAuditLog) -> str

"""

    OldStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldStatus(self: LicensePlateAuditLog) -> Nullable[LicensePlateStatusEnum]

Set: OldStatus(self: LicensePlateAuditLog) = value
"""

    OldStatusAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldStatusAsString(self: LicensePlateAuditLog) -> str

"""



class LicensePlateAuditLogs:
    """ LicensePlateAuditLogs() """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalRowsMatched(self: LicensePlateAuditLogs) -> Int64

Set: TotalRowsMatched(self: LicensePlateAuditLogs) = value
"""


    DisplayMember = None
    ValueMember = None


class LicensePlateBarcodeStructureInfo:
    """ LicensePlateBarcodeStructureInfo() """
    BestBeforeDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BestBeforeDate(self: LicensePlateBarcodeStructureInfo) -> Nullable[DateTime]

Set: BestBeforeDate(self: LicensePlateBarcodeStructureInfo) = value
"""

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: LicensePlateBarcodeStructureInfo) -> str

Set: Code(self: LicensePlateBarcodeStructureInfo) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: LicensePlateBarcodeStructureInfo) -> str

Set: Description(self: LicensePlateBarcodeStructureInfo) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: LicensePlateBarcodeStructureInfo) -> int

Set: Id(self: LicensePlateBarcodeStructureInfo) = value
"""

    NoOfItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NoOfItems(self: LicensePlateBarcodeStructureInfo) -> int

Set: NoOfItems(self: LicensePlateBarcodeStructureInfo) = value
"""



class LicensePlateItem:
    """ LicensePlateItem() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: LicensePlateItem) -> int

Set: Id(self: LicensePlateItem) = value
"""

    IsBatchItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBatchItem(self: LicensePlateItem) -> bool

Set: IsBatchItem(self: LicensePlateItem) = value
"""

    IsSerialItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSerialItem(self: LicensePlateItem) -> bool

Set: IsSerialItem(self: LicensePlateItem) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: LicensePlateItem) -> str

Set: ItemCode(self: LicensePlateItem) = value
"""

    ItemDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemDescription(self: LicensePlateItem) -> str

Set: ItemDescription(self: LicensePlateItem) = value
"""

    ItemId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemId(self: LicensePlateItem) -> str

Set: ItemId(self: LicensePlateItem) = value
"""

    LicensePlateId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicensePlateId(self: LicensePlateItem) -> int

Set: LicensePlateId(self: LicensePlateItem) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: LicensePlateItem) -> Decimal

Set: Quantity(self: LicensePlateItem) = value
"""



class LicensePlateItems:
    """ LicensePlateItems() """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalRowsMatched(self: LicensePlateItems) -> Int64

Set: TotalRowsMatched(self: LicensePlateItems) = value
"""


    DisplayMember = 'ItemCode'
    ValueMember = 'Id'


class LicensePlates:
    """ LicensePlates() """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalRowsMatched(self: LicensePlates) -> Int64

Set: TotalRowsMatched(self: LicensePlates) = value
"""


    DisplayMember = None
    ValueMember = None


class LicensePlateStatusEnum:
    """ enum (flags) LicensePlateStatusEnum, values: Active (1), Archived (16), Broken (8), Inactive (4), InTransfer (32), Pending (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Active = None
    Archived = None
    Broken = None
    Inactive = None
    InTransfer = None
    Pending = None
    value__ = None


class LocationItem:
    """ LocationItem() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    ItemDefaultLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemDefaultLocation(self: LocationItem) -> str

Set: ItemDefaultLocation(self: LocationItem) = value
"""

    ItemsOnStock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemsOnStock(self: LocationItem) -> Decimal

"""

    ItemStock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemStock(self: LocationItem) -> ItemStockLocation

Set: ItemStock(self: LocationItem) = value
"""

    ItemStockLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemStockLocation(self: LocationItem) -> str

"""

    ItemStockWarehouse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemStockWarehouse(self: LocationItem) -> str

"""

    UniqueId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UniqueId(self: LocationItem) -> str

"""



class LocationItems:
    """ LocationItems() """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalRowsMatched(self: LocationItems) -> Int64

Set: TotalRowsMatched(self: LocationItems) = value
"""


    DisplayMember = 'Description'
    UniqueIdMember = 'UniqueId'
    ValueMember = 'Code'


class LocationPickTypeEnum:
    """ enum (flags) LocationPickTypeEnum, values: Bulk (1), Pick (0), Unspecified (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Bulk = None
    Pick = None
    Unspecified = None
    value__ = None


class LocationPickTypeEnumExtensions:
    # no doc
    @staticmethod
    def IsTypeInValue(val, type):
        """ IsTypeInValue(val: LocationPickTypeEnum, type: LocationPickTypeEnum) -> bool """
        pass

    __all__ = [
        'IsTypeInValue',
    ]


class Locations:
    """ Locations() """
    @staticmethod
    def FromItemLocations(itemLocations):
        """ FromItemLocations(itemLocations: ItemLocations) -> Locations """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalRowsMatched(self: Locations) -> Int64

Set: TotalRowsMatched(self: Locations) = value
"""


    DisplayMember = 'Description'
    UniqueIdMember = 'Id'
    ValueMember = 'Code'


class LocationsBase:
    # no doc
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass


class LocationTypeEnum:
    """ enum LocationTypeEnum, values: FixedItemLocation (1), MultipleItemLocation (0), VariableItemLocation (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FixedItemLocation = None
    MultipleItemLocation = None
    value__ = None
    VariableItemLocation = None


class LpLocationItem:
    """ LpLocationItem() """
    IsBatchItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBatchItem(self: LpLocationItem) -> bool

Set: IsBatchItem(self: LpLocationItem) = value
"""

    IsSerialItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSerialItem(self: LpLocationItem) -> bool

Set: IsSerialItem(self: LpLocationItem) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: LpLocationItem) -> str

Set: ItemCode(self: LpLocationItem) = value
"""

    ItemDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemDescription(self: LpLocationItem) -> str

Set: ItemDescription(self: LpLocationItem) = value
"""

    ItemId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemId(self: LpLocationItem) -> str

Set: ItemId(self: LpLocationItem) = value
"""

    QuantityToAdd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityToAdd(self: LpLocationItem) -> Decimal

Set: QuantityToAdd(self: LpLocationItem) = value
"""

    Stock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Stock(self: LpLocationItem) -> Decimal

Set: Stock(self: LpLocationItem) = value
"""



class PrintLicensePlateLabelArgs:
    """ PrintLicensePlateLabelArgs() """
    LabelName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelName(self: PrintLicensePlateLabelArgs) -> str

Set: LabelName(self: PrintLicensePlateLabelArgs) = value
"""

    LicensePlateId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicensePlateId(self: PrintLicensePlateLabelArgs) -> int

Set: LicensePlateId(self: PrintLicensePlateLabelArgs) = value
"""



class ProcessWarehouseTransferArgs:
    """ ProcessWarehouseTransferArgs() """
    CacheKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CacheKey(self: ProcessWarehouseTransferArgs) -> CacheKey

Set: CacheKey(self: ProcessWarehouseTransferArgs) = value
"""

    CustomReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomReference(self: ProcessWarehouseTransferArgs) -> str

Set: CustomReference(self: ProcessWarehouseTransferArgs) = value
"""



class ReplenishmentOrder:
    """ ReplenishmentOrder() """
    def Clone(self):
        """ Clone(self: ReplenishmentOrder) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Approved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Approved(self: ReplenishmentOrder) -> bool

Set: Approved(self: ReplenishmentOrder) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Number(self: ReplenishmentOrder) -> str

Set: Number(self: ReplenishmentOrder) = value
"""

    ReplenishToLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReplenishToLocation(self: ReplenishmentOrder) -> Location

Set: ReplenishToLocation(self: ReplenishmentOrder) = value
"""

    ReplenishToLocationCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReplenishToLocationCode(self: ReplenishmentOrder) -> str

"""

    ReplenishToWarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReplenishToWarehouseCode(self: ReplenishmentOrder) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: ReplenishmentOrder) -> OutboundOrderTypeEnum

"""



class ReplenishmentOrderLine:
    """ ReplenishmentOrderLine() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    OrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderNumber(self: ReplenishmentOrderLine) -> str

Set: OrderNumber(self: ReplenishmentOrderLine) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: ReplenishmentOrderLine) -> OutboundOrderTypeEnum

"""



class ReplenishmentOrderLines:
    """ ReplenishmentOrderLines() """
    @staticmethod
    def FromIEnumerable(list):
        """
        FromIEnumerable(list: IEnumerable[ReplenishmentOrderLine]) -> ReplenishmentOrderLines
        FromIEnumerable(list: IEnumerable[OutboundOrderLine]) -> ReplenishmentOrderLines
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    TotalRowsMatched = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalRowsMatched(self: ReplenishmentOrderLines) -> Int64

Set: TotalRowsMatched(self: ReplenishmentOrderLines) = value
"""



class ReplenishmentOrders:
    """ ReplenishmentOrders() """
    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[OutboundOrder]) -> ReplenishmentOrders """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass


class Warehouse:
    """ Warehouse() """
    Active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Active(self: Warehouse) -> bool

Set: Active(self: Warehouse) = value
"""

    AddressLine1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AddressLine1(self: Warehouse) -> str

Set: AddressLine1(self: Warehouse) = value
"""

    AddressLine2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AddressLine2(self: Warehouse) -> str

Set: AddressLine2(self: Warehouse) = value
"""

    AddressLine3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AddressLine3(self: Warehouse) -> str

Set: AddressLine3(self: Warehouse) = value
"""

    City = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: City(self: Warehouse) -> str

Set: City(self: Warehouse) = value
"""

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: Warehouse) -> str

Set: Code(self: Warehouse) = value
"""

    Contact = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Contact(self: Warehouse) -> str

Set: Contact(self: Warehouse) = value
"""

    ContactEmail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContactEmail(self: Warehouse) -> str

Set: ContactEmail(self: Warehouse) = value
"""

    CountryCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CountryCode(self: Warehouse) -> str

Set: CountryCode(self: Warehouse) = value
"""

    CountryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CountryName(self: Warehouse) -> str

Set: CountryName(self: Warehouse) = value
"""

    DefaultInboundLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultInboundLocation(self: Warehouse) -> str

Set: DefaultInboundLocation(self: Warehouse) = value
"""

    DefaultOutboundLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultOutboundLocation(self: Warehouse) -> str

Set: DefaultOutboundLocation(self: Warehouse) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: Warehouse) -> str

Set: Description(self: Warehouse) = value
"""

    PhoneNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhoneNumber(self: Warehouse) -> str

Set: PhoneNumber(self: Warehouse) = value
"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: State(self: Warehouse) -> str

Set: State(self: Warehouse) = value
"""

    Zipcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Zipcode(self: Warehouse) -> str

Set: Zipcode(self: Warehouse) = value
"""



class Warehouses:
    """
    Warehouses()
    Warehouses(filterWarehouses: IEnumerable[Warehouse])
    """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, filterWarehouses=None):
        """
        __new__(cls: type)
        __new__(cls: type, filterWarehouses: IEnumerable[Warehouse])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    DisplayMember = 'Description'
    ValueMember = 'Code'


class WarehouseTransfer:
    """ WarehouseTransfer() """
    def GetHashCode(self):
        """ GetHashCode(self: WarehouseTransfer) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    BatchId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BatchId(self: WarehouseTransfer) -> Guid

Set: BatchId(self: WarehouseTransfer) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: WarehouseTransfer) -> str

Set: Description(self: WarehouseTransfer) = value
"""

    GroupGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupGuid(self: WarehouseTransfer) -> Guid

"""

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Items(self: WarehouseTransfer) -> WarehouseTransferItems

"""

    Lifetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lifetime(self: WarehouseTransfer) -> CacheLifeTimes

"""

    LocationFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationFrom(self: WarehouseTransfer) -> Location

Set: LocationFrom(self: WarehouseTransfer) = value
"""

    LocationTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationTo(self: WarehouseTransfer) -> Location

Set: LocationTo(self: WarehouseTransfer) = value
"""

    ValidateTransferWithStockManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValidateTransferWithStockManager(self: WarehouseTransfer) -> bool

Set: ValidateTransferWithStockManager(self: WarehouseTransfer) = value
"""

    WarehouseCodeFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCodeFrom(self: WarehouseTransfer) -> str

Set: WarehouseCodeFrom(self: WarehouseTransfer) = value
"""

    WarehouseCodeTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCodeTo(self: WarehouseTransfer) -> str

Set: WarehouseCodeTo(self: WarehouseTransfer) = value
"""


    BatchRecordId = None
    Type = None


class WarehouseTransferItem:
    """ WarehouseTransferItem() """
    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: WarehouseTransferItem) -> str

Set: Description(self: WarehouseTransferItem) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: WarehouseTransferItem) -> str

Set: ItemCode(self: WarehouseTransferItem) = value
"""

    ItemType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemType(self: WarehouseTransferItem) -> ItemTypeEnum

Set: ItemType(self: WarehouseTransferItem) = value
"""

    LocationFrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationFrom(self: WarehouseTransferItem) -> Location

Set: LocationFrom(self: WarehouseTransferItem) = value
"""

    LocationTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationTo(self: WarehouseTransferItem) -> Location

Set: LocationTo(self: WarehouseTransferItem) = value
"""

    NewQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewQuantity(self: WarehouseTransferItem) -> Decimal

Set: NewQuantity(self: WarehouseTransferItem) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: WarehouseTransferItem) -> WarehouseTransfer

Set: Parent(self: WarehouseTransferItem) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: WarehouseTransferItem) -> Decimal

Set: Quantity(self: WarehouseTransferItem) = value
"""


    ItemIdentifications = None
    ProcessDate = None


class WarehouseTransferItems:
    """
    WarehouseTransferItems()
    WarehouseTransferItems(parent: WarehouseTransfer)
    """
    def Add(self, item):
        """ Add(self: WarehouseTransferItems, item: WarehouseTransferItem) """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: WarehouseTransferItems) -> int """
        pass

    def GetItem(self, itemCode):
        """ GetItem(self: WarehouseTransferItems, itemCode: str) -> WarehouseTransferItem """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, parent=None):
        """
        __new__(cls: type)
        __new__(cls: type, parent: WarehouseTransfer)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    DisplayMember = 'Description'
    ValueMember = 'ItemCode'


class WarehouseTransferType:
    """ enum WarehouseTransferType, values: DirectTransfer (3), InterBranch (1), LicensePlateItems (2), Normal (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DirectTransfer = None
    InterBranch = None
    LicensePlateItems = None
    Normal = None
    value__ = None

