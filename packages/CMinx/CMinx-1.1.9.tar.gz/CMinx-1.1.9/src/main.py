
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

"""
If CMinx is built with CMake, we use PyInstaller to create an executable.
PyInstaller requires us to import CMinx so it can discover the contents of
CMinx. This file imports CMinx and calls its entry point so PyInstaller can
do its thing.

:Author: CMakePP
:License: Apache 2.0
"""

from cminx import *

if __name__ == "__main__":
    main(sys.argv[1:])
