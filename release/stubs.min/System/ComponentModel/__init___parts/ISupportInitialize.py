class ISupportInitialize:
 """ Specifies that this object supports a simple,transacted notification for batch initialization. """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ISupportInitialize()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def BeginInit(self):
  """
  BeginInit(self: ISupportInitialize)
   Signals the object that initialization is starting.
  """
  pass
 def EndInit(self):
  """
  EndInit(self: ISupportInitialize)
   Signals the object that initialization is complete.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
