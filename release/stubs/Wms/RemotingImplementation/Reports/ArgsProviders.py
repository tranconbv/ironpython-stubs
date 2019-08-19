# encoding: utf-8
# module Wms.RemotingImplementation.Reports.ArgsProviders calls itself ArgsProviders
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ReportArgsProviderBase():
    # no doc
    def GetCustomOrDefaultReportPath(self, *args): #cannot find CLR method
        """ GetCustomOrDefaultReportPath(defaultReportPath: str, customReportPath: str, reportFile: str) -> str """
        pass

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ReportArgsProviderBase()

class ReportPackageSlipArgsProvider(ReportArgsProviderBase):
    """ ReportPackageSlipArgsProvider(general: General) """
    def Prepare(self, args):
        """ Prepare(self: ReportPackageSlipArgsProvider, args: PrintPackageSlipArgs) -> ReportPackageSlipArgsProvider """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, general):
        """ __new__(cls: type, general: General) """
        pass

    DataArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataArgs(self: ReportPackageSlipArgsProvider) -> ReportDataArgs

"""

    PrintArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintArgs(self: ReportPackageSlipArgsProvider) -> ReportPrintArgs

"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ReportPackageSlipArgsProvider()

class ReportPickListArgsProvider(ReportArgsProviderBase):
    """ ReportPickListArgsProvider(general: General) """
    def Prepare(self, args, batch):
        """ Prepare(self: ReportPickListArgsProvider, args: PrintPickingListArgs, batch: Batch) -> ReportPickListArgsProvider """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, general):
        """ __new__(cls: type, general: General) """
        pass

    DataArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataArgs(self: ReportPickListArgsProvider) -> ReportDataArgs

"""

    ExportArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExportArgs(self: ReportPickListArgsProvider) -> ReportExportArgs

"""

    PrintArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintArgs(self: ReportPickListArgsProvider) -> ReportPrintArgs

"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ReportPickListArgsProvider()

class ReportPrereceivementReceiptArgsProvider(ReportArgsProviderBase):
    """ ReportPrereceivementReceiptArgsProvider(general: General) """
    def Prepare(self, dataset):
        """ Prepare(self: ReportPrereceivementReceiptArgsProvider, dataset: PurchaseOrders_GetHistoryLinesDataTable) -> ReportPrereceivementReceiptArgsProvider """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, general):
        """ __new__(cls: type, general: General) """
        pass

    DataArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataArgs(self: ReportPrereceivementReceiptArgsProvider) -> ReportDataArgs

"""

    PrintArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintArgs(self: ReportPrereceivementReceiptArgsProvider) -> ReportPrintArgs

"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ReportPrereceivementReceiptArgsProvider()

class ReportPurchaseReceiptArgsProvider(ReportArgsProviderBase):
    """ ReportPurchaseReceiptArgsProvider(general: General) """
    def Prepare(self, groupGuid, printer, noOfCopies):
        """ Prepare(self: ReportPurchaseReceiptArgsProvider, groupGuid: Guid, printer: str, noOfCopies: int) -> ReportPurchaseReceiptArgsProvider """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, general):
        """ __new__(cls: type, general: General) """
        pass

    DataArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataArgs(self: ReportPurchaseReceiptArgsProvider) -> ReportDataArgs

"""

    PrintArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintArgs(self: ReportPurchaseReceiptArgsProvider) -> ReportPrintArgs

"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ReportPurchaseReceiptArgsProvider()

class ReportRmaReceiptArgsProvider(ReportArgsProviderBase):
    """ ReportRmaReceiptArgsProvider(general: General) """
    def Prepare(self, groupGuid, printer, noOfCopies):
        """ Prepare(self: ReportRmaReceiptArgsProvider, groupGuid: Guid, printer: str, noOfCopies: int) -> ReportRmaReceiptArgsProvider """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, general):
        """ __new__(cls: type, general: General) """
        pass

    DataArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataArgs(self: ReportRmaReceiptArgsProvider) -> ReportDataArgs

"""

    PrintArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintArgs(self: ReportRmaReceiptArgsProvider) -> ReportPrintArgs

"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ReportRmaReceiptArgsProvider()

