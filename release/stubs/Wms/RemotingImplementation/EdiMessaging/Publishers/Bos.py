from Wms.EdiMessaging import *
# encoding: utf-8
# module Wms.RemotingImplementation.EdiMessaging.Publishers.Bos calls itself Bos
# from Wms.RemotingImplementation, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BosGenerateDptmntDatFileMessagePublisher(MessagePublisherBase):
    """ BosGenerateDptmntDatFileMessagePublisher(offlineScanning: IOfflineScanning, layoutFactory: IFixedLengthLayoutFactory[BosDepartment]) """
    Instance = BosGenerateDptmntDatFileMessagePublisher
    """hardcoded/returns an instance of the class"""
    def Start(self, onStoreMessage):
        """ Start(self: BosGenerateDptmntDatFileMessagePublisher, onStoreMessage: OnStoreMessage) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, offlineScanning, layoutFactory):
        """ __new__(cls: type, offlineScanning: IOfflineScanning, layoutFactory: IFixedLengthLayoutFactory[BosDepartment]) """
        pass


class BosGenerateKanbanDatFilesMessagePublisher(MessagePublisherBase):
    """ BosGenerateKanbanDatFilesMessagePublisher(offlineScanning: IOfflineScanning, layoutFactoryBarcodes: IFixedLengthLayoutFactory[BosKanbanBarcode], layoutFactoryProducts: IFixedLengthLayoutFactory[BosKanbanProduct]) """
    Instance = BosGenerateKanbanDatFilesMessagePublisher
    """hardcoded/returns an instance of the class"""
    def Start(self, onStoreMessage):
        """ Start(self: BosGenerateKanbanDatFilesMessagePublisher, onStoreMessage: OnStoreMessage) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, offlineScanning, layoutFactoryBarcodes, layoutFactoryProducts):
        """ __new__(cls: type, offlineScanning: IOfflineScanning, layoutFactoryBarcodes: IFixedLengthLayoutFactory[BosKanbanBarcode], layoutFactoryProducts: IFixedLengthLayoutFactory[BosKanbanProduct]) """
        pass


class BosGenerateMetaDatFileMessagePublisher(MessagePublisherBase):
    """ BosGenerateMetaDatFileMessagePublisher(offlineScanning: IOfflineScanning, layoutFactory: IFixedLengthLayoutFactory[BosMeta]) """
    Instance = BosGenerateMetaDatFileMessagePublisher
    """hardcoded/returns an instance of the class"""
    def Start(self, onStoreMessage):
        """ Start(self: BosGenerateMetaDatFileMessagePublisher, onStoreMessage: OnStoreMessage) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, offlineScanning, layoutFactory):
        """ __new__(cls: type, offlineScanning: IOfflineScanning, layoutFactory: IFixedLengthLayoutFactory[BosMeta]) """
        pass


class BosGenerateProductDatFilesPublisher(MessagePublisherBase):
    """ BosGenerateProductDatFilesPublisher(general: General, offlineScanning: IOfflineScanning, layoutFactoryItem: IFixedLengthLayoutFactory[BosProduct], layoutFactoryItemIndexFactory: IFixedLengthLayoutFactory[BosProductIndex]) """
    Instance = BosGenerateProductDatFilesPublisher
    """hardcoded/returns an instance of the class"""
    def Start(self, onStoreMessage):
        """ Start(self: BosGenerateProductDatFilesPublisher, onStoreMessage: OnStoreMessage) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, general, offlineScanning, layoutFactoryItem, layoutFactoryItemIndexFactory):
        """ __new__(cls: type, general: General, offlineScanning: IOfflineScanning, layoutFactoryItem: IFixedLengthLayoutFactory[BosProduct], layoutFactoryItemIndexFactory: IFixedLengthLayoutFactory[BosProductIndex]) """
        pass


class BosGenerateUsersDatFileMessagePublisher(MessagePublisherBase):
    """ BosGenerateUsersDatFileMessagePublisher(general: General, offlineScanning: IOfflineScanning, layoutFactory: IFixedLengthLayoutFactory[UserWithSecrets]) """
    Instance = BosGenerateUsersDatFileMessagePublisher
    """hardcoded/returns an instance of the class"""
    def Start(self, onStoreMessage):
        """ Start(self: BosGenerateUsersDatFileMessagePublisher, onStoreMessage: OnStoreMessage) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, general, offlineScanning, layoutFactory):
        """ __new__(cls: type, general: General, offlineScanning: IOfflineScanning, layoutFactory: IFixedLengthLayoutFactory[UserWithSecrets]) """
        pass


