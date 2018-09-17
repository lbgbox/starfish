"""
This module describes the contracts to provide data to the experiment builder.
"""

from typing import IO, Mapping, Tuple, Union

from slicedimage import (
    ImageFormat,
)

from starfish.types import Coordinates, Number


class FetchedTile:
    """
    This is the contract for providing the data for constructing a :class:`slicedimage.Tile`.
    """

    @property
    def shape(self) -> Tuple[int, ...]:
        """Return Tile shape.

        Returns
        -------
        Tuple[int, ...]
            The tile shape in (y, x)
        """
        raise NotImplementedError()

    @property
    def coordinates(self) -> Mapping[Union[str, Coordinates], Union[Number, Tuple[Number, Number]]]:
        """Return the tile's coordinates in the global coordinate space..

        Returns
        -------
        Mapping[Union[str, Coordinates], Union[Number, Tuple[Number, Number]]]
            Maps from a coordinate type (e.g. 'x', 'y', or 'z') to its value or range.
        """
        raise NotImplementedError()

    @property
    def format(self) -> ImageFormat:
        """Return the Tile's format

        Returns
        -------
        ImageFormat :
            a slicedimage format type, e.g. ImageFormat.TIFF
        """
        raise NotImplementedError()

    @property
    def tile_data_handle(self) -> IO:
        """Return an open file handle containing image data

        Returns
        -------
        IO :
            An open file handle that references image data
        """
        raise NotImplementedError()


class TileFetcher:
    """
    This is the contract for providing the image data for constructing a
    :class:`slicedimage.Collection`.
    """
    def get_tile(self, fov: int, hyb: int, ch: int, z: int) -> FetchedTile:
        """
        Given fov, hyb, ch, and z, return an instance of a :class:`.FetchedImage` that can be
        queried for the image data.
        """
        raise NotImplementedError()