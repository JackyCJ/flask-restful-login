#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from flask_restful import Api
from flask import make_response
from api.handlers.UserHandlers import (
    DataAdminRequired,
    DataUserRequired,
    Index,
    Login,
    Logout,
    RefreshToken,
    Register,
    ResetPassword,
    UsersData,
    DataSuperAdminRequired)


def generate_routes(app):

    # Create api.
    api = Api(app)

    @api.representation("text/html")  # 保证restful也能够通过render_template渲染模板
    def output_html(data, code, headers):
        if isinstance(data, str):
            # data是字符串形式的html文本
            resp = make_response(data)  # 构造Response对象
            return resp
        else:
            return make_response(json.dumps(data), mimetype='application/json')

    # Add all routes resources.
    # Index page.
    api.add_resource(Index, "/")

    # Register page.
    api.add_resource(Register, "/v1/auth/register")

    # Login page.
    api.add_resource(Login, "/v1/auth/login")

    # Logout page.
    api.add_resource(Logout, "/v1/auth/logout")

    # Refresh page.
    api.add_resource(RefreshToken, "/v1/auth/refresh")

    # Password reset page. Not forgot.
    api.add_resource(ResetPassword, "/v1/auth/password_reset")

    # Example user handler for user permission.
    api.add_resource(DataUserRequired, "/data_user")

    # Example admin handler for admin permission.
    api.add_resource(DataAdminRequired, "/data_admin")

    # Example user handler for user permission.
    api.add_resource(DataSuperAdminRequired, "/data_super_admin")

    # Get users page with admin permissions.
    api.add_resource(UsersData, "/users")
