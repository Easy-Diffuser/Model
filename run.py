import easy_diffuser

class export_tag():
    def __init__(self) -> None:
        self.model=easy_diffuser.start()
    
    def run(self,img):
        self.model.run(img)
        # self.model.send2ui()