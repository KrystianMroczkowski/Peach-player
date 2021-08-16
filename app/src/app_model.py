from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///localdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

SONG_FOLDER = "C:/Users/mrocz/PycharmProjects/Peach-player/app/src/songs"


class User(db.Model):
    id = Column(Integer, primary_key=True, nullable=False)
    token = Column(String(100))
    hashed_name = Column(String(200))


class Songs(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    author = Column(String(100))
    category_id = Column(Integer, ForeignKey("music_categories.id"))
    album_id = Column(Integer, ForeignKey("albums.id"))
    path = Column(String(300))
    date_added = Column(String)
    length = Column(Integer)
    user_hashed_name = Column(String(200))
    album = relationship("Albums", back_populates="song")
    category = relationship("MusicCategories", back_populates="song")
    playlist = relationship("PlaylistSongs")


class MusicCategories(db.Model):
    id = Column(Integer, primary_key=True)
    category_name = Column(String(100))
    song = relationship("Songs")
    album = relationship("Albums")
    playlist = relationship("Playlist")


class Albums(db.Model):
    id = Column(Integer, primary_key=True)
    album_name = Column(String(100))
    category_id = Column(Integer, ForeignKey("music_categories.id"))
    song = relationship("Songs")
    category = relationship("MusicCategories", back_populates="album")


class Playlist(db.Model):
    id = Column(Integer, primary_key=True)
    playlist_name = Column(String(100))
    category_id = Column(Integer, ForeignKey("music_categories.id"))
    category = relationship("MusicCategories", back_populates="playlist")
    songs = relationship("PlaylistSongs")


class PlaylistSongs(db.Model):
    id = Column(Integer, primary_key=True)
    playlist_id = Column(Integer, ForeignKey("playlist.id"))
    song_id = Column(Integer, ForeignKey("songs.id"))
    playlist = relationship("Playlist", back_populates="songs")
    songs = relationship("Songs", back_populates="playlist")


db.create_all()
