import os

import numpy as np

from kswutils.fileio import FileIO
from kswutils.calculator import isfloat


class Accelerometer:
    def __init__(self, filepath) -> None:
        self.filepath = filepath

    def get_A1(self):
        acc = []
        with open(self.filepath, 'r') as f:
            for i, line in enumerate(f):
                if isfloat(line.strip('\n').split('\t')[0]):
                    acc.append(float(line.strip('\n').split('\t')[1]))
        return np.array(acc)

    def get_A2(self):
        acc = []
        with open(self.filepath, 'r') as f:
            for i, line in enumerate(f):
                if isfloat(line.strip('\n').split('\t')[0]):
                    acc.append(float(line.strip('\n').split('\t')[2]))
        return np.array(acc)

    def get_sample_rate(self):
        c = 0
        ts = []
        with open(self.filepath, 'r') as f:
            for i, line in enumerate(f):
                if isfloat(line.strip('\n').split('\t')[0]):
                    ts.append(float(line.strip('\n').split('\t')[0]))
                    c += 1
                if c == 2:
                    sr = 1 / (ts[1] - ts[0])
                    break
        return sr


def combine_data(folder):
    files = FileIO.get_subdirectories(folder)

    acc1_ls = []
    acc2_ls = []

    print('Concatenate files...')
    for f in files:
        if f.endswith('.lvm'):
            print(os.path.basename(f))
            accelerometer = Accelerometer(f)
            acc1_ls.append(accelerometer.get_A1())
            acc2_ls.append(accelerometer.get_A2())

    return np.concatenate(acc1_ls), np.concatenate(acc2_ls)


def save_pkl(inpdir, outdir, name):
    print('Input:', inpdir)

    data1, data2 = combine_data(inpdir)

    savepath = os.path.join(outdir, name + '_acc1.pickle')
    FileIO.write_pickle(data1, savepath=savepath)
    print('data1 saved to:', outdir)

    savepath = os.path.join(outdir, name + '_acc2.pickle')
    FileIO.write_pickle(data2, savepath=savepath)
    print('data1 saved to:', outdir)
    return None


# s = Accelerometer('test_23-03-08_1252_1.lvm')
# a1 = s.get_A1()
# a2 = s.get_A2()
# print()
