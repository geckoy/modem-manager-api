from commands.BaseCommand import BaseCommand
from App.Helpers import *
from App.abstract.process_managment.BaseProcessCommands import BaseProcessCommands
class manage_services(BaseCommand, BaseProcessCommands):

    processname = "service"

    def exec(self, action: str, metaData: dict) -> exec_command_returned_dict:
        return super().execAbstract(action, metaData)