import os
import pickle
import urllib.request
import urllib.error
import numpy as np

def to_pickle(**kwargs):
    '''save kwargs to tbd00.pkl

    Parameters:
        kwargs (dict): key-value pairs to be saved

    Returns:
        ret (NoneType): None
    '''
    if os.path.exists('tbd00.pkl'):
        with open('tbd00.pkl', 'rb') as fid:
            z0 = pickle.load(fid)
        z0.update(**kwargs)
    else:
        z0 = kwargs
    with open('tbd00.pkl', 'wb') as fid:
        pickle.dump(z0, fid)


def from_pickle(key):
    '''load value from tbd00.pkl

    Parameters:
        key (str): key to be loaded

    Returns:
        ret (any): value corresponding to key
    '''
    with open('tbd00.pkl', 'rb') as fid:
        return pickle.load(fid)[key]


def to_np(x):
    '''convert tensorflow/torch/cupy array to numpy array

    Parameters:
        x (array): array to be converted, could be tensorflow/torch/cupy/numpy array

    Returns:
        ret (numpy.array): converted array
    '''
    # not a good idea to use isinstance()
    # if use isinstance(), here have to import all of them (tf/torch/cupy)
    tmp0 = str(type(x))[8:-2]
    if tmp0.startswith('tensorflow'):
        ret = x.numpy()
    elif tmp0.startswith('torch'):
        ret = x.detach().to('cpu').numpy()
    elif tmp0.startswith('cupy'):
        ret = x.get()
    else:
        ret = np.asarray(x)
    return ret

def hfe(x, y, eps=1e-5):
    r'''calculate relative error

    $$ f(x,y)=\max \frac{|x-y|}{|x|+|y|+\varepsilon} $$

    Parameters:
        x (numpy.array): array to be compared
        y (numpy.array): array to be compared

    Returns:
        ret (float): relative error
    '''
    x = to_np(x)
    y = to_np(y)
    ret = np.max(np.abs(x-y)/(np.abs(x)+np.abs(y)+eps))
    return ret

# a simple hfe()
# hfe = lambda x,y,eps=1e-3: np.max(np.abs(x-y)/(np.abs(x)+np.abs(y)+eps))


def moving_average(np0, num=3):
    '''calculate moving average

    Parameters:
        np0 (numpy.array): array to be averaged
        num (int): number of elements to be averaged

    Returns:
        ret (numpy.array): averaged array
    '''
    # see https://stackoverflow.com/q/13728392/7290857
    kernel = np.ones(num) / num
    ret = np.convolve(np.asarray(np0), kernel, mode='same')
    return ret


def check_internet_available(timeout=1):
    '''check if internet is available (by trying to connect to google.com)

    Parameters:
        timeout (float): timeout in seconds

    Returns:
        ret (bool): True if internet is available, False otherwise
    '''
    host = 'https://www.google.com' #dnsloopup google.com #172.217.161.142 (20190817)
    try:
        urllib.request.urlopen(host, timeout=timeout)
        return True
    except urllib.error.URLError:
        return False


def script_print_lucky():
    '''print lucky message. This function is available in command line `zzz233`

    Parameters:

    Returns:
        ret (NoneType): None
    '''
    print('[zzz233] I am feelly lucky today!')
