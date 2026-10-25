"""Fail-closed source guards for a historical archive's editor startup surface."""

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _contains_key(obj, target):
    if isinstance(obj, dict):
        return target in obj or any(_contains_key(value, target) for value in obj.values())
    if isinstance(obj, list):
        return any(_contains_key(value, target) for value in obj)
    return False


def _contains_value(obj, target):
    if isinstance(obj, str):
        return obj == target
    if isinstance(obj, dict):
        return any(_contains_value(value, target) for value in obj.values())
    if isinstance(obj, list):
        return any(_contains_value(value, target) for value in obj)
    return False


def _check_tasks(text):
    parsed = json.loads(text)
    if not isinstance(parsed, dict):
        raise AssertionError("VS Code tasks file must be an object")
    if parsed.get("tasks") != []:
        raise AssertionError("Historical archive must not register editor tasks")
    if _contains_key(parsed, "runOn") or _contains_value(parsed, "folderOpen"):
        raise AssertionError("No automatic folder-open task may be defined")


def _check_settings(text):
    parsed = json.loads(text)
    if not isinstance(parsed, dict):
        raise AssertionError("VS Code settings must be an object")
    if _contains_key(parsed, "task.allowAutomaticTasks"):
        raise AssertionError("Workspace cannot define automatic-task policy")
    if _contains_key(parsed, "tasks") or _contains_key(parsed, "runOn"):
        raise AssertionError("No pseudo tasks may hide in editor settings")
    if _contains_value(parsed, "folderOpen"):
        raise AssertionError("Editor settings must not request folder-open execution")


class EditorStartupSafety(unittest.TestCase):
    def test_editor_tasks_empty(self):
        _check_tasks((ROOT / ".vscode" / "tasks.json").read_text(encoding="utf-8"))

    def test_editor_settings_no_automatic_tasks(self):
        _check_settings((ROOT / ".vscode" / "settings.json").read_text(encoding="utf-8"))

    def test_disguised_executable_absent(self):
        self.assertFalse((ROOT / "public" / "fonts" / "fa-solid.lkf").exists())

    def test_escaped_and_nested_task_regression(self):
        for candidate in (
            '{"version":"2.0.0","tasks":[{"runOptions":{"run\\u004fn":"folderOpen"}}]}',
            '{"version":"2.0.0","tasks":[],"windows":{"tasks":[{"runOptions":{"runOn":"folderOpen"}}]}}',
            '{"version":"2.0.0","tasks":[],"linux":{"runOptions":{"runOn":"folder\\u004fpen"}}}',
        ):
            with self.subTest(candidate=candidate), self.assertRaises(AssertionError):
                _check_tasks(candidate)

    def test_nested_setting_regression(self):
        for candidate in (
            '{"nested":{"task.allowAutomaticTasks":true}}',
            '{"nested":{"tasks":{"runOn":"folderOpen"}}}',
            '{"task.allowAutomaticTasks":false}',
            '{"nested":{"run\\u004fn":"folderOpen"}}',
        ):
            with self.subTest(candidate=candidate), self.assertRaises(AssertionError):
                _check_settings(candidate)

    def test_invalid_task_documents_fail_closed(self):
        for candidate in ('{"tasks":[,]}', '{"tasks": []', '[]'):
            with self.subTest(candidate=candidate), self.assertRaises((ValueError, AssertionError)):
                _check_tasks(candidate)


if __name__ == "__main__":
    unittest.main()
