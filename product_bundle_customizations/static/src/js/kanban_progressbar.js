odoo.define('olivervalves_customizations.kanban_progressbar', function (require) {
    'use strict';

    var session = require('web.session');
    var utils = require('web.utils');
    var KanbanColumnProgressBar = require('web.KanbanColumnProgressBar');

    KanbanColumnProgressBar.include({
        init: function (parent, options, columnState) {
            this._super.apply(this, arguments);

            this.columnID = options.columnID;
            this.columnState = columnState;

            // <progressbar/> new attribute
            this.sumField2 = columnState.progressBarValues.sum_field2;
            var state = options.progressBarStates[this.columnID];
            if (state) {
                this.groupCount = state.groupCount;
                this.subgroupCounts = state.subgroupCounts;
                this.totalCounterValue = state.totalCounterValue;
                this.totalCounterValue2 = state.totalCounterValue2;
                this.activeFilter = state.activeFilter;
            }

        },

        start: function() {
            this.$counter2 = this.$('.o_kanban_counter_side2');
            this.$number2 = this.$counter2.find('b');

            if (this.currency) {
                var $currency = $('<span/>', {
                    text: this.currency.symbol
                });
                if (this.currency.position === 'before') {
                    $currency.prependTo(this.$counter2);
                } else {
                    $currency.appendTo(this.$counter2);
                }
            }
            this.prevTotalCounterValue2 = this.totalCounterValue2;
            this.totalCounterValue2 = this.sumField2 ? (this.columnState.aggregateValues[this.sumField2] || 0) : this.columnState.count;
            var self = this;
            return this._super.apply(this, arguments).then(function () {
                self._notifyState();
                self._render();
            });
        },

        _render: function () {
            var self = this;

            var start2 = this.prevTotalCounterValue2;
            var end2 = this.totalCounterValue2;
            var animationClass = start2 > 999 ? 'o_kanban_grow' : 'o_kanban_grow_huge';

            if (start2 !== undefined && end2 > start2 && this.ANIMATE) {
                $({currentValue: start2}).animate({currentValue: end2}, {
                    duration: 1000,
                    start: function () {
                        self.$counter2.addClass(animationClass);
                    },
                    step: function () {
                        self.$number2.html(_getCounterHTML(this.currentValue));
                    },
                    complete: function () {
                        self.$number2.html(_getCounterHTML(this.currentValue));
                        self.$counter2.removeClass(animationClass);
                    },
                });
            } else {
                this.$number2.html(_getCounterHTML(end2));
            }

            function _getCounterHTML(value) {
                return utils.human_number(value, 0, 3);
            }

            return this._super.apply(this, arguments);
        },

        _notifyState: function () {
            this.trigger_up('set_progress_bar_state', {
            columnID: this.columnID,
            values: {
                groupCount: this.groupCount,
                subgroupCounts: this.subgroupCounts,
                totalCounterValue: this.totalCounterValue,
                totalCounterValue2: this.totalCounterValue2,
                activeFilter: this.activeFilter,
            },
        });

        }
    });
    return KanbanColumnProgressBar;
});
