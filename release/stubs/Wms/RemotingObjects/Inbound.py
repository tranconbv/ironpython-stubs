# encoding: utf-8
# module Wms.RemotingObjects.Inbound calls itself Inbound
# from Wms.RemotingObjects, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class PreReceipt:
    """ PreReceipt() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Date(self: PreReceipt) -> DateTime

Set: Date(self: PreReceipt) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: PreReceipt) -> str

Set: Description(self: PreReceipt) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: PreReceipt) -> int

Set: Id(self: PreReceipt) = value
"""

    Notes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Notes(self: PreReceipt) -> str

Set: Notes(self: PreReceipt) = value
"""

    NumberOfCollo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfCollo(self: PreReceipt) -> int

Set: NumberOfCollo(self: PreReceipt) = value
"""

    PendingOrderCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PendingOrderCount(self: PreReceipt) -> int

Set: PendingOrderCount(self: PreReceipt) = value
"""

    PercentageReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PercentageReceived(self: PreReceipt) -> int

"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: PreReceipt) -> PreReceiptStatus

Set: Status(self: PreReceipt) = value
"""

    Tags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tags(self: PreReceipt) -> str

Set: Tags(self: PreReceipt) = value
"""

    TotalOrderLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalOrderLines(self: PreReceipt) -> int

Set: TotalOrderLines(self: PreReceipt) = value
"""

    TotalOrderLinesReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalOrderLinesReceived(self: PreReceipt) -> int

Set: TotalOrderLinesReceived(self: PreReceipt) = value
"""

    TotalOrderLinesToReceive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalOrderLinesToReceive(self: PreReceipt) -> int

Set: TotalOrderLinesToReceive(self: PreReceipt) = value
"""

    TotalQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalQuantity(self: PreReceipt) -> Decimal

Set: TotalQuantity(self: PreReceipt) = value
"""

    TotalQuantityReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalQuantityReceived(self: PreReceipt) -> Decimal

Set: TotalQuantityReceived(self: PreReceipt) = value
"""



class CreatePreReceiptArgs:
    """ CreatePreReceiptArgs() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Lines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lines(self: CreatePreReceiptArgs) -> List[PreReceiptLine]

Set: Lines(self: CreatePreReceiptArgs) = value
"""

    OrderIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderIds(self: CreatePreReceiptArgs) -> List[int]

Set: OrderIds(self: CreatePreReceiptArgs) = value
"""

    OrderLineIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderLineIds(self: CreatePreReceiptArgs) -> List[int]

Set: OrderLineIds(self: CreatePreReceiptArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: CreatePreReceiptArgs) -> str

Set: WarehouseCode(self: CreatePreReceiptArgs) = value
"""



class ErpInboundLocationMode:
    """ enum ErpInboundLocationMode, values: DefaultItemLocation (1), DefaultWarehouseLocation (0) """
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

    DefaultItemLocation = None
    DefaultWarehouseLocation = None
    value__ = None


class ErpProcessInboundOrderResult:
    """ ErpProcessInboundOrderResult() """
    CreatedOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatedOrder(self: ErpProcessInboundOrderResult) -> InboundOrder

Set: CreatedOrder(self: ErpProcessInboundOrderResult) = value
"""

    HasOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasOrder(self: ErpProcessInboundOrderResult) -> bool

"""



class InboundOrder:
    """ InboundOrder() """
    def GetHashCode(self):
        """ GetHashCode(self: InboundOrder) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    BusinessUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BusinessUnit(self: InboundOrder) -> str

Set: BusinessUnit(self: InboundOrder) = value
"""

    DateFirstExpected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DateFirstExpected(self: InboundOrder) -> DateTime

Set: DateFirstExpected(self: InboundOrder) = value
"""

    DateOrdered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DateOrdered(self: InboundOrder) -> DateTime

Set: DateOrdered(self: InboundOrder) = value
"""

    DeliveryMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeliveryMethod(self: InboundOrder) -> str

Set: DeliveryMethod(self: InboundOrder) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: InboundOrder) -> str

Set: Description(self: InboundOrder) = value
"""

    GroupKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupKey(self: InboundOrder) -> int

Set: GroupKey(self: InboundOrder) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: InboundOrder) -> int

Set: Id(self: InboundOrder) = value
"""

    Notes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Notes(self: InboundOrder) -> str

Set: Notes(self: InboundOrder) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Number(self: InboundOrder) -> str

Set: Number(self: InboundOrder) = value
"""

    PendingOrderLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PendingOrderLines(self: InboundOrder) -> int

Set: PendingOrderLines(self: InboundOrder) = value
"""

    ProjectCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectCode(self: InboundOrder) -> str

Set: ProjectCode(self: InboundOrder) = value
"""

    ProjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectName(self: InboundOrder) -> str

Set: ProjectName(self: InboundOrder) = value
"""

    SelectionCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectionCode(self: InboundOrder) -> str

