def up(db):
    db.create_collection('three')


def down(db):
    db.drop_collection('three')
