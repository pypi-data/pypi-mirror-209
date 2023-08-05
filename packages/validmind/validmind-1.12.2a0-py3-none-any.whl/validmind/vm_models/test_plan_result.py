"""
TestPlanResult
"""
import base64
import json
import os

from abc import ABC, abstractmethod
from dataclasses import dataclass
from io import BytesIO
from typing import List, Optional

import markdown

from IPython.display import display
import ipywidgets as widgets
import pandas as pd

from ..api_client import (
    get_metadata,
    log_figure,
    log_metadata,
    log_metrics,
    log_model,
    log_test_result,
)
from .figure import Figure
from .metric_result import MetricResult
from .model import Model
from .result_summary import ResultSummary
from .test_result import TestResults
from ..utils import NumpyEncoder


def update_metadata(content_id: str, text: str) -> None:
    """
    Update the metadata of a content item. By default we don't
    override the existing metadata, but we can override it by
    setting the VM_OVERRIDE_METADATA environment variable to True
    """
    VM_OVERRIDE_METADATA = os.environ.get("VM_OVERRIDE_METADATA", False)
    existing_metadata = get_metadata(content_id)

    if (
        existing_metadata is None
        or VM_OVERRIDE_METADATA == "True"
        or VM_OVERRIDE_METADATA is True
    ):
        log_metadata(content_id, text)


def plot_figures(figures: List[Figure]) -> None:
    """
    Plot figures to a ipywidgets GridBox
    """

    plots = []

    for fig in figures:
        tmpfile = BytesIO()
        fig.figure.savefig(tmpfile, format="png")
        encoded = base64.b64encode(tmpfile.getvalue()).decode("utf-8")
        plots.append(
            widgets.HTML(
                value=f"""
                <img style="width:100%; height: auto;" src="data:image/png;base64,{encoded}"/>
                """
            )
        )

    num_columns = 2 if len(figures) > 1 else 1
    return widgets.GridBox(
        plots,
        layout=widgets.Layout(grid_template_columns=f"repeat({num_columns}, 1fr)"),
    )


@dataclass
class TestPlanResult(ABC):
    """Base Class for test plan results"""

    name: str = "TestPlanResult"
    # id of the result, can be set by the subclass. This helps
    # looking up results later on
    result_id: str = None
    # Text metadata about the result, can include description, etc.
    result_metadata: List[dict] = None

    def __str__(self) -> str:
        """May be overridden by subclasses"""
        return self.__class__.__name__

    @abstractmethod
    def _to_widget(self):
        """Create an ipywdiget representation of the result... Must be overridden by subclasses"""
        raise NotImplementedError

    def _markdown_description_to_html(self, description: str):
        """
        Convert a markdown string to html
        """

        return markdown.markdown(description, extensions=["markdown.extensions.tables"])

    def _summary_tables_to_widget(self, summary: ResultSummary):
        """
        Create an ipywdiget representation of the summary tables
        """
        tables = []
        for table in summary.results:
            # Explore advanced styling
            summary_table = (
                pd.DataFrame(table.data)
                .style.format(precision=4)
                .hide(axis="index")
                .to_html()
            )  # table.data is an orient=records dump

            if table.metadata and table.metadata.title:
                tables.append(widgets.HTML(value=f"<h3>{table.metadata.title}</h3>"))
            tables.append(widgets.HTML(value=summary_table))
        return tables

    def show(self):
        """Display the result... May be overridden by subclasses"""
        display(self._to_widget())

    @abstractmethod
    def log(self):
        """Log the result... Must be overridden by subclasses"""
        raise NotImplementedError


