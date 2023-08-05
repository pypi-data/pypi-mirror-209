#!/usr/bin/python3
# -*- coding: utf-8 -*-

from slpkg.configs import Configs
from slpkg.utilities import Utilities


class FindInstalled(Configs):
    """ Find installed packages. """

    def __init__(self, flags: list, packages: list):
        super(Configs, self).__init__()
        self.packages: list = packages

        self.utils = Utilities()
        self.matching: list = []

        self.option_for_no_case: bool = self.utils.is_option(
            ['-m', '--no-case'], flags)

    def find(self) -> None:
        self.view_title()
        for pkg in self.packages:
            for package in self.utils.installed_packages.values():

                if self.option_for_no_case:
                    pkg: str = pkg.lower()
                    package: str = package.lower()

                if pkg in package or pkg == '*':
                    self.matching.append(package)
        self.matched()

    def view_title(self):
        print(f'The list below shows the installed packages '
              f'that contains \'{", ".join([p for p in self.packages])}\' files:\n')

    def matched(self) -> None:
        if self.matching:
            self.view_matched_packages()
        else:
            print('\nDoes not match any package.\n')

    def view_matched_packages(self):
        for package in self.matching:
            print(f'{self.cyan}{package}{self.endc}')
        self.view_summary()

    def view_summary(self):
        print(f'\n{self.grey}Total found {len(self.matching)} packages.{self.endc}')
