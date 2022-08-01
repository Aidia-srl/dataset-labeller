# Images Labeller

This script is an utility to help with image labelling for classification tasks.

Write a classes txt file like the following:

```txt
Good
Bad
```

where each line is a class and the corrisponding class number is the line number starting from 1 (`Good` is `1`, `Bad` is `2`).
At the moment up to 10 classes are supported.

To label images run the script:

```bash
❯ python main.py -h
usage: main.py [-h] [--images IMAGES] [--classes CLASSES] [--save_dir SAVE_DIR] [--ext EXT]

Label a dataset.

optional arguments:
  -h, --help           show this help message and exit
  --images IMAGES      [str] Path to the directory containing the input images
  --classes CLASSES    [str] Path to the classes file (one class per line, max 10 classes)
  --save_dir SAVE_DIR  [str] Path where to save the labelled images
  --ext EXT            [str] Images extension, Default=jpg
```

Example:

```bash
python main.py --images /path/to/images --classes classes.txt --save_dir /path/output
```

You can use numbers from 1 to 0 in your keyboard to label an image with the corresponding class.

Press `\` or `w` to skip an image.

Press `q` to quit.

## requirements

Install the requirements before running:

```bash
pip install -r requirements.txt
```

### Resuming

The script remembers where you left and it starts from the first unlabelled image.