@dataclass
class TestPlanMetricResult(TestPlanResult):
    """
    Result wrapper for metrics that run as part of a test plan
    """

    name: str = "Metric"
    figures: Optional[List[Figure]] = None
    metric: Optional[MetricResult] = None

    def __repr__(self) -> str:
        if self.metric:
            return f'{self.__class__.__name__}(result_id="{self.result_id}", metric, figures)'
        else:
            return f'{self.__class__.__name__}(result_id="{self.result_id}", figures)'

    def __str__(self) -> str:
        if self.metric:
            return f'{self.__class__.__name__}(result_id="{self.result_id}", metric, figures)'
        else:
            return f"{self.__class__.__name__}(result_id={self.result_id}, figures)"

    def _to_widget(self):
        if self.metric and self.metric.key == "dataset_description":
            return ""

        vbox_children = []

        if self.result_metadata:
            metric_description = self.result_metadata[0]
            vbox_children.append(
                widgets.HTML(
                    value=self._markdown_description_to_html(
                        metric_description.get("text", "")
                    )
                )
            )

        if self.metric:
            if self.metric.summary:
                tables = self._summary_tables_to_widget(self.metric.summary)
                vbox_children.extend(tables)
            # else:
            # vbox_children.append(
            #     widgets.HTML(
            #         value=f"""<h4>Unable to display metric summary for {self.result_id}. Please make sure the summary() method is implemented for this metric</h4>"""
            #     )
            # )

            # Disable for now and fix later
            #
            # view_raw_data_button = widgets.Button(description="View Raw Data")

            # # Hide raw data by default
            # output = widgets.Output()
            # output.layout.display = "none"

            # metric_value = self.metric.value
            # metric_output = (
            #     json.dumps(metric_value, indent=2, cls=NumpyEncoder)
            #     if type(metric_value) == dict
            #     else str(metric_value)
            # )

            # with output:
            #     display(
            #         widgets.HTML(
            #             value=f"""
            #         <div class="metric-result">
            #             <div class="metric-value">
            #                 <div class="metric-value-title">Raw Metric Value</div>
            #                 <div class="metric-value-value">
            #                     <pre>{metric_output}</pre>
            #                 </div>
            #             </div>
            #         </div>
            #         """
            #         )
            #     )

            # def on_button_clicked(b):
            #     if output.layout.display == "none":
            #         output.layout.display = "block"
            #     else:
            #         output.layout.display = "none"

            # view_raw_data_button.on_click(on_button_clicked)

            # vbox_children.append(view_raw_data_button)
            # vbox_children.append(output)

        if self.figures:
            vbox_children.append(widgets.HTML(value="<h3>Plots</h3>"))
            plot_widgets = plot_figures(self.figures)
            vbox_children.append(plot_widgets)

        vbox_children.append(
            widgets.HTML(
                value="""
        <style>
            .metric-result {
                background-color: #F5F5F5;
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                padding: 10px;
                margin: 10px 0;
            }
            .metric-result-body {
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                gap: 10px;
            }
            .metric-body-column {
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                width: 33%;
            }
            .metric-body-column-title {
                font-size: 16px;
                font-weight: 600;
            }
            .metric-value {
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                margin-top: 15px;
            }
            .metric-value-title {
                font-size: 16px;
                font-weight: 600;
            }
            .metric-value-value {
                font-size: 14px;
                font-weight: 500;
                margin-top: 10px;
            }
        </style>
        """
            )
        )

        return widgets.VBox(vbox_children)

    def log(self):
        if self.metric:
            log_metrics([self.metric])
        if self.figures:
            for fig in self.figures:
                log_figure(fig.figure, fig.key, fig.metadata)
        if hasattr(self, "result_metadata") and self.result_metadata:
            for metadata in self.result_metadata:
                update_metadata(metadata["content_id"], metadata["text"])


