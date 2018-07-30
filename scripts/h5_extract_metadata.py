# Extracts metadata from h5 files
from __future__ import print_function, division, unicode_literals
import os
import numpy as np
import h5py
import json
import sys

# converts numpy values
def numpy_to_dt(numpy_values):
    int_values = []
    for v in numpy_values:
        if isinstance(v, np.generic):
            v = np.asscalar(v)

        int_values.append(v)
    return int_values

h5_path =  sys.argv[1]
h5_dataset = h5py.File(h5_path)
h5_file = os.path.basename(h5_path)
resource_name, format = h5_file.split('.')

keys = list(h5_dataset.attrs.keys())
values = list(h5_dataset.attrs.values())
keys = numpy_to_dt(keys)
values = numpy_to_dt(values)
metadata = dict(zip(keys,values))
with open(resource_name + '.json', 'w') as fp:
    json.dump(metadata, fp)
