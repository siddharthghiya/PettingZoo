from ._mpe_utils.simple_env import SimpleEnv
from .scenarios.simple_speaker_listener import Scenario


class env(SimpleEnv):
    def __init__(self, max_frames=500):
        scenario = Scenario()
        world = scenario.make_world()
        super(env, self).__init__(scenario, world, max_frames)
