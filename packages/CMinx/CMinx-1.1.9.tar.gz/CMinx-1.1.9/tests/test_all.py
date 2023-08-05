#!/usr/bin/python3
# Copyright 2021 CMakePP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import unittest
import os



def main():
    loader = unittest.TestLoader()
    cwd = os.path.abspath(os.path.dirname(__file__))
    suites = loader.discover(cwd, "test_*.py")
    all_tests = unittest.TestSuite(suites)
    runner = unittest.TextTestRunner()
    result = runner.run(all_tests)

    if result.wasSuccessful():
        exit(0)
    else:
        exit(1)


if __name__ == '__main__':
    main()
