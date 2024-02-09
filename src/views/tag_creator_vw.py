from src.views.http_types.htttp_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_ctrl import TagCratorController
class TagCreatorView:
  """Responsible for http interactions
  """
  
  def validate_and_create(self,http_request:HttpRequest) -> HttpResponse:
    tag_creator_controller = TagCratorController()
    
    body = http_request.body
    product_code = body['product_code']
    
    
    #! lógica de negócio
    formatted_response = tag_creator_controller.create(product_code)
    #! retorno http
    return HttpResponse(status_code=200,body=formatted_response)