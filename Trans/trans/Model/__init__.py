__author__ = 'yeounjunpark'

from sqlalchemy import (Column, Integer, Text, String, Float, TIMESTAMP, String)
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (scoped_session, sessionmaker)
from sqlalchemy.schema import ForeignKey
from datetime import datetime

DBSession = scoped_session(
    sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class UsrInfo(Base):
    __tablename__ = "usr"
    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    usrID = Column("usrID", String(50), unique=True)
    salt = Column("salt", String(8), unique=True)
    password = Column("password", String)
    primaryRole = Column("primaryRole", Integer, ForeignKey(UsrRole.id.description))

class UsrRole(Base):
    __tablename__ = "usrRole"
    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    primaryRole = Column("primaryRole", String(50))

class UsrOrigin(Base):
    __tablename__ = "usrOrigin"
    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    usrID = Column("usrID", Integer, ForeignKey(UsrInfo.id.description))
    megatonName = Column("megatonName", Integer, unique=True)

class OriginalText(Base):
    __tablename__ = "OriginalText"
    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    type = Column("Type", Integer, ForeignKey(TextType.id.description))

class Dialogue(Base):
    __tablename__ = "Dialogue"
    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    topicInfo = Column("TopicInfo", Text)
    questID = Column("QuestID", Text)
    editorialID = Column("EditorialID", Text)
    responseIndex = Column("ResponseIndex", int)
    emotion = Column("Emotion", int)
    responseText = Column("ResponseText", Text)
    notes = Column("Notes", Text)
    speechChallenge = Column("SpeechChallenge", Text)


class TextType(Base):
    __tablename__ = "TextType"
    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    description = Column("ID", Text, unique=True)

class InitialTranslation(Base):
    __tablename__ = 'InitialTranslation'
    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    translator = Column("TranslatorID", Integer, ForeignKey(UsrInfo.id.description))
    translation = Column(Text)
    checkedInDate = Column(datetime, default=datetime.utcnow)

class Review(Base):
    __tablename__ = 'Review'
    id = Column(Integer, primary_key=True, autoincrement=True)
    reviewIter = Column(Integer)
    referencedTranslation = Column(Integer)
    changes = Column(Text)
    checkedInDate = Column(datetime, default=datetime.utcnow)

