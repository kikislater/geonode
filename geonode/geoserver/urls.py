#########################################################################
#
# Copyright (C) 2016 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from django.conf import settings
from django.urls import re_path
from . import views

urlpatterns = [  # 'geonode.geoserver.views',
    # REST Endpoints
    re_path(r"^rest/stores/(?P<store_type>\w+)/$", views.stores, name="gs_stores"),
    re_path(
        r"^rest/styles",
        views.geoserver_proxy,
        dict(proxy_path="/geoserver/rest/styles", downstream_path="rest/styles"),
        name="gs_styles",
    ),
    re_path(
        r"^rest/workspaces/(?P<workspace>\w+)",
        views.geoserver_proxy,
        dict(proxy_path="/geoserver/rest/workspaces", downstream_path="rest/workspaces"),
        name="gs_workspaces",
    ),
    re_path(
        r"^rest/layers",
        views.geoserver_proxy,
        dict(proxy_path="/geoserver/rest/layers", downstream_path="rest/layers"),
        name="gs_layers",
    ),
    re_path(
        r"^rest/imports",
        views.geoserver_proxy,
        dict(proxy_path="/geoserver/rest/imports", downstream_path="rest/imports"),
        name="gs_imports",
    ),
    re_path(
        r"^rest/sldservice",
        views.geoserver_proxy,
        dict(proxy_path="/geoserver/rest/sldservice", downstream_path="rest/sldservice"),
        name="gs_sldservice",
    ),
    # OWS Endpoints
    re_path(r"^ows", views.geoserver_proxy, dict(proxy_path="/geoserver/ows", downstream_path="ows"), name="ows_endpoint"),
    re_path(r"^gwc", views.geoserver_proxy, dict(proxy_path="/geoserver/gwc", downstream_path="gwc"), name="gwc_endpoint"),
    re_path(r"^wms", views.geoserver_proxy, dict(proxy_path="/geoserver/wms", downstream_path="wms"), name="wms_endpoint"),
    re_path(r"^wfs", views.geoserver_proxy, dict(proxy_path="/geoserver/wfs", downstream_path="wfs"), name="wfs_endpoint"),
    re_path(r"^wcs", views.geoserver_proxy, dict(proxy_path="/geoserver/wcs", downstream_path="wcs"), name="wcs_endpoint"),
    re_path(r"^wps", views.geoserver_proxy, dict(proxy_path="/geoserver/wps", downstream_path="wps"), name="wps_endpoint"),
    re_path(r"^pdf", views.geoserver_proxy, dict(proxy_path="/geoserver/pdf", downstream_path="pdf"), name="pdf_endpoint"),
    re_path(
        r"^(?P<workspace>[^/]*)/(?P<layername>[^/]*)/ows",
        views.geoserver_proxy,
        dict(proxy_path=f"/geoserver/{settings.DEFAULT_WORKSPACE}", downstream_path="ows"),
    ),
    re_path(
        r"^(?P<workspace>[^/]*)/(?P<layername>[^/]*)/wms",
        views.geoserver_proxy,
        dict(proxy_path=f"/geoserver/{settings.DEFAULT_WORKSPACE}", downstream_path="wms"),
    ),
    re_path(
        r"^(?P<workspace>[^/]*)/(?P<layername>[^/]*)/wfs",
        views.geoserver_proxy,
        dict(proxy_path=f"/geoserver/{settings.DEFAULT_WORKSPACE}", downstream_path="wfs"),
    ),
    re_path(
        r"^(?P<workspace>[^/]*)/(?P<layername>[^/]*)/wcs",
        views.geoserver_proxy,
        dict(proxy_path=f"/geoserver/{settings.DEFAULT_WORKSPACE}", downstream_path="wcs"),
    ),
    re_path(r"^updatelayers/$", views.updatelayers, name="updatelayers"),
    re_path(r"^acls/?$", views.dataset_acls, name="dataset_acls"),
    re_path(r"^online/?$", views.server_online, name="server_online"),
]
