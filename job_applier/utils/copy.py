import os
import random
import string
import shutil

def create_directory_if_not_exists(path) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def copy_directory(src) -> str:
    current_working_directory = os.getcwd()

    browser_profiles_path = os.path.join(current_working_directory, "browser_profiles")

    create_directory_if_not_exists(browser_profiles_path)

    new_profile_directory = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

    new_profile_path = os.path.join(browser_profiles_path, new_profile_directory)

    try:
        shutil.copytree(src, new_profile_path)
    except:
        pass

    return new_profile_path
