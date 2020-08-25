# coding=utf-8
"""Pasta enables AST-based transformations on python source code."""
# Copyright 2017 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .base import annotate
from .base import ast_utils
from .base import codegen
import re


def custom_sanitizer(src):
    # comment out error skeleton
    src = re.sub(r'(.*?[\r\n])(.*?def .+?[\r\n])(.*?# Error generating skeleton.*)', r'#\1#\2\3 removed', src, flags=re.M)
    # comment out None=None
    src = re.sub(r'(None = None)', r'#\1', src, flags=re.M)
    # rename "from" param
    src = re.sub(r'(def .+?\(.*?)from([,\)])', r'\1from_sanitized\2', src, flags=re.M)
    return src


def parse(src, filename="<unknown>"):
    src = custom_sanitizer(src)
    t = ast_utils.parse(src, filename)
    annotator = annotate.AstAnnotator(src)
    annotator.visit(t)
    return t


def dump(tree):
  return codegen.to_str(tree)
