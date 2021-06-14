import TorMonitor
import sys

import TorMonitor.starter


def main():       #程序入口点
  try:
    print('MSG: Starting TorMonitor......')
    TorMonitor.starter.main()
  except ImportError as exc:
    print('ERROR: Unable to start TorMonitor: %s' % exc)
    sys.exit(1)
