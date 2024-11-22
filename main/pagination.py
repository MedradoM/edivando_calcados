from rest_framework.pagination import LimitOffsetPagination

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 24 
    max_limit = 100  

    def get_limit(self, request):
        if 'page_size' in request.query_params:
            return min(int(request.query_params.get('page_size', self.default_limit)), self.max_limit)
        return super().get_limit(request)