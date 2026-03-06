odoo.define('custom_pdf_download', function (require) {
    'use strict';

    document.addEventListener('DOMContentLoaded', function () {
        const button = document.getElementById('custom_download_button');
        if (button) {
            button.addEventListener('click', function () {
                // Replace with actual record ID and model
                const recordId = this.closest('.o_form_view').dataset.id;
                const model = 'your.model'; // Adjust accordingly

                window.open('/custom/pdf/download?report_id=' + recordId + '&model=' + model);
            });
        }
    });
});
