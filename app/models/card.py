from .db import db, environment, SCHEMA, add_prefix_for_prod

class Card(db.Model):
    __tablename__ = 'cards'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)

    question = db.Column(db.String(80), nullable=False)

    answer = db.Column(db.String(80), nullable=False)

    deckId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('decks.id')), nullable=False)

    deck = db.relationship('Deck', back_populates='cards')



    def to_dict(self):
        return {
            'id': self.id,
            'deckId': self.deckId,
            'question': self.question,
            'answer': self.answer,
        }