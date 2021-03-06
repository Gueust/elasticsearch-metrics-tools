
import logging

class MockLoggingHandler(logging.Handler):
  """Mock logging handler to check for expected logs.

  Messages are available from an instance's ``messages`` dict, in order, indexed by
  a lowercase log level string (e.g., 'debug', 'info', etc.).
  """

  def __init__(self, *args, **kwargs):
    self.messages = {'debug': [], 'info': [], 'warning': [], 'error': [],
                     'critical': []}
    super(MockLoggingHandler, self).__init__(*args, **kwargs)

  def emit(self, record):
    "Store a message from ``record`` in the instance's ``messages`` dict."
    self.acquire()
    try:
      self.messages[record.levelname.lower()].append(record.getMessage())
    finally:
      self.release()

  def reset(self):
    self.acquire()
    try:
      for message_list in self.messages.values():
        del message_list[:]
    finally:
      self.release()

  def __str__(self):
    return str(self.messages)