from core.base_page import BasePage
from core.helpers import safe_fill, safe_click


class LoginPage(BasePage):
    def open(self, url):
        self.page.goto(url)

    def login(self, username, password):
        safe_fill(self.page.get_by_role("textbox", name="Username"), username)
        safe_fill(self.page.get_by_role("textbox", name="Password"), password)
        safe_click(self.page.get_by_role("button", name="Log in"))
