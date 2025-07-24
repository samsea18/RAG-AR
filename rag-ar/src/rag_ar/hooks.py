from kedro.framework.hooks import hook_impl


class ProjectHooks:
    @hook_impl
    def before_pipeline_run(self, run_params, pipeline, catalog):
        print(f"Starting pipeline run: {run_params['pipeline_name']}")
