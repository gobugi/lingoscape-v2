from .db import db, environment, SCHEMA, add_prefix_for_prod

class Favorite(db.Model):
    __tablename__ = 'favorites'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)

    deckId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('decks.id')), nullable=False)

    followerId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)


    def to_dict(self):
        return {
            'id': self.id,
            'deckId': self.deckId,
            'followerId': self.followerId,
        }