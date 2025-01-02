import configparser
from pathlib import Path
from Game_Module import game_over, game_continue


class ConfigManager:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.config = configparser.ConfigParser()
        self.load_config()

    def load_config(self):
        """Загружает конфигурацию из файла."""
        if not self.file_path.exists():
            raise FileNotFoundError(f'Файл "settings.ini" не найден по пути: {self.file_path}')
        self.config.read(self.file_path)

    def get(self, section, key, fallback=None):
        """Получает значение из конфигурации."""
        return self.config.get(section, key, fallback=fallback)

    def has_section(self, section):
        """Проверяет наличие секции."""
        return self.config.has_section(section)

    def check_keys(self, section, keys):
        """Проверяет наличие ключей в секции конфигурации."""
        for key in keys:
            value: str = self.get(section, key)
            if value is None:
                print(f'Ключ "{key}" отсутствует в секции "{section}".')
            elif not value:
                print(f'Значение "{key}" пустое.')
            else:
                print(f'{key.capitalize()}: {value}')

def main():
    """Основная функция программы."""
    config_file_path: str = 'D:/My_Pro/res/settings.ini'

    try:
        config_manager = ConfigManager(config_file_path)  # Создание объекта конфигурации

        # Проверка секций и ключей
        if config_manager.has_section('Settings'):
            config_manager.check_keys('Settings', ['directory', 'read_only', 'max_files'])
        if config_manager.has_section('Language'):
            config_manager.check_keys('Language', ['lang'])

    except (configparser.Error, FileNotFoundError) as e:
        print(f'Ошибка: файл settings.ini повреждён, проверьте наличие и целостность [секций].'
              f' Детали ошибки: {e}')

# Прямой вызов основной функции
if __name__ == "__main__":
    main()
    game_over()
    game_continue()