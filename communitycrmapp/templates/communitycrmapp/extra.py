Edit:

views.py
def member_edit(request, id):
    member = Member.objects.get(pk=id)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('communitycrmapp/success.html', {'form': form})
    else:
        form = MemberForm(instance=post)
    return render(request, 'communitycrmapp/edit.html', {
        'member': member,
    })

search.html
      <form method="POST" action="/engagement_search">
        {% csrf_token %}
        Engagement Score? <input type="number" name="engagmentquery"/>
        <button type="submit"> Search </button>
      </form>

engagement score

def engagement_search(request, key=get_key()):
    score = member.engagement_score(key)
    if request.method == "POST":
        search_id = request.Post.get('engagementquery')
        try:
            engagement = Member.objects.filter(score__gte= search_id)
            for member in engagment:
                # meetups pull starts here
                meetup_id = member.meetupid
                r = requests.get("{}{}{}{}".format('https://api.meetup.com/members/', meetup_id, key, '&sign=true&fields=topics'))
                meetups = (r.json()['topics'])
                li = []
                topics = (r.json()['topics'])
                for topic in topics:
                    li.append(topic['name'])
                # meetups pull ends here
            return render(request, 'communitycrmapp/results.html', {
                'engagement': engagement,
                'meetups': li})
        except Member.DoesNotExist:
            return HttpResponse("no such user")
    else:
        return render(request, 'communitycrmapp/searchpage.html')


edit.html

<h1> Edit To Do List Item </h1>
<p>{{id}}</p>
<form method="POST" action="{% url 'member_edit' id=id %}" class="post-form">{% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="save_btn_btn-default"> Submit </button>
</form>

member.html

    <form action="{% url edit id=member.pk %}" method="post">{% csrf_token %}
        <input type="submit" value="Edit" />
    </form>

url
    url(r'^engagement_search', views.engagement_search, name='engagement_search'),
]

url(r'^member_edit/(?P<id>\d+)/', views.member_edit, name='member_edit'),
