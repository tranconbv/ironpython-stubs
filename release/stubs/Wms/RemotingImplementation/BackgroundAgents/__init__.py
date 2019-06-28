# encoding: utf-8
# module Wms.RemotingImplementation.BackgroundAgents calls itself BackgroundAgents
# from Wms.RemotingImplementation, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DatabaseBackgroundAgentHealthMonitor:
    """ DatabaseBackgroundAgentHealthMonitor() """
    def CreateOrUpdateBackgroundAgent(self, arg):
        """ CreateOrUpdateBackgroundAgent(self: DatabaseBackgroundAgentHealthMonitor, arg: DataFlowObject[BackgroundAgent]) -> DataFlowObject[BackgroundAgent] """
        pass

    def DeleteBackgroundAgent(self, arg):
        """ DeleteBackgroundAgent(self: DatabaseBackgroundAgentHealthMonitor, arg: DataFlowObject[BackgroundAgent]) -> DataFlowObject[BackgroundAgent] """
        pass

    def GetBackgroundAgentById(self, id, agent):
        """ GetBackgroundAgentById(self: DatabaseBackgroundAgentHealthMonitor, id: str) -> (bool, BackgroundAgent) """
        pass

    def GetBackgroundAgentsAll(self, agents):
        """ GetBackgroundAgentsAll(self: DatabaseBackgroundAgentHealthMonitor) -> (int, BackgroundAgents) """
        pass

    def GetBackgroundAgentsByType(self, type, agents):
        """ GetBackgroundAgentsByType(self: DatabaseBackgroundAgentHealthMonitor, type: BackgroundAgentType) -> (int, BackgroundAgents) """
        pass

    def RegisterBackgroundAgentLastSeen(self, agent):
        """ RegisterBackgroundAgentLastSeen(self: DatabaseBackgroundAgentHealthMonitor, agent: BackgroundAgent) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class IBackgroundAgentHealthMonitor:
    # no doc
    def CreateOrUpdateBackgroundAgent(self, arg):
        """ CreateOrUpdateBackgroundAgent(self: IBackgroundAgentHealthMonitor, arg: DataFlowObject[BackgroundAgent]) -> DataFlowObject[BackgroundAgent] """
        pass

    def DeleteBackgroundAgent(self, arg):
        """ DeleteBackgroundAgent(self: IBackgroundAgentHealthMonitor, arg: DataFlowObject[BackgroundAgent]) -> DataFlowObject[BackgroundAgent] """
        pass

    def GetBackgroundAgentById(self, id, agent):
        """ GetBackgroundAgentById(self: IBackgroundAgentHealthMonitor, id: str) -> (bool, BackgroundAgent) """
        pass

    def GetBackgroundAgentsAll(self, agents):
        """ GetBackgroundAgentsAll(self: IBackgroundAgentHealthMonitor) -> (int, BackgroundAgents) """
        pass

    def GetBackgroundAgentsByType(self, type, agents):
        """ GetBackgroundAgentsByType(self: IBackgroundAgentHealthMonitor, type: BackgroundAgentType) -> (int, BackgroundAgents) """
        pass

    def RegisterBackgroundAgentLastSeen(self, agent):
        """ RegisterBackgroundAgentLastSeen(self: IBackgroundAgentHealthMonitor, agent: BackgroundAgent) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class InMemoryBackgroundAgentHealthMonitor:
    """ InMemoryBackgroundAgentHealthMonitor() """
    def CreateOrUpdateBackgroundAgent(self, arg):
        """ CreateOrUpdateBackgroundAgent(self: InMemoryBackgroundAgentHealthMonitor, arg: DataFlowObject[BackgroundAgent]) -> DataFlowObject[BackgroundAgent] """
        pass

    def DeleteBackgroundAgent(self, arg):
        """ DeleteBackgroundAgent(self: InMemoryBackgroundAgentHealthMonitor, arg: DataFlowObject[BackgroundAgent]) -> DataFlowObject[BackgroundAgent] """
        pass

    def GetBackgroundAgentById(self, id, agent):
        """ GetBackgroundAgentById(self: InMemoryBackgroundAgentHealthMonitor, id: str) -> (bool, BackgroundAgent) """
        pass

    def GetBackgroundAgentsAll(self, agents):
        """ GetBackgroundAgentsAll(self: InMemoryBackgroundAgentHealthMonitor) -> (int, BackgroundAgents) """
        pass

    def GetBackgroundAgentsByType(self, type, agents):
        """ GetBackgroundAgentsByType(self: InMemoryBackgroundAgentHealthMonitor, type: BackgroundAgentType) -> (int, BackgroundAgents) """
        pass

    def RegisterBackgroundAgentLastSeen(self, agent):
        """ RegisterBackgroundAgentLastSeen(self: InMemoryBackgroundAgentHealthMonitor, agent: BackgroundAgent) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Agents = None


# variables with complex values
