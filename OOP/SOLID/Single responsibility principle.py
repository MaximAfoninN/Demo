# Нарушение принципа single responsibility:
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save(self):
        # Логика сохранения пользователя в базе данных
        pass

    def send_email(self, message):
        # Логика отправки электронной почты пользователю
        pass

    def generate_report(self):
        # Логика генерации отчета пользователя
        pass


# Каждый клас несет одну ответственность:
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save(self):
        # Логика сохранения пользователя в базе данных
        pass


class EmailSender:
    def send_email(self, user, message):
        # Логика отправки электронной почты пользователю
        pass


class ReportGenerator:
    def generate_report(self, user):
        # Логика генерации отчета пользователя
        pass
