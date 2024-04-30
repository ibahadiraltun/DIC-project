from ._anvil_designer import Form2Template
from anvil import *
import anvil.server


class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.data_grid_1.foreground 
    self.repeating_panel_1.items = []
    self.prev_repeating_panel_1 = []

    # Any code you write here will run before the form opens.

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def parse_test_data(self, test_data):
    return [float(i) for i in test_data.split(' ')]
  
  def button_1_click(self, **event_args):
    result = anvil.server.call('predict_test_data', self.parse_test_data(self.text_box_1.text))
    self.label_prediction.text = result

  def button_2_click(self, **event_args):
    test_data = [float(self.text_box_2.text), float(self.text_box_3.text), float(self.text_box_4.text)]
    result = anvil.server.call('predict_test_data_by_top_3_features', test_data)
    self.repeating_panel_1.items = [{
      'column_1': self.text_box_2.text,
      'column_2': self.text_box_3.text,
      'column_3': self.text_box_4.text,
      'column_4': result
    }] + self.prev_repeating_panel_1
    self.prev_repeating_panel_1 = self.repeating_panel_1.items
    
  
