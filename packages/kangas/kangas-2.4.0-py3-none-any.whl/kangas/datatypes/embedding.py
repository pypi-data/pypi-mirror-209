# -*- coding: utf-8 -*-
######################################################
#     _____                  _____      _     _      #
#    (____ \       _        |  ___)    (_)   | |     #
#     _   \ \ ____| |_  ____| | ___ ___ _  _ | |     #
#    | |  | )/ _  |  _)/ _  | |(_  / __) |/ || |     #
#    | |__/ ( ( | | | ( ( | | |__| | | | ( (_| |     #
#    |_____/ \_||_|___)\_||_|_____/|_| |_|\____|     #
#                                                    #
#    Copyright (c) 2023 Kangas Development Team      #
#    All rights reserved                             #
######################################################

import json
import random
import time

from ..server.utils import Cache, pickle_dumps
from .base import Asset
from .utils import get_color, get_file_extension, is_valid_file_path

PROJECTION_DIMENSIONS = 50

SAMPLE_CACHE = Cache(100)


def prepare_embedding(embedding, dimensions, seed):
    if len(embedding) <= dimensions:
        return embedding

    key = (seed, dimensions)
    if not SAMPLE_CACHE.contains(key):
        random.seed(seed)
        indices = list(range(len(embedding)))
        random.shuffle(indices)
        SAMPLE_CACHE.put(key, set(indices[:dimensions]))

    indices = SAMPLE_CACHE.get(key)

    return [v for i, v in enumerate(embedding) if i in indices]

    SAMPLE_CACHE.get(key)


