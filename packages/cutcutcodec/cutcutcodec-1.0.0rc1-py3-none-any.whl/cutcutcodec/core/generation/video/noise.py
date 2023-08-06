#!/usr/bin/env python3

"""
** Generate a video noise signal. **
------------------------------------
"""

from fractions import Fraction
import hashlib
import math
import numbers
import struct
import typing

import numpy as np

from cutcutcodec.core.classes.container import ContainerInput
from cutcutcodec.core.classes.frame_video import FrameVideo
from cutcutcodec.core.classes.stream import Stream
from cutcutcodec.core.classes.stream_video import StreamVideo
from cutcutcodec.core.exceptions import OutOfTimeRange
from cutcutcodec.core.interfaces.seedable import Seedable



class GeneratorVideoNoise(ContainerInput, Seedable):
    """
    ** Generate a pure noise video signal. **

    Examples
    --------
    >>> from cutcutcodec.core.generation.video.noise import GeneratorVideoNoise
    >>> stream = GeneratorVideoNoise(0).out_streams[0]
    >>> stream.snapshot(0, (13, 9))[..., 0]
    tensor([[101,  34,  59, 100, 156,   8,   3,  84, 212],
            [126, 226, 235,  61, 236,  95,  66, 227, 176],
            [  5, 131, 171,  18,  40, 203, 177, 135, 106],
            [229, 114, 147,  37, 124,  27,   6, 145,  73],
            [152, 203, 198,  95,  66,  45, 186, 126,  30],
            [ 72, 208, 154, 150, 225, 233,  21,   5, 155],
            [ 49,  21,  19, 231, 195, 141, 144, 100,   5],
            [ 19, 113,  99, 110, 242, 128,  71, 161,  90],
            [241, 195, 113, 105, 173, 105,  97,  64,  55],
            [106, 106, 204,  34, 201,  59,  45, 252,  94],
            [234,  87, 105, 230, 203,  51,  87, 245, 147],
            [ 64, 181, 159, 214, 210, 211, 160, 208, 202],
            [ 42, 147,  75,  81, 236,  31, 162, 141, 225]], dtype=torch.uint8)
    >>>
    """

    def __init__(self, seed: typing.Optional[numbers.Real]=None):
        """
        Parameters
        ----------
        seed : numbers.Real, optional
            Transmitted to ``cutcutcodec.core.interfaces.seedable.Seedable``.
        """
        Seedable.__init__(self, seed)
        super().__init__([_StreamVideoNoiseUniform(self)])

    @classmethod
    def default(cls):
        return cls(0)

    def getstate(self) -> dict:
        return self._getstate_seed()

    def setstate(self, in_streams: typing.Iterable[Stream], state: dict) -> None:
        assert set(state) == {"seed"}, set(state)
        self._setstate_seed(state)
        ContainerInput.__init__(self, [_StreamVideoNoiseUniform(self)])


class _StreamVideoNoiseUniform(StreamVideo):
    """
    ** Random video stream where each pixel follows a uniform law. **
    """

    is_space_continuous = True
    is_time_continuous = True

    def __init__(self, node: GeneratorVideoNoise):
        assert isinstance(node, GeneratorVideoNoise), node.__class__.__name__
        super().__init__(node)

    def _snapshot(self, timestamp: Fraction, shape: tuple[int, int]) -> FrameVideo:
        if timestamp < 0:
            raise OutOfTimeRange(f"there is no audio frame at timestamp {timestamp} (need >= 0)")
        seed = int.from_bytes(
            hashlib.md5(
                struct.pack(
                    "dLL",
                    self.node.seed,
                    timestamp.numerator % (1 << 64),
                    timestamp.denominator % (1 << 64),
                )
            ).digest(),
            byteorder="big",
        ) % (1 << 64) # solve RuntimeError: Overflow when unpacking long
        # numpy 1.24.1 vs torch 2.0.0 is 9 times faster
        return FrameVideo(
            timestamp,
            np.random.default_rng(seed=seed).integers(0, 256, (*shape, 3), dtype=np.uint8),
        )

    @property
    def beginning(self) -> Fraction:
        return Fraction(0)

    @property
    def duration(self) -> typing.Union[Fraction, float]:
        return math.inf
