import os
import shutil
import tempfile
import zipfile

import sublime
import unittesting


class TestSublimeSuperSettings(unittesting.DeferrableTestCase):
    @classmethod
    def setUpClass(cls):
        # If we store the test settings files in a directory, they are
        # mistaken as regular settings files. This leads to them being
        # loaded whenever we open Sublime Text.
        cls.tmp_dir = tempfile.mkdtemp()
        data_zip = os.path.dirname(os.path.realpath(__file__)) + "/data.zip"
        with zipfile.ZipFile(data_zip, "r") as data_zip:
            data_zip.extractall(cls.tmp_dir)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp_dir)

    def setUp(self):
        sublime.run_command("new_window")
        self.sublime_window = window = sublime.active_window()
        self.root_py_view = window.open_file(self.tmp_dir + "/test.py")
        self.root_txt_view = window.open_file(self.tmp_dir + "/test.txt")
        self.sub_py_view = window.open_file(self.tmp_dir + "/test/test.py")
        self.sub_txt_view = window.open_file(self.tmp_dir + "/test/test.txt")
        yield self.views_loaded

    def tearDown(self):
        self.sublime_window.run_command("close_window")

    def views_loaded(self):
        return (
            not self.root_py_view.is_loading()
            and not self.root_txt_view.is_loading()
            and not self.sub_py_view.is_loading()
            and not self.sub_txt_view.is_loading()
        )

    def test_general_root_dir_settings(self):
        setting = "super_settings_test_root_general"
        self.assertEqual(self.root_py_view.settings().get(setting), True)
        self.assertEqual(self.root_txt_view.settings().get(setting), True)
        self.assertEqual(self.sub_py_view.settings().get(setting), True)
        self.assertEqual(self.sub_txt_view.settings().get(setting), True)

    def test_syntax_specific_root_dir_settings(self):
        setting = "super_settings_test_root_txt"
        self.assertEqual(self.root_py_view.settings().get(setting), None)
        self.assertEqual(self.root_txt_view.settings().get(setting), True)
        self.assertEqual(self.sub_py_view.settings().get(setting), None)
        self.assertEqual(self.sub_txt_view.settings().get(setting), True)

    def test_general_sub_dir_settings(self):
        setting = "super_settings_test_sub_general"
        self.assertEqual(self.root_py_view.settings().get(setting), None)
        self.assertEqual(self.root_txt_view.settings().get(setting), None)
        self.assertEqual(self.sub_py_view.settings().get(setting), True)
        self.assertEqual(self.sub_txt_view.settings().get(setting), True)

    def test_syntax_specific_sub_dir_settings(self):
        setting = "super_settings_test_sub_txt"
        self.assertEqual(self.root_py_view.settings().get(setting), None)
        self.assertEqual(self.root_txt_view.settings().get(setting), None)
        self.assertEqual(self.sub_py_view.settings().get(setting), None)
        self.assertEqual(self.sub_txt_view.settings().get(setting), True)

    def test_settings_override(self):
        setting = "super_settings_test_override"
        self.assertEqual(self.root_py_view.settings().get(setting), False)
        self.assertEqual(self.root_txt_view.settings().get(setting), False)
        self.assertEqual(self.sub_py_view.settings().get(setting), True)
        self.assertEqual(self.sub_txt_view.settings().get(setting), True)


if __name__ == "__main__":
    unittest.main()