Set: SelectionCode(self: InboundOrder) = value
"""

    SelectionCodeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectionCodeDescription(self: InboundOrder) -> str

Set: SelectionCodeDescription(self: InboundOrder) = value
"""

    Warehouse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Warehouse(self: InboundOrder) -> str

Set: Warehouse(self: InboundOrder) = value
"""



class InboundOrderLine:
    """ InboundOrderLine() """
    def AddReceiving(self, *__args):
        """
        AddReceiving(self: InboundOrderLine, quantity: Decimal) -> bool
        AddReceiving(self: InboundOrderLine, itemId: ItemIdentification) -> bool
        """
        pass

    def Clone(self):
        """ Clone(self: InboundOrderLine) -> object """
        pass

    @staticmethod
    def FromItem(item, itemDefaultLocation):
        """ FromItem(item: Item, itemDefaultLocation: str) -> InboundOrderLine """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: InboundOrderLine) -> int """
        pass

    def IsBatchNumberItemCheck(self, checkRegistration):
        """ IsBatchNumberItemCheck(self: InboundOrderLine, checkRegistration: bool) -> bool """
        pass

    def IsSerialNumberItemCheck(self, checkRegistration):
        """ IsSerialNumberItemCheck(self: InboundOrderLine, checkRegistration: bool) -> bool """
        pass

    def PutBack(self, *__args):
        """
        PutBack(self: InboundOrderLine, quantity: Decimal) -> Decimal
        PutBack(self: InboundOrderLine, itemId: ItemIdentification) -> Decimal
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

    CustomErpFields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomErpFields(self: InboundOrderLine) -> SerializableDictionary[str, object]

Set: CustomErpFields(self: InboundOrderLine) = value
"""

    CustomFields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomFields(self: InboundOrderLine) -> SerializableDictionary[str, object]

Set: CustomFields(self: InboundOrderLine) = value
"""

    DateExpected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DateExpected(self: InboundOrderLine) -> DateTime

Set: DateExpected(self: InboundOrderLine) = value
"""

    DefaultVendorBarcode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultVendorBarcode(self: InboundOrderLine) -> str

Set: DefaultVendorBarcode(self: InboundOrderLine) = value
"""

    DefaultVendorItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultVendorItemCode(self: InboundOrderLine) -> str

Set: DefaultVendorItemCode(self: InboundOrderLine) = value
"""

    GTINCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GTINCode(self: InboundOrderLine) -> str

Set: GTINCode(self: InboundOrderLine) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: InboundOrderLine) -> int

Set: Id(self: InboundOrderLine) = value
"""

    IsBatchNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBatchNumberItem(self: InboundOrderLine) -> bool

Set: IsBatchNumberItem(self: InboundOrderLine) = value
"""

    IsFractionAllowed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFractionAllowed(self: InboundOrderLine) -> bool

Set: IsFractionAllowed(self: InboundOrderLine) = value
"""

    IsProcessed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsProcessed(self: InboundOrderLine) -> bool

Set: IsProcessed(self: InboundOrderLine) = value
"""

    IsSerialNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSerialNumberItem(self: InboundOrderLine) -> bool

Set: IsSerialNumberItem(self: InboundOrderLine) = value
"""

    ItemBrand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemBrand(self: InboundOrderLine) -> str

Set: ItemBrand(self: InboundOrderLine) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: InboundOrderLine) -> str

Set: ItemCode(self: InboundOrderLine) = value
"""

    ItemDefaultLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemDefaultLocation(self: InboundOrderLine) -> str

Set: ItemDefaultLocation(self: InboundOrderLine) = value
"""

    ItemDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemDescription(self: InboundOrderLine) -> str

Set: ItemDescription(self: InboundOrderLine) = value
"""

    ItemIdRegistration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIdRegistration(self: InboundOrderLine) -> ItemIdentificationRegistration

Set: ItemIdRegistration(self: InboundOrderLine) = value
"""

    ItemIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIds(self: InboundOrderLine) -> ItemIdentifications

Set: ItemIds(self: InboundOrderLine) = value
"""

    ItemWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemWeight(self: InboundOrderLine) -> Decimal

Set: ItemWeight(self: InboundOrderLine) = value
"""

    LineCurrencyCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineCurrencyCode(self: InboundOrderLine) -> str

Set: LineCurrencyCode(self: InboundOrderLine) = value
"""

    LineDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineDescription(self: InboundOrderLine) -> str

Set: LineDescription(self: InboundOrderLine) = value
"""

    LineInstruction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineInstruction(self: InboundOrderLine) -> str

Set: LineInstruction(self: InboundOrderLine) = value
"""

    LineNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineNumber(self: InboundOrderLine) -> int

