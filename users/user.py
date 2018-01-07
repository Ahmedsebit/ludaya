class Task(object):
    """Base class for creating rooms in amity."""
    def __init__(self, user_id):
        self.user_id = user_id
        self.tasks = []


class Communication(Task):
    """Creates communication and inherits from User."""
    def __init__(self, user_id):
        super(Communication, self).__init__(
            user_id, task_category="communication", tasks=[])


class Electronics(Task):
    """Creates electronics and inherits from User."""
    def __init__(self, user_id):
        super(Electronics, self).__init__(
            user_id, task_category="electronics", tasks=[])


class Hardware(Task):
    """Creates hardware and inherits from User."""
    def __init__(self, user_id):
        super(Hardware, self).__init__(
            user_id, task_category="hardware", tasks=[])


class Learning(Task):
    """Creates learning and inherits from User."""
    def __init__(self, user_id):
        super(Learning, self).__init__(
            user_id, task_category="learning", tasks=[])

class Mac(Task):
    """Creates mac and inherits from User."""
    def __init__(self, user_id):
        super(Mac, self).__init__(
            user_id, task_category="mac", tasks=[])

class Maintainance(Task):
    """Creates maintainance and inherits from User."""
    def __init__(self, user_id):
        super(Maintainance, self).__init__(
            user_id, task_category="maintainance", tasks=[])

class Networking(Task):
    """Creates networking and inherits from User."""
    def __init__(self, user_id):
        super(Networking, self).__init__(
            user_id, task_category="networking", tasks=[])

class Security(Task):
    """Creates security and inherits from User."""
    def __init__(self, user_id):
        super(Security, self).__init__(
            user_id, task_category="security", tasks=[])

class Server(Task):
    """Creates server and inherits from User."""
    def __init__(self, user_id):
        super(Server, self).__init__(
            user_id, task_category="server", tasks=[])

class Support(Task):
    """Creates support and inherits from User."""
    def __init__(self, user_id):
        super(Support, self).__init__(
            user_id, task_category="support", tasks=[])

class Unix(Task):
    """Creates unix and inherits from User."""
    def __init__(self, user_id):
        super(Unix, self).__init__(
            user_id, task_category="unix", tasks=[])

class Windows(Task):
    """Creates windows and inherits from User."""
    def __init__(self, user_id):
        super(Windows, self).__init__(
            user_id, task_category="windows", tasks=[])
