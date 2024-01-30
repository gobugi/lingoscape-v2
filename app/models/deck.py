from .db import db, environment, SCHEMA, add_prefix_for_prod

class Deck(db.Model):
    __tablename__ = 'decks'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(50), nullable=False)

    languageId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('languages.id')), nullable=False)
    language = db.relationship('Language', back_populates='decks')

    authorId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)

    author = db.relationship('User', back_populates='decks')

    cards = db.relationship('Card', back_populates='deck',
                               cascade="all, delete")



    def to_dict(self):
        return {
            'id': self.id,
            'languageId': self.languageId,
            'authorId': self.authorId,
            'author': self.author.to_dict(),
            'title': self.title,
            'cards': [card.to_dict() for card in self.cards]
        }