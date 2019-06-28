# encoding: utf-8
# module Wms.RemotingImplementation.Reports calls itself Reports
# from Wms.RemotingImplementation, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class IReportDataArgsProvider:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DataArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataArgs(self: IReportDataArgsProvider) -> ReportDataArgs

"""



class IReportExportArgsProvider:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ExportArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExportArgs(self: IReportExportArgsProvider) -> ReportExportArgs

"""



class IReportPrintArgsProvider:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    PrintArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintArgs(self: IReportPrintArgsProvider) -> ReportPrintArgs

"""



class IReportRenderer:
    # no doc
    def Export(self, *__args):
        """
        Export[T](self: IReportRenderer, provider: T) -> ReportExport
        Export(self: IReportRenderer, args: ReportExportArgs, dataArgs: ReportDataArgs) -> ReportExport
        """
        pass

    def Print(self, *__args):
        """ Print[T](self: IReportRenderer, provider: T)Print(self: IReportRenderer, args: ReportPrintArgs, dataArgs: ReportDataArgs) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ReportArgs:
    # no doc
    ReportFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReportFile(self: ReportArgs) -> str

Set: ReportFile(self: ReportArgs) = value
"""

    ReportParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReportParameters(self: ReportArgs) -> Dictionary[str, object]

Set: ReportParameters(self: ReportArgs) = value
"""



class ReportDataArgs:
    """ ReportDataArgs() """
    DataSources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataSources(self: ReportDataArgs) -> Dictionary[str, object]

Set: DataSources(self: ReportDataArgs) = value
"""

    MetaData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetaData(self: ReportDataArgs) -> SerializableDictionary[str, str]

Set: MetaData(self: ReportDataArgs) = value
"""



class ReportExport:
    """ ReportExport() """
    Buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Buffer(self: ReportExport) -> Array[Byte]

Set: Buffer(self: ReportExport) = value
"""

    Encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Encoding(self: ReportExport) -> str

Set: Encoding(self: ReportExport) = value
"""

    FileExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileExtension(self: ReportExport) -> str

Set: FileExtension(self: ReportExport) = value
"""

    Format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Format(self: ReportExport) -> ReportExportFormat

Set: Format(self: ReportExport) = value
"""

    MimeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MimeType(self: ReportExport) -> str

Set: MimeType(self: ReportExport) = value
"""

    NumberOfPages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfPages(self: ReportExport) -> int

Set: NumberOfPages(self: ReportExport) = value
"""



class ReportExportArgs:
    """ ReportExportArgs() """
    Format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Format(self: ReportExportArgs) -> ReportExportFormat

Set: Format(self: ReportExportArgs) = value
"""



class ReportExportFormat:
    """ enum ReportExportFormat, values: Excel (1), Image (3), PDF (0), Word (2) """
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

    Excel = None
    Image = None
    PDF = None
    value__ = None
    Word = None


class ReportPrintArgs:
    """ ReportPrintArgs() """
    DocumentName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DocumentName(self: ReportPrintArgs) -> str

Set: DocumentName(self: ReportPrintArgs) = value
"""

    NoOfCopies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NoOfCopies(self: ReportPrintArgs) -> int

Set: NoOfCopies(self: ReportPrintArgs) = value
"""

    PrinterName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrinterName(self: ReportPrintArgs) -> str

Set: PrinterName(self: ReportPrintArgs) = value
"""



# variables with complex values
