import random
from .labyrinth import Labyrinth
from .actioncollection import ActionCollection
from .mapobjects.entities.player import Player
from .mapobjects.cells.exitcell import ExitCell


class LabyrinthGame:
    def __init__(self, labyrinth : Labyrinth, playerControllers, logger):
        self.labyrinth = labyrinth
        self.actionCollection = ActionCollection()
        self.playerControllers = playerControllers
        self.logger = logger
        self.players = list()
        for controller in playerControllers:
            name, sex = controller.getPlayerInfo() # TODO не хватет уникальности имен
            startCell = random.choice(self.labyrinth.starts)
            player = Player(name, sex, logger, startCell)
            self.players.append(player)
        self.gameOver = False
    
    
    def makeTurn(self):
        if self.gameOver:
            return False
        
        for player in self.players:
            player.turnProperties.clear() # очищаем временные свойства с прошлого хода
            if player.permanentProperties.get('dead', False):
                #self.logger.sendMessage('') # TODO Оно отправляется же само при убийстве?
                hospital = random.choice(self.labyrinth.hospitals)
                player.putIn(hospital)
                
        
        for i in range(len(self.playerControllers)):
            actionCode, paramCode = self.playerControllers[i].do()
            self.actionCollection.actionFromCode(actionCode).doAction(self.players[i], paramCode)

        # TODO точно также можно npc обработать. Просто, их контроллер в лабиринте
        self.labyrinth.processNPC()
        
        for player in self.players:
            if player.cell.cellType() == ExitCell.cellType():
                self.logger.sendMessage(player, 'leaves the Labyrinth! Game over!')
                self.gameOver = True
        
        return not self.gameOver
