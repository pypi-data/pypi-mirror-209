import json
import os
import ezdxf
from ezdxf.addons import odafc
from pathlib import Path
import numpy as np
from collections import defaultdict
import argparse
from tqdm import tqdm


def retrieve_texts_from_dwgs(dwg):
    doc = odafc.readfile(dwg)
    msp = doc.modelspace()
    texts = []
    for entity in msp:
        if entity.dxftype() in ['MTEXT', 'TEXT']:
            text = entity.dxf.text
            pos = entity.dxf.insert[0], entity.dxf.insert[1]
            texts.append([text, pos])
    return texts


Position = dict(
    # anchor_text='钻 孔 柱 状 图',
    # anchor_pos=(57.4664364136012, 245.9999914201628),
    num_borehole=((20.0, 234.0), (47.0, 227.0)),
    elevation=((20.0, 227.0), (42.0, 220.0)),
    xy=((58.5231, 234.0), (80.0, 220.0)),
    depth=((100.0, 234.0), (120.073, 227.0)),
    gw=((147.0, 227.0), (168.0, 220.0)),
    num_layer=((12.0, 200.0), (20.0, -8.8303e-06)),
    ele_layer=((20.0, 200.0), (32.0, -8.8303e-06)),
    dsc_layer=((67.0, 200.0), (121.5, -8.8303e-06))
)


def is_in_scope(pnt, pnt_coners):
    pnt = np.array(pnt)
    pnt_coners = np.array(pnt_coners)
    determine = pnt - pnt_coners
    return (determine[0, 0] > 0) and \
        (determine[0, 1] < 0) and \
        (determine[1, 0] < 0) and \
        (determine[1, 1] > 0)


def filter_texts(texts):
    rst = defaultdict(list)
    for text in texts:
        pos = text[1]
        for k, scope in Position.items():
            if is_in_scope(pos, scope):
                rst[k].append(text)
    return rst


def sort_texts_by_y(d: dict, reverse=True):
    rst = defaultdict(list)
    for k, v in d.items():
        v = sorted(v, key=lambda x: x[1][1], reverse=reverse)
        rst[k] = [vi[0] for vi in v]
    return rst


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--dwgs_folder')
    parser.add_argument('--out_file')
    parser.add_argument('--test', help='used for testing', action="store_true")
    args = parser.parse_args(argv)

    dwgs_folder = args.dwgs_folder
    out_file = os.path.join(os.getcwd(), args.out_file)
    is_test = args.test
    p = Path(dwgs_folder)
    dwg_files = p.glob('*.dwg')
    if is_test:
        dwg_files = np.random.choice([dwg for dwg in dwg_files], size=5)
    np.random.sample
    rst = []
    for i, dwg in tqdm(enumerate(dwg_files)):
        texts = retrieve_texts_from_dwgs(dwg)
        texts_filtered = filter_texts(texts)
        rsti = sort_texts_by_y(texts_filtered)
        rst.append(rsti)

    with open(out_file, 'w') as f:
        json.dump(rst, f)


if __name__ == "__main__":
    # dwgs_folder = r"C:\Users\xiao-laptop\Documents\dwgs\柱状图"
    main()
