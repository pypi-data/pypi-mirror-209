# -*- coding: utf-8 -*-

import os
import dataclasses
from pathlib import Path
import pytest
import json


def pytest_addoption(parser):
    group = parser.getgroup("goldie")
    group.addoption(
        "--update_goldens",
        action="store_true",
        dest="update_goldens",
        default=False,
        help="Update golden files.",
    )
    group.addoption(
        "--goldens_folder",
        dest="goldens_folder",
        default="goldens",
        help="Goldens folder name.",
    )


@dataclasses.dataclass
class GoldieFixture:
    update_goldens: bool
    goldens_folder: str
    test_file_path: Path
    test_name: str

    @property
    def _golden_dir(self) -> Path:
        return self.test_file_path.parent / self.goldens_folder

    @property
    def _golden_filename(self) -> str:
        return self.test_file_path.name + "-" + self.test_name

    @property
    def _golden_path(self) -> Path:
        return self._golden_dir / self._golden_filename

    def test(self, output):
        """Compare the given test output to the saved one. If the fixture has `update_goldens` set, updates the saved data instead."""

        if isinstance(output, bytes):
            return self._test(output, is_binary=True)

        if isinstance(output, str):
            return self._test(output, is_binary=False)

        return self._test(json.dumps(output, sort_keys=True, indent=2), is_binary=False)

    def _test(self, output, is_binary: bool):
        if self.update_goldens:
            os.makedirs(self._golden_path.parent, exist_ok=True)
            with open(self._golden_path, "wb" if is_binary else "w") as f:
                f.write(output)
        else:
            if not os.path.exists(self._golden_path):
                pytest.fail(f"Golden output file not found: {self._golden_path}")

            with open(self._golden_path, "rb" if is_binary else "r") as f:
                golden_output = f.read()

            # TODO: do a smarter text diff if it's not binary.
            assert output == golden_output, "\n".join(
                [
                    "Golden output mismatch.",
                    "Expected:",
                    golden_output,
                    "Actual:",
                    output,
                ]
                if not is_binary
                else "Binary values differ."
            )


@pytest.fixture(scope="function")
def golden(request):
    yield GoldieFixture(
        update_goldens=request.config.getoption("update_goldens"),
        goldens_folder=request.config.getoption("goldens_folder"),
        test_file_path=Path(request.node.fspath),
        test_name=request.node.name,
    )