@dataclass
class TestPlanModelResult(TestPlanResult):
    """
    Result wrapper for models that run as part of a test plan
    """

    name: str = "Metric"
    model: Model = None

    def _to_widget(self):
        return widgets.HTML(
            value=f"""
        <div class="model-result">
            <div class="model-result-header">
                <div class="model-result-header-title">
                    <span class="model-result-header-title-text">
                        {self.model.model.__class__.__name__} ({self.model.model_id})
                    </span>
                    <span class="model-result-header-title-icon">📦</span>
                </div>
            </div>
            <div class="model-result-body">
                <div class="model-body-column">
                    <div class="model-body-column-title">Framework</div>
                    <div class="model-body-column-value">
                        {self.model.attributes.framework}
                        <span>(v{self.model.attributes.framework_version})</span>
                    </div>
                </div>
                <div class="model-body-column">
                    <div class="model-body-column-title">Architecture</div>
                    <div class="model-body-column-value">{self.model.attributes.architecture}</div>
                </div>
                <div class="model-body-column">
                    <div class="model-body-column-title">Task</div>
                    <div class="model-body-column-value">{self.model.task}</div>
                </div>
                <div class="model-body-column">
                    <div class="model-body-column-title">Subtask</div>
                    <div class="model-body-column-value">{self.model.subtask}</div>
                </div>
            </div>
        </div>
        <style>
            .model-result {{
                border: 1px solid #ccc;
                border-radius: 5px;
                margin: 10px 0;
            }}
            .model-result-header {{
                padding: 10px;
                background-color: #eee;
                border-radius: 5px 5px 0 0;
            }}
            .model-result-header-title {{
                display: flex;
                align-items: center;
            }}
            .model-result-header-title-text {{
                font-weight: bold;
                font-size: 1.2em;
            }}
            .model-result-header-title-icon {{
                margin-left: 10px;
            }}
            .model-result-body {{
                padding: 10px;
                display: flex;
                flex-wrap: wrap;
            }}
            .model-body-column {{
                flex: 1 1 50%;
                padding: 5px;
            }}
            .model-body-column-title {{
                font-weight: bold;
            }}
        </style>
        """
        )

    def log(self):
        log_model(self.model)


@dataclass
class TestPlanTestResult(TestPlanResult):
    """
    Result wrapper for test results produced by the tests that run as part of a test plan
    """

    name: str = "Threshold Test"
    figures: Optional[List[Figure]] = None
    test_results: TestResults = None

    def __repr__(self) -> str:
        if self.test_results:
            return (
                f'{self.__class__.__name__}(result_id="{self.result_id}", test_results)'
            )
        else:
            return f'{self.__class__.__name__}(result_id="{self.result_id}", figures)'

    def __str__(self) -> str:
        if self.test_results:
            return (
                f'{self.__class__.__name__}(result_id="{self.result_id}", test_results)'
            )
        else:
            return f'{self.__class__.__name__}(result_id="{self.result_id}", figures)'

    def _to_widget(self):
        vbox_children = []
        description_html = []

        test_params = json.dumps(self.test_results.params, cls=NumpyEncoder)

        description_html.append(
            f"""
            <h2>{" ".join(self.test_results.test_name.split("_")).title()} {"✅" if self.test_results.passed else "❌"}</h2>
            """
        )

        if self.result_metadata:
            metric_description = self.result_metadata[0]
            description_html.append(
                self._markdown_description_to_html(metric_description.get("text", ""))
            )

        description_html.append(
            f"""
                <h4>Test Parameters</h4>
                <pre>{test_params}</pre>
            """
        )

        vbox_children.append(widgets.HTML(value="".join(description_html)))

        if self.test_results.summary:
            tables = self._summary_tables_to_widget(self.test_results.summary)
            vbox_children.extend(tables)

        if self.figures:
            vbox_children.append(widgets.HTML(value="<h3>Plots</h3>"))
            plot_widgets = plot_figures(self.figures)
            vbox_children.append(plot_widgets)

        return widgets.VBox(vbox_children)

    def log(self):
        log_test_result(self.test_results)
        if self.figures:
            for fig in self.figures:
                log_figure(fig.figure, fig.key, fig.metadata)
        if hasattr(self, "result_metadata") and self.result_metadata:
            for metadata in self.result_metadata:
                update_metadata(metadata["content_id"], metadata["text"])
