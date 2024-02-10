from .tag_creator_ctrl import TagCratorController
from src.drivers.barcode_handler import BarcodeHandler
from unittest.mock import patch

@patch.object(BarcodeHandler,'create_barcode')
def test_create(mock_create_barcode):
  mock_value = 'image_path'
  mock_create_barcode.return_value = mock_value
  tag_creator_controller = TagCratorController()
  
  result = tag_creator_controller.create(mock_value)
  
  assert isinstance(result,dict)
  assert 'data' in result
  assert 'type' in result['data']
  assert 'count' in result['data']
  assert 'path' in result['data']
  
  assert result['data']['type'] == 'Tag Image'
  assert result['data']['count'] == 1
  assert result['data']['path'] == f'{mock_value}.png'