Set: LineNumber(self: InboundOrderLine) = value
"""

    OrderId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderId(self: InboundOrderLine) -> int

Set: OrderId(self: InboundOrderLine) = value
"""

    OrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderNumber(self: InboundOrderLine) -> str

Set: OrderNumber(self: InboundOrderLine) = value
"""

    QuantityOrdered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityOrdered(self: InboundOrderLine) -> Decimal

Set: QuantityOrdered(self: InboundOrderLine) = value
"""

    QuantityReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityReceived(self: InboundOrderLine) -> Decimal

Set: QuantityReceived(self: InboundOrderLine) = value
"""

    QuantityToReceive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityToReceive(self: InboundOrderLine) -> Decimal

Set: QuantityToReceive(self: InboundOrderLine) = value
"""

    UnitCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitCode(self: InboundOrderLine) -> str

Set: UnitCode(self: InboundOrderLine) = value
"""



class InboundOrderLines:
    """ InboundOrderLines() """
    def GetHashCode(self):
        """ GetHashCode(self: InboundOrderLines) -> int """
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

    IsDisposable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDisposable(self: InboundOrderLines) -> bool

"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreserveState(self: InboundOrderLines) -> bool

"""


    DisplayMember = 'ItemCode'
    ValueMember = 'Id'


class InboundOrders:
    """ InboundOrders() """
    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[InboundOrder]) -> InboundOrders """
        pass

    def GetCacheKey(self):
        """ GetCacheKey(self: InboundOrders) -> int """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: InboundOrders) -> int """
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

    DisplayMember = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayMember(self: InboundOrders) -> str

"""

    ValueMember = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueMember(self: InboundOrders) -> str

"""



class InboundOrderTypeEnum:
    """ enum InboundOrderTypeEnum, values: AdhocPurchase (2), AdhocRma (3), AdhocRmaTouch (4), PreReceipt (5), Purchase (0), Rma (1) """
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

    AdhocPurchase = None
    AdhocRma = None
    AdhocRmaTouch = None
    PreReceipt = None
    Purchase = None
    Rma = None
    value__ = None


class InboundReceiveLine:
    """ InboundReceiveLine() """
    def Clone(self):
        """ Clone(self: InboundReceiveLine) -> object """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: InboundReceiveLine) -> int """
        pass

    def GetItemIdsReceived(self):
        """ GetItemIdsReceived(self: InboundReceiveLine) -> ItemIdentifications """
        pass

    def PutBack(self, *__args):
        """
        PutBack(self: InboundReceiveLine, orderNumber: str, quantity: Decimal) -> bool
        PutBack(self: InboundReceiveLine, orderId: int, quantity: Decimal) -> bool
        PutBack(self: InboundReceiveLine, orderNumber: str, itemId: ItemIdentification) -> bool
        PutBack(self: InboundReceiveLine, orderId: int, itemId: ItemIdentification) -> bool
        """
        pass

    def Receive(self, *__args):
        """
        Receive(self: InboundReceiveLine, orderNumber: str, quantity: Decimal) -> bool
        Receive(self: InboundReceiveLine, orderId: int, quantity: Decimal) -> bool
        Receive(self: InboundReceiveLine, orderNumber: str, itemId: ItemIdentification) -> bool
        Receive(self: InboundReceiveLine, orderId: int, itemId: ItemIdentification) -> bool
        """
        pass

    def ValidateOrderIdWithOrderLine(self, *args): #cannot find CLR method
        """ ValidateOrderIdWithOrderLine(self: InboundReceiveLine, orderLine: InboundOrderLine, orderId: int) -> bool """
        pass

    def ValidateOrderNumberWithOrderLine(self, *args): #cannot find CLR method
        """ ValidateOrderNumberWithOrderLine(self: InboundReceiveLine, orderLine: InboundOrderLine, orderNumber: str) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BarcodePresent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BarcodePresent(self: InboundReceiveLine) -> Nullable[bool]

Set: BarcodePresent(self: InboundReceiveLine) = value
"""

    CurrentVendorItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentVendorItemCode(self: InboundReceiveLine) -> str

"""

    DefaultVendorItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultVendorItemCode(self: InboundReceiveLine) -> str

"""

    HasInstructions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasInstructions(self: InboundReceiveLine) -> bool

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: InboundReceiveLine) -> str

"""

    Instructions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Instructions(self: InboundReceiveLine) -> Array[str]

"""

    IsBatchNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBatchNumberItem(self: InboundReceiveLine) -> bool

"""

    IsSerialNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSerialNumberItem(self: InboundReceiveLine) -> bool

"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: InboundReceiveLine) -> str

Set: ItemCode(self: InboundReceiveLine) = value
"""

    ItemDefaultLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemDefaultLocation(self: InboundReceiveLine) -> str

"""

    ItemIdRegistration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIdRegistration(self: InboundReceiveLine) -> ItemIdentificationRegistration

