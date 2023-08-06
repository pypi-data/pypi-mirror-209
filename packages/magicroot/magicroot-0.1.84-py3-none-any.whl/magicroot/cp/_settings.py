from .._saved.locator import path
from ._component import Component
from ..os import Folder


class SettingNotFoundError(KeyError):
    pass


class _SettingsComponent(Component):
    def __init__(self, module, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.module = module
        self.name = name

    @property
    def settings_folder(self):
        return Folder(str(path))

    @property
    def file_name(self):
        return self.module + '_' + self.name + '.json'

    @property
    def current_settings(self):
        return self.settings_folder.get(self.file_name)

    def save_settings(self, updated_settings):
        self.settings_folder.new(file=self.file_name, with_obj=updated_settings)


class _Save(_SettingsComponent):
    def __call__(self, edited_settings, *args, **kwargs):
        self.save_settings({**self.current_settings, **edited_settings})


class _Delete(_SettingsComponent):
    def __call__(self, settings_to_delete, *args, **kwargs):
        settings_to_delete = settings_to_delete if isinstance(settings_to_delete, list) else [settings_to_delete]
        current_settings = self.current_settings
        for setting in settings_to_delete:
            del current_settings[setting]
        self.save_settings(current_settings)


class _Settings(_SettingsComponent):
    @property
    def save(self):
        return _Save(self.module, self.name)

    @property
    def delete(self):
        return _Delete(self.module, self.name)

    def __getitem__(self, item):
        try:
            return self.current_settings[item]
        except KeyError:
            raise SettingNotFoundError(f'File \'{self.name}\' of module \'{self.module}\' has no setting \'{item}\'')

    def __setitem__(self, key, value):
        self.save({key: value})

    def __delitem__(self, key):
        self.delete(key)
