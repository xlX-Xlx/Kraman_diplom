import os
from math import floor
import shutil
from tqdm import tqdm
import glob

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def prepare_data(input_folders, BASE_DIR_ABSOLUTE, OUT_DIR, coeff):
    OUT_TRAIN = os.path.join(OUT_DIR, 'train')
    OUT_VAL = os.path.join(OUT_DIR, 'val')

    if int(coeff[0]) + int(coeff[1]) > 100:
        print("Coeff can't exceed 100%.")
        exit(1)

    print(f'Preparing images data by {coeff[0]}/{coeff[1]} rule.')
    print(f'Source folders: {len(input_folders)}')
    print('Gathering data ...')

    source = {}
    for sf in input_folders:
        source.setdefault(sf, [])

        os.chdir(BASE_DIR_ABSOLUTE)
        os.chdir(sf)

        for filename in glob.glob('*.png'):
            source[sf].append(filename)

    train = {}
    val = {}
    for sk, sv in source.items():
        chunks = 10
        train_chunk = floor(chunks * (coeff[0] / 100))
        val_chunk = chunks - train_chunk

        train.setdefault(sk, [])
        val.setdefault(sk, [])
        for item in chunker(sv, chunks):
            train[sk].extend(item[0:train_chunk])
            val[sk].extend(item[train_chunk:])

    train_sum = sum(len(sv) for sv in train.values())
    val_sum = sum(len(sv) for sv in val.values())

    print(f'\nOverall TRAIN images count: {train_sum}')
    print(f'\nOverall TEST images count: {val_sum}')

    os.chdir(BASE_DIR_ABSOLUTE)
    print('\nCopying TRAIN source items to prepared folder ...')
    for sk, sv in tqdm(train.items()):
        for item in tqdm(sv):
            imgfile_source = os.path.join(sk, item)
            imgfile_dest = os.path.join(OUT_TRAIN, sk.split('/')[-2])

            os.makedirs(imgfile_dest, exist_ok=True)
            shutil.copyfile(imgfile_source, os.path.join(imgfile_dest, item))

            # Копируем соответствующий текстовый файл
            label_file_source = os.path.join(sk.replace("images", "labels"), item[:-3] + 'txt')
            label_file_dest = os.path.join(OUT_TRAIN, sk.split('/')[-2])
            shutil.copyfile(label_file_source, os.path.join(label_file_dest, item[:-3] + 'txt'))

    os.chdir(BASE_DIR_ABSOLUTE)
    print('\nCopying VAL source items to prepared folder ...')
    for sk, sv in tqdm(val.items()):
        for item in tqdm(sv):
            imgfile_source = os.path.join(sk, item)
            imgfile_dest = os.path.join(OUT_VAL, sk.split('/')[-2])

            os.makedirs(imgfile_dest, exist_ok=True)
            shutil.copyfile(imgfile_source, os.path.join(imgfile_dest, item))

            # Копируем соответствующий текстовый файл
            label_file_source = os.path.join(sk.replace("images", "labels"), item[:-3] + 'txt')
            label_file_dest = os.path.join(OUT_VAL, sk.split('/')[-2])
            shutil.copyfile(label_file_source, os.path.join(label_file_dest, item[:-3] + 'txt'))

    print('\nDONE!')


if __name__ == '__main__':
    input_folders = ['dataset/images/train/']
    BASE_DIR_ABSOLUTE = "/home/x-x/Python code/map"
    OUT_DIR = 'dataset/map_prepared/'
    coeff = [80, 20]

    prepare_data(input_folders, BASE_DIR_ABSOLUTE, OUT_DIR, coeff)
