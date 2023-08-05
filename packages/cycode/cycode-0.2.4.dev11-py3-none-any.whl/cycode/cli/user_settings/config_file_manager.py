import os
from typing import Optional, List, Dict

from cycode.cli.user_settings.base_file_manager import BaseFileManager
from cycode.cli.consts import CYCODE_CONFIGURATION_DIRECTORY


class ConfigFileManager(BaseFileManager):
    CYCODE_HIDDEN_DIRECTORY: str = CYCODE_CONFIGURATION_DIRECTORY
    FILE_NAME: str = 'config.yaml'

    ENVIRONMENT_SECTION_NAME: str = 'environment'
    EXCLUSIONS_SECTION_NAME: str = 'exclusions'
    SCAN_SECTION_NAME: str = 'scan'

    API_URL_FIELD_NAME: str = 'cycode_api_url'
    APP_URL_FIELD_NAME: str = 'cycode_app_url'
    VERBOSE_FIELD_NAME: str = 'verbose'

    MAX_COMMITS_FIELD_NAME: str = 'max_commits'
    COMMAND_TIMEOUT_FIELD_NAME: str = 'command_timeout'
    EXCLUDE_DETECTIONS_IN_DELETED_LINES: str = 'exclude_detections_in_deleted_lines'

    def __init__(self, path):
        self.path = path

    def get_api_url(self) -> Optional[str]:
        return self._get_value_from_environment_section(self.API_URL_FIELD_NAME)

    def get_app_url(self) -> Optional[str]:
        return self._get_value_from_environment_section(self.APP_URL_FIELD_NAME)

    def get_verbose_flag(self) -> Optional[bool]:
        return self._get_value_from_environment_section(self.VERBOSE_FIELD_NAME)

    def get_exclusions_by_scan_type(self, scan_type) -> Dict:
        exclusions_section = self._get_section(self.EXCLUSIONS_SECTION_NAME)
        scan_type_exclusions = exclusions_section.get(scan_type, {})
        return scan_type_exclusions

    def get_max_commits(self, command_scan_type) -> Optional[int]:
        return self._get_value_from_command_scan_type_configuration(command_scan_type, self.MAX_COMMITS_FIELD_NAME)

    def get_command_timeout(self, command_scan_type) -> Optional[int]:
        return self._get_value_from_command_scan_type_configuration(command_scan_type, self.COMMAND_TIMEOUT_FIELD_NAME)

    def get_exclude_detections_in_deleted_lines(self, command_scan_type) -> Optional[bool]:
        return self._get_value_from_command_scan_type_configuration(command_scan_type,
                                                                    self.EXCLUDE_DETECTIONS_IN_DELETED_LINES)

    def update_base_url(self, base_url: str):
        update_data = {
            self.ENVIRONMENT_SECTION_NAME: {
                self.API_URL_FIELD_NAME: base_url
            }
        }
        self.write_content_to_file(update_data)

    def add_exclusion(self, scan_type, exclusion_type, new_exclusion):
        exclusions = self._get_exclusions_by_exclusion_type(scan_type, exclusion_type)
        if new_exclusion in exclusions:
            return

        exclusions.append(new_exclusion)

        update_data = {
            self.EXCLUSIONS_SECTION_NAME: {
                scan_type: {
                    exclusion_type: exclusions
                }
            }
        }
        self.write_content_to_file(update_data)

    def get_config_directory_path(self) -> str:
        return os.path.join(self.path, self.CYCODE_HIDDEN_DIRECTORY)

    def get_filename(self) -> str:
        return os.path.join(self.get_config_directory_path(), self.FILE_NAME)

    @staticmethod
    def get_config_file_route() -> str:
        return os.path.join(ConfigFileManager.CYCODE_HIDDEN_DIRECTORY, ConfigFileManager.FILE_NAME)

    def _get_exclusions_by_exclusion_type(self, scan_type, exclusion_type) -> List:
        scan_type_exclusions = self.get_exclusions_by_scan_type(scan_type)
        return scan_type_exclusions.get(exclusion_type, [])

    def _get_value_from_environment_section(self, field_name: str):
        environment_section = self._get_section(self.ENVIRONMENT_SECTION_NAME)
        value = environment_section.get(field_name)
        return value

    def _get_scan_configuration_by_scan_type(self, command_scan_type: str) -> Dict:
        scan_section = self._get_section(self.SCAN_SECTION_NAME)
        return scan_section.get(command_scan_type, {})

    def _get_value_from_command_scan_type_configuration(self, command_scan_type: str, field_name: str):
        command_scan_type_configuration = self._get_scan_configuration_by_scan_type(command_scan_type)
        value = command_scan_type_configuration.get(field_name)
        return value

    def _get_section(self, section_name: str) -> Dict:
        file_content = self.read_file()
        return file_content.get(section_name, {})
