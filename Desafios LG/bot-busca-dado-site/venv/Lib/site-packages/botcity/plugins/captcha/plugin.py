from __future__ import annotations

import io
from typing import Any

from deathbycaptcha import deathbycaptcha
from PIL import Image
from python_anticaptcha import (AnticaptchaClient, FunCaptchaProxylessTask,
                                ImageToTextTask, NoCaptchaTaskProxylessTask)


class BotAntiCaptchaPlugin:
    def __init__(self, api_key: str) -> None:
        """
        BotAntiCaptchaPlugin.

        Args:
            api_key (str): Api_key found in your AntiCaptcha account.
        """
        # Credentials
        self.api_key = api_key
        self._client = AnticaptchaClient(api_key)
        self._last_job = None
        self._last_job_type = None

    def solve_text(self, img_or_path: Any[str, Image.Image], timeout: int = 120) -> str:
        """
        Solves a Text Captcha.

        Args:
            img_or_path: Either an Image or a path to an image file
            timeout: Maximum amount of time in seconds to wait until the captcha is solved.

        Returns:
            The captcha's solution, which is a text or a few letters.
        """
        # Checks if it needs to load the image
        if isinstance(img_or_path, str):
            file_handler = open(img_or_path, "rb")
        elif isinstance(img_or_path, Image.Image):
            file_handler = io.BytesIO()
            img_or_path.save(file_handler, "png")
            file_handler.seek(0)

        # Solves Text Captcha
        task = ImageToTextTask(file_handler)
        self._last_job = self._client.createTask(task)
        self._last_job.join(timeout)

        # Returns the result in text format
        return self._last_job.get_captcha_text()

    def solve_re(self, url: str, site_key: str, timeout: int = 120) -> str:
        """
        Solves a ReCaptcha.

        Args:
            url: URL of the page where the captcha is located.
            site_key: iFrame ID of the captcha.
            timeout: Maximum amount of time in seconds to wait until the captcha is solved.

        Returns:
            The captcha's solution.
        """

        # Obtains the captcha from an URL and a Site key
        task = NoCaptchaTaskProxylessTask(url, site_key)
        self._last_job = self._client.createTask(task)
        self._last_job.join(timeout)
        self._last_job_type = "re"

        # Returns the result in string format
        return self._last_job.get_solution_response()

    def solve_fun(self, url: str, site_key: str, timeout: int = 120) -> str:
        """
        Solves a FunCaptcha.

        Args:
            url: URL of the page where the captcha is located.
            site_key: iFrame ID of the captcha.
            timeout: Maximum amount of time in seconds to wait until the captcha is solved.

        Returns:
            The captcha's solution.
        """
        # Obtains the captcha from an URL and a Site key
        task = FunCaptchaProxylessTask(url, site_key)
        self._last_job = self._client.createTask(task)
        self._last_job.join(timeout)
        self._last_job_type = "fun"

        # Returns the result in token format
        return self._last_job.get_token_response()

    def auth(self, api_key: str) -> BotAntiCaptchaPlugin:
        """
        Updates the api_key for this object.
        This method does NOT need to be used if you have provided the correct key in this class' constructor.

        Args:
            api_key: AntiCaptcha's key that allow you to use it's API Service.

        Returns:
            self (allows method chaining).
        """
        self.api_key = api_key
        return self

    def report(self) -> BotAntiCaptchaPlugin:
        """
        Allows you to report the last solved captcha in case it was incorrect, and get refunded.

        Returns:
            self, allowing method chaining
        """
        # Checks if there is nothing to report
        if not self._last_job:
            return self

        # Reports according to the captcha type
        if self._last_job_type == "text":
            self._last_job.report_incorrect_image()
        elif self._last_job_type == "re":
            self._last_job.report_incorrect_recaptcha()
        elif self._last_job_type == "fun":
            raise NotImplementedError('Fun Captcha error report is not supported at the moment.')

        return self


class BotDeathByCaptchaPlugin:
    def __init__(self, username: str, password: str) -> None:
        """
        Provides an easy way to solve captcha's using Death By Captcha's API.

        Args:
            username: Your Death By Captcha login.
            password: Your Death By Captcha password.
        """
        # Credentials
        self._client = deathbycaptcha.SocketClient(username, password)
        self._last_job = None

    def solve(self, img_or_path: Any[str, Image.Image], timeout: int = 120) -> str:
        """
        Solves a captcha of any supported type.

        Args:
            img_or_path: Either an Image object or a path to an image file.
            timeout: Maximum amount of time in seconds to wait until the captcha is solved.

        Returns:
            The captcha's solution, which is a text or a few letters.
        """

        # Checks if it needs to load the image
        if isinstance(img_or_path, str):
            file_handler = open(img_or_path, "rb")
        elif isinstance(img_or_path, Image.Image):
            file_handler = io.BytesIO()
            img_or_path.save(file_handler, "png")
            file_handler.seek(0)

        # Uploads the captcha
        ret = self._client.decode(file_handler, timeout)
        self._last_job = ret.get('captcha')
        return ret.get('text')

    def auth(self, username: str, password: str) -> BotDeathByCaptchaPlugin:
        """
        Updates the username and password for this object.
        This method does NOT need to be used if you have provided the correct login/password
        in this class' constructor.

        Args:
            username: Your Death By Captcha username.
            password: Your Death By Captcha password.

        Returns:
            self (allows method chaining)
        """
        self._client = deathbycaptcha.SocketClient(username, password)
        return self

    def report(self) -> BotDeathByCaptchaPlugin:
        """
        Allows you to report the last solved captcha in case it was incorrect, and get refunded.

        Returns:
            self (allows method chaining)
        """
        if self._last_job:
            self._client.report(self._last_job)

        return self
