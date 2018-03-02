from tasks.electronics import ELECTRONICS as electronics, electronics_list_length
from tasks.hardware import HARDWARE as hardware, hardware_list_length
from tasks.mac import MAC as mac, mac_list_length
from tasks.maintainance import MAINTAINANCE as maintainance, maintainance_list_length
from tasks.networking import NETWORKING as networking, networking_list_length
from tasks.security import SECURITY as security, security_list_length
from tasks.server import SERVER as server, server_list_length
from tasks.support import SUPPORT as support, support_list_length
from tasks.unix import UNIX as unix, unix_list_length
from tasks.windows import WINDOWS as windows, windows_list_length

ALLTASKS = [
    electronics,
    hardware,
    learning,
    mac,
    maintainance,
    networking,
    security,
    server,
    support
    ]
