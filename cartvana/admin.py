from flask_admin.contrib.sqla import ModelView
from flask_admin.form import FileUploadField
from flask_login import current_user
from werkzeug.utils import secure_filename
from flask import redirect, url_for
from wtforms.validators import DataRequired
import os
from datetime import datetime

class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('ui.login'))

    def scaffold_form(self):
        form_class = super(AdminModelView, self).scaffold_form()
        if hasattr(self.model, 'image'):
            base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
            form_class.image = FileUploadField(
                'Image',
                base_path=base_path,
                allow_overwrite=True,
                namegen=lambda obj, file_data: secure_filename(file_data.filename)
            )
        return form_class

    def on_model_change(self, form, model, is_created):
        if hasattr(model, 'image') and model.image:
            model.image = os.path.basename(model.image)
        if hasattr(model, 'updated_at'):
            model.updated_at = datetime.utcnow()

class ProductModelView(AdminModelView):
    column_list = ['name', 'price', 'stock_quantity']
    form_columns = ['name', 'description', 'price', 'stock_quantity', 'image']