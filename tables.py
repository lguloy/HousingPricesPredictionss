def create_classes(db):
    class Features(db.Model):
        __tablename__ = 'User_Inputs'

        id = db.Column(db.Integer, primary_key=True)
        firstflrsf = db.Column(db.String(64))
        grlivarea = db.Column(db.String(64))
        lotarea = db.Column(db.String(64))
        garagearea  = db.Column(db.String(64))
        bsmtunfsf  = db.Column(db.String(64))
        totalbsmtsf  = db.Column(db.String(64))
        lotfrontage  = db.Column(db.String(64))
        garageyrblt  = db.Column(db.String(64))
        mosol  = db.Column(db.String(64))
        yearbuilt  = db.Column(db.String(64))
        saleprice = db.Column(db.String(64))
        
        def __repr__(self):
            return '<Features %r>' % (self.name)
    return Features
