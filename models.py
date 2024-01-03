from django.db import models
from django.conf import settings
from django.utils import timezone

class FriendList(models.Model):
    user     = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")
    friends  = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="friends")

    def __str__(self):
        return self.user.userame
    
    def add_friend(self, account):
        """
        Thêm một người bạn mới
        """
        if not account in self.friends.aal():
            self.friends.add(accont)
            self.save()

    def remove_friend(self, account):
        """
        Xóa một người bạn
        """
        if account in self.friends.all():
            self.friends.remove(account)

    def unfriend(self, removee):
        """
        Bắt đầu hành động hủy kết bạn với ai đó
        """ 
        remover_friend_list = self 
        # xóa bạn bè khỏi danh sách bạn bè đã xóa
        remover_friend_list.remove_friend(removee)

        friends_list = FriendList.objects.get(user=removee)
        friends_list.remove_friend(self.user)

    def is_mutual_friend(self, friend):
        """
        Đây có phải là một người bạn không?
        """ 
        if friend in delf.friends.all():
            return True
        return False
    
class FriendRequest(models.Model):
    """ 
    Một yêu cầu kết bạn bao gồm hai phần chính:
    1. Người gửi
        -người gửi/bắt đầu yêu cầu kết bạn
    2. Người nhận
        -người nhận được yêu cầu kết bạn
    """

    sender     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender")
    receiver   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver")
    is_active  = models.BooleanField(blank=True, null=False, default=True)
    timestamp  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username
    
    def accept(self):
        """
        Chấp nhận yêu cầu kết bạn
        Cập nhật cả danh sách bạn bè NGƯỜI GỬI và NGƯỜI NHẬN
        """ 
        receiver_friend_list = FriendList.objects.get(user=self.receiver)
        if receiver_friend_list:
            receiver_friend_list.add_friend(self.sender)
            sender_friend_list = FriendList.objects.get(user=self.sender)
            if sender_friend_list:
                sender_friend_list.add_friend(self.receiver)
                self.is_active = False
                self.save()

    
    def decline(self):
        """ 
        Từ chối yêu cầu kết bạn
        "Từ chối" bằng cách đặt 'is_active' 
        """
        self.is_active = False
        self.save()

    def cancel(self):
        """ 
        Hủy yêu cầu kết bạn
        "Hủy" bằng cách đặt 'is_active'
        Điều này chỉ khác với việc "từ chối" thông qua thông báo được tạo
        """ 
        self




