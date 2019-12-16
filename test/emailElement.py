class EmailElement:
    to_name = ""
    address = ""
    email_subject = ""
    replaceList = []

    def __init__(self, dict):
        self.to_name = dict["to_name"]
        self.address = dict["address"]
        self.email_subject = dict["email_subject"]
        for k in dict:
            if "#" in k:
                self.replaceList.append([k, dict[k]])



