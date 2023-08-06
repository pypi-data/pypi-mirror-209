# %%
import ast
import logging
import os
import shutil
from subprocess import check_call, DEVNULL, STDOUT

from tqdm import tqdm

from .parse import Parse
from .find import Find
from .download import get_data
from . import utils
from .unparse import unparse_module
from .combine import combine

# If True, the script will exit if mypy's stubs already exist
# Keeping stubs can cause errors if files has been changed already
ERROR_ON_EXISTING_STUBS = True


def main():
    logging.basicConfig(level=logging.INFO)

    out = "tmp_stubs"

    if os.path.exists(out) and ERROR_ON_EXISTING_STUBS:
        logging.error(f"Temporary directory {out} already exists!")
        exit(1)
    else:
        logging.info("Temporary directory: " + out)

    # Generate stubs for rdkit
    if not os.path.exists(out):
        logging.info("Generating stubs for RDKit in temporary directory")
        check_call(['stubgen', '-p', 'rdkit', '-o', out], stdout=DEVNULL, stderr=STDOUT)
        shutil.rmtree(".mypy_cache")
    else:
        logging.info("Stubs for RDKit already exists in temporary directory and will be used")

    # Download documentation from RDKit
    try:
        file = __file__
    except NameError:
        file = os.getcwd()

    TMP_FILE = os.path.dirname(file) + "/data.pkl"
    logging.info("Using temporary file: " + TMP_FILE)

    logging.info("Downloading documentation from RDKit to temporary file")
    data = get_data(TMP_FILE)

    logging.info("Parsing documentation and combining with mypy's stubs")
    for link in tqdm(data):
        doc, functions, classes = Find.module(data[link])
        name = link.removesuffix(".html")
        module = Parse.module(name, doc, functions, classes)

        base_path = utils.find_path(out, name)

        new = ast.parse(utils.format_and_sort(unparse_module(module)))

        if os.path.exists(base_path):
            base = utils.parse_base(base_path)
            combined = combine(new, base)
        else:
            combined = new

        open(base_path, "w").write(utils.unparse_and_format(combined))

    logging.info("Format and source output with black and isort")
    check_call(["isort", out], stdout=DEVNULL, stderr=STDOUT)
    check_call(["black", out], stdout=DEVNULL, stderr=STDOUT)

    main_dir = os.path.dirname(__file__)+"/.."
    
    logging.info("Removing old stubs in the rdkit-stubs package")
    for file_or_folder in os.listdir(main_dir):
        if file_or_folder not in ("install", "__pycache__"):
            if os.path.isfile(main_dir + "/" + file_or_folder):
                os.remove(main_dir + "/" + file_or_folder)
            else:
                shutil.rmtree(main_dir + "/" + file_or_folder)

    # Move directory to src, so that it can be used as a package
    # Remove the temporary directory
    logging.info("Moving stubs from temporary directory to the rdkit-stubs package")
    shutil.copytree(out + "/rdkit", main_dir, dirs_exist_ok=True)
    shutil.rmtree(out)


if __name__ == "__main__":
    main()
