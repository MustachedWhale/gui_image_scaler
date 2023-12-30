import sys
import os
import cv2
from PIL import Image

import lists

'''
Functions for the gui_image_scaler.py file.

Functions:
    has_cla()
    check_cla_is_dir()
    check_run_repeat(base_dir, ill_dir_list)
    check_ill_dirs(ill_dir_list)
    check_file_is_jpg(file_path)
    check_dir_contains_jpgs(base_dir, ill_dir)
    create_dirs(base_dir, ill_dir)
    create_dir_from_images(file, current_dir)
    move_images(base_dir, ill_dir)
    create_images(ill_path, orig_image)
'''

# Checks that 2 command-line arguments have been passed in.
def has_cla():
    if len(sys.argv) != 2:
        print("Provide the base folder as a command line argument.")
        exit()
    else:
        return True

# Checks that the second argument is a directory.
def check_cla_is_dir():
    if not os.path.isdir(sys.argv[1]):
        print("Provide the base folder as a command line argument.")
        exit()
    else:
        return True
    
# Checks that the script has not already been run on the folder.
def check_run_repeat(base_dir, ill_dir_list):
    for ill_dir in ill_dir_list:
        current_dir = os.path.join(base_dir, ill_dir)
        for root, dirs, files in os.walk(current_dir):
            if len(dirs) == 0:
                break
            elif len(dirs) == 6:
                print('\nThe script has already been run inside this directory.')
                exit() 

# Checks each folder name follows the convention 'Illustration X'.    
def check_ill_dirs(ill_dir_list):
    for dir_name in ill_dir_list:
        if 'Illustration' in dir_name and dir_name[-1].isnumeric():
            continue
        else:
            print("Ensure that all subdirectories are named in the convention 'Illustration X', where X is a number.")
            exit()

# Checks that a file is of the .jpg file type.
def check_file_is_jpg(file_path):
    img = Image.open(file_path)
    if img.format == 'JPEG':
        img.close()
        return True
    else:
        img.close()
        return False

# Checks that all the files in the directory are .jpeg.
def check_dir_contains_jpgs(base_dir, ill_dir):
    current_dir = os.path.join(base_dir, ill_dir)
    for root, dir, files in os.walk(current_dir):
        for file in files:
            file_path = os.path.join(current_dir, file)
            if not check_file_is_jpg(file_path):
                print(f"Ensure all the files in {current_dir} are of the .jpeg file format.")
                exit()

# Creates the directories required using the images in the folder.
def create_dirs(base_dir, ill_dir):
    current_dir = os.path.join(base_dir, ill_dir)
    for root, dirs, files in os.walk(current_dir):
        # For each file, create a directory.
        for file in files:
            create_dir_from_image(file, current_dir)

# Generates a new directory for each image in current_dir.
def create_dir_from_image(file, current_dir):
    for tup in lists.dir_creation_list:
        if file == tup[0]:
            new_file_path = os.path.join(current_dir, tup[1])
            os.mkdir(new_file_path)

# Moves the images to the correct directory.
def move_images(base_dir, ill_dir):
    ill_path = os.path.join(base_dir, ill_dir)
    for root, dirs, files in os.walk(ill_path):
        # If there aren't any dirs. Breaks os.walk() after the first pass.
        if len(dirs) == 0:
            break
        else:
            for file in files:
                src = os.path.join(ill_path, file)
                for tup in lists.dir_creation_list:
                    if file == tup[0]:
                        equiv_dir = tup[1]
                        new_file_path = os.path.join(ill_path, equiv_dir, file)
                        os.rename(src, new_file_path)
                        break

# Creates the new images.
def create_images(ill_path, orig_image):
    orig_im_file_path = os.path.join(ill_path, orig_image)
    for aspect_ratio_list in lists.aspect_ratio_lists:
        if orig_image == aspect_ratio_list[0]:
            for item in aspect_ratio_list:
                if item == orig_image:
                    continue
                else:
                    for size_dict in lists.image_size_list:
                        for key, value in size_dict.items():
                            if item == key:
                                new_im_file_path = os.path.join(ill_path, item)
                                new_width = value[0]
                                new_height = value[1]
                                cv2_im = cv2.imread(orig_im_file_path)
                                resized_image = cv2.resize(cv2_im, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)
                                cv2.imwrite(new_im_file_path, resized_image)
                                pil_im = Image.open(new_im_file_path)
                                pil_im.save(new_im_file_path, "JPEG", quality=100, dpi=(300,300))