Set: ItemIdRegistration(self: InboundReceiveLine) = value
"""

    LineDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineDescription(self: InboundReceiveLine) -> str

"""

    OrderLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderLines(self: InboundReceiveLine) -> InboundOrderLines

"""

    QuantityLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityLeft(self: InboundReceiveLine) -> Decimal

"""

    QuantityOrdered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityOrdered(self: InboundReceiveLine) -> Decimal

"""

    QuantityReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityReceived(self: InboundReceiveLine) -> Decimal

"""

    QuantityToReceive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityToReceive(self: InboundReceiveLine) -> Decimal

"""

    SalesUnitCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SalesUnitCode(self: InboundReceiveLine) -> str

Set: SalesUnitCode(self: InboundReceiveLine) = value
"""

    UnitCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitCode(self: InboundReceiveLine) -> str

Set: UnitCode(self: InboundReceiveLine) = value
"""



class InboundReceiveLines:
    """
    InboundReceiveLines(collection: IEnumerable[InboundReceiveLine])
    InboundReceiveLines()
    """
    def AddLinesFrom(self, orderLines):
        """ AddLinesFrom(self: InboundReceiveLines, orderLines: InboundOrderLines) """
        pass

    def AddOrUpdateLicensePlate(self, licensePlate):
        """ AddOrUpdateLicensePlate(self: InboundReceiveLines, licensePlate: LicensePlate) """
        pass

    def AddOrUpdateLicensePlateItems(self, item):
        """ AddOrUpdateLicensePlateItems(self: InboundReceiveLines, item: LicensePlateItem) """
        pass

    def Clear(self):
        """ Clear(self: InboundReceiveLines) """
        pass

    @staticmethod
    def FromIEnumerable(lines):
        """ FromIEnumerable(lines: IEnumerable[InboundReceiveLine]) -> InboundReceiveLines """
        pass

    def GetById(self, lineId):
        """ GetById(self: InboundReceiveLines, lineId: str) -> InboundReceiveLine """
        pass

    def GetIdsOfReceivedOrders(self):
        """ GetIdsOfReceivedOrders(self: InboundReceiveLines) -> List[int] """
        pass

    def GetKey(self):
        """ GetKey(self: InboundReceiveLines) -> int """
        pass

    def GetOrderLines(self):
        """ GetOrderLines(self: InboundReceiveLines) -> InboundOrderLines """
        pass

    def GetOrderLinesByOrderId(self, orderId):
        """ GetOrderLinesByOrderId(self: InboundReceiveLines, orderId: int) -> InboundOrderLines """
        pass

    def GetQuantityReceived(self, predicate):
        """ GetQuantityReceived(self: InboundReceiveLines, predicate: Predicate[InboundReceiveLine]) -> Decimal """
        pass

    def GetQuantityReceivedByItemCode(self, itemCode):
        """ GetQuantityReceivedByItemCode(self: InboundReceiveLines, itemCode: str) -> Decimal """
        pass

    def GetQuantityReceivedOfItem(self, *__args):
        """
        GetQuantityReceivedOfItem(self: InboundReceiveLines, receiveLineId: str) -> Decimal
        GetQuantityReceivedOfItem(self: InboundReceiveLines, itemCode: str, itemIdNumber: str) -> Decimal
        """
        pass

    def GetQuantityToReceiveOfItem(self, receiveLineId):
        """ GetQuantityToReceiveOfItem(self: InboundReceiveLines, receiveLineId: str) -> Decimal """
        pass

    def GetReceivedOrderLines(self):
        """ GetReceivedOrderLines(self: InboundReceiveLines) -> InboundOrderLines """
        pass

    def GetReceivedOrderLinesByOrderId(self, orderId):
        """ GetReceivedOrderLinesByOrderId(self: InboundReceiveLines, orderId: int) -> InboundOrderLines """
        pass

    def IndexOf(self, item, index=None, count=None):
        """ IndexOf(self: InboundReceiveLines, lineId: str) -> int """
        pass

    def MarkOrderLinesAsProcessed(self, orderId):
        """ MarkOrderLinesAsProcessed(self: InboundReceiveLines, orderId: int) """
        pass

    def RemoveLicensePlate(self, id):
        """ RemoveLicensePlate(self: InboundReceiveLines, id: int) """
        pass

    def RemoveLicensePlateItem(self, id):
        """ RemoveLicensePlateItem(self: InboundReceiveLines, id: int) """
        pass

    def SetOrderData(self, order):
        """ SetOrderData(self: InboundReceiveLines, order: InboundOrder) """
        pass

    def Sort(self, *__args):
        """ Sort(self: InboundReceiveLines, comparer: Func[InboundReceiveLine, str]) -> InboundReceiveLines """
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
    def __new__(self, collection=None):
        """
        __new__(cls: type, collection: IEnumerable[InboundReceiveLine])
        __new__(cls: type)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    CustomerNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomerNumber(self: InboundReceiveLines) -> str

