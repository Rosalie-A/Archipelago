"""Int subclass instances representing the layer of a wave effect."""

from .types.classes import WaveEffectLayer, WaveEffectDirection

WAVE_LAYER_BATTLEFIELD = WaveEffectLayer(0)
WAVE_LAYER_4BPP = WaveEffectLayer(1)
WAVE_LAYER_2BPP = WaveEffectLayer(2)

WAVE_LAYER_HORIZONTAL = WaveEffectDirection(0)
WAVE_LAYER_VERTICAL = WaveEffectDirection(1)
