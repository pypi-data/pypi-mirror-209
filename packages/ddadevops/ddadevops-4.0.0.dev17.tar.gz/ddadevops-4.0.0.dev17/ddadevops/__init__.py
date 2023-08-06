"""
ddadevops provide tools to support builds combining gopass,
terraform, dda-pallet, aws & hetzner-cloud.

"""

from .python_util import execute
from .provs_k3s_mixin import ProvsK3sMixin, add_provs_k3s_mixin_config
from .aws_rds_pg_mixin import AwsRdsPgMixin, add_aws_rds_pg_mixin_config
from .aws_mfa_mixin import AwsMfaMixin, add_aws_mfa_mixin_config
from .aws_backend_properties_mixin import AwsBackendPropertiesMixin, add_aws_backend_properties_mixin_config
from .c4k_build import C4kBuild, add_c4k_mixin_config
from .exoscale_mixin import ExoscaleMixin, add_exoscale_mixin_config
from .digitalocean_backend_properties_mixin import DigitaloceanBackendPropertiesMixin, add_digitalocean_backend_properties_mixin_config
from .digitalocean_terraform_build import DigitaloceanTerraformBuild, create_digitalocean_terraform_build_config
from .hetzner_mixin import HetznerMixin, add_hetzner_mixin_config
from .devops_image_build import DevopsImageBuild, create_devops_docker_build_config
from .devops_terraform_build import DevopsTerraformBuild, create_devops_terraform_build_config
from .devops_build import DevopsBuild, create_devops_build_config, get_devops_build
from .credential import gopass_password_from_path, gopass_field_from_path
from .release_mixin import ReleaseMixin
from .domain import Validateable, DnsRecord, Devops, Image, Release, Version

__version__ = "${version}"
