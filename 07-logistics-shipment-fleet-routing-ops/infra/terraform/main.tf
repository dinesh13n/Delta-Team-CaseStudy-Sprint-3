# IaC baseline (still intentionally minimal, F-48 tracked for Stage M).
# F-15: the previous local_file resource wrote "shared_user=app_shared" into generated-env.txt, a credential
# artifact. It has been removed. No credential, user name or secret is emitted by this module.
terraform {
  required_version = ">= 1.6"
}

variable "environment" {
  type        = string
  default     = "local"
  description = "Deployment environment label. Platform resources are added once the platform is chosen (OQ-01)."
}

output "environment" {
  value = var.environment
}
