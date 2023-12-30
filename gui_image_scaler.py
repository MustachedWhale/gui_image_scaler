import sys
import os
import cv2
from PIL import Image

import lists

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
def check_repeat(base_dir, ill_dir_list):
    for ill_dir in ill_dir_list:
        current_dir = os.path.join(base_dir, ill_dir)
        for root, dirs, files in os.walk(current_dir):
            if len(dirs) == 0:
                break
            elif len(dirs) == 6:
                print('\nThe script has already been run inside this directory.')
                exit() 

# Checks each folder name follows the convention 'Illustration X'.    
def check_ill_dirs(illustration_dir_list):
    for dir_name in illustration_dir_list:
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
def check_dir_contains_jpegs(base_dir, ill_dir):
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
    for tup in lists.dir_list:
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
                for tup in lists.dir_list:
                    if file == tup[0]:
                        equiv_dir = tup[1]
                        new_file_path = os.path.join(ill_path, equiv_dir, file)
                        os.rename(src, new_file_path)
                        break

# Creates the new images.
def create_images(ill_path, orig_image):
    orig_im_file_path = os.path.join(ill_path, orig_image)
    for ar_set in lists.ar_list:
        if orig_image == ar_set[0]:
            for item in ar_set:
                if item == orig_image:
                    continue
                else:
                    for size_dict in lists.size_list:
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
            
# == Main Code ==

# If a command-line argument has been passed in and it's a directory.
if has_cla() and check_cla_is_dir():
    base_dir = sys.argv[1]

print('\n== Image Scaler ==')

# Get a list of the directories inside base_dir.
ill_dir_list = os.listdir(base_dir)
# Checks that the directory has not already had the script run.
check_repeat(base_dir, ill_dir_list)
print('\nDirectories discovered.')
# Checks that each directory has names following the convention 'Illustration X'.
check_ill_dirs(ill_dir_list)
print('\nIllustration directories are named correctly.')

# Checks that each directory contains all .jpeg files.
print('')
for ill_dir in ill_dir_list:
    check_dir_contains_jpegs(base_dir, ill_dir)
    print(f'{ill_dir} contain files of the correct file type.')

# Creates a directory per image.
print('')
for ill_dir in ill_dir_list:
    create_dirs(base_dir, ill_dir)
    print(f'Subdirectories created for {ill_dir}.')

# Moves the initial images into the correct directory.
print('')
for ill_dir in ill_dir_list:
    move_images(base_dir, ill_dir)
    print(f'Images moved to the correct subdirectory for {ill_dir}.')

# Creates new images for each aspect ratio.
print('\nCreating images...')
for ill_dir in ill_dir_list:
    ill_dir_path = os.path.join(base_dir, ill_dir)
    ar_dir_list = os.listdir(ill_dir_path)
    if len(ar_dir_list) == 1:
        create_images(ill_dir_path, ar_dir_list[0])
        print(f'Images created in {ill_dir} directory.')
    else:
        for ar_dir in ar_dir_list:
            ar_dir_path = os.path.join(ill_dir_path, ar_dir)
            ar_file_list = os.listdir(ar_dir_path)
            create_images(ar_dir_path, ar_file_list[0])
        print(f'Images created in {ill_dir} directory.')

print('\nScaling complete.')