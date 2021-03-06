# V1alpha1DAGTask

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | [**V1alpha1Arguments**](V1alpha1Arguments.md) |  | [optional] 
**continue_on** | [**V1alpha1ContinueOn**](V1alpha1ContinueOn.md) |  | [optional] 
**dependencies** | **list[str]** |  | [optional] 
**name** | **str** |  | 
**on_exit** | **str** | OnExit is a template reference which is invoked at the end of the template, irrespective of the success, failure, or error of the primary template. | [optional] 
**template** | **str** |  | [optional] 
**template_ref** | [**V1alpha1TemplateRef**](V1alpha1TemplateRef.md) | TemplateRef is the reference to the template resource to execute. | [optional] 
**when** | **str** |  | [optional] 
**with_items** | [**list[V1alpha1Item]**](V1alpha1Item.md) |  | [optional] 
**with_param** | **str** | WithParam expands a task into multiple parallel tasks from the value in the parameter, which is expected to be a JSON list. | [optional] 
**with_sequence** | [**V1alpha1Sequence**](V1alpha1Sequence.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


