
from App.database import db

class Job(db.Model):
    Job_ID = db.Column('Job_ID', db.Integer, primary_key=True)
    Name =  db.Column('Name', db.String(50), nullable=False)
    Company = db.Column('Company', db.String(50), nullable=False)
    Contact_Info = db.Column('Contant_Info', db.String(50), nullable=False)
    Degree_Experience = db.Column('Degree/Experience', db.String(50), nullable=False)
    Requirements = db.Column('Requirements', db.String(50), nullable=False)

    def toDict(self):
        return{
            'Job_ID': self.Job_ID,
            'Name': self.Name,
            'Company': self.Company,
            'Contact_Info': self.Contact_Info,
            'Degree/Experience': self.Degree_Experience,
            'Requirements': self.Requirements
        }

