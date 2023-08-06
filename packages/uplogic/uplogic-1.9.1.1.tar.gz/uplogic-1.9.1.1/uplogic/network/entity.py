from bge.types import KX_GameObject
import pickle
from uplogic.utils.constants import STREAMTYPE_DOWNSTREAM, STREAMTYPE_UPSTREAM


class Entity:
    pass


class StaticObject(Entity):
    def __init__(self, game_object: KX_GameObject):
        self.streamtype = STREAMTYPE_DOWNSTREAM
        self.game_object = game_object
    
    def get_data(self):
        return pickle.dumps({
            'id': self.game_object.blenderObject.name,
            'name': self.game_object.name,
            'set_attrs': {}
        })


class Actor(Entity):
    def __init__(self, game_object: KX_GameObject):
        self.streamtype = STREAMTYPE_DOWNSTREAM
        self.game_object = game_object
    
    def get_data(self):
        go = self.game_object
        wpos = go.worldPosition
        wori = go.worldOrientation
        wsca = go.worldScale
        wlinvel = go.worldLinearVelocity
        wangvel = go.worldAngularVelocity
        lpos = go.localPosition
        lori = go.localOrientation
        lsca = go.localScale
        return {
            'id': self.game_object.blenderObject.name,
            'name': self.game_object.name,
            'streamtype': self.streamtype,
            'set_attrs': {
                'worldPosition': [
                    wpos.x,
                    wpos.y,
                    wpos.z
                ],
                'worldOrientation': [
                    [wori[0][0], wori[0][1], wori[0][2]],
                    [wori[1][0], wori[1][1], wori[1][2]],
                    [wori[2][0], wori[2][1], wori[2][2]],
                ],
                'worldScale': [
                    wsca.x,
                    wsca.y,
                    wsca.z
                ],
                'worldLinearVelocity': [
                    wlinvel.x,
                    wlinvel.y,
                    wlinvel.z
                ],
                'worldAngularVelocity': [
                    wangvel.x,
                    wangvel.y,
                    wangvel.z
                ],
                'localPosition': [
                    lpos.x,
                    lpos.y,
                    lpos.z
                ],
                'localOrientation': [
                    [lori[0][0], lori[0][1], lori[0][2]],
                    [lori[1][0], lori[1][1], lori[1][2]],
                    [lori[2][0], lori[2][1], lori[2][2]],
                ],
                'localScale': [
                    lsca.x,
                    lsca.y,
                    lsca.z
                ]
            }
        }


class Player(Actor):

    def __init__(self, game_object: KX_GameObject):
        super().__init__(game_object)
        self.streamtype = STREAMTYPE_UPSTREAM
