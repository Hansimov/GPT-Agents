import asyncio
import datetime
import json
import logging
import os
import platform
import shutil
import sys


from pathlib import Path


def init_os_envs(apis=["openai", "bard", "claude"], set_proxy=True, cuda_device=None):
    with open(Path(__file__).parent / "secrets.json", "r") as rf:
        secrets = json.load(rf)

    if type(apis) == str:
        apis = [apis]

    if set_proxy:
        for proxy_env in ["http_proxy", "https_proxy"]:
            os.environ[proxy_env] = secrets["http_proxy"]

    apis = [api.lower() for api in apis]

    if "openai" in apis:
        os.environ["OPENAI_API_KEY"] = secrets["openai_api_key"]

    if "bard" in apis:
        os.environ["BARD_API_KEY"] = secrets["bard_api_key"]

    if "claude" in apis:
        os.environ["CLAUDE_API_KEY"] = secrets["claude_api_key"]

    if "huggingface" in apis:
        """
        https://stackoverflow.com/questions/63312859/how-to-change-huggingface-transformers-default-cache-directory
        https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables
        """
        hf_envs = {
            "TRANSFORMERS_CACHE": "models",
            "HF_DATASETS_CACHE": "datasets",
            "HF_HOME": "misc",
        }
        for env_name, env_path in hf_envs.items():
            os.environ[env_name] = str(
                Path(__file__).parent / f".cache/huggingface/{env_path}"
            )

    if cuda_device:
        os.environ["CUDA_VISIBLE_DEVICES"] = str(cuda_device)
