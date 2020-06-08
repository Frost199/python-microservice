"""
Hello service
"""
from time import sleep
from nameko.rpc import rpc


class GreetingService:
    """
    A greeting service class
    """
    name = "greeting_service"

    @rpc
    def hello(self, name):
        """
        A hello service
        :param name: a string of a given name
        :return:
        """
        sleep(5)
        return "Hello, {}".format(name)
