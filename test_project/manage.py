#!/usr/bin/env python
import os
import sys

parent = os.path.dirname

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    sys.path.append(parent(parent(os.path.abspath(__file__))))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
