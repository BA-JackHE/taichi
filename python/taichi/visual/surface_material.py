from taichi.util import *
from taichi.core import tc_core

class SurfaceMaterial:
    def __init__(self, name, **kwargs):
        self.c = tc_core.create_surface_material(name)
        self.c.initialize(config_from_dict(kwargs))
