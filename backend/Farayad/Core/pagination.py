
from rest_framework.pagination import PageNumberPagination

'''Override page_size_query_param attribute of PageNumberPagination'''
class CustomizePagination(PageNumberPagination):
    page_size_query_param = 'limit'
    page_size = 10


"""Pagination Handler"""
class PaginationHandlerMixin(object):
    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is  None:
                 self._paginator =None
            else :
                self._paginator = self.pagination_class()
        else :
            pass

        return self._paginator

    def  paginate_queryset(self,queryset):
        if self.paginator is None:
            return None
        
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self,data):
        if self.paginator is None:
            raise "Paginator is None"
        return self.paginator.get_paginated_response(data)
