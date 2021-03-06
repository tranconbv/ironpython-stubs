# encoding: utf-8
# module Wms.RemotingObjects.Scripting.Modules calls itself Modules
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class AddModuleArgs(object):
 """ AddModuleArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return AddModuleArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Content=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Content(self: AddModuleArgs) -> Array[Byte]

Set: Content(self: AddModuleArgs)=value
"""

 FileName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: FileName(self: AddModuleArgs) -> str

Set: FileName(self: AddModuleArgs)=value
"""

 Path=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Path(self: AddModuleArgs) -> str

Set: Path(self: AddModuleArgs)=value
"""



class GetLibArgs(object):
 """ GetLibArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return GetLibArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Path=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Path(self: GetLibArgs) -> str

Set: Path(self: GetLibArgs)=value
"""



class LibContent(object):
 """ LibContent() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return LibContent()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Directory=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Directory(self: LibContent) -> str

Set: Directory(self: LibContent)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Name(self: LibContent) -> str

Set: Name(self: LibContent)=value
"""

 ReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ReadOnly(self: LibContent) -> bool

Set: ReadOnly(self: LibContent)=value
"""

 SubContent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: SubContent(self: LibContent) -> LibContents

Set: SubContent(self: LibContent)=value
"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Type(self: LibContent) -> LibContentType

Set: Type(self: LibContent)=value
"""



class LibContents(FindableList):
 """ LibContents() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return LibContents()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Path=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Directory to retrieve the contents. An empty path will retrieve the root content.

Get: Path(self: LibContents) -> str

Set: Path(self: LibContents)=value
"""



class LibContentType:
 """ enum LibContentType,values: File (1),Folder (0) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return LibContentType()
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
 File=None
 Folder=None
 value__=None


class ModuleArgs(object):
 """ ModuleArgs() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ModuleArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Directory=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Directory(self: ModuleArgs) -> str

Set: Directory(self: ModuleArgs)=value
"""

 FileName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: FileName(self: ModuleArgs) -> str

Set: FileName(self: ModuleArgs)=value
"""

 Overwrite=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Overwrite(self: ModuleArgs) -> bool

Set: Overwrite(self: ModuleArgs)=value
"""

 Script=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Script(self: ModuleArgs) -> Array[Byte]

Set: Script(self: ModuleArgs)=value
"""



class PythonModule(object):
 """ PythonModule() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PythonModule()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Content=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Content(self: PythonModule) -> str

Set: Content(self: PythonModule)=value
"""

 IsReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: IsReadOnly(self: PythonModule) -> bool

Set: IsReadOnly(self: PythonModule)=value
"""

 Path=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Path(self: PythonModule) -> str

Set: Path(self: PythonModule)=value
"""



