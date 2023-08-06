import shutil
import tempfile
from pathlib import Path

import pytest

from tetra_hub.client import (
    UserError,
    _assert_is_valid_zipped_mlmodelc,
    _zip_mlmodelc_if_needed,
)


def create_sample_mlmodelc(modelDir: Path):
    Path(modelDir).mkdir(parents=True)
    Path(modelDir / "model.espresso.net").touch()
    Path(modelDir / "model.espresso.shape").touch()
    Path(modelDir / "model.espresso.weights").touch()


def test_valid_zipped_mlmodelc():
    #  1. <filepath>/model.espresso.net or
    #  2. <filepath>/model0/model.espresso.net in case of pipeline model
    #  3. <filepath>/foo.mlmodelc/model.espresso.net or
    #  4. <filepath>/foo.mlmodelc/model0/model.espresso.net in case of pipeline model

    # Case 1 and 3:
    with tempfile.TemporaryDirectory(suffix="baseDir") as baseDir:
        modelDir = Path(baseDir) / "myModel.mlmodelc"

        create_sample_mlmodelc(modelDir)
        # Case 1
        zipPath = Path(baseDir) / "my_model_archive"
        shutil.make_archive(str(zipPath), "zip", root_dir=modelDir, base_dir=modelDir)
        _assert_is_valid_zipped_mlmodelc(f"{zipPath}.zip")

        # Case 3
        zipPath = Path(baseDir) / "my_model_archive_flat"
        shutil.make_archive(str(zipPath), "zip", root_dir=modelDir, base_dir=baseDir)
        _assert_is_valid_zipped_mlmodelc(f"{zipPath}.zip")

    # Case 2 and 4:
    with tempfile.TemporaryDirectory(suffix="baseDir") as baseDir:
        modelDir = Path(baseDir) / "myModel.mlmodelc"
        pipelinePath = Path(modelDir) / "model0"
        create_sample_mlmodelc(pipelinePath)

        # Case 2
        zipPath = Path(baseDir) / "my_model_archive"
        shutil.make_archive(str(zipPath), "zip", root_dir=modelDir, base_dir=modelDir)
        _assert_is_valid_zipped_mlmodelc(f"{zipPath}.zip")

        # Case 4
        zipPath = Path(baseDir) / "my_model_archive_flat"
        shutil.make_archive(str(zipPath), "zip", root_dir=modelDir, base_dir=baseDir)
        _assert_is_valid_zipped_mlmodelc(f"{zipPath}.zip")

    with tempfile.TemporaryDirectory(suffix="baseDir") as baseDir:
        # Make an invalid model
        modelDir = Path(baseDir) / "myModel.mlmodelc"
        Path(modelDir).mkdir()
        Path(modelDir / "bad_file").touch()

        # Check that this fails
        zipPath = Path(baseDir) / "my_model_archive"
        shutil.make_archive(str(zipPath), "zip", root_dir=modelDir, base_dir=baseDir)
        with pytest.raises(UserError):
            _assert_is_valid_zipped_mlmodelc(f"{zipPath}.zip")


def test_zip_mlmodelc_if_needed_does_not_zip_zip():
    with tempfile.TemporaryDirectory(suffix="baseDir") as base_dir:
        model_dir = Path(base_dir) / "myModel.mlmodelc"
        create_sample_mlmodelc(model_dir)

        zip_base_path = Path(base_dir) / "my_model_archive"
        zip_path = shutil.make_archive(
            str(zip_base_path), "zip", root_dir=model_dir, base_dir=model_dir
        )

        with tempfile.NamedTemporaryFile(suffix=".mlmodelc.zip") as model_zip_tempfile:
            mlmodelc_zip_path = _zip_mlmodelc_if_needed(
                zip_path, model_zip_tempfile.name
            )
            assert mlmodelc_zip_path == zip_path


def test_zip_mlmodelc_if_needed_zips_dir():
    with tempfile.TemporaryDirectory(suffix="baseDir") as base_dir:
        model_dir = Path(base_dir) / "myModel.mlmodelc"
        create_sample_mlmodelc(model_dir)
        with tempfile.NamedTemporaryFile(suffix=".mlmodelc.zip") as model_zip_tempfile:
            zipfile_path = _zip_mlmodelc_if_needed(
                str(model_dir), model_zip_tempfile.name
            )
            assert zipfile_path == model_zip_tempfile.name
            _assert_is_valid_zipped_mlmodelc(zipfile_path)
