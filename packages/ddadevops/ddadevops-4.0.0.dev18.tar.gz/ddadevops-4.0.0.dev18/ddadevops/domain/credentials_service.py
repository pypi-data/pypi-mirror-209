from pathlib import Path
from .common import Devops, MixinType
from .devops_factory import DevopsFactory
from .version import Version
from .infrastructure import (
    BuildFileRepository    
)

class CredentialsService:
    def __init__(self, gopass_api, environment_api):
        
    @classmethod
    def prod(cls):
        return cls(
            DevopsFactory(),
            BuildFileRepository(base_dir),
        )
    
    def initialize(self, input: dict) -> Devops: 
        mixin_types = self.devops_factory.__parse_mixin_types__(input["mixin_types"])
        version = None

        if MixinType.RELEASE in mixin_types:
            primary_build_file_id = input.get("release_primary_build_file", "./project.clj")
            primary_build_file = self.build_file_repository.get(Path(primary_build_file_id))
            version = primary_build_file.get_version()

        return self.devops_factory.build_devops(input, version=version)
