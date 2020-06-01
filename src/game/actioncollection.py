from .actions.boataction import BoatAction
from .actions.firegunaction import FireGunAction
from .actions.grenadeaction import GrenadeAction
from .actions.knifeaction import KnifeAction
from .actions.leavethegameaction import LeaveTheGameAction
from .actions.moveaction import MoveAction
from .actions.passaction import PassAction


class ActionCollection:
    def __init__(self):
        self.codeToAction = dict()
        self.nameToAction = dict()
        
        # TODO как-то сделать более гибко, а не на говздях
        
        self.codeToAction[MoveAction.actionCode()] = MoveAction()
        self.nameToAction[MoveAction.actionName()] = MoveAction()
        
        self.codeToAction[PassAction.actionCode()] = PassAction()
        self.nameToAction[PassAction.actionName()] = PassAction()
        
        #self.codeToAction[FireGunAction.actionCode()] = FireGunAction()
        #self.nameToAction[FireGunAction.actionName()] = FireGunAction()
        
        self.codeToAction[GrenadeAction.actionCode()] = GrenadeAction()
        self.nameToAction[GrenadeAction.actionName()] = GrenadeAction()
        
        #self.codeToAction[KnifeAction.actionCode()] = KnifeAction()
        #self.nameToAction[KnifeAction.actionName()] = KnifeAction()
        
        #self.codeToAction[BoatAction.actionCode()] = BoatAction()
        #self.nameToAction[BoatAction.actionName()] = BoatAction()
        
        #self.codeToAction[LeaveTheGameAction.actionCode()] = LeaveTheGameAction()
        #self.nameToAction[LeaveTheGameAction.actionName()] = LeaveTheGameAction()

    
    
    def actionNames(self):
        return [action.actionName() for action in self.codeToAction.values()]
    
    
    def actionFromCode(self, code):
        return self.codeToAction[code]
    
    
    def actionFromName(self, name):
        return self.nameToAction[name]
    
