# encoding: utf-8
# module Wms.RemotingImplementation.Reports.ArgsProviders calls itself ArgsProviders
# from Wms.RemotingImplementation,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class ReportArgsProviderBase(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReportArgsProviderBase()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetCustomOrDefaultReportPath(self,*args):
  """ GetCustomOrDefaultReportPath(defaultReportPath: str,customReportPath: str,reportFile: str) -> str """
  pass

class ReportPackageSlipArgsProvider(ReportArgsProviderBase):
 """ ReportPackageSlipArgsProvider(general: General) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReportPackageSlipArgsProvider()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Prepare(self,args):
  """ Prepare(self: ReportPackageSlipArgsProvider,args: PrintPackageSlipArgs) -> ReportPackageSlipArgsProvider """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,general):
  """ __new__(cls: type,general: General) """
  pass
 DataArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DataArgs(self: ReportPackageSlipArgsProvider) -> ReportDataArgs

"""

 PrintArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PrintArgs(self: ReportPackageSlipArgsProvider) -> ReportPrintArgs

"""



class ReportPickListArgsProvider(ReportArgsProviderBase):
 """ ReportPickListArgsProvider(general: General) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReportPickListArgsProvider()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Prepare(self,args,batch):
  """ Prepare(self: ReportPickListArgsProvider,args: PrintPickingListArgs,batch: Batch) -> ReportPickListArgsProvider """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,general):
  """ __new__(cls: type,general: General) """
  pass
 DataArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DataArgs(self: ReportPickListArgsProvider) -> ReportDataArgs

"""

 ExportArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExportArgs(self: ReportPickListArgsProvider) -> ReportExportArgs

"""

 PrintArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PrintArgs(self: ReportPickListArgsProvider) -> ReportPrintArgs

"""



class ReportPrereceivementReceiptArgsProvider(ReportArgsProviderBase):
 """ ReportPrereceivementReceiptArgsProvider(general: General) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReportPrereceivementReceiptArgsProvider()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Prepare(self,dataset):
  """ Prepare(self: ReportPrereceivementReceiptArgsProvider,dataset: PurchaseOrders_GetHistoryLinesDataTable) -> ReportPrereceivementReceiptArgsProvider """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,general):
  """ __new__(cls: type,general: General) """
  pass
 DataArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DataArgs(self: ReportPrereceivementReceiptArgsProvider) -> ReportDataArgs

"""

 PrintArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PrintArgs(self: ReportPrereceivementReceiptArgsProvider) -> ReportPrintArgs

"""



class ReportPurchaseReceiptArgsProvider(ReportArgsProviderBase):
 """ ReportPurchaseReceiptArgsProvider(general: General) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReportPurchaseReceiptArgsProvider()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Prepare(self,groupGuid,printer,noOfCopies):
  """ Prepare(self: ReportPurchaseReceiptArgsProvider,groupGuid: Guid,printer: str,noOfCopies: int) -> ReportPurchaseReceiptArgsProvider """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,general):
  """ __new__(cls: type,general: General) """
  pass
 DataArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DataArgs(self: ReportPurchaseReceiptArgsProvider) -> ReportDataArgs

"""

 PrintArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PrintArgs(self: ReportPurchaseReceiptArgsProvider) -> ReportPrintArgs

"""



class ReportRmaReceiptArgsProvider(ReportArgsProviderBase):
 """ ReportRmaReceiptArgsProvider(general: General) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ReportRmaReceiptArgsProvider()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Prepare(self,groupGuid,printer,noOfCopies):
  """ Prepare(self: ReportRmaReceiptArgsProvider,groupGuid: Guid,printer: str,noOfCopies: int) -> ReportRmaReceiptArgsProvider """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,general):
  """ __new__(cls: type,general: General) """
  pass
 DataArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DataArgs(self: ReportRmaReceiptArgsProvider) -> ReportDataArgs

"""

 PrintArgs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PrintArgs(self: ReportRmaReceiptArgsProvider) -> ReportPrintArgs

"""



