from apps import db


# class Results(db.Model):
#     __tablename__ = 'Results'
#     id = db.Column(db.Integer, primary_key=True)
#     page_reach= db.Column(db.BigInteger(unsigned=True), unique=True)
#     source = db.Column(db.String(64), unique=True)
#     date = db.Column(db.String(64), unique=True)
    

#     def __str__(self)-> int:
#         return self.page_reach


class Leadgens(db.Model):
    __tablename__ = "Leadgens"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    lead_id = db.Column(db.String(256))
    locale = db.Column(db.String(256))
    name = db.Column(db.String(256))
    status = db.Column(db.String(256))
    leads_count = db.Column(db.Integer)
    page_name = db.Column(db.String(256))
    created_time = db.Column(db.String(256))
    expired_leads_count = db.Column(db.Integer)


    def __init__(self,lead_id,locale,name,status,leads_count,page_name,created_time,expired_leads_count):
        self.lead_id = lead_id
        self.locale = locale
        self.name = name
        self.status = status
        self.leads_count = leads_count
        self.page_name = page_name
        self.created_time = created_time
        self.expired_leads_count = expired_leads_count
        

    @staticmethod
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_leads_gen():
        return Leadgens.query.with_entities(Leadgens.lead_id,Leadgens.locale,Leadgens.name,Leadgens.status,
            Leadgens.leads_count,Leadgens.page_name,Leadgens.created_time,Leadgens.expired_leads_count).all()
        

    def __str__(self) -> str:
        return self.name



# class Campaign(db.Model):
#     pass

# class Adsets(db.Model):
#     pass