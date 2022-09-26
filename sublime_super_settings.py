"""
SublimeSuperSettings
https://github.com/TobyGiacometti/SublimeSuperSettings
Copyright (c) 2017-2022 Toby Giacometti and contributors
Apache License 2.0
"""

import json
import os

import sublime  # pylint: disable=import-error
import sublime_plugin  # pylint: disable=import-error


configured_views = []  # pylint: disable=invalid-name


def plugin_loaded():
    """https://www.sublimetext.com/docs/3/api_reference.html"""

    # Sometimes a view is opened before the plugin is loaded. We
    # therefore apply settings to all open views once the plugin is
    # loaded.
    for window in sublime.windows():
        for view in window.views():
            apply_settings(view)


def parent_dir(path):
    """
    :param str path: Path for which the parent directory should be
        retrieved.
    :return: Parent directory path. An empty string is returned if the
        provided path is the root directory.
    :rtype: str
    """

    parent_path = os.path.abspath(os.path.join(path, os.pardir))

    # We want to detect if the provided path is the root directory.
    if parent_path == path:
        return ""

    return parent_path


def file_settings(file):
    """
    :param str file: Path of a file that contains settings.
    :return: Settings that are stored in the provided file. If the file
        cannot be found or an error occurs, an empty dictionary is
        returned.
    :rtype: dict
    """

    if not os.path.isfile(file):
        return {}

    print("SublimeSuperSettings: loading settings from " + file)

    with open(file, encoding="utf-8") as file_object:
        try:
            return json.load(file_object)
        except ValueError as exception:
            print(
                "SublimeSuperSettings: error loading settings from "
                + file_object.name
                + ": "
                + repr(exception)
            )
            return {}


def view_settings(view):
    """Retrieve settings that should be applied to a Sublime Text view.

    Settings files that are stored in the same directory as the view
    file and directories higher up are used to construct the settings
    dictionary.

    :param sublime.View view: Sublime Text view to which settings should
        be applied.
    :return: Settings that should be applied to the provided view.
    :rtype: dict
    """

    settings = {}

    syntax_file = view.settings().get("syntax")
    syntax_name = os.path.splitext(os.path.basename(syntax_file))[0]

    settings_dir = parent_dir(view.file_name())

    while True:
        # Syntax specific settings have higher priority and are loaded
        # first.
        settings_files = [
            settings_dir + "/" + syntax_name + ".sublime-settings",
            settings_dir + "/Preferences.sublime-settings",
        ]

        for settings_file in settings_files:
            dir_settings = file_settings(settings_file)

            # Settings which were loaded from a directory that is lower
            # in the directory tree have higher priority and therefore
            # override existing settings from the loaded file.
            dir_settings.update(settings)
            settings = dir_settings

        settings_dir = parent_dir(settings_dir)

        if not settings_dir:
            break

    return settings


def apply_settings(view):
    """
    :param sublime.View view: Sublime Text view to which settings should
    be applied.
    """

    # We only want to apply settings once per view for performance
    # reasons.
    if view.id() in configured_views:
        return

    for name, value in view_settings(view).items():
        view.settings().set(name, value)

    configured_views.append(view.id())


class SublimeSuperSettingsListener(sublime_plugin.EventListener):
    """https://www.sublimetext.com/docs/3/api_reference.html"""

    def on_load(self, view):  # pylint: disable=no-self-use
        """https://www.sublimetext.com/docs/3/api_reference.html"""

        apply_settings(view)

    def on_post_save(self, view):  # pylint: disable=no-self-use
        """https://www.sublimetext.com/docs/3/api_reference.html"""

        # Used to apply settings for newly created files once they are
        # saved.
        apply_settings(view)

    def on_close(self, view):  # pylint: disable=no-self-use
        """https://www.sublimetext.com/docs/3/api_reference.html"""

        try:
            configured_views.remove(view.id())
        except ValueError:
            pass
