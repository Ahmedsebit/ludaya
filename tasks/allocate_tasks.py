from tasks.system_administrator.allocate_tasks import assign_system_admin_task
from tasks.socialmedia_administrator.allocate_tasks import assign_socalmedia_admin_task

from tasks.server_administrator.allocate_tasks import assign_server_admin_task
from tasks.security_administrator.allocate_tasks import assign_security_admin_task
from tasks.network_administrator.allocate_tasks import assign_network_admin_task
from tasks.database_administrator.allocate_tasks import assign_database_admin_task

def allocate_tasks():
    assign_system_admin_task()
    assign_socalmedia_admin_task()
    assign_server_admin_task()
    assign_security_admin_task()
    assign_network_admin_task()
    assign_database_admin_task()

def category_task():
    pass