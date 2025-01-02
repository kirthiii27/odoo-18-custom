odoo.define('custom_invoice_report.print_invoice',['web.ajax'], function(require) {
    "use strict";

    // Import necessary dependencies
    var FormView = require('web.FormView');
    var core = require('web.core');
    var rpc = require('web.rpc');
    var Dialog = require('web.Dialog');
    var QWeb = core.qweb;
    var ajax = require('web.ajax');

    // Extend the FormView to add custom behavior
    var PrintInvoiceButton = FormView.include({
        events: _.extend({}, FormView.prototype.events, {
            'click button[name="action_print_invoice"]': '_onPrintInvoiceClick',
        }),

        /**
         * This function will be triggered when the "Print Invoice" button is clicked.
         * It sends an RPC call to print the invoice and opens it in a new window.
         */
        _onPrintInvoiceClick: function(event) {
            event.preventDefault();  // Prevent the default action of the button
            var self = this;

            // Perform an RPC query to call the print invoice action
            rpc.query({
                model: 'account.move',
                method: 'action_print_invoice',
                args: [[self.model.get(self.handle).id]], // Pass the current record's ID
            })
            .then(function(result) {
                // If the RPC call is successful, open the result (the invoice) in a new window
                var printWindow = window.open(result, '_blank');
                printWindow.print();  // Trigger the print action in the new window
            })
            .fail(function() {
                alert('Error printing the invoice.');  // If there is an error, show an alert
            });
        }
    });

    return PrintInvoiceButton;  // Return the extended FormView with the custom behavior
});
