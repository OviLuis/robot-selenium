import abc

class WebPublisherInterface(metaclass=abc.ABCMeta):
    """docstring for IWebPublisher."""
    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    @abc.abstractmethod
    def login(self):
        pass

    @abc.abstractmethod
    def post(self):
        pass

    @abc.abstractmethod
    def open_page(self):
        pass
