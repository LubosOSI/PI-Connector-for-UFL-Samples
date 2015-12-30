""" piuflgen.py

   Copyright 2015 OSIsoft, LLC.
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

Generate sample data to publish to the PI Connector for UFL REST endpoint

The syntax is: python piuflgen.py format

Parameters:
    format - Specify the sample format to generate.
    Valid formats are: value or values.

Example:
    python piuflgen.py values
"""

import argparse
import datetime
import random


# Script documentation and argument checking
description = 'Create sample data for use with PI Connector for UFL'
parser = argparse.ArgumentParser(description=description)
parser.add_argument('format',
                    help='specify sample format to generate. '
                         'Select one of: value, values')
args = parser.parse_args()

try:
    sample = {'value': 'value', 'values': 'values'}[args.format]
except KeyError:
    parser.print_help()
    parser.exit(status=1)

# define devices and sensors for sample dataset
devices = ('00-00-00-b2-11-1a',
           '00-00-00-b2-11-1b',
           '00-00-00-b2-11-1c',
           '00-00-00-b2-11-1d')

sensors = ('rpm', 'temperature', 'vibration')

# Get the time a minute ago
timestamp = datetime.datetime.utcnow() - datetime.timedelta(minutes=1)

# print out sample records - one record per sensor value
timeFormat = '%Y-%m-%dT%H:%M:%SZ'
if sample == 'value':
    for device in devices:
        for sensor in sensors:
            print('{}:{},{},{}'.format(device,
                                       sensor,
                                       timestamp.strftime(timeFormat),
                                       random.randint(1000, 3450)))
        timestamp += datetime.timedelta(seconds=1)

# print out sample records - one record per asset
if sample == 'values':
    for device in devices:
        print('{},{},{},{},{}'.format(device,
                                      timestamp.strftime(timeFormat),
                                      random.randint(1000, 3450),
                                      random.randint(35, 120),
                                      random.randint(1000, 3450)))
