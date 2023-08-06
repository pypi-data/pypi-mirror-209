def up(db):
    db.create_collection('one')


def down(db):
    db.drop_collection('one')
