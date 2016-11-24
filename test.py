import sys
import time
import random
from mechanize import ParseResponse, urlopen, urljoin
import mechanize
import sqlite3
from datetime import datetime
from datetime import timedelta
import threading


eingabe = raw_input("Eingabe:")