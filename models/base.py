from playwright.sync_api import Page


class Base(object):
    def __init__(self, page: Page):
        self.page = page