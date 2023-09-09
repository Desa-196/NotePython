class Note:
    def __init__(self, id, title, text, date_time):
        self.id = id
        self.title = title
        self.text = text
        self.dateTime = date_time

    def get_id(self):
        return self.id 
    
    def get_title(self):
        return self.title 
    
    def get_text(self):
        return self.text
    
    def get_date_time(self):
        return self.date_time
    