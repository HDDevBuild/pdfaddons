from odoo import http
import subprocess
import os

class CustomPDFController(http.Controller):

    @http.route('/custom/pdf/download', type='http', auth='user')
    def download_pdf(self, report_id, model):
        # Generate the report URL
        host_url = http.request.httprequest.host_url.rstrip('/')
        report_url = f"{host_url}/web#id={report_id}&view_type=form&model={model}"

        # Path to wkhtmltopdf
        wkhtmltopdf_path = '/usr/bin/wkhtmltopdf'  # Adjust if different

        # Temporary PDF path
        pdf_filename = f"{model}_{report_id}.pdf"
        pdf_path = os.path.join('/tmp', pdf_filename)

        # Call wkhtmltopdf
        command = [wkhtmltopdf_path, report_url, pdf_path]
        try:
            subprocess.check_call(command)
        except subprocess.CalledProcessError:
            return http.Response("Error generating PDF", status=500)

        # Read PDF content
        with open(pdf_path, 'rb') as f:
            pdf_content = f.read()

        # Remove temp file
        os.remove(pdf_path)

        headers = [
            ('Content-Type', 'application/pdf'),
            ('Content-Disposition', 'attachment; filename="%s"' % pdf_filename),
        ]

        return http.Response(pdf_content, headers=headers)
