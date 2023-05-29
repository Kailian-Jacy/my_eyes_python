#!/usr/bin/env python
import os
import sys

import web
from handler import Handle

urls = (
    '/wx', 'Handle',
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()