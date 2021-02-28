# about captcha image
IMAGE_HEIGHT = 50
IMAGE_WIDTH = 200
CHAR_SETS = 'abcdefghjklmnpqrstuvwxyz0123456789ABCDEFGHJKLMNPQRSTUVWXYZ'
CLASSES_NUM = len(CHAR_SETS)
CHARS_NUM = 5
# for train
RECORD_DIR = './data'
TRAIN_FILE = 'train.tfrecords'
VALID_FILE = 'valid.tfrecords'