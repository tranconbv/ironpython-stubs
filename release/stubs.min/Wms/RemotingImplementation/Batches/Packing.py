# encoding: utf-8
# module Wms.RemotingImplementation.Batches.Packing calls itself Packing
# from Wms.RemotingImplementation,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DefaultPackageCreator:
 """ DefaultPackageCreator(manager: BatchPackManager,customer: PackCustomer,batches: IEnumerable[Batch],packages: TransportPackages,autoPackItems: bool,addNewPackages: bool) """
 def AddPackage(self,*args):
  """ AddPackage(self: DefaultPackageCreator,generateSSCCNumber: bool) -> Guid """
  pass
 def AddTransportItem(self,*args):
  """ AddTransportItem(self: DefaultPackageCreator,line: OutboundOrderLine,packLoc: ItemPackLocation,colloReference: str) -> TransportItem """
  pass
 def Cleanup(self,*args):
  """ Cleanup(self: DefaultPackageCreator) """
  pass
 def Create(self):
  """ Create(self: DefaultPackageCreator) """
  pass
 def GetPackageGuidForPacking(self,*args):
  """ GetPackageGuidForPacking(self: DefaultPackageCreator) -> Guid """
  pass
 def HasItemsLeft(self,*args):
  """ HasItemsLeft(self: DefaultPackageCreator) -> bool """
  pass
 def PrepareItems(self,*args):
  """ PrepareItems(self: DefaultPackageCreator) -> TransportItems """
  pass
 def ShouldAddExtraPackage(self,*args):
  """ ShouldAddExtraPackage(self: DefaultPackageCreator) -> bool """
  pass
 @staticmethod
 def __new__(self,manager,customer,batches,packages,autoPackItems,addNewPackages):
  """ __new__(cls: type,manager: BatchPackManager,customer: PackCustomer,batches: IEnumerable[Batch],packages: TransportPackages,autoPackItems: bool,addNewPackages: bool) """
  pass
 Items=None
 _batches=None
 _customer=None
 _transportPackages=None


class ColloReferencePacker:
 """ ColloReferencePacker(manager: BatchPackManager,customer: PackCustomer,batches: IEnumerable[Batch],packages: TransportPackages) """
 @staticmethod
 def __new__(self,manager,customer,batches,packages):
  """ __new__(cls: type,manager: BatchPackManager,customer: PackCustomer,batches: IEnumerable[Batch],packages: TransportPackages) """
  pass
 Items=None
 _batches=None
 _customer=None
 _transportPackages=None


class OrderPackageCreator:
 """ OrderPackageCreator(manager: BatchPackManager,customer: PackCustomer,batches: IEnumerable[Batch],packages: TransportPackages) """
 @staticmethod
 def __new__(self,manager,customer,batches,packages):
  """ __new__(cls: type,manager: BatchPackManager,customer: PackCustomer,batches: IEnumerable[Batch],packages: TransportPackages) """
  pass
 Items=None
 _batches=None
 _customer=None
 _transportPackages=None


class PackageCreatorFactory:
 # no doc
 @staticmethod
 def Create(packages,batches,customer):
  """ Create(packages: TransportPackages,batches: IEnumerable[Batch],customer: PackCustomer) """
  pass
 __all__=[
  'Create',
 ]


class TransportPackagesHelper:
 """ TransportPackagesHelper() """
 def AddTransportPackage(self,args):
  """ AddTransportPackage(self: TransportPackagesHelper,args: AddTransportPackageArgs) """
  pass
 def GetNewSSCC(self):
  """ GetNewSSCC(self: TransportPackagesHelper) -> str """
  pass
 NewPackageGuid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NewPackageGuid(self: TransportPackagesHelper) -> Guid

"""

 Packages=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Packages(self: TransportPackagesHelper) -> TransportPackages

"""


