from django.shortcuts import redirect

class RoleRequiredMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    path = request.path
    if request.user.is_authenticated:
        # Contoh: user officer tidak boleh akses /sdm/*
        if path.startswith('/sdm/') and request.user.role != 'sdm':
            return redirect('no_permission')
    return self.get_response(request)