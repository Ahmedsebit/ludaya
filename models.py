from ludaya.ludaya import db
from sqlalchemy.dialects.postgresql import JSON
from passlib.apps import custom_app_context as pwd_context

from ludaya.ludaya import ma

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
    taskgroup = db.Column(db.String())
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
    name = db.Column(db.String(2000))
    group = db.Column(db.String(1000))
    category = db.Column(db.String(1000))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,
                              default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
    date_opened = db.Column(db.DateTime)
    date_resolved = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    status = db.Column(db.String(255), default="not started")
    satisfaction = db.Column(db.Integer)
    user_answer = db.Column(db.String(2000))
    evaluate_id = db.Column(db.Integer, default=19)
    evaluate_comment = db.Column(db.String(2000))
    evaluated_status = db.Column(db.String(255), default="not yet evaluated")


    def __init__(self, name, group, category, user_id):
        '''
        initialize with name, user_id and assignedtask_id
        '''
        self.category = category
        self.group = group
        self.name = name
        self.user_id = user_id

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


class User(db.Model):
    """This class defines the users table """

    __tablename__ = 'users'

    # Define the columns of the users table, starting with the primary key
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(256), nullable=False)
    lastname = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    assignedtask = db.relationship(
        'AssignedTask', order_by='AssignedTask.id', cascade="all, delete-orphan")
    group = db.Column(db.Integer)
    job_description = db.Column(db.String(256), nullable=True)

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
    
    def save(self):
        '''
        Saving new assignedtask
        '''
        db.session.add(self)
        db.session.commit()


class AssignedTaskSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = (
            'id',
            'name',
            'group',
            'category',
            'status',
            'user_answer',
            'satisfaction',
            'evaluate_comment'
        )
    # Smart hyperlinking
    _links = ma.Hyperlinks({
        'self': ma.URLFor('task_detail', id='<id>'),
        'collection': ma.URLFor('tasks')
    })

assignedtask_schema = AssignedTaskSchema()
assignedtasks_schema = AssignedTaskSchema(many=True)


class Groups(db.Model):
    '''
    This class represents the assignedtasks table.
    '''
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    current_members = db.Column(db.Integer)
    team_lead = db.Column(db.Integer)
    

    def __init__(self, name, current_members, team_lead):
        '''
        initialize with name, current_members, team_lead
        '''
        self.name = name
        self.current_members = current_members
        self.team_lead = team_lead

    def save(self):
        '''
        Saving new assignedtask
        '''
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_group(user_id):
        '''
        retrieving all groups
        '''
        return Groups.query.filter_by(user_id = user_id).all()

    def delete(self):
        '''
        deleting assignedtask
        '''
        db.session.delete(self)
        db.session.commit()