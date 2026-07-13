import time
from django.utils import timezone


class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        request.start_time = start_time
        request.request_time = timezone.now()

        response = self.get_response(request)

        duration = round((time.time() - start_time) * 1000, 2)
        user = request.user.username if request.user.is_authenticated else 'Anonymous'

        print(f"[REQ] {request.method} {request.path} | user={user} | time={duration}ms")
        return response
