from flask.cli import AppGroup
from .users import seed_users, undo_users
from .languages import seed_languages, undo_languages
from .decks import seed_decks, undo_decks
from .cards import seed_cards, undo_cards
from .favorites import seed_favorites, undo_favorites

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        undo_favorites()
        undo_cards()
        undo_decks()
        undo_languages()
        undo_users()
    user = seed_users()
    seed_languages()
    seed_decks()
    seed_cards()
    seed_favorites()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_favorites()
    undo_cards()
    undo_decks()
    undo_languages()
    undo_users()
    # Add other undo functions here