from . import _version
from .plugin import BotAntiCaptchaPlugin  # noqa: F401, F403
from .plugin import BotDeathByCaptchaPlugin  # noqa: F401, F403

__version__ = _version.get_versions()['version']
