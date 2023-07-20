import argparse
import os
import logging
from collections import namedtuple

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent'])

def get_file_info(path):
    name, extension = os.path.splitext(os.path.basename(path))
    is_dir = os.path.isdir(path)
    parent = os.path.basename(os.path.dirname(path))
    return FileInfo(name, extension, is_dir, parent)

def main():
    parser = argparse.ArgumentParser(description='Process directory')
    parser.add_argument('dir', help='directory to process')
    args = parser.parse_args()

    logging.basicConfig(filename='file_info.log', level=logging.INFO)
    logger = logging.getLogger(__name__)

    for root, dirs, files in os.walk(args.dir):
        for name in dirs + files:
            path = os.path.join(root, name)
            info = get_file_info(path)
            logger.info(info)

if __name__ == '__main__':
    main()
    # python task4.py C:\Users\irina\Downloads\Drops.of.God.Mini-Series.WEB-DL.1080p.TeamHD-RGzsRutracker