class Embedding(Asset):
    """
    An Embedding asset.
    """

    ASSET_TYPE = "Embedding"

    def __init__(
        self,
        embedding=None,
        name=None,
        text=None,
        color=None,
        projection="pca",
        include=True,
        file_name=None,
        metadata=None,
        source=None,
        unserialize=False,
        dimensions=PROJECTION_DIMENSIONS,
    ):
        """
        Create an embedding vector.

        Args:
            embedding: a vector (list of numbers)
            name: (str) a name that provides the color (if not given below) and
                set name to which this embedding point belongs
            text: (str) text that will show when you hover over point in expanded
                view
            color: (str) a string that represents a color for the chart, typically
                given as a "#rrggbb" hex string where "rr" is between "00" and "ff".
            projection: (str) the type of projection either 'pca' or 't-sne'
            include: (bool) whether to include this vector when determining the
                projection. Useful if you want to see one part of the datagrid in
                the project of another.
            dimensions: (int) maximum number of dimensions

        Example:

        ```python
        >>> import kangas as kg
        >>> dg = kg.DataGrid()
        >>> for row in rows:
        >>>     target = row[0]
        >>>     kg.append([kg.Embedding(row[1:], name=target)])
        >>> dg.save("embeddings.datagrid")
        ```
        """
        super().__init__(source)
        if unserialize:
            self._unserialize = unserialize
            return
        if self.source is not None:
            # FIXME: this is for images, not others?
            self._log_metadata(
                filename=self.source,
                extension=get_file_extension(self.source),
            )
            if metadata:
                self._log_metadata(**metadata)
            return

        if color is None:
            if name:
                color = get_color(name)

        self.metadata["name"] = name
        self.metadata["text"] = text
        self.metadata["color"] = color
        self.metadata["projection"] = projection
        self.metadata["include"] = include
        self.metadata["dimensions"] = dimensions

        if file_name:
            if is_valid_file_path(file_name):
                with open(file_name, "r") as io_object:
                    self.asset_data = json.dumps(
                        {
                            "vector": io_object.read(),
                            "name": name,
                            "color": color,
                            "text": text,
                            "dimensions": dimensions,
                        }
                    )
                self.metadata["extension"] = get_file_extension(file_name)
                self.metadata["filename"] = file_name
            else:
                raise ValueError("file not found: %r" % file_name)
        else:
            self.asset_data = json.dumps(
                {
                    "vector": embedding,
                    "name": name,
                    "color": color,
                    "text": text,
                    "dimensions": dimensions,
                    "include": include,
                }
            )
        if metadata:
            self.metadata.update(metadata)

    def log_and_serialize(self, datagrid, row_id):
        """
        Override to save row_id.
        """
        # Put row_id in asset_data and metadata:
        asset_data = json.loads(self.asset_data)
        asset_data["row_id"] = row_id
        self.asset_data = json.dumps(asset_data)
        self.metadata["row_id"] = row_id
        return super().log_and_serialize(datagrid, row_id)

    @classmethod
    def get_statistics(cls, datagrid, col_name, field_name):
        import numpy as np

        # FIXME: compute min and max of eigenspace
        minimum = None
        maximum = None
        avg = None
        variance = None
        total = None
        stddev = None
        other = None
        name = col_name
        seed = time.time()  # set the same for all embeddings

        projection = None
        batch = []
        for row in datagrid.conn.execute(
            """SELECT {field_name} as assetId, asset_data, asset_metadata from datagrid JOIN assets ON assetId = assets.asset_id;""".format(
                field_name=field_name
            )
        ):
            asset_id, asset_data_json, asset_metadata_json = row
            if not asset_metadata_json:
                continue

            asset_metdata = json.loads(asset_metadata_json)
            projection = asset_metdata["projection"]
            include = asset_metdata["include"]
            dimensions = asset_metdata["dimensions"]

            # Skip if explicitly False
            if not include:
                continue

            asset_data = json.loads(asset_data_json)
            vector = prepare_embedding(asset_data["vector"], dimensions, seed)

            batch.append(vector)
            if projection is None or projection == "pca":
                projection_name = "pca"
            elif projection == "t-sne":
                projection_name = "t-sne"
            elif projection == "umap":
                projection_name = "umap"

        if projection_name == "pca":
            from sklearn.decomposition import PCA

            projection = PCA(n_components=2)
            transformed = projection.fit_transform(np.array(batch))
            x_max = float(transformed[:, 0].max())
            x_min = float(transformed[:, 0].min())
            y_max = float(transformed[:, 1].max())
            y_min = float(transformed[:, 1].min())
            x_span = abs(x_max - x_min)
            x_max += x_span * 0.1
            x_min -= x_span * 0.1
            y_span = abs(y_max - y_min)
            y_max += y_span * 0.1
            y_min -= y_span * 0.1
            other = json.dumps(
                {
                    "pca_eigen_vectors": projection.components_.tolist(),
                    "pca_mean": projection.mean_.tolist(),
                    "projection": projection_name,
                    "x_range": [x_min, x_max],
                    "y_range": [y_min, y_max],
                    "dimensions": dimensions,
                    "seed": seed,
                }
            )
        elif projection_name == "t-sne":
            from openTSNE import TSNE

            projection = TSNE()
            transformed = projection.fit(np.array(batch))
            x_max = float(transformed[:, 0].max())
            x_min = float(transformed[:, 0].min())
            y_max = float(transformed[:, 1].max())
            y_min = float(transformed[:, 1].min())
            x_span = abs(x_max - x_min)
            x_max += x_span * 0.1
            x_min -= x_span * 0.1
            y_span = abs(y_max - y_min)
            y_max += y_span * 0.1
            y_min -= y_span * 0.1
            other = json.dumps(
                {
                    "projection": projection_name,
                    "pickled_projection": pickle_dumps(transformed),
                    "x_range": [x_min, x_max],
                    "y_range": [y_min, y_max],
                    "dimensions": dimensions,
                    "seed": seed,
                }
            )
        elif projection_name == "umap":
            projection_name = (projection_name,)
            other = json.dumps(
                {
                    "projection": projection_name,
                }
            )

        return [minimum, maximum, avg, variance, total, stddev, other, name]
