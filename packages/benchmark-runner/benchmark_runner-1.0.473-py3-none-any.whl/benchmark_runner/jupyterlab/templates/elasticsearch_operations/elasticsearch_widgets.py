import ipywidgets as widgets
from datetime import datetime, time
from IPython.display import HTML, display
from benchmark_runner.common.elasticsearch.elasticsearch_operations import ElasticSearchOperations


class ElasticSearchWidgets:
    """
    This class contains elasticsearch widgets
    """

    DEFAULT_TIME = 0

    def __init__(self, elasticsearch: ElasticSearchOperations):
        self.__elasticsearch = elasticsearch

    def index_dropdown(self):
        """
        index dropdown widget
        @return:
        """
        dropdown = widgets.Dropdown(
            options=self.__elasticsearch.get_all_result_index(),
            value=self.__elasticsearch.get_all_result_index()[0],
            description='Choose index & time:',
            style={'description_width': 'initial'},
            layout=widgets.Layout(width='500px')
        )
        elastic_index = dropdown.value

        def on_dropdown_change(change):
            global elastic_index
            elastic_index = change.new

        dropdown.observe(on_dropdown_change, names='value')
        display(dropdown)
        return elastic_index

    def choose_datetime(self):
        """
        datetime widget
        @return:
        """
        start_date_picker = widgets.DatePicker(description='Start Date')
        end_date_picker = widgets.DatePicker(description='End Date')
        start_time_picker = widgets.TimePicker(description='Start Time', value=time(hour=self.DEFAULT_TIME, minute=self.DEFAULT_TIME, second=self.DEFAULT_TIME))
        end_time_picker = widgets.TimePicker(description='End Time', value=time(hour=self.DEFAULT_TIME, minute=self.DEFAULT_TIME, second=self.DEFAULT_TIME))

        display(start_date_picker)
        display(start_time_picker)
        display(end_date_picker)
        display(end_time_picker)

        def on_value_change(change):
            global start_datetime
            global end_datetime
            start_date = start_date_picker.value
            end_date = end_date_picker.value
            start_time = start_time_picker.value or time(hour=0, minute=0, second=0)
            end_time = end_time_picker.value or time(hour=0, minute=0, second=0)
            start_datetime = datetime.combine(start_date, start_time)
            end_datetime = datetime.combine(end_date, end_time)

        start_date_picker.observe(on_value_change, names='value')
        end_date_picker.observe(on_value_change, names='value')
        start_time_picker.observe(on_value_change, names='value')
        end_time_picker.observe(on_value_change, names='value')
        return start_datetime, end_datetime
