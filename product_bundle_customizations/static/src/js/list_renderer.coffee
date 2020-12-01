odoo.define 'olivervalves_customizations.list_renderer', (require) ->
    ListRenderer = require 'web.ListRenderer'

    ListRenderer.include
        _renderHeaderCell: (node) ->
            ret = @_super.apply this, arguments

            if @arch.attrs.class == 'tree-header-classes' and @state.model == 'sale.order.line'
                ret.addClass "field-#{node.attrs.name}"

            ret
