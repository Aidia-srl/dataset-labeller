from get_files_list import get_dir_content
import os
import sys
import cv2
import argparse

from rich import print
from rich.traceback import install
install(show_locals=True)


def main(args):
    with open(args.classes, "r") as classes_file:
        classes_list = [c.replace("\n", "") for c in classes_file.readlines()]

    for c in classes_list:
        os.makedirs(os.path.join(args.save_dir, c), exist_ok=True)

    done_file_names = set([os.path.basename(f) for f in get_dir_content(
        args.save_dir, pattern=f"*.{args.ext}")])

    for img_path in get_dir_content(args.images, pattern=f"*.{args.ext}"):
        base_name = os.path.basename(img_path)
        if base_name in done_file_names:
            continue

        img = cv2.imread(img_path)
        cv2.imshow("Label", img)
        recognized_command = False

        while not recognized_command:
            key = cv2.waitKey(0)
            if key == 113:  # q pressed so quit
                cv2.destroyWindow("Label")
                recognized_command = True
                sys.exit(0)
            # elif key == 119:  # w, skip image
            #     continue
            elif key == 92:  # \ pressed. Skip image.
                recognized_command = True
                print(
                    f"[bold blue]Skipped[/bold blue] [bold white]image[/bold white] [bold yellow]{base_name}[/bold yellow]")
                continue
            elif key >= 49 and key <= 58:  # number from 1 to 5 pressed to select a sku.
                selected = key - 49
                if selected < len(classes_list):
                    sel_class = classes_list[selected]
                    cv2.imwrite(os.path.join(args.save_dir,
                                sel_class, base_name), img)
                    print(
                        f"[bold white]Classified image[/bold white] [bold yellow]{base_name}[/bold yellow] [bold white]as[/bold white] [bold green]{sel_class}[/bold green]")
                    recognized_command = True
                    continue


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Label a dataset.')
    parser.add_argument(
        '--images',
        type=str,
        help='[str] Path to the directory containing the input images')
    parser.add_argument(
        '--classes',
        type=str,
        default="classes.txt",
        help='[str] Path to the classes file (one class per line, max 10 classes)')
    parser.add_argument(
        '--save_dir',
        type=str,
        help='[str] Path where to save the labelled images')
    parser.add_argument(
        '--ext',
        type=str,
        default="jpg",
        help='[str] Images extension, Default=jpg')
    args = parser.parse_args()

    if not os.path.exists(args.images):
        print("[red bold]The input directory of images does not exist![/red bold]")
        sys.exit(-1)

    if not os.path.exists(args.classes):
        print("[red bold]The classes file does not exist![/red bold]")
        sys.exit(-2)

    if args.save_dir is None:
        print("[red bold]The save_dir is not specified![/red bold]")
        sys.exit(-3)

    main(args)