Set: CustomerNumber(self: InboundReceiveLines) = value
"""

    GroupGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupGuid(self: InboundReceiveLines) -> Guid

Set: GroupGuid(self: InboundReceiveLines) = value
"""

    HasLicensePlates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasLicensePlates(self: InboundReceiveLines) -> bool

"""

    IsDisposable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDisposable(self: InboundReceiveLines) -> bool

"""

    LicensePlateItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicensePlateItems(self: InboundReceiveLines) -> LicensePlateItems

"""

    LicensePlates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicensePlates(self: InboundReceiveLines) -> LicensePlates

"""

    Notes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Notes(self: InboundReceiveLines) -> str

Set: Notes(self: InboundReceiveLines) = value
"""

    OrderIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderIds(self: InboundReceiveLines) -> Dictionary[int, str]

"""

    OrderNumberList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderNumberList(self: InboundReceiveLines) -> str

"""

    OrderType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderType(self: InboundReceiveLines) -> InboundOrderTypeEnum

Set: OrderType(self: InboundReceiveLines) = value
"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreserveState(self: InboundReceiveLines) -> bool

"""

    ProcessState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProcessState(self: InboundReceiveLines) -> ProcessReceiveLinesStepsEnum

Set: ProcessState(self: InboundReceiveLines) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: InboundReceiveLines) -> str

Set: WarehouseCode(self: InboundReceiveLines) = value
"""


    ValueMember = 'Id'


class PrepareAdhocRmaReceiveLinesArgs:
    """ PrepareAdhocRmaReceiveLinesArgs() """
    def GetHashCode(self):
        """ GetHashCode(self: PrepareAdhocRmaReceiveLinesArgs) -> int """
        pass

    def ToPrepareInboundReceiveLinesArgs(self):
        """ ToPrepareInboundReceiveLinesArgs(self: PrepareAdhocRmaReceiveLinesArgs) -> PrepareInboundReceiveLinesArgs """
        pass

    Customer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Customer(self: PrepareAdhocRmaReceiveLinesArgs) -> Customer

Set: Customer(self: PrepareAdhocRmaReceiveLinesArgs) = value
"""

    HistoryOutboundOrders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HistoryOutboundOrders(self: PrepareAdhocRmaReceiveLinesArgs) -> HistoryOutboundOrders

Set: HistoryOutboundOrders(self: PrepareAdhocRmaReceiveLinesArgs) = value
"""

    OrderType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderType(self: PrepareAdhocRmaReceiveLinesArgs) -> InboundOrderTypeEnum

"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: PrepareAdhocRmaReceiveLinesArgs) -> str

Set: WarehouseCode(self: PrepareAdhocRmaReceiveLinesArgs) = value
"""



class PrepareInboundReceiveLinesArgs:
    """ PrepareInboundReceiveLinesArgs() """
    CustomerNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomerNumber(self: PrepareInboundReceiveLinesArgs) -> str

Set: CustomerNumber(self: PrepareInboundReceiveLinesArgs) = value
"""

    OrderType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderType(self: PrepareInboundReceiveLinesArgs) -> InboundOrderTypeEnum

Set: OrderType(self: PrepareInboundReceiveLinesArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: PrepareInboundReceiveLinesArgs) -> str

Set: WarehouseCode(self: PrepareInboundReceiveLinesArgs) = value
"""



class PreReceiptArgs:
    """ PreReceiptArgs() """
    IncludeCompleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeCompleted(self: PreReceiptArgs) -> bool

Set: IncludeCompleted(self: PreReceiptArgs) = value
"""

    Paging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Paging(self: PreReceiptArgs) -> PagingParams

Set: Paging(self: PreReceiptArgs) = value
"""

    StatusFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StatusFlags(self: PreReceiptArgs) -> PreReceiptStatus

Set: StatusFlags(self: PreReceiptArgs) = value
"""



class PreReceiptLine:
    """ PreReceiptLine() """
    CurrentVendorItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentVendorItemCode(self: PreReceiptLine) -> str

Set: CurrentVendorItemCode(self: PreReceiptLine) = value
"""

    DateReceipt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DateReceipt(self: PreReceiptLine) -> DateTime

Set: DateReceipt(self: PreReceiptLine) = value
"""

    DefaultVendorItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultVendorItemCode(self: PreReceiptLine) -> str

Set: DefaultVendorItemCode(self: PreReceiptLine) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: PreReceiptLine) -> int

Set: Id(self: PreReceiptLine) = value
"""

    IsBatchNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBatchNumberItem(self: PreReceiptLine) -> bool

Set: IsBatchNumberItem(self: PreReceiptLine) = value
"""

    IsFullyReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFullyReceived(self: PreReceiptLine) -> bool

"""

    IsSerialNumberItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSerialNumberItem(self: PreReceiptLine) -> bool

