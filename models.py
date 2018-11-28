from flask_sqlalchemy import SQLAlchemy
from settings import app
db = SQLAlchemy(app)

class PoliceDepCalls(db.Model):
    __tablename__ = 'Police_Dep_Calls'
    crime_ID = db.Column(db.Integer, primary_key = True)
    original_crime_type_name = db.Column(db.String(30))
    raport_date = db.Column(db.DateTime())
    call_date = db.Column(db.DateTime())
    offense_date = db.Column(db.DateTime())
    call_time  = db.Column(db.String(5))
    call_date_time = db.Column(db.DateTime())
    disposition = db.Column(db.String(30))
    adress = db.Column(db.String(50))
    city = db.Column(db.String(30))
    state = db.Column(db.String(3))
    agency_id = db.Column(db.Integer)
    adress_type = db.Column(db.String(30))
    common_location = db.Column(db.String(50))

    def AddCall(_crime_ID, _original_crime_type_name, _raport_date, _call_date, _offense_date, _call_time, _call_date_time, _disposition, _adress, _city, _state, _agency_id, _adress_type, _common_locatio$
        new_call = PoliceDepCalls(crime_ID = _crime_ID, original_crime_type_name = _original_crime_type_name, raport_date = _raport_date, call_date = _call_date, offense_date = _offense_date, call_time =$
        db.session.add(new_call)
        db.session.commit()

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })
