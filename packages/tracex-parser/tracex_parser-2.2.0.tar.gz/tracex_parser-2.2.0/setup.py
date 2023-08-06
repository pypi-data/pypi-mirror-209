# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tracex_parser']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'tracex-parser',
    'version': '2.2.0',
    'description': "Parser for ThreadX RTOS's trace buffers (aka TraceX)",
    'long_description': "# TraceX Parser\n[![Documentation Status](https://readthedocs.org/projects/tracex_parser/badge/?version=latest)](https://tracex_parser.readthedocs.io/en/latest/?badge=latest)\n[![CircleCI](https://circleci.com/gh/julianneswinoga/tracex_parser.svg?style=shield)](https://circleci.com/gh/julianneswinoga/tracex_parser)\n[![Coverage Status](https://coveralls.io/repos/github/julianneswinoga/tracex_parser/badge.svg?branch=master)](https://coveralls.io/github/julianneswinoga/tracex_parser?branch=master)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tracex_parser)](https://pypi.org/project/tracex_parser/)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/tracex_parser)\n\nThis python package parses ThreadX trace buffers into both human and machine-readable formats.\nDon't know where to begin? Check out the [quick-start](https://tracex-parser.readthedocs.io/en/latest/quickstart.html) documentation.\nMore documentation about ThreadX trace buffers can be found [here](https://docs.microsoft.com/en-us/azure/rtos/tracex/chapter5).\n\n## Install\n`pip3 install tracex-parser`\n\n## Example trace buffers\nIn the repository source there are a couple example TraceX traces which can be used to verify that things are working correctly.\n### As a python module\n[documentation](https://tracex-parser.readthedocs.io/en/latest/py-interface.html)\n```pycon\n>>> from tracex_parser.file_parser import parse_tracex_buffer\n>>> events, obj_map = parse_tracex_buffer('./demo_threadx.trx')\n>>> events\n[4265846278:thread 7 threadResume(thread_ptr=thread 6,prev_state=0xd,stack_ptr=0x12980,next_thread=), 4265846441:thread 7 mtxPut(obj_id=mutex 0,owning_thread=0x6adc,own_cnt=0x1,stack_ptr=0x129a0), 4265846566:thread 7 mtxPut(obj_id=mutex 0,owning_thread=0x6adc,own_cnt=0x2,stack_ptr=0x129a0)]\n>>> obj_map[0xeea4]\n{'obj_reg_entry_obj_available **': '0x0', 'obj_reg_entry_obj_type **': '0x1', 'thread_reg_entry_obj_ptr': '0xeea4', 'obj_reg_entry_obj_parameter_1': '0xef4c', 'obj_reg_entry_obj_parameter_2': '0x3fc', 'thread_reg_entry_obj_name': b'System Timer Thread'}\n```\n\n### As a command line utility\n[documentation](https://tracex-parser.readthedocs.io/en/latest/cli-interface.html)\nThe `file_parser` module can also be run as a script, which will provide simple statistics on the trace as well as dumping all the events in the trace:\n```console\n$ python3 -m tracex_parser.file_parser -vvv ./demo_threadx.trx\nParsing ./demo_threadx.trx\ntotal events: 974\nobject registry size: 16\ndelta ticks: 156206\nEvent Histogram:\nqueueSend           493\nqueueReceive        428\nthreadResume        19\nthreadSuspend       16\nmtxPut              4\nisrExit             3\nisrEnter            3\nsemGet              2\nsemPut              2\nthreadSleep         2\nmtxGet              2\nAll events:\n4265846278:thread 7 threadResume(thread_ptr=thread 6,prev_state=0xd,stack_ptr=0x12980,next_thread=)\n4265846441:thread 7 mtxPut(obj_id=mutex 0,owning_thread=0x6adc,own_cnt=0x1,stack_ptr=0x129a0)\n4265846566:thread 7 mtxPut(obj_id=mutex 0,owning_thread=0x6adc,own_cnt=0x2,stack_ptr=0x129a0)\n4265846825:thread 4 threadSuspend(thread_ptr=thread 4,new_state=0x6,stack_ptr=0x11d70,next_thread=thread 7)\n4265846953:thread 4 semGet(obj_id=semaphore 0,timeout=WaitForever,cur_cnt=0x0,stack_ptr=0x11d98)\n...\n",
    'author': 'Julianne Swinoga',
    'author_email': 'julianneswinoga@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
