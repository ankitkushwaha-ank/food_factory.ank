from .models import WebUsers

def webuser_context(request):
    user_id = request.session.get('user_id')
    webuser = None
    if user_id:
        try:
            webuser = WebUsers.objects.get(id=user_id)
        except WebUsers.DoesNotExist:
            pass
    return {'webuser': webuser}
