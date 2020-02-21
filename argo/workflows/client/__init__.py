# coding: utf-8

# flake8: noqa

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    OpenAPI spec version: 2.5.0-rc10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from argo.workflows.client.api.archived_workflow_service_api import ArchivedWorkflowServiceApi
from argo.workflows.client.api.cron_workflow_service_api import CronWorkflowServiceApi
from argo.workflows.client.api.info_service_api import InfoServiceApi
from argo.workflows.client.api.workflow_service_api import WorkflowServiceApi
from argo.workflows.client.api.workflow_template_service_api import WorkflowTemplateServiceApi
from argo.workflows.client.api.v1alpha1_api import V1alpha1Api

# import ApiClient
from argo.workflows.client.api_client import ApiClient
from argo.workflows.client.configuration import Configuration
# import models into sdk package
from argo.workflows.client.models.v1alpha1_archive_strategy import V1alpha1ArchiveStrategy
from argo.workflows.client.models.v1alpha1_arguments import V1alpha1Arguments
from argo.workflows.client.models.v1alpha1_artifact import V1alpha1Artifact
from argo.workflows.client.models.v1alpha1_artifact_location import V1alpha1ArtifactLocation
from argo.workflows.client.models.v1alpha1_artifact_repository_ref import V1alpha1ArtifactRepositoryRef
from argo.workflows.client.models.v1alpha1_artifactory_artifact import V1alpha1ArtifactoryArtifact
from argo.workflows.client.models.v1alpha1_artifactory_auth import V1alpha1ArtifactoryAuth
from argo.workflows.client.models.v1alpha1_backoff import V1alpha1Backoff
from argo.workflows.client.models.v1alpha1_continue_on import V1alpha1ContinueOn
from argo.workflows.client.models.v1alpha1_cron_workflow import V1alpha1CronWorkflow
from argo.workflows.client.models.v1alpha1_cron_workflow_list import V1alpha1CronWorkflowList
from argo.workflows.client.models.v1alpha1_cron_workflow_spec import V1alpha1CronWorkflowSpec
from argo.workflows.client.models.v1alpha1_cron_workflow_status import V1alpha1CronWorkflowStatus
from argo.workflows.client.models.v1alpha1_dag_task import V1alpha1DAGTask
from argo.workflows.client.models.v1alpha1_dag_template import V1alpha1DAGTemplate
from argo.workflows.client.models.v1alpha1_executor_config import V1alpha1ExecutorConfig
from argo.workflows.client.models.v1alpha1_git_artifact import V1alpha1GitArtifact
from argo.workflows.client.models.v1alpha1_hdfs_artifact import V1alpha1HDFSArtifact
from argo.workflows.client.models.v1alpha1_hdfs_config import V1alpha1HDFSConfig
from argo.workflows.client.models.v1alpha1_hdfs_krb_config import V1alpha1HDFSKrbConfig
from argo.workflows.client.models.v1alpha1_http_artifact import V1alpha1HTTPArtifact
from argo.workflows.client.models.v1alpha1_inputs import V1alpha1Inputs
from argo.workflows.client.models.v1alpha1_item_value import V1alpha1ItemValue
from argo.workflows.client.models.v1alpha1_metadata import V1alpha1Metadata
from argo.workflows.client.models.v1alpha1_node_status import V1alpha1NodeStatus
from argo.workflows.client.models.v1alpha1_outputs import V1alpha1Outputs
from argo.workflows.client.models.v1alpha1_parallel_steps import V1alpha1ParallelSteps
from argo.workflows.client.models.v1alpha1_parameter import V1alpha1Parameter
from argo.workflows.client.models.v1alpha1_pod_gc import V1alpha1PodGC
from argo.workflows.client.models.v1alpha1_raw_artifact import V1alpha1RawArtifact
from argo.workflows.client.models.v1alpha1_resource_template import V1alpha1ResourceTemplate
from argo.workflows.client.models.v1alpha1_retry_strategy import V1alpha1RetryStrategy
from argo.workflows.client.models.v1alpha1_s3_artifact import V1alpha1S3Artifact
from argo.workflows.client.models.v1alpha1_s3_bucket import V1alpha1S3Bucket
from argo.workflows.client.models.v1alpha1_script_template import V1alpha1ScriptTemplate
from argo.workflows.client.models.v1alpha1_sequence import V1alpha1Sequence
from argo.workflows.client.models.v1alpha1_suspend_template import V1alpha1SuspendTemplate
from argo.workflows.client.models.v1alpha1_ttl_strategy import V1alpha1TTLStrategy
from argo.workflows.client.models.v1alpha1_template import V1alpha1Template
from argo.workflows.client.models.v1alpha1_template_ref import V1alpha1TemplateRef
from argo.workflows.client.models.v1alpha1_user_container import V1alpha1UserContainer
from argo.workflows.client.models.v1alpha1_value_from import V1alpha1ValueFrom
from argo.workflows.client.models.v1alpha1_workflow import V1alpha1Workflow
from argo.workflows.client.models.v1alpha1_workflow_list import V1alpha1WorkflowList
from argo.workflows.client.models.v1alpha1_workflow_spec import V1alpha1WorkflowSpec
from argo.workflows.client.models.v1alpha1_workflow_status import V1alpha1WorkflowStatus
from argo.workflows.client.models.v1alpha1_workflow_step import V1alpha1WorkflowStep
from argo.workflows.client.models.v1alpha1_workflow_template import V1alpha1WorkflowTemplate
from argo.workflows.client.models.v1alpha1_workflow_template_list import V1alpha1WorkflowTemplateList
from argo.workflows.client.models.v1alpha1_workflow_template_spec import V1alpha1WorkflowTemplateSpec
