from communications import COMMUNICATION as communication, communcation_list_length
from electronics import ELECTRONICS as electronics, electronics_list_length
from hardware import HARDWARE as hardware, hardware_list_length
from learning import LEARNING as learning, learning_list_length
from mac import MAC as mac, mac_list_length
from maintainance import MAINTAINANCE as maintainance, maintainance_list_length
from networking import NETWORKING as networking, networking_list_length
from security import SECURITY as security, security_list_length
from server import SERVER as server, server_list_length
from support import SUPPORT as support, support_list_length
from unix import UNIX as unix, unix_list_length
from windows import WINDOWS as windows, windows_list_length

ALLTASKS = [
    communication,
    electronics,
    hardware,
    learning,
    mac,
    maintainance,
    # networking,
    security,
    server,
    support
    ]
