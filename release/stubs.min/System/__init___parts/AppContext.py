class AppContext(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return AppContext()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def GetData(name):
  """ GetData(name: str) -> object """
  pass
 @staticmethod
 def SetSwitch(switchName,isEnabled):
  """ SetSwitch(switchName: str,isEnabled: bool) """
  pass
 @staticmethod
 def TryGetSwitch(switchName,isEnabled):
  """ TryGetSwitch(switchName: str) -> (bool,bool) """
  pass
 BaseDirectory='C:\\Users\\k.pawiroredjo\\Downloads\\IronPython.2.7.9\\net45\\'
 TargetFrameworkName='.NETFramework,Version=v4.5'
 __all__=[
  'GetData',
  'SetSwitch',
  'TryGetSwitch',
 ]