Set: IsSerialNumberItem(self: PreReceiptLine) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: PreReceiptLine) -> str

Set: ItemCode(self: PreReceiptLine) = value
"""

    ItemDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemDescription(self: PreReceiptLine) -> str

Set: ItemDescription(self: PreReceiptLine) = value
"""

    ItemIdRegistration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIdRegistration(self: PreReceiptLine) -> ItemIdentificationRegistration

Set: ItemIdRegistration(self: PreReceiptLine) = value
"""

    ItemIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIds(self: PreReceiptLine) -> ItemIdentifications

Set: ItemIds(self: PreReceiptLine) = value
"""

    ItemPurchasePrice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemPurchasePrice(self: PreReceiptLine) -> Decimal

Set: ItemPurchasePrice(self: PreReceiptLine) = value
"""

    LineCurrencyCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineCurrencyCode(self: PreReceiptLine) -> str

Set: LineCurrencyCode(self: PreReceiptLine) = value
"""

    LineInstruction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineInstruction(self: PreReceiptLine) -> str

Set: LineInstruction(self: PreReceiptLine) = value
"""

    PercentageReceived = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PercentageReceived(self: PreReceiptLine) -> int

"""

    PreReceiptId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreReceiptId(self: PreReceiptLine) -> int

Set: PreReceiptId(self: PreReceiptLine) = value
"""

    PurchaseOrderId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PurchaseOrderId(self: PreReceiptLine) -> int

Set: PurchaseOrderId(self: PreReceiptLine) = value
"""

    PurchaseOrderLineId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PurchaseOrderLineId(self: PreReceiptLine) -> int

Set: PurchaseOrderLineId(self: PreReceiptLine) = value
"""

    PurchaseOrderLineNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PurchaseOrderLineNumber(self: PreReceiptLine) -> int

Set: PurchaseOrderLineNumber(self: PreReceiptLine) = value
"""

    PurchaseOrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PurchaseOrderNumber(self: PreReceiptLine) -> str

Set: PurchaseOrderNumber(self: PreReceiptLine) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: PreReceiptLine) -> Decimal

Set: Quantity(self: PreReceiptLine) = value
"""

    QuantityOrdered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityOrdered(self: PreReceiptLine) -> Decimal

Set: QuantityOrdered(self: PreReceiptLine) = value
"""

    QuantitySupplierPackageSlip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantitySupplierPackageSlip(self: PreReceiptLine) -> Decimal

Set: QuantitySupplierPackageSlip(self: PreReceiptLine) = value
"""

    QuantityToReceive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityToReceive(self: PreReceiptLine) -> Decimal

"""

    SalesUnitCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SalesUnitCode(self: PreReceiptLine) -> str

Set: SalesUnitCode(self: PreReceiptLine) = value
"""

    SalesUnitFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SalesUnitFactor(self: PreReceiptLine) -> Decimal

Set: SalesUnitFactor(self: PreReceiptLine) = value
"""

    SupplierCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupplierCode(self: PreReceiptLine) -> str

Set: SupplierCode(self: PreReceiptLine) = value
"""

    SupplierName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupplierName(self: PreReceiptLine) -> str

Set: SupplierName(self: PreReceiptLine) = value
"""

    UnitCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitCode(self: PreReceiptLine) -> str

Set: UnitCode(self: PreReceiptLine) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: PreReceiptLine) -> str

Set: WarehouseCode(self: PreReceiptLine) = value
"""



class PreReceiptLinesArgs:
    """ PreReceiptLinesArgs() """
    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filter(self: PreReceiptLinesArgs) -> str

Set: Filter(self: PreReceiptLinesArgs) = value
"""

    IncludeCompleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeCompleted(self: PreReceiptLinesArgs) -> bool

Set: IncludeCompleted(self: PreReceiptLinesArgs) = value
"""

    PreReceiptIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreReceiptIds(self: PreReceiptLinesArgs) -> Array[int]

Set: PreReceiptIds(self: PreReceiptLinesArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: PreReceiptLinesArgs) -> str

Set: WarehouseCode(self: PreReceiptLinesArgs) = value
"""



class PreReceiptReceiveLines:
    """ PreReceiptReceiveLines() """
    def GetIdsOfReceivedOrders(self):
        """ GetIdsOfReceivedOrders(self: PreReceiptReceiveLines) -> List[int] """
        pass

    def IndexOf(self, item, index=None, count=None):
        """ IndexOf(self: InboundReceiveLines, lineId: str) -> int """
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

    PreReceiptId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreReceiptId(self: PreReceiptReceiveLines) -> int

