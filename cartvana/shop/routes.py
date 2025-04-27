from flask import Blueprint, url_for
from flask_restful import Api, Resource
from cartvana.ui.models import Product, Category

shop = Blueprint('shop', __name__)
api = Api(shop)

class ProductResource(Resource):
    def get(self, category_id=None):
        if category_id:
            products = Product.query.filter_by(category_id=category_id).all()
        else:
            products = Product.query.all()
            
        return {
            'products': [
                {
                    'id': p.id,
                    'name': p.name,
                    'description': p.description,
                    'price': p.price,
                    'stock_quantity': p.stock_quantity,
                    'category_id': p.category_id,
                    'image_url': url_for('static', filename=p.image) if p.image else None
                } for p in products
            ]
        }

# Register endpoints
api.add_resource(ProductResource, '/api/products', '/api/products/<int:category_id>')
