# coding=utf-8
# Copyright 2018-2022 EVA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
from pathlib import Path
from typing import Any

import yaml

from eva.configuration.bootstrap_environment import bootstrap_environment
from eva.configuration.constants import (
    EVA_CONFIG_FILE,
    EVA_DEFAULT_DIR,
    EVA_INSTALLATION_DIR,
)
from eva.utils.logging_manager import logger


class ConfigurationManager(object):
    _yml_path = EVA_DEFAULT_DIR / EVA_CONFIG_FILE

    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._create_if_not_exists()

        return cls._instance

    @classmethod
    def suffix_pytest_xdist_worker_id_to_dir(cls, path: Path):
        try:
            worker_id = os.environ["PYTEST_XDIST_WORKER"]
            path = path / str(worker_id)
        except KeyError:
            pass
        return path

    @classmethod
    def _create_if_not_exists(cls):
        # if not cls._yml_path.exists():
        initial_eva_config_dir = Path(EVA_DEFAULT_DIR)

        # parallelize tests using pytest-xdist
        # activated only under pytest-xdist
        # Changes config dir From EVA_DEFAULT_DIR To EVA_DEFAULT_DIR / gw1
        # (where gw1 is worker id)
        updated_eva_config_dir = cls.suffix_pytest_xdist_worker_id_to_dir(
            initial_eva_config_dir
        )
        cls._yml_path = updated_eva_config_dir / EVA_CONFIG_FILE
        bootstrap_environment(
            eva_config_dir=updated_eva_config_dir,
            eva_installation_dir=EVA_INSTALLATION_DIR,
        )

    @classmethod
    def _get(cls, category: str, key: str) -> Any:
        with cls._yml_path.open("r") as yml_file:
            config_obj = yaml.load(yml_file, Loader=yaml.FullLoader)
            if config_obj is None:
                raise ValueError(f"Invalid yaml file at {cls._yml_path}")
            key_warning = (
                f"Add the entry '{category}: {key}' to the yaml file. Or, if "
                f"you did not modify the yaml file, remove it (rm {cls._yml_path}),"
                f"and the system will auto-generate one."
            )
            if category not in config_obj or key not in config_obj[category]:
                # log a warning and return None
                logger.warn(key_warning)
                return None

            return config_obj[category][key]

    @classmethod
    def _update(cls, category: str, key: str, value: str):
        with cls._yml_path.open("r+") as yml_file:
            config_obj = yaml.load(yml_file, Loader=yaml.FullLoader)

            if config_obj is None:
                raise ValueError(f"Invalid yml file at {cls._yml_path}")

            key_warning = (
                f"Cannot update the key {key} for the missing category {category}."
                f"Add the entry '{category}' to the yaml file. Or, if "
                f"you did not modify the yaml file, remove it (rm {cls._yml_path}),"
                f"and the system will auto-generate one."
            )
            if category not in config_obj:
                # log a warning and create the category
                logger.warn(key_warning)
                config_obj[category] = {}

            config_obj[category][key] = value
            yml_file.seek(0)
            yml_file.write(yaml.dump(config_obj))
            yml_file.truncate()

    @classmethod
    def get_value(cls, category: str, key: str) -> Any:
        return cls._get(category, key)

    @classmethod
    def update_value(cls, category, key, value) -> None:
        cls._update(category, key, value)
