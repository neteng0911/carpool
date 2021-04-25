from django.contrib import admin
from .models import Listing,Bid,Comment

class ListingAdmin(admin.ModelAdmin):
    list_display=("id","title","price","category","created_date","closed_auction")

class BidAdmin(admin.ModelAdmin):
    list_display=("val","bidder","listing_bid")


class CommentAdmin(admin.ModelAdmin):
    list_display={"comment","listing_comment","comment_author"}

# Register your models here.
admin.site.register(Bid,BidAdmin)
admin.site.register(Comment)
admin.site.register(Listing, ListingAdmin)



