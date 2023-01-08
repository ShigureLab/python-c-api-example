from __future__ import annotations

from functools import partial
from typing import Any

from setuptools.command.build_ext import build_ext
from setuptools.extension import Extension

ext_modules = [
    Extension(
        "c_api_example.spam",
        sources=["csrc/spam.c"],
        language="c",
    ),
]


class BuildExt(build_ext):

    compiler_flags = {
        "msvc": "/std:{std}",
        "unix": "-std={std}",
    }

    def __init__(self, *args: Any, std: str = "", **kwargs: Any):
        self.std = std
        super().__init__(*args, **kwargs)

    def build_extensions(self):
        if self.std:
            std_options = [self.compiler_flags[self.compiler.compiler_type].format(std=self.std)]
        else:
            std_options = []

        for ext in self.extensions:
            ext.extra_compile_args += std_options
            ext.extra_link_args += std_options

        super().build_extensions()


C11BuildExt = partial(BuildExt, std="c11")


def build(setup_kwargs: dict[str, Any]):
    setup_kwargs.update(
        {
            "ext_modules": ext_modules,
            "cmdclass": {"build_ext": C11BuildExt},
        }
    )


if __name__ == "__main__":
    from setuptools import setup

    setup_kwargs = {}
    build(setup_kwargs)
    setup(**setup_kwargs)
