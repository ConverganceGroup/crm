from apps import db



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



class Campaign(db.Model):
    __tablename__ = "Campaign"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    campaign_id  = db.Column(db.String(256))
    campaign_name = db.Column(db.String(256))
    bid_startegy= db.Column(db.String(256))
    budget_remainin = db.Column(db.String(256))
    buying_type = db.Column(db.String(256))
    objective = db.Column(db.String(256))
    pacing_type = db.Column(db.String(256))
    smart_promotion_type = db.Column(db.String(256))
    status = db.Column(db.String(256))
    start_time = db.Column(db.String(256))
    end_time = db.Column(db.String(256))

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
