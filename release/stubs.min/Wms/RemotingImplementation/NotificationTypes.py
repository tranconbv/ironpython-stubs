# encoding: utf-8
# module Wms.RemotingImplementation.NotificationTypes calls itself NotificationTypes
# from Wms.RemotingImplementation,Version=1.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DailyOnWorkdaysSchedule:
 """ DailyOnWorkdaysSchedule() """
 def GetNextTime(self,lastTime):
  """ GetNextTime(self: DailyOnWorkdaysSchedule,lastTime: DateTime) -> DateTime """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass

class DailySchedule:
 """ DailySchedule() """
 def GetNextTime(self,lastTime):
  """ GetNextTime(self: DailySchedule,lastTime: DateTime) -> DateTime """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass

class EmailDigestNotificationSummary:
 """ EmailDigestNotificationSummary(mailer: IMailer,general: General) """
 def ExecuteSummary(self,summary):
  """ ExecuteSummary(self: EmailDigestNotificationSummary,summary: ExecuteNotificationSummaryArgs) -> Task """
  pass
 def GetConfigurationForm(self):
  """ GetConfigurationForm(self: EmailDigestNotificationSummary) -> UiForm """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,mailer,general):
  """ __new__(cls: type,mailer: IMailer,general: General) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Group=None
 ResolverName='EmailDigestNotificationSummary'
 TemplateData=None


class INotificationSummaryExecution:
 # no doc
 def ExecuteSummary(self,summary):
  """ ExecuteSummary(self: INotificationSummaryExecution,summary: ExecuteNotificationSummaryArgs) -> Task """
  pass
 def GetConfigurationForm(self):
  """ GetConfigurationForm(self: INotificationSummaryExecution) -> UiForm """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class INotificationSummarySchedule:
 # no doc
 def GetNextTime(self,lastTime):
  """ GetNextTime(self: INotificationSummarySchedule,lastTime: DateTime) -> DateTime """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass

class NotificationTypeContainer:
 """ NotificationTypeContainer(iocContainer: IUnityContainer) """
 def RegisterExecution(self,*__args):
  """ RegisterExecution(self: NotificationTypeContainer,implementation: Type,name: str)RegisterExecution[T](self: NotificationTypeContainer,name: str) """
  pass
 def RegisterSchedule(self,*__args):
  """ RegisterSchedule(self: NotificationTypeContainer,implementation: Type,name: str)RegisterSchedule[T](self: NotificationTypeContainer,name: str) """
  pass
 def ResolveExcution(self,name):
  """ ResolveExcution(self: NotificationTypeContainer,name: str) -> INotificationSummaryExecution """
  pass
 def ResolveSchedule(self,name):
  """ ResolveSchedule(self: NotificationTypeContainer,name: str) -> INotificationSummarySchedule """
  pass
 @staticmethod
 def __new__(self,iocContainer):
  """ __new__(cls: type,iocContainer: IUnityContainer) """
  pass
 ExecutionKeys=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ExecutionKeys(self: NotificationTypeContainer) -> IEnumerable[str]

"""

 ScheduleKeys=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ScheduleKeys(self: NotificationTypeContainer) -> IEnumerable[str]

"""



class SlackWebDigestNotificationSummary:
 """ SlackWebDigestNotificationSummary(general: General) """
 def ExecuteSummary(self,summary):
  """ ExecuteSummary(self: SlackWebDigestNotificationSummary,summary: ExecuteNotificationSummaryArgs) -> Task """
  pass
 def GetConfigurationForm(self):
  """ GetConfigurationForm(self: SlackWebDigestNotificationSummary) -> UiForm """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,general):
  """ __new__(cls: type,general: General) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass

class WeeklySchedule:
 """ WeeklySchedule() """
 def GetNextTime(self,lastTime):
  """ GetNextTime(self: WeeklySchedule,lastTime: DateTime) -> DateTime """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
