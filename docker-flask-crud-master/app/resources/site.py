from flask_restful import Resource, reqparse
from model.site import SiteModel
from flask_jwt_extended import jwt_required

class Sites(Resource):
    def get(self):
        return{'sites':[site.json() for site in SiteModel.query.all()]}

class Site(Resource):
    def get(self, url):
        site = SiteModel.find_site(url)
        if site:
            return site.json()
        return {'message':'site nao informado'}, 404

    @jwt_required
    def post(self, url):
        if SiteModel.find_site(url):
            return {'message':'site ja existe'}, 404
        site = SiteModel(url)
        site.save_site()
        return site.json()

    def delete(self, url):
        site = SiteModel.find_site(url)
        if site:
            site.delete_site()
            return {'message': 'deletado'}
        return {'message':'site nao eiste'}, 404
