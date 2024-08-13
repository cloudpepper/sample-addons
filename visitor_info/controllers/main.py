from odoo import http
from odoo.http import request

class WebsiteVisitorIP(http.Controller):

    @http.route('/visitor_ip', type='http', auth='public', website=True)
    def visitor_ip(self, **kwargs):
        # Get the visitor's IP address
        visitor_ip = request.geoip.ip

        # Render the IP address on the webpage
        return request.render('visitor_info.visitor_ip_template', {'visitor_ip': visitor_ip})
