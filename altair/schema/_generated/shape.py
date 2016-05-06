# This file auto-generated by `_schema_parser.py`.
# Do not modify this file directly.

import traitlets as T


class Shape(T.Enum):
    def __init__(self, default_value=T.Undefined, **metadata):
        super(Shape, self).__init__(['circle', 'square', 'cross', 'diamond', 'triangle-up', 'triangle-down'],
                                    default_value=default_value,
                                    **metadata)