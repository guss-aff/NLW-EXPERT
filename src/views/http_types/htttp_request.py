from typing import Dict

class HttpRequest:
  def __init__(self, 
               body: Dict = None,
               header: Dict = None,
               query_params: Dict = None
               ) -> None:
    self.header=header
    self.body=body
    self.query_params=query_params