from typing import List, Optional
from .common import (
    Validateable,
    DnsRecord,
    Devops,
)


class C4k(Validateable):
    def __init__(self, input: dict):
        self.module = input.get("module")
        self.stage = input.get("stage")
        self.c4k_executable_name = input.get("c4k_executable_name", input.get("module"))
        self.c4k_config = input.get("c4k_config", {})
        self.c4k_grafana_cloud_url = input.get(
            "c4k_grafana_cloud_url",
            "https://prometheus-prod-01-eu-west-0.grafana.net/api/prom/push",
        )
        self.c4k_auth = input.get("c4k_auth", {})
        self.c4k_grafana_cloud_user = input.get('c4k_grafana_cloud_user')
        self.c4k_grafana_cloud_password = input.get('c4k_grafana_cloud_password')
        self.dns_record: Optional[DnsRecord] = None

    # TODO: these functions should be located at TerraformBuild later on.
    def update_runtime_config(self, dns_record: DnsRecord):
        self.dns_record = dns_record

    def validate(self) -> List[str]:
        result = []
        result += self.__validate_is_not_empty__("module")
        result += self.__validate_is_not_empty__("stage")
        result += self.__validate_is_not_empty__("c4k_executable_name")
        result += self.__validate_is_not_empty__("c4k_grafana_cloud_user")
        result += self.__validate_is_not_empty__("c4k_grafana_cloud_password")
        if self.dns_record:
            result += self.dns_record.validate()
        return result

    def config(self):
        if not self.dns_record:
            raise ValueError("dns_reqord was not set.")
        result = self.c4k_config.copy()
        result["fqdn"] = self.dns_record.fqdn
        result["mon-cfg"] = {
            "cluster-name": self.module,
            "cluster-stage": self.stage,
            "grafana-cloud-url": self.c4k_grafana_cloud_url,
        }
        return result

    def auth(self):
        result = self.c4k_auth.copy()
        result["mon-auth"] = {
            "grafana-cloud-user": self.c4k_grafana_cloud_user,
            "grafana-cloud-password": self.c4k_grafana_cloud_password,
        }
        return result

    def command(self, devops: Devops):
        module = devops.module
        build_path = devops.build_path()
        config_path = f"{build_path}/out_c4k_config.yaml"
        auth_path = f"{build_path}/out_c4k_auth.yaml"
        output_path = f"{build_path}/out_{module}.yaml"
        return f"c4k-{self.c4k_executable_name}-standalone.jar {config_path} {auth_path} > {output_path}"
