from view.InputView import inputSettingValue
from controller.KBOController import KBOController

if __name__ == '__main__':
    settings = inputSettingValue()
    controller = KBOController(settings)
    controller.run()