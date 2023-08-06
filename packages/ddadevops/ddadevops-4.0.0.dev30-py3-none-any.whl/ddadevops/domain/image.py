from typing import Optional, List
from .common import (
    filter_none,
    Validateable,
)


class Image(Validateable):
    def __init__(
        self,
        input: dict,
    ):
        self.image_dockerhub_user = input.get("image_dockerhub_user")
        self.image_dockerhub_password = input.get("image_dockerhub_password")
        self.image_tag = input.get("image_tag")
        self.image_build_commons_path = input.get("image_build_commons_path")
        self.image_use_package_common_files = input.get(
            "image_use_package_common_files", True
        )
        self.image_build_commons_dir_name = input.get(
            "image_build_commons_dir_name", "docker"
        )

    def validate(self) -> List[str]:
        result = []
        result += self.__validate_is_not_empty__("image_dockerhub_user")
        result += self.__validate_is_not_empty__("image_dockerhub_password")
        if not self.image_use_package_common_files:
            result += self.__validate_is_not_empty__("image_build_commons_path")
            result += self.__validate_is_not_empty__("image_build_commons_dir_name")
        return result

    def build_commons_path(self):
        commons_path = [
            self.image_build_commons_path,
            self.image_build_commons_dir_name,
        ]
        return "/".join(filter_none(commons_path)) + "/"
