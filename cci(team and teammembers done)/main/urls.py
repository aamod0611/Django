from django.conf.urls import url
from . import views
app_name = 'main'

urlpatterns = [
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='details'),
        url(r'^main/add/$', views.TeamMemberCreate.as_view(), name='TeamMember'),
        url(r'^main/(?P<pk>[0-9]+)/delete/$', views.TeamMemberDelete.as_view(), name='TeamMember-delete'),
        url(r'^main/teams/add/$', views.TeamsCreate.as_view(), name='Teams'),

      #  url(r'^main/team/update/(?P<pk>[0-9]+)/$', views.TeamUpdate.as_view(), name='Team-update'),
        url(r'^main/team/(?P<pk>[0-9]+)/update/$', views.TeamUpdate.as_view(), name='Team-update'),

        url(r'^main/teams/(?P<pk>[0-9]+)$', views.TeamDetailView.as_view(), name='TeamDetails'),
        url(r'^main/teams/$', views.TeamView.as_view(), name='AllTeams'),
        url(r'^main/(?P<pk>[0-9]+)/teams/delete/', views.TeamsDelete.as_view(), name = 'Teams-delete'),
        url(r'^(?P<pk>[0-9]+)$', views.TeamMemberDetailView.as_view(), name='TeamMemberDetails'),
        url(r'^main/groupadd/$', views.GroupCreate.as_view(), name='Groups'),

        url(r'^main/groups/(?P<pk>[0-9]+)/delete/$', views.GroupDelete.as_view(), name='Group-delete'),
        url(r'^main/group/(?P<pk>[0-9]+)/update/$', views.GroupUpdate.as_view(), name='Group-update'),

        url(r'^main/groups/$',views.GroupView.as_view(), name='GroupDetails'),
        url(r'^main/groupsDetail/(?P<pk>[0-9]+)$', views.GroupDetailView.as_view(), name='GroupTeamDetails'),
        url(r'^main/teammembers/(?P<pk>[0-9]+)/update/$', views.TeamMemberUpdate.as_view(), name='TeamMember-update'),

        url(r'^register/$', views.UserFormView.as_view(), name='register'),


        ]