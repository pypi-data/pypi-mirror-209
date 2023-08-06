import os
import sys
from timeit import default_timer as timer
from datetime import datetime, timedelta
import yaml


from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin


class FlavorWheelPlugin(BasePlugin):
    config_scheme = (
        ('param', config_options.Type(str, default='')),
    )

    def __init__(self):
        self.almafa = []

    def on_serve(self, server, **kwargs):
        return server

    def on_page_markdown(self, markdown, page, config, **kwargs):
        print("on_page_markdown", page.meta)

    def on_page_context(self, context, page, config, nav, **kwargs):
        print("on_page_context", context)