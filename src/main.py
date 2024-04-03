from view.InputView import inputSettingValue
from controller.KBOController import KBOController
import schedule

if __name__ == '__main__':
    settings = inputSettingValue()
    controller = KBOController(settings)
    # controller.run()


    schedule.every().day.at('08:00:00').do(controller.run)
    while True:
        schedule.run_pending()