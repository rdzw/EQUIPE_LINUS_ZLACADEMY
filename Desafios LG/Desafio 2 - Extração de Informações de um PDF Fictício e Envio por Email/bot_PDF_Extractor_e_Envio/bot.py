from botcity.core import DesktopBot

from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()