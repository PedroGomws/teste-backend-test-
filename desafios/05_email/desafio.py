def email_valido(email):
        if " " in email:
            return False
        if email.count("@") != 1:
            return False
        if "." not in email:
            return False

        return True
