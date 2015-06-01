import hashlib, os

from sqlalchemy import Column, Integer, String, Boolean, Binary, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    password = Column(Binary)

    def __repr__(self):
        return "<User: {}>".format(self.name)

    def set_password(self, password):
        salt = os.urandom(10)
        hashed_pw = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
        hashed_value = salt + hashed_pw
        self.password = hashed_value

    def check_password(self, password):
        salt, hashed_pw = self.password[:10], self.password[10:]
        return hashed_pw == hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    created = Column(DateTime)
    author_id = Column(Integer, ForeignKey('users.id'))

    author = relationship("User", backref=backref('messages', order_by=id))


class Medium(Base):
    __tablename__ = 'channel_media'

    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    text = Column(String)
    api_key = Column(String)
    api_secret_key = Column(String)


class MediaMessage(Base):
    __tablename__ = 'channel_media_message'

    id = Column(Integer, primary_key=True)
    message_id = Column(Integer, ForeignKey('messages.id'))
    medium_id = Column(Integer, ForeignKey('channel_media.id'))
    status = Column(Integer)

    message = relationship("Message", backref=backref('channel_statuses', order_by=id))
    channel = relationship("Medium")
    


