# Copyright 2014 Cameron Brown

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

class Post():
	""" Blog post, page or something else """

	def __init__(self, blot):
		pass

def find_types(blot):
	folder = os.listdir(blot.path.path)
	dirs = ['images', 'templates', 'config.json']
	types = []

	# All paths except special
	for i in folder:
		if i in dirs:
			# Remove when found
			folder.remove(i)
		else:
			types.append(i)
	return types
