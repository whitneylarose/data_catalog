from __future__ import print_function, division, unicode_literals
import os
import numpy as np
import h5py
import json
import sys

if sys.version_info.major == 3:
    unicode = str

def get_attr(h5_object, attr_name):
    """
    Returns the attribute from the h5py object
    Parameters
    ----------
    h5_object : h5py.Dataset, h5py.Group or h5py.File object
        object whose attribute is desired
    attr_name : str
        Name of the attribute of interest
    Returns
    -------
    att_val : object
        value of attribute, in certain cases (byte strings or list of byte strings) reformatted to readily usable forms
    """
    if not isinstance(h5_object, (h5py.Dataset, h5py.Group, h5py.File)):
        raise TypeError('h5_object should be a h5py.Dataset, h5py.Group or h5py.File object')

    if not isinstance(attr_name, (str, unicode)):
        raise TypeError('attr_name should be a string')

    if attr_name not in h5_object.attrs.keys():
        raise KeyError("'{}' is not an attribute in '{}'".format(attr_name, h5_object.name))

    att_val = h5_object.attrs.get(attr_name)
    if isinstance(att_val, np.bytes_) or isinstance(att_val, bytes):
        att_val = att_val.decode('utf-8')

    elif type(att_val) == np.ndarray:
        if sys.version_info.major == 3:
            if att_val.dtype.type in [np.bytes_, np.object_]:
                att_val = np.array([str(x, 'utf-8') for x in att_val])

    return att_val


def get_attributes(h5_object, attr_names=None):
    """
    Returns attribute associated with some DataSet.
    Parameters
    ----------
    h5_object : h5py.Dataset
        Dataset object reference.
    attr_names : string or list of strings, optional, default = all (DataSet.attrs).
        Name of attribute object to return.
    Returns
    -------
    Dictionary containing (name,value) pairs of attributes
    """
    if not isinstance(h5_object, (h5py.Dataset, h5py.Group, h5py.File)):
        raise TypeError('h5_object should be a h5py.Dataset, h5py.Group or h5py.File object')

    if attr_names is None:
        attr_names = h5_object.attrs.keys()
    else:
        if isinstance(attr_names, (str, unicode)):
            attr_names = [attr_names]
        if not isinstance(attr_names, (list, tuple)):
            raise TypeError('attr_names should be a string or list / tuple of strings')
        if not np.all([isinstance(x, (str, unicode)) for x in attr_names]):
            raise TypeError('attr_names should be a string or list / tuple of strings')

    att_dict = {}

    for attr in attr_names:
        try:
            att_dict[attr] = get_attr(h5_object, attr)
        except KeyError:
            raise KeyError('%s is not an attribute of %s' % (str(attr), h5_object.name))

    return att_dict

def h5_root_atts_to_json(h5_path):
    if not h5_path.endswith('.h5'):
        print('Provided file did not have an h5 extension.')
        return
    with h5py.File(h5_path, mode='r') as h5_f:
        metadata = get_attributes(h5_f)
        
    for key, val in metadata.items():
        if type(val) in [np.uint16, np.uint8, np.uint]:
            metadata[key] = int(val)
        if type(val) in [np.bool, np.bool_]:
            metadata[key] = bool(val)
            

    json_path = h5_path.replace('.h5','.json')

    with open(json_path, mode='w') as json_handle:
        json.dump(metadata, json_handle)

if __name__ == '__main__':        
    if len(sys.argv) == 2:
        h5_root_atts_to_json(sys.argv[1])