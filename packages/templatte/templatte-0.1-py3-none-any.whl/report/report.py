from datamodel import data_source
from reportmodel import report_generator
from typing import Callable


class Report:
    """Generates reports using a data source and report generator."""

    def __init__(
        self,
        data_model: data_source.IDataSource,
        report_model: report_generator.ReportGenerator,
    ) -> None:
        """
        Initialize the Report object.

        Args:
            data_model: An instance of a data source implementing the IDataSource interface.
            report_model: An instance of a report generator.

        """
        self._reportmodel = report_model
        self._datamodel = data_model

    def create(self, path: Callable[[dict], str]):
        """
        Create reports using the provided data source and report generator.

        Args:
            path: A callable that returns the path for each generated report, based on the provided data.

        """
        records = self._datamodel.data
        for row in records:
            self._reportmodel.generate(data=row, path=path(row))
