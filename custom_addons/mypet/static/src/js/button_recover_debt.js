/** @odoo-module **/

import ListController from "web.ListController";

ListController.include({                                       // Kế thừa vào ListController để thêm event

    events: Object.assign({}, ListController.prototype.events, {
        'click .o_btn_recover_debt': '_onClickRecoverDebt',   // Thêm event click vào button mình đã thêm
    }),

    _onClickRecoverDebt: function (ev) {     // Đây sẽ là hàm mình xử lý logic
        this.do_action({
            name: 'Đối trừ công nợ',
            res_model: 'my.pet',
            views: [[false, 'form']],
            type: 'ir.actions.act_window',
            target: 'new',
            view_mode: 'form',
        });
    }
});