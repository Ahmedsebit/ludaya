from ludaya.ludaya import db
from sqlalchemy.dialects.postgresql import JSON
from passlib.apps import custom_app_context as pwd_context

class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    taskname = db.Column(db.String())

    def __init__(self, taskname):
        self.taskname = taskname

    def __repr__(self):
        return '<id {}>'.format(self.id)


class AssignedTask(db.Model):
    '''
    This class represents the assignedtasks table.
    '''
    __tablename__ = 'assignedtasks'

    id = db.Column(db.Integer, primary_key=True)
    assignedtask_id = db.Column(db.Integer)
    name = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,
                              default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))

    def __init__(self, name, user_id, assignedtask_id):
        '''
        initialize with name, user_id and assignedtask_id
        '''
        self.name = name
        self.user_id = user_id
        self.assignedtask_id = assignedtask_id

    def save(self):
        '''
        Saving new assignedtask
        '''
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_assignedtask(user_id):
        '''
        retrieving all assignedtask
        '''
        return AssignedTask.query.filter_by(user_id = user_id).all()

    def delete(self):
        '''
        deleting assignedtask
        '''
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<AssignedTask: {}>".format(self.name)


class User(db.Model):
    """This class defines the users table """

    __tablename__ = 'users'

    # Define the columns of the users table, starting with the primary key
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    assignedtask = db.relationship(
        'AssignedTask', order_by='AssignedTask.id', cascade="all, delete-orphan")

    def hash_password(self, entered_password):
        '''
        function for hashing a password
        '''
        self.password = pwd_context.encrypt(entered_password)

    def verify_password(self, entered_password):
        '''
        function for verifying a hashed a password
        '''
        return pwd_context.verify(entered_password, self.password)