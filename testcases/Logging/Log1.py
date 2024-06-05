import logging

# Corrected the filemode to 'w'
# "a " is append, "w" is overwrite
# logging.basicConfig(level=logging.DEBUG, filename=".\logs\log_file", filemode="a")
#  Format logs
logging.basicConfig(level=logging.DEBUG, filename=".\logs\log_file", filemode="a", format = '%(asctime)s - %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class Log:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

dl = Log()
add_result = dl.add(5, 3)
logging.warning("Warning: This is first Log for add is:{}".format(add_result))
logging.debug("Debug: This is first Log for add is:{}".format(add_result))
logging.error("Error: This is first Log for add is:{}".format(add_result))
logging.critical("Critical: This is first Log for add is:{}".format(add_result))
logging.info("Info: This is first Log for add is:{}".format(add_result))

multiply_result = dl.multiply(5, 3)
logging.warning("This is first Log for multiply is:{}".format(multiply_result))