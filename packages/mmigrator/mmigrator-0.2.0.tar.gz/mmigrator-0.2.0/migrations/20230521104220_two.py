def up(db):
    db.create_collection('two')


def down(db):
    db.drop_collection('two')
