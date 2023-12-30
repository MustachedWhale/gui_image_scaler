import sys
import os

import lists
import funcs
            
# == Main Code ==

# CLA check.
if funcs.has_cla() and funcs.check_cla_is_dir():
    base_dir = sys.argv[1]

print('\n== Image Scaler ==')

ill_dir_list = os.listdir(base_dir)
funcs.check_run_repeat(base_dir, ill_dir_list)
print('\nDirectories discovered.')

funcs.check_ill_dirs(ill_dir_list)
print('\nIllustration directories are named correctly.')

# Checks that each directory contains all .jpeg files.
print('')
for ill_dir in ill_dir_list:
    funcs.check_dir_contains_jpgs(base_dir, ill_dir)
    print(f'{ill_dir} contain files of the correct file type.')

# Creates a directory per image.
print('')
for ill_dir in ill_dir_list:
    funcs.create_dirs(base_dir, ill_dir)
    print(f'Subdirectories created for {ill_dir}.')

# Moves the initial images into the correct directory.
print('')
for ill_dir in ill_dir_list:
    funcs.move_images(base_dir, ill_dir)
    print(f'Images moved to the correct subdirectory for {ill_dir}.')

# Creates new images for each aspect ratio.
print('\nCreating images...')
for ill_dir in ill_dir_list:
    ill_dir_path = os.path.join(base_dir, ill_dir)
    ar_dir_list = os.listdir(ill_dir_path)
    # Creates images for a square image.
    if len(ar_dir_list) == 1:
        funcs.create_images(ill_dir_path, ar_dir_list[0])
        print(f'Images created in {ill_dir} directory.')
    # Creates images for portrait or landscape image.
    else:
        for ar_dir in ar_dir_list:
            ar_dir_path = os.path.join(ill_dir_path, ar_dir)
            ar_file_list = os.listdir(ar_dir_path)
            funcs.create_images(ar_dir_path, ar_file_list[0])
            print(f'Images creates for {ar_file_list[0]}.')
        print(f'Images created in {ill_dir} directory.')

print('\nScaling complete.')