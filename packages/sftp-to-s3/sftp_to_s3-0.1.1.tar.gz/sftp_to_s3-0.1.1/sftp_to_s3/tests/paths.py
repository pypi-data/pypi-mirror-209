# -*- coding: utf-8 -*-

from pathlib import Path

dir_project_root = Path(__file__).absolute().parent.parent.parent
dir_htmlcov = dir_project_root / "htmlcov"
path_test_config = dir_project_root / "tests" / "test-config.json"
path_pkey = Path.home() / ".ssh" / "id_rsa"
