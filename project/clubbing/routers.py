class MongoDBRouter:
    """
    A router to control all database operations on models in the
    Django application.
    """
    
    route_app_labels = {'yourappname'}  # Replace 'yourappname' with your actual app name

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'mongodb'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'mongodb'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'mongodb'
        return None