Set: PreReceiptId(self: PreReceiptReceiveLines) = value
"""



class PreReceipts:
    """ PreReceipts() """
    @staticmethod
    def FromIEnumerable(list):
        """ FromIEnumerable(list: IEnumerable[PreReceipt]) -> PreReceipts """
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


class PreReceiptStatus:
    """ enum (flags) PreReceiptStatus, values: Active (2), Archived (16), InProcess (4), PartiallyReceived (8), Pending (1) """
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
    InProcess = None
    PartiallyReceived = None
    Pending = None
    value__ = None


class PreReceiptSummaries:
    """ PreReceiptSummaries() """
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

    UniquePreReceiptsAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UniquePreReceiptsAsString(self: PreReceiptSummaries) -> str

"""


    Delimiter = None


class PreReceiptSummary:
    """ PreReceiptSummary() """
    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: PreReceiptSummary) -> int

Set: Id(self: PreReceiptSummary) = value
"""

    IdAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IdAsString(self: PreReceiptSummary) -> str

"""

    OrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderNumber(self: PreReceiptSummary) -> str

Set: OrderNumber(self: PreReceiptSummary) = value
"""



class ProcessInboundReceiveLinesArgs:
    """ ProcessInboundReceiveLinesArgs() """
    CacheKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CacheKey(self: ProcessInboundReceiveLinesArgs) -> CacheKey

Set: CacheKey(self: ProcessInboundReceiveLinesArgs) = value
"""

    CacheKeyOfResults = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CacheKeyOfResults(self: ProcessInboundReceiveLinesArgs) -> CacheKey

Set: CacheKeyOfResults(self: ProcessInboundReceiveLinesArgs) = value
"""

    DefaultReceiptLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultReceiptLocation(self: ProcessInboundReceiveLinesArgs) -> str

Set: DefaultReceiptLocation(self: ProcessInboundReceiveLinesArgs) = value
"""

    OrderDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderDescription(self: ProcessInboundReceiveLinesArgs) -> str

Set: OrderDescription(self: ProcessInboundReceiveLinesArgs) = value
"""

    PreReceiptId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreReceiptId(self: ProcessInboundReceiveLinesArgs) -> int

Set: PreReceiptId(self: ProcessInboundReceiveLinesArgs) = value
"""

    PrintLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintLines(self: ProcessInboundReceiveLinesArgs) -> PrintLinesBase

Set: PrintLines(self: ProcessInboundReceiveLinesArgs) = value
"""

    YourReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YourReference(self: ProcessInboundReceiveLinesArgs) -> str

Set: YourReference(self: ProcessInboundReceiveLinesArgs) = value
"""



class ProcessInboundReceiveLinesResult:
    """ ProcessInboundReceiveLinesResult() """
    def GetKey(self):
        """ GetKey(self: ProcessInboundReceiveLinesResult) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Lifetime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lifetime(self: ProcessInboundReceiveLinesResult) -> CacheLifeTimes

"""

    PreserveState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreserveState(self: ProcessInboundReceiveLinesResult) -> bool

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: ProcessInboundReceiveLinesResult) -> Dictionary[InboundOrder, ErpProcessPurchaseOrderLinesResult]

Set: Results(self: ProcessInboundReceiveLinesResult) = value
"""



class ProcessReceiveLinesStepsEnum:
    """ enum ProcessReceiveLinesStepsEnum, values: CreatePrintLines (2), Done (7), LogReceiveLines (1), PrintErpReceipt (5), PrintReceipt (6), ProcessReceiveLines (0), UpdateLicensePlates (4), UpdateStock (3) """
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

    CreatePrintLines = None
    Done = None
    LogReceiveLines = None
    PrintErpReceipt = None
    PrintReceipt = None
    ProcessReceiveLines = None
    UpdateLicensePlates = None
    UpdateStock = None
    value__ = None


class ReceiptTypeEnum:
    """ enum ReceiptTypeEnum, values: PreReceipt (0), Purchase (1) """
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

    PreReceipt = None
    Purchase = None
    value__ = None


class ReceiveArgs:
    """ ReceiveArgs() """
    CacheKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CacheKey(self: ReceiveArgs) -> CacheKey

Set: CacheKey(self: ReceiveArgs) = value
"""

    EndDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndDate(self: ReceiveArgs) -> Nullable[DateTime]

Set: EndDate(self: ReceiveArgs) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: ReceiveArgs) -> str

Set: ItemCode(self: ReceiveArgs) = value
"""

    ItemIdNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIdNumber(self: ReceiveArgs) -> str

Set: ItemIdNumber(self: ReceiveArgs) = value
"""

    LabelArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelArgs(self: ReceiveArgs) -> PrintLabelArgs

Set: LabelArgs(self: ReceiveArgs) = value
"""

    OrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderNumber(self: ReceiveArgs) -> str

Set: OrderNumber(self: ReceiveArgs) = value
"""

    Quantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Quantity(self: ReceiveArgs) -> Decimal

