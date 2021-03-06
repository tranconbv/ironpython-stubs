# encoding: utf-8
# module Wms.RemotingImplementation.TaskScheduler calls itself TaskScheduler
# from Wms.RemotingImplementation,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from System.Collections.Generic import *
from ..__init__ import *

# no functions
# classes

class TaskAlreadyRunningException(Exception):
 """
 TaskAlreadyRunningException()
 TaskAlreadyRunningException(message: str)
 TaskAlreadyRunningException(message: str,innerException: Exception)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return TaskAlreadyRunningException()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,message=None,innerException=None):
  """
  __new__(cls: type)
  __new__(cls: type,message: str)
  __new__(cls: type,message: str,innerException: Exception)
  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __str__(self,*args):
  pass
 SerializeObjectState=None


class TaskBase(object):
 """ TaskBase() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return TaskBase()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def CalculateNextMoment(self):
  """ CalculateNextMoment(self: TaskBase) -> DateTime """
  pass
 def CalculateSchedule(self):
  """ CalculateSchedule(self: TaskBase) -> Array[DateTime] """
  pass
 def Run(self):
  """ Run(self: TaskBase) """
  pass
 def RunAsync(self,*args):
  """ RunAsync(self: TaskBase,token: CancellationToken) -> Task[object] """
  pass
 def StartAsync(self,token,behaviour):
  """ StartAsync(self: TaskBase,token: CancellationToken,behaviour: AlreadyRunningBehaviour) -> Task[object] """
  pass
 def ToCronTabFormat(self):
  """ ToCronTabFormat(self: TaskBase) -> str """
  pass
 Active=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Active(self: TaskBase) -> bool

Set: Active(self: TaskBase)=value
"""

 Days=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Days(self: TaskBase) -> str

Set: Days(self: TaskBase)=value
"""

 DaysToExecute=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DaysToExecute(self: TaskBase) -> List[str]

"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Description(self: TaskBase) -> str

Set: Description(self: TaskBase)=value
"""

 Editable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Editable(self: TaskBase) -> bool

Set: Editable(self: TaskBase)=value
"""

 EndDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: EndDate(self: TaskBase) -> DateTime

Set: EndDate(self: TaskBase)=value
"""

 ExecuteOnFriday=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExecuteOnFriday(self: TaskBase) -> bool

Set: ExecuteOnFriday(self: TaskBase)=value
"""

 ExecuteOnMonday=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExecuteOnMonday(self: TaskBase) -> bool

Set: ExecuteOnMonday(self: TaskBase)=value
"""

 ExecuteOnSaturday=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExecuteOnSaturday(self: TaskBase) -> bool

Set: ExecuteOnSaturday(self: TaskBase)=value
"""

 ExecuteOnSunday=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExecuteOnSunday(self: TaskBase) -> bool

Set: ExecuteOnSunday(self: TaskBase)=value
"""

 ExecuteOnThursday=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExecuteOnThursday(self: TaskBase) -> bool

Set: ExecuteOnThursday(self: TaskBase)=value
"""

 ExecuteOnTuesday=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExecuteOnTuesday(self: TaskBase) -> bool

Set: ExecuteOnTuesday(self: TaskBase)=value
"""

 ExecuteOnWednesday=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExecuteOnWednesday(self: TaskBase) -> bool

Set: ExecuteOnWednesday(self: TaskBase)=value
"""

 Hours=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Hours(self: TaskBase) -> str

Set: Hours(self: TaskBase)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: TaskBase) -> int

Set: Id(self: TaskBase)=value
"""

 Interval=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Interval(self: TaskBase) -> TimeSpan

Set: Interval(self: TaskBase)=value
"""

 IntervalSpecified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IntervalSpecified(self: TaskBase) -> bool

"""

 IsRunning=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsRunning(self: TaskBase) -> bool

"""

 LogMessages=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LogMessages(self: TaskBase) -> bool

Set: LogMessages(self: TaskBase)=value
"""

 MaximumRuntimeInSeconds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: MaximumRuntimeInSeconds(self: TaskBase) -> int

Set: MaximumRuntimeInSeconds(self: TaskBase)=value
"""

 Minutes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Minutes(self: TaskBase) -> str

Set: Minutes(self: TaskBase)=value
"""

 Months=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Months(self: TaskBase) -> str

Set: Months(self: TaskBase)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: TaskBase) -> str

Set: Name(self: TaskBase)=value
"""

 NextMoment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NextMoment(self: TaskBase) -> DateTime

Set: NextMoment(self: TaskBase)=value
"""

 PreCheck=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PreCheck(self: TaskBase) -> bool

Set: PreCheck(self: TaskBase)=value
"""

 RunningTask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: RunningTask(self: TaskBase) -> Task[object]

"""

 StartDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: StartDate(self: TaskBase) -> DateTime

Set: StartDate(self: TaskBase)=value
"""

 TaskStarted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TaskStarted(self: TaskBase) -> DateTime

Set: TaskStarted(self: TaskBase)=value
"""

 Type=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Type(self: TaskBase) -> TaskType

Set: Type(self: TaskBase)=value
"""


 AlreadyRunningBehaviour=None
 LogCategory='Tasks'


class TaskScheduler(object):
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return TaskScheduler()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def AddDefaultTasks(self):
  """ AddDefaultTasks(self: TaskScheduler) """
  pass
 def AddTask(self,task,findDelegate):
  """ AddTask(self: TaskScheduler,task: TaskBase,findDelegate: Func[TaskBase,bool]) -> int """
  pass
 def IsTaskEnqueued(self,id):
  """ IsTaskEnqueued(self: TaskScheduler,id: int) -> bool """
  pass
 def RemoveTask(self,task):
  """ RemoveTask(self: TaskScheduler,task: TaskBase) """
  pass
 def RemoveTaskByName(self,name):
  """ RemoveTaskByName(self: TaskScheduler,name: str) """
  pass
 def RestartTasksAsync(self):
  """ RestartTasksAsync(self: TaskScheduler) -> Task """
  pass
 def Run(self,*args):
  """ Run(self: TaskScheduler,ct: CancellationToken) -> Task """
  pass
 def RunOnce(self,taskToAdd,findDelegate):
  """ RunOnce(self: TaskScheduler,taskToAdd: TaskBase,findDelegate: Func[TaskBase,bool]) -> Task[object] """
  pass
 def Start(self,ct):
  """ Start(self: TaskScheduler,ct: CancellationToken) -> Task """
  pass
 def Stop(self,waitUntillAllCompleted):
  """ Stop(self: TaskScheduler,waitUntillAllCompleted: bool) -> Task """
  pass
 Tasks=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Tasks(self: TaskScheduler) -> IEnumerable[TaskBase]

"""


 Instance=None


class TaskType:
 """ enum TaskType,values: Erp (0),General (1),NotificationSummary (3),ScriptTask (2) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return TaskType()
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
 Erp=None
 General=None
 NotificationSummary=None
 ScriptTask=None
 value__=None


# variables with complex values

