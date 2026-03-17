class PlaywrightLoginPage:
    def __init__(self, page):
        self.page = page
        self.username = "input[name='username']"
        self.password = "input[name='password']"
        self.login_btn = "button[type='submit']"

    def login(self, username, password):
        self.page.fill(self.username, username)
        self.page.fill(self.password, password)
        self.page.click(self.login_btn)