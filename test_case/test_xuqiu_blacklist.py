"""
作业思路：人为制造黑名单页面进行测试

测试顺序：进入雪球--->点击行情--->点击市场--->验证页面
在“进入雪球”与“点击行情”的步骤之间,插入一部点击登录的步骤，人为制造出弹窗效果。
然后对此进行黑名单的封装测试。
"""

import pytest
from page.app import App



class TestAddMember():

    def setup(self):
        self.app = App()
        self.main = self.app.start_app().goto_main()

    def teardown(self):
        self.app.stop_app()

    def test_wework_add_mem(self):
        result = self.main.goto_blacklist().goto_quotation().goto_market().check_page()
        assert result == "上证指数"