import deprecation
from enum import Enum
from typing import List
from .common import Devops, BuildType, MixinType
from .image import Image
from .c4k import C4k
from .release import Release
from .version import Version


class DevopsFactory:
    def __init__(self):
        pass

    def build_devops(self, input: dict, version: Version = None) -> Devops:
        build_types = self.__parse_build_types__(input["build_types"])
        mixin_types = self.__parse_mixin_types__(input["mixin_types"])

        specialized_builds = {}
        if BuildType.IMAGE in build_types:
            specialized_builds[BuildType.IMAGE] = Image(input)
        if BuildType.C4K in build_types:
            specialized_builds[BuildType.C4K] = C4k(input)

        mixins = {}
        if MixinType.RELEASE in mixin_types:
            mixins[MixinType.RELEASE] = Release(input, version)

        devops = Devops(input, specialized_builds=specialized_builds, mixins=mixins)

        devops.throw_if_invalid()

        return devops

    def merge(self, input: dict, context: dict, authorization: dict) -> dict:
        return {} | context | authorization | input

    def __parse_build_types__(self, build_types: List[str]) -> List[BuildType]:
        result = []
        for build_type in build_types:
            result += [BuildType[build_type]]
        return result

    def __parse_mixin_types__(self, mixin_types: List[str]) -> List[MixinType]:
        result = []
        for mixin_type in mixin_types:
            result += [MixinType[mixin_type]]
        return result
