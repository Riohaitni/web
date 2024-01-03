from django.http import HttpResponse
import json

from account.models import Account
from friend.models import FriendRequest

def send_friend_request(request, *args, **kwargs):
    user = request.user
    payload = {}
    if request.method == "POST" and user.is_authenticated:
        user_id = request.POST.get("receiver_user_id")
        if user_id:
            receiver = Account.objects.get(pk=user_id)
            try:
                # nhận được bất kỳ yêu cầu kết bạn nào
                friendRequest = FriendRequest.objects.filter(sender=user, receiver=receiver)
                # tìm xem có ai trong số họ đang hoạt động không
                try:
                    for request in friend_requests:
                        if request.is_active:
                            raise Exception("Bạn đã gửi cho họ lời mời kết bạn.")
                    # nếu không có gì hoạt động thì hãy tạo yêu cầu kết bạn mới
                    friendRequest = FriendRequest(sender=user, receiver=receiver)
                    friendRequest.save()
                    # payload['result'] = "Thành công."
                    payload['response'] = "Yêu cầu kết bạn đã được gửi."
                except Exception as e:
                    # payload['result'] = "Lỗi."
                    payload['response'] = str(e)
            except FriendRequest.DoesNotExist:
                # không có yêu cầu kết bạn nào để tạo một yêu cầu
                friend_request = FriendRequest(sender=user, receiver=receiver)
                friend_request.save()
                payload['response'] = "Yêu cầu kết bạn đã được gửi."
                
                if payload['response'] = None:
                payload['response'] = "Đã xảy ra sự cố."
        else:
            payload['response'] = "Không thể gửi yêu cầu kết bạn."
    else:
        payload['response'] = "Bạn phải được xác thực để gửi yêu cầu kết bạn."

    return HttpResponse(json.dumps(payload), content_type="application/json")