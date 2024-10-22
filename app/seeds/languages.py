from app.models import db, Language, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_languages():
    language01 = Language(language="Arabic")
    language02 = Language(language="Basque")
    language03 = Language(language="Bulgarian")
    language04 = Language(language="Catalan")
    language05 = Language(language="Chinese")
    language06 = Language(language="Croatian")
    language07 = Language(language="Czech")
    language08 = Language(language="Danish")
    language09 = Language(language="Dutch")
    language10 = Language(language="Estonian")
    language11 = Language(language="Finnish")
    language12 = Language(language="French")
    language13 = Language(language="Galician")
    language14 = Language(language="German")
    language15 = Language(language="Greek")
    language16 = Language(language="Hebrew")
    language17 = Language(language="Hungarian")
    language18 = Language(language="Indonesian")
    language19 = Language(language="Italian")
    language20 = Language(language="Japanese")
    language21 = Language(language="Korean")
    language22 = Language(language="Latvian")
    language23 = Language(language="Lithuanian")
    language24 = Language(language="Norwegian")
    language25 = Language(language="Polish")
    language26 = Language(language="Portuguese")
    language27 = Language(language="Romanian")
    language28 = Language(language="Russian")
    language29 = Language(language="Serbian")
    language30 = Language(language="Slovak")
    language31 = Language(language="Slovenian")
    language32 = Language(language="Spanish")
    language33 = Language(language="Swedish")
    language34 = Language(language="Thai")
    language35 = Language(language="Turkish")
    language36 = Language(language="Ukrainian")
    language37 = Language(language="Vietnamese")

    db.session.add(language01)
    db.session.add(language02)
    db.session.add(language03)
    db.session.add(language04)
    db.session.add(language05)
    db.session.add(language06)
    db.session.add(language07)
    db.session.add(language08)
    db.session.add(language09)
    db.session.add(language10)
    db.session.add(language11)
    db.session.add(language12)
    db.session.add(language13)
    db.session.add(language14)
    db.session.add(language15)
    db.session.add(language16)
    db.session.add(language17)
    db.session.add(language18)
    db.session.add(language19)
    db.session.add(language20)
    db.session.add(language21)
    db.session.add(language22)
    db.session.add(language23)
    db.session.add(language24)
    db.session.add(language25)
    db.session.add(language26)
    db.session.add(language27)
    db.session.add(language28)
    db.session.add(language29)
    db.session.add(language30)
    db.session.add(language31)
    db.session.add(language32)
    db.session.add(language33)
    db.session.add(language34)
    db.session.add(language35)
    db.session.add(language36)
    db.session.add(language37)


    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_languages():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.languages RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM languages"))
        
    db.session.commit()