Set: Quantity(self: ReceiveArgs) = value
"""

    ReceiveLineId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReceiveLineId(self: ReceiveArgs) -> str

Set: ReceiveLineId(self: ReceiveArgs) = value
"""

    UnitCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitCode(self: ReceiveArgs) -> str

Set: UnitCode(self: ReceiveArgs) = value
"""



class ReceiveItemIdMultiArgs:
    """ ReceiveItemIdMultiArgs() """
    CacheKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CacheKey(self: ReceiveItemIdMultiArgs) -> CacheKey

Set: CacheKey(self: ReceiveItemIdMultiArgs) = value
"""

    InboundReceiveLineUpdatet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InboundReceiveLineUpdatet(self: ReceiveItemIdMultiArgs) -> InboundReceiveLine

Set: InboundReceiveLineUpdatet(self: ReceiveItemIdMultiArgs) = value
"""

    ItemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCode(self: ReceiveItemIdMultiArgs) -> str

Set: ItemCode(self: ReceiveItemIdMultiArgs) = value
"""

    ItemIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemIds(self: ReceiveItemIdMultiArgs) -> ItemIdentifications

Set: ItemIds(self: ReceiveItemIdMultiArgs) = value
"""

    OrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderNumber(self: ReceiveItemIdMultiArgs) -> str

Set: OrderNumber(self: ReceiveItemIdMultiArgs) = value
"""

    ReceiveArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReceiveArgs(self: ReceiveItemIdMultiArgs) -> ReceiveArgs

"""

    ReceiveLineId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReceiveLineId(self: ReceiveItemIdMultiArgs) -> str

Set: ReceiveLineId(self: ReceiveItemIdMultiArgs) = value
"""



class ReceiveItemIdRangeArgs:
    """ ReceiveItemIdRangeArgs() """
    CacheKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CacheKey(self: ReceiveItemIdRangeArgs) -> CacheKey

Set: CacheKey(self: ReceiveItemIdRangeArgs) = value
"""

    OrderNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderNumber(self: ReceiveItemIdRangeArgs) -> str

Set: OrderNumber(self: ReceiveItemIdRangeArgs) = value
"""

    ReceiveArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReceiveArgs(self: ReceiveItemIdRangeArgs) -> ReceiveArgs

Set: ReceiveArgs(self: ReceiveItemIdRangeArgs) = value
"""

    ReceiveLineId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReceiveLineId(self: ReceiveItemIdRangeArgs) -> str

Set: ReceiveLineId(self: ReceiveItemIdRangeArgs) = value
"""



class ReceiveLinesForPreReceiptArgs:
    """ ReceiveLinesForPreReceiptArgs() """
    PreReceiptId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreReceiptId(self: ReceiveLinesForPreReceiptArgs) -> int

Set: PreReceiptId(self: ReceiveLinesForPreReceiptArgs) = value
"""

    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Result(self: ReceiveLinesForPreReceiptArgs) -> InboundReceiveLines

Set: Result(self: ReceiveLinesForPreReceiptArgs) = value
"""

    VendorNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VendorNumber(self: ReceiveLinesForPreReceiptArgs) -> str

Set: VendorNumber(self: ReceiveLinesForPreReceiptArgs) = value
"""

    WarehouseCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarehouseCode(self: ReceiveLinesForPreReceiptArgs) -> str

Set: WarehouseCode(self: ReceiveLinesForPreReceiptArgs) = value
"""



class ReceiveWithLicensePlateArgs:
    """ ReceiveWithLicensePlateArgs() """
    AddNewLicensePlate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AddNewLicensePlate(self: ReceiveWithLicensePlateArgs) -> bool

Set: AddNewLicensePlate(self: ReceiveWithLicensePlateArgs) = value
"""

    LicensePlateId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicensePlateId(self: ReceiveWithLicensePlateArgs) -> int

Set: LicensePlateId(self: ReceiveWithLicensePlateArgs) = value
"""

    ModifiedLicensePlateItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModifiedLicensePlateItems(self: ReceiveWithLicensePlateArgs) -> LicensePlateItems

Set: ModifiedLicensePlateItems(self: ReceiveWithLicensePlateArgs) = value
"""

    NewLicensePlates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewLicensePlates(self: ReceiveWithLicensePlateArgs) -> LicensePlates

Set: NewLicensePlates(self: ReceiveWithLicensePlateArgs) = value
"""



class UpdatePreReceiptStatusArgs:
    """ UpdatePreReceiptStatusArgs() """
    NewStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewStatus(self: UpdatePreReceiptStatusArgs) -> PreReceiptStatus

Set: NewStatus(self: UpdatePreReceiptStatusArgs) = value
"""

    PreReceiptId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreReceiptId(self: UpdatePreReceiptStatusArgs) -> int

Set: PreReceiptId(self: UpdatePreReceiptStatusArgs) = value
"""


