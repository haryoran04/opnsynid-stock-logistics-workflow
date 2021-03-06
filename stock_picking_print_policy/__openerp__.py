# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Stock Picking Print Policy",
    "version": "8.0.1.1.0",
    "category": "Stock Management",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "stock_picking_policy",
        "stock_operation_type_create_menu",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/stock_picking_type_views.xml",
    ],
}
