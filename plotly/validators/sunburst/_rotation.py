import _plotly_utils.basevalidators


class RotationValidator(_plotly_utils.basevalidators.AngleValidator):
    def __init__(self, plotly_name="rotation", parent_name="sunburst", **kwargs):
        super(RotationValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs
        )
