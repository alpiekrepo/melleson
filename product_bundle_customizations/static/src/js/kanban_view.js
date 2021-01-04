odoo.define('olivervalves_customizations.kanban_view', function (require) {
    'use strict';

    var session = require('web.session');
    var utils = require('web.utils');
    var config = require('web.config');
    var KanbanView = require('web.KanbanView');

    var _lt = core._lt;

    KanbanView.include({
        init: function (viewInfo, params) {
            var arch = viewInfo.arch;

            var progressBar;
            utils.traverse(arch, function (n) {
                var isProgressBar = (n.tag === 'progressbar');
                if (isProgressBar) {
                    progressBar = _.clone(n.attrs);
                    progressBar.colors = JSON.parse(progressBar.colors);
                    progressBar.sum_field = progressBar.sum_field || false;
                    progressBar.sum_field2 = progressBar.sum_field2 || false;
                }
                return !isProgressBar;
            });

            if (progressBar) {
                this.loadParams.progressBar = progressBar;
            }
            return this._super.apply(this, arguments);
        }
    });
    return KanbanView;
});