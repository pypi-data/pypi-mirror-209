from vaxadium.constants import MASKKEYS
from vaxadium.io.nexus_reader import VanillaNexusReader


def get_mask_from_mask_file(filepath):
    v = VanillaNexusReader(MASKKEYS)
    v.read(filepath)
    return v.params.get